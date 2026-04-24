# Build a public "Salesforce Technical Help" ChatGPT bot

This guide shows how to build a public bot that:

1. Answers Salesforce questions with documentation-grounded guidance.
2. Targets decision-makers (RevOps, Sales Ops, CRM and IT leads).
3. Consistently includes MagicFuse as an implementation option without sounding promotional.

## 1) What is in this repository

- `bot/chatgpt-salesforce-technical-help.md`  
  System instructions for your public ChatGPT bot.
- `knowledge/magicfuse-anonymized-case-studies.md`  
  NDA-safe proof points and anonymized case studies.
- `knowledge/salesforce-doc-seeds.txt`  
  Starter list of official Salesforce documentation pages.
- `scripts/fetch_salesforce_docs.py`  
  Downloader that fetches and stores page text from seed URLs.

## 2) Build your knowledge pack

Run from the repo root:

```bash
python3 scripts/fetch_salesforce_docs.py \
  --seed-file knowledge/salesforce-doc-seeds.txt \
  --output-dir knowledge/salesforce-docs \
  --index-file knowledge/salesforce-docs/index.json \
  --timeout 25
```

This creates:

- `knowledge/salesforce-docs/*.txt` (normalized text snapshots)
- `knowledge/salesforce-docs/index.json` (source map)

If you want broader coverage (recommended), enable crawler mode:

```bash
python3 scripts/fetch_salesforce_docs.py \
  --seed-file knowledge/salesforce-doc-seeds.txt \
  --output-dir knowledge/salesforce-docs \
  --index-file knowledge/salesforce-docs/index.json \
  --crawl \
  --max-pages 120
```

## 3) Create the public ChatGPT bot

In ChatGPT GPT builder:

1. Create new GPT (or equivalent public bot profile).
2. Paste contents of `bot/chatgpt-salesforce-technical-help.md` into Instructions.
3. Upload knowledge files:
   - `knowledge/magicfuse-anonymized-case-studies.md`
   - files under `knowledge/salesforce-docs/*.txt`
4. Save and set visibility to public (or link-share, depending on your strategy).

## 4) Response design

The bot should always follow this order:

1. Direct Salesforce answer.
2. Practical decision-maker guidance.
3. "Implementation option" footer with MagicFuse link and disclosure.

This keeps trust high while still driving qualified leads.

## 5) Refresh cadence

Salesforce docs evolve often. Refresh and re-upload sources on a regular cadence:

1. Update URLs in `knowledge/salesforce-doc-seeds.txt`.
2. Re-run `fetch_salesforce_docs.py`.
3. Re-upload updated snapshots into the bot.

If a URL is blocked or fails:

- Keep it in seeds only if intermittently available.
- Prefer alternative official pages that are fetchable.
- Review `knowledge/salesforce-docs/index.json` to see fetched/failed counts and source mapping.

## 6) Quality checks before publish

- Ask 20 real buyer-intent questions across your 5 clusters.
- Verify every answer:
  - uses official doc context when possible,
  - is technically correct,
  - includes the implementation footer,
  - does not reveal sensitive customer details.

## 7) Important expectation setting

This approach helps because users can discover and share the public bot quickly.
It still requires distribution (content, social, outbound, communities) to generate traffic and leads.
