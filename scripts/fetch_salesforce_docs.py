#!/usr/bin/env python3
"""
Fetch Salesforce documentation pages and store them locally as text snapshots.

Examples:
  # Fetch only seed URLs
  python3 scripts/fetch_salesforce_docs.py \
      --seed-file knowledge/salesforce-doc-seeds.txt \
      --output-dir knowledge/salesforce-docs \
      --index-file knowledge/salesforce-docs/index.json

  # Crawl additional Salesforce docs pages from seed links
  python3 scripts/fetch_salesforce_docs.py \
      --seed-file knowledge/salesforce-doc-seeds.txt \
      --output-dir knowledge/salesforce-docs \
      --index-file knowledge/salesforce-docs/index.json \
      --crawl \
      --max-pages 120
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_UA = (
    "Mozilla/5.0 (compatible; SalesforceBotDocFetcher/1.0; +https://magicfuse.co)"
)
DEFAULT_ALLOWED_DOMAINS = (
    "developer.salesforce.com",
    "help.salesforce.com",
    "trailhead.salesforce.com",
    "www.salesforce.com",
)
SKIP_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".pdf",
    ".zip",
    ".exe",
    ".dmg",
    ".css",
    ".js",
    ".ico",
)
SKIP_PATH_SNIPPETS = (
    "/sfsites/c/resource/",
    "/resource/",
    "/favicon",
)


def slugify(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    base = f"{parsed.netloc}{parsed.path}".strip("/")
    base = base.replace("/", "__")
    base = re.sub(r"[^a-zA-Z0-9._-]+", "-", base)
    if not base:
        base = "index"
    return f"{base}.txt"


def to_text(html: str) -> str:
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
    title = re.sub(r"\s+", " ", match.group(1)).strip()
    return title


def extract_links(base_url: str, html: str) -> list[str]:
    links: list[str] = []
    for match in re.finditer(r'(?is)href=["\'](.*?)["\']', html):
        raw = match.group(1).strip()
        if not raw:
            continue
        absolute = urllib.parse.urljoin(base_url, raw)
        parsed = urllib.parse.urlparse(absolute)
        if parsed.scheme not in {"http", "https"}:
            continue
        if parsed.path.lower().endswith(SKIP_SUFFIXES):
            continue
        path_lower = parsed.path.lower()
        if any(snippet in path_lower for snippet in SKIP_PATH_SNIPPETS):
            continue
        normalized = parsed._replace(fragment="").geturl()
        links.append(normalized)
    return links


def read_seed_urls(seed_file: pathlib.Path) -> list[str]:
    urls: list[str] = []
    for raw in seed_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line)
    return urls


def fetch_url(url: str, timeout_s: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": DEFAULT_UA})
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def is_allowed_domain(url: str, allowed_domains: tuple[str, ...]) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    if not host:
        return False
    return any(host == domain or host.endswith(f".{domain}") for domain in allowed_domains)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download Salesforce docs from seed URLs.")
    parser.add_argument(
        "--seed-file",
        "--seeds",
        dest="seed_file",
        required=True,
        help="Path to URL seed file.",
    )
    parser.add_argument(
        "--output-dir",
        "--out",
        dest="output_dir",
        required=True,
        help="Output directory for downloaded docs.",
    )
    parser.add_argument(
        "--index-file",
        help="Optional index JSON file path to map source URLs to local files.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="Per-request timeout in seconds.",
    )
    parser.add_argument(
        "--sleep-ms",
        type=int,
        default=700,
        help="Delay in milliseconds between requests.",
    )
    parser.add_argument(
        "--crawl",
        action="store_true",
        help="Crawl internal links found in pages under allowed domains.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=60,
        help="Maximum number of pages to fetch (including seeds).",
    )
    parser.add_argument(
        "--allowed-domain",
        action="append",
        default=[],
        help="Allowed domain for crawling (can be passed multiple times).",
    )
    args = parser.parse_args()

    seed_path = pathlib.Path(args.seed_file)
    out_dir = pathlib.Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    index_path = pathlib.Path(args.index_file) if args.index_file else None

    urls = read_seed_urls(seed_path)
    if not urls:
        print("No URLs found in seed file.")
        return 1

    allowed_domains = tuple(args.allowed_domain) if args.allowed_domain else DEFAULT_ALLOWED_DOMAINS
    queue: collections.deque[str] = collections.deque(urls)
    visited: set[str] = set()
    queued: set[str] = set(urls)
    index_rows: list[dict[str, str | int]] = []
    failed_rows: list[dict[str, str]] = []

    fetched = 0
    failed = 0
    while queue and fetched + failed < max(args.max_pages, 1):
        url = queue.popleft()
        queued.discard(url)
        if url in visited:
            continue
        visited.add(url)
        idx = fetched + failed + 1
        filename = slugify(url)
        output_path = out_dir / filename
        print(f"[{idx}] Fetching {url}")
        try:
            html = fetch_url(url, timeout_s=max(args.timeout, 1))
            title = extract_title(html)
            text = to_text(html)
            fetched_unix = int(time.time())
            payload = (
                f"Source URL: {url}\n"
                f"Title: {title}\n"
                f"Fetched at (unix): {fetched_unix}\n\n"
                f"{text}\n"
            )
            output_path.write_text(payload, encoding="utf-8")
            fetched += 1
            index_rows.append(
                {
                    "url": url,
                    "title": title,
                    "output_file": output_path.name,
                    "fetched_unix": fetched_unix,
                }
            )

            if args.crawl:
                for link in extract_links(url, html):
                    if link in visited or link in queued:
                        continue
                    if not is_allowed_domain(link, allowed_domains):
                        continue
                    queue.append(link)
                    queued.add(link)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            failed += 1
            print(f"  FAILED: {exc}")
            failed_rows.append({"url": url, "error": str(exc)})
        time.sleep(max(args.sleep_ms, 0) / 1000.0)

    if index_path:
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_payload = {
            "generated_unix": int(time.time()),
            "fetched": fetched,
            "failed": failed,
            "crawl_enabled": args.crawl,
            "allowed_domains": list(allowed_domains),
            "rows": index_rows,
            "failed_rows": failed_rows,
        }
        index_path.write_text(json.dumps(index_payload, indent=2), encoding="utf-8")
        print(f"Wrote index: {index_path}")

    print(f"\nDone. fetched={fetched}, failed={failed}, out={out_dir}")
    return 0 if fetched > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
