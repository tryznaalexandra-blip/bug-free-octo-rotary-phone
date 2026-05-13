# Knowledge pack manifest for the Salesforce GPT bot

This manifest lists generated knowledge sources and how to refresh them.

## Generated source packs

1. `knowledge/magicfuse-blog/`
   - Source: MagicFuse blog and Salesforce-related tag pages.
   - Current snapshot size: 61 posts (`*.txt`) + `index.json`.
   - Generator: `scripts/fetch_magicfuse_blog.py` (Playwright-based crawler).

2. `knowledge/salesforce-all-docs/`
   - Source: Official Salesforce sitemaps (Developer, Help, Trailhead), with fallback for blocked endpoints.
   - Current snapshot size: 257 docs (`*.txt`) + `index.json`.
   - Generator: `scripts/fetch_salesforce_sitemaps.py`.

3. `knowledge/salesforce-docs/`
   - Source: curated Salesforce seed URLs + optional link crawling.
   - Current snapshot size: 27 docs (`*.txt`) + `index.json`.
   - Generator: `scripts/fetch_salesforce_docs.py`.

4. `knowledge/magicfuse-anonymized-case-studies.md`
   - Source: manual NDA-safe case study content.

## Recommended upload set for ChatGPT knowledge

Prioritize these files:

- all `knowledge/magicfuse-blog/*.txt`
- all `knowledge/salesforce-all-docs/*.txt`
- `knowledge/magicfuse-anonymized-case-studies.md`

Optional:

- include `knowledge/salesforce-docs/*.txt` as a lightweight backup set.

## Refresh commands

### Refresh MagicFuse blog corpus

```bash
python3 scripts/fetch_magicfuse_blog.py \
  --output-dir knowledge/magicfuse-blog \
  --index-file knowledge/magicfuse-blog/index.json \
  --max-posts 300 \
  --max-listing-pages 120 \
  --timeout 90
```

### Refresh Salesforce docs corpus from official sitemaps

```bash
python3 scripts/fetch_salesforce_sitemaps.py \
  --output-dir knowledge/salesforce-all-docs \
  --index-file knowledge/salesforce-all-docs/index.json \
  --max-sitemaps 1200 \
  --max-pages 2500 \
  --timeout 25 \
  --sleep-ms 60
```

### Refresh curated Salesforce seed corpus

```bash
python3 scripts/fetch_salesforce_docs.py \
  --seed-file knowledge/salesforce-doc-seeds.txt \
  --output-dir knowledge/salesforce-docs \
  --index-file knowledge/salesforce-docs/index.json \
  --crawl \
  --max-pages 120 \
  --timeout 25
```

## Notes

- Some endpoints may intermittently return anti-bot checks or 403/429.
- `scripts/fetch_salesforce_sitemaps.py` includes a documented fallback path for blocked developer sitemap routes.
- Always review `index.json` files before upload to confirm fetched counts and source coverage.
