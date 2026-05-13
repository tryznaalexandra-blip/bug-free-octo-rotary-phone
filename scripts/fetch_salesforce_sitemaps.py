#!/usr/bin/env python3
"""
Fetch Salesforce documentation pages by traversing official Salesforce sitemaps.

This script targets:
  - developer.salesforce.com sitemap hierarchy
  - help.salesforce.com sitemap hierarchy
  - trailhead.salesforce.com sitemap hierarchy

It writes normalized text files and index metadata for GPT knowledge uploads.
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import time
import html
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; SalesforceSitemapFetcher/1.0; +https://magicfuse.co)"

SEED_SITEMAPS = [
    "https://developer.salesforce.com/sitemap.xml",
    "https://developer.salesforce.com/docs/ssg-sitemap.xml",
    "https://developer.salesforce.com/docs-atlas-sitemap.xml",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=ai",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=service",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=sales",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=platform",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=data",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=xcloud",
    "https://help.salesforce.com/apex/Help_SiteMapIndexExternal?producttype=mktg",
    "https://trailhead.salesforce.com/sitemap.xml",
]

ALLOWED_HOSTS = {
    "developer.salesforce.com",
    "help.salesforce.com",
    "trailhead.salesforce.com",
}

SKIP_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".pdf",
    ".zip",
    ".css",
    ".js",
    ".ico",
)

SKIP_PATTERNS = (
    "/search",
    "/login",
    "/signin",
    "/community",
)


def fetch(url: str, timeout_s: int) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def fetch_with_fallback(url: str, timeout_s: int) -> tuple[str, str]:
    """Fetch URL content; fallback to r.jina.ai for blocked developer docs."""
    try:
        return fetch(url, timeout_s=timeout_s), "direct"
    except urllib.error.HTTPError as exc:
        host = urllib.parse.urlparse(url).netloc.lower()
        if host.endswith("developer.salesforce.com") and exc.code in {401, 403, 429}:
            mirror_url = f"https://r.jina.ai/http://{host}{urllib.parse.urlparse(url).path}"
            if urllib.parse.urlparse(url).query:
                mirror_url = f"{mirror_url}?{urllib.parse.urlparse(url).query}"
            return fetch(mirror_url, timeout_s=timeout_s), "r.jina.ai"
        raise


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url.strip())
    cleaned = parsed._replace(fragment="")
    return cleaned.geturl()


def is_allowed_host(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return host in ALLOWED_HOSTS or any(host.endswith(f".{h}") for h in ALLOWED_HOSTS)


def should_skip_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lower()
    if path.endswith(SKIP_SUFFIXES):
        return True
    return any(p in path for p in SKIP_PATTERNS)


def slugify(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    base = f"{parsed.netloc}{parsed.path}".strip("/")
    if parsed.query:
        base = f"{base}__{parsed.query}"
    base = base.replace("/", "__")
    base = re.sub(r"[^a-zA-Z0-9._=-]+", "-", base)
    if not base:
        base = "index"
    return f"{base}.txt"


def html_to_text(html: str) -> str:
    html = re.sub(r"(?is)<script.*?>.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?>.*?</style>", " ", html)
    html = re.sub(r"(?is)<noscript.*?>.*?</noscript>", " ", html)
    html = re.sub(r"(?is)<[^>]+>", " ", html)
    html = html.replace("&nbsp;", " ")
    html = html.replace("&amp;", "&")
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")
    html = re.sub(r"\s+", " ", html).strip()
    return html


def extract_title(html: str) -> str:
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", html)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def parse_sitemap(xml_or_markdown: str) -> tuple[list[str], list[str]]:
    text = html.unescape(xml_or_markdown)
    submaps: set[str] = set()
    urls: set[str] = set()

    # XML style parsing (namespace-agnostic) via regex.
    # Some sitemap providers include additional tags (lastmod/xhtml:link) inside <url> entries,
    # so locate <loc> anywhere within the block, not only as the first child.
    for block in re.finditer(r"(?is)<sitemap\b[^>]*>(.*?)</sitemap>", text):
        loc_match = re.search(r"(?is)<loc\b[^>]*>\s*(.*?)\s*</loc>", block.group(1))
        if loc_match:
            submaps.add(loc_match.group(1).strip())
    for block in re.finditer(r"(?is)<url\b[^>]*>(.*?)</url>", text):
        loc_match = re.search(r"(?is)<loc\b[^>]*>\s*(.*?)\s*</loc>", block.group(1))
        if loc_match:
            urls.add(loc_match.group(1).strip())

    # r.jina.ai markdown fallback: links listed as [https://...](https://...)
    for match in re.finditer(r"\((https?://[^)\s]+)\)", text):
        link = match.group(1).strip()
        lower = link.lower()
        if "sitemap" in lower or "help_sitemap" in lower:
            submaps.add(link)
        else:
            urls.add(link)

    return sorted(submaps), sorted(urls)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Salesforce docs from official sitemaps.")
    parser.add_argument("--output-dir", required=True, help="Directory for downloaded docs text files.")
    parser.add_argument("--index-file", required=True, help="Output JSON index path.")
    parser.add_argument("--max-sitemaps", type=int, default=1200, help="Maximum sitemap files to traverse.")
    parser.add_argument("--max-pages", type=int, default=2500, help="Maximum docs pages to download.")
    parser.add_argument("--timeout", type=int, default=30, help="Request timeout in seconds.")
    parser.add_argument("--sleep-ms", type=int, default=150, help="Delay between requests in milliseconds.")
    parser.add_argument(
        "--max-runtime-seconds",
        type=int,
        default=0,
        help="Stop gracefully after this many seconds (0 disables).",
    )
    args = parser.parse_args()

    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = pathlib.Path(args.index_file)
    started_at = time.time()

    sitemap_queue: collections.deque[str] = collections.deque(SEED_SITEMAPS)
    seen_sitemaps: set[str] = set()
    page_urls: set[str] = set()
    sitemap_rows: list[dict[str, str | int]] = []
    page_rows: list[dict[str, str | int]] = []
    sitemap_failures: list[dict[str, str]] = []
    page_failures: list[dict[str, str]] = []

    # Traverse sitemap tree.
    while sitemap_queue and len(seen_sitemaps) < max(args.max_sitemaps, 1):
        if args.max_runtime_seconds > 0 and (time.time() - started_at) >= args.max_runtime_seconds:
            break
        sm_url = normalize_url(sitemap_queue.popleft())
        if sm_url in seen_sitemaps:
            continue
        seen_sitemaps.add(sm_url)

        if not is_allowed_host(sm_url):
            continue

        try:
            xml_text, source = fetch_with_fallback(sm_url, timeout_s=max(args.timeout, 1))
            submaps, urls = parse_sitemap(xml_text)
            sitemap_rows.append(
                {
                    "sitemap_url": sm_url,
                    "submap_count": len(submaps),
                    "url_count": len(urls),
                    "fetch_source": source,
                }
            )
            for sub in submaps:
                nsub = normalize_url(sub)
                if nsub not in seen_sitemaps:
                    sitemap_queue.append(nsub)
            for url in urls:
                nurl = normalize_url(url)
                if is_allowed_host(nurl) and not should_skip_url(nurl):
                    page_urls.add(nurl)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            sitemap_failures.append({"sitemap_url": sm_url, "error": str(exc)})
        time.sleep(max(args.sleep_ms, 0) / 1000.0)

    # Download pages.
    fetched = 0
    failed = 0
    for idx, page_url in enumerate(sorted(page_urls), start=1):
        if args.max_runtime_seconds > 0 and (time.time() - started_at) >= args.max_runtime_seconds:
            break
        if fetched + failed >= max(args.max_pages, 1):
            break
        try:
            html, source = fetch_with_fallback(page_url, timeout_s=max(args.timeout, 1))
            title = extract_title(html)
            text = html_to_text(html)
            out_file = slugify(page_url)
            out_path = output_dir / out_file
            ts = int(time.time())
            payload = (
                f"Source URL: {page_url}\n"
                f"Title: {title}\n"
                f"Fetched at (unix): {ts}\n\n"
                f"{text}\n"
            )
            out_path.write_text(payload, encoding="utf-8")
            page_rows.append(
                {
                    "url": page_url,
                    "title": title,
                    "output_file": out_file,
                    "fetched_unix": ts,
                    "order": idx,
                    "fetch_source": source,
                }
            )
            fetched += 1
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            failed += 1
            page_failures.append({"url": page_url, "error": str(exc)})
        time.sleep(max(args.sleep_ms, 0) / 1000.0)

    index_payload = {
        "generated_unix": int(time.time()),
        "seed_sitemaps": SEED_SITEMAPS,
        "sitemaps_seen": len(seen_sitemaps),
        "candidate_pages_discovered": len(page_urls),
        "pages_fetched": fetched,
        "pages_failed": failed,
        "sitemap_rows": sitemap_rows,
        "sitemap_failures": sitemap_failures,
        "page_rows": page_rows,
        "page_failures": page_failures,
    }
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index_payload, indent=2), encoding="utf-8")

    print(f"Wrote index: {index_path}")
    print(
        "Done. "
        f"sitemaps_seen={len(seen_sitemaps)} discovered={len(page_urls)} fetched={fetched} failed={failed}"
    )
    return 0 if fetched > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
