#!/usr/bin/env python3
"""
Crawl MagicFuse blog listings and export reachable post pages to text files.

This crawler uses Playwright because MagicFuse is commonly protected by a
browser challenge that blocks plain HTTP clients.

Usage:
  python3 scripts/fetch_magicfuse_blog.py \
      --output-dir knowledge/magicfuse-blog \
      --index-file knowledge/magicfuse-blog/index.json
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import time
import urllib.parse
from typing import Iterable

from playwright.sync_api import BrowserContext, Page, TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

ALLOWED_HOST = "magicfuse.co"
DEFAULT_START_URL = "https://magicfuse.co/blog"
DEFAULT_TAG_PATHS = (
    "/blog/tag/salesforce",
    "/blog/tag/salesforce-agentforce",
    "/blog/tag/salesforce-appexchange",
    "/blog/tag/salesforce-commerce-cloud",
    "/blog/tag/salesforce-consulting",
    "/blog/tag/salesforce-data-cloud",
    "/blog/tag/salesforce-development",
    "/blog/tag/salesforce-education-cloud",
    "/blog/tag/salesforce-einstein-ai",
    "/blog/tag/salesforce-integration",
    "/blog/tag/salesforce-lightning",
    "/blog/tag/salesforce-marketing",
    "/blog/tag/salesforce-pdo",
    "/blog/tag/salesforce-partners",
    "/blog/tag/salesforce-sales-cloud",
    "/blog/tag/salesforce-service-cloud",
)
AUTOMATION_SAFE_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url.strip())
    return parsed._replace(fragment="", query="").geturl()


def slugify(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    base = f"{parsed.netloc}{parsed.path}".strip("/")
    base = base.replace("/", "__")
    base = re.sub(r"[^a-zA-Z0-9._-]+", "-", base)
    if not base:
        base = "index"
    return f"{base}.txt"


def is_magicfuse_url(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return host == ALLOWED_HOST or host.endswith(f".{ALLOWED_HOST}")


def is_listing_url(url: str) -> bool:
    path = urllib.parse.urlparse(url).path.rstrip("/")
    if path in {"/blog", ""}:
        return True
    if path.startswith("/blog/tag/"):
        return True
    if "/page/" in path and path.startswith("/blog/"):
        return True
    return False


def is_post_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.rstrip("/")
    if not path.startswith("/blog/"):
        return False
    if path in {"/blog", "/blog/tag"}:
        return False
    for forbidden in ("/blog/tag/", "/blog/author/", "/blog/page/"):
        if forbidden in path:
            return False
    return path.count("/") >= 2


def sanitize_text(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def wait_for_checkpoint_pass(page: Page, timeout_ms: int) -> None:
    start = time.time()
    while (time.time() - start) * 1000 < timeout_ms:
        title = page.title().lower()
        if "security checkpoint" not in title and "verifying your browser" not in title:
            return
        page.wait_for_timeout(1200)
    # One extra hard reload attempt.
    page.reload(wait_until="domcontentloaded", timeout=timeout_ms)
    page.wait_for_timeout(2000)


def load_page(context: BrowserContext, url: str, timeout_ms: int, retries: int) -> Page:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        page = context.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=timeout_ms)
            wait_for_checkpoint_pass(page, timeout_ms=timeout_ms)
            return page
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            page.close()
            if attempt < retries:
                time.sleep(1.25 * attempt)
    raise RuntimeError(f"Failed to load URL after retries: {url}; error={last_error}")


def click_load_more(page: Page, max_clicks: int) -> None:
    for _ in range(max_clicks):
        button = page.locator("button", has_text=re.compile(r"load more", re.I))
        if button.count() < 1:
            return
        before = page.evaluate("() => document.querySelectorAll('a[href*=\"/blog/\"]').length")
        button.first.click()
        page.wait_for_timeout(1200)
        try:
            page.wait_for_load_state("networkidle", timeout=10000)
        except PlaywrightTimeoutError:
            pass
        after = page.evaluate("() => document.querySelectorAll('a[href*=\"/blog/\"]').length")
        if after <= before:
            return


def extract_links(page: Page, base_url: str) -> set[str]:
    hrefs: list[str] = page.eval_on_selector_all(
        "a[href]", "els => Array.from(new Set(els.map(e => e.getAttribute('href') || '')))"
    )
    result: set[str] = set()
    for href in hrefs:
        if not href:
            continue
        absolute = normalize_url(urllib.parse.urljoin(base_url, href))
        if not is_magicfuse_url(absolute):
            continue
        result.add(absolute)
    return result


def build_listing_seed_urls(start_url: str) -> list[str]:
    urls = [normalize_url(start_url)]
    for path in DEFAULT_TAG_PATHS:
        urls.append(normalize_url(urllib.parse.urljoin(start_url, path)))
    seen: set[str] = set()
    deduped: list[str] = []
    for url in urls:
        if url in seen:
            continue
        seen.add(url)
        deduped.append(url)
    return deduped


def write_post_file(output_dir: pathlib.Path, url: str, title: str, text: str) -> str:
    output_file = slugify(url)
    out_path = output_dir / output_file
    payload = (
        f"Source URL: {url}\n"
        f"Title: {title}\n"
        f"Fetched at (unix): {int(time.time())}\n\n"
        f"{sanitize_text(text)}\n"
    )
    out_path.write_text(payload, encoding="utf-8")
    return output_file


def crawl_listing_pages(
    context: BrowserContext,
    seed_urls: Iterable[str],
    timeout_ms: int,
    max_listing_pages: int,
) -> tuple[set[str], dict[str, str]]:
    queue: collections.deque[str] = collections.deque(seed_urls)
    visited: set[str] = set()
    post_urls: set[str] = set()
    failures: dict[str, str] = {}

    while queue and len(visited) < max_listing_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        print(f"[listing] {len(visited)}: {url}")
        try:
            page = load_page(context, url=url, timeout_ms=timeout_ms, retries=3)
            click_load_more(page, max_clicks=8)
            for link in extract_links(page, base_url=url):
                if is_listing_url(link) and link not in visited:
                    queue.append(link)
                elif is_post_url(link):
                    post_urls.add(link)
            page.close()
        except Exception as exc:  # noqa: BLE001
            failures[url] = str(exc)
            print(f"  FAILED listing: {exc}")
    return post_urls, failures


def fetch_post_text(page: Page) -> tuple[str, str]:
    title = page.locator("h1").first.inner_text(timeout=5000).strip()
    article_blocks = page.eval_on_selector_all(
        "article, main",
        "els => els.map(e => e.innerText || '').filter(Boolean)",
    )
    if article_blocks:
        body = max(article_blocks, key=len)
    else:
        body = page.inner_text("body")
    return title, body


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch all reachable MagicFuse blog posts.")
    parser.add_argument("--start-url", default=DEFAULT_START_URL, help="Blog listing start URL.")
    parser.add_argument("--output-dir", required=True, help="Directory for output text files.")
    parser.add_argument("--index-file", required=True, help="Path to output index JSON.")
    parser.add_argument("--timeout", type=int, default=90, help="Per-page timeout in seconds.")
    parser.add_argument("--sleep-ms", type=int, default=450, help="Delay between post fetches.")
    parser.add_argument(
        "--max-listing-pages",
        type=int,
        default=250,
        help="Maximum listing/tag pages to crawl.",
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=5000,
        help="Maximum number of posts to export.",
    )
    args = parser.parse_args()

    output_dir = pathlib.Path(args.output_dir)
    index_path = pathlib.Path(args.index_file)
    output_dir.mkdir(parents=True, exist_ok=True)

    seed_urls = build_listing_seed_urls(args.start_url)
    timeout_ms = max(args.timeout, 15) * 1000

    rows: list[dict[str, str | int]] = []
    listing_failures: dict[str, str] = {}
    post_failures: dict[str, str] = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent=AUTOMATION_SAFE_UA,
            locale="en-US",
            viewport={"width": 1366, "height": 768},
        )
        # Hide automation hints used by many bot checks.
        context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

        post_urls, listing_failures = crawl_listing_pages(
            context=context,
            seed_urls=seed_urls,
            timeout_ms=timeout_ms,
            max_listing_pages=max(args.max_listing_pages, 1),
        )

        export_urls = sorted(post_urls)[: max(args.max_posts, 1)]
        print(f"Discovered posts: {len(post_urls)} | Exporting: {len(export_urls)}")
        for idx, url in enumerate(export_urls, start=1):
            print(f"[post] {idx}/{len(export_urls)} {url}")
            try:
                page = load_page(context, url=url, timeout_ms=timeout_ms, retries=3)
                title, body = fetch_post_text(page)
                output_file = write_post_file(output_dir=output_dir, url=url, title=title, text=body)
                rows.append(
                    {
                        "url": url,
                        "title": title,
                        "output_file": output_file,
                        "fetched_unix": int(time.time()),
                    }
                )
                page.close()
            except Exception as exc:  # noqa: BLE001
                post_failures[url] = str(exc)
                print(f"  FAILED post: {exc}")
            time.sleep(max(args.sleep_ms, 0) / 1000.0)

        browser.close()

    index_payload = {
        "generated_unix": int(time.time()),
        "seed_urls": seed_urls,
        "listing_failures": listing_failures,
        "post_failures": post_failures,
        "fetched": len(rows),
        "failed": len(post_failures),
        "rows": rows,
    }
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index_payload, indent=2), encoding="utf-8")
    print(f"Wrote index: {index_path}")
    print(f"Done. fetched={len(rows)}, failed={len(post_failures)}")
    return 0 if rows else 2


if __name__ == "__main__":
    raise SystemExit(main())
