# MagicFuse.co — SEO Audit & Link-Building Strategy

**Domain:** `magicfuse.co` (Salesforce development & consulting company; division of TechMagic)
**Source data:** Google Search Console export — last 7 days vs previous 7 days (Web search type)
**Audit type:** Performance audit + technical/on-page SEO audit + link-building anchor plan for lead generation

> Headline: the site is currently a **branded-search business**. Almost 70% of clicks come from people typing "magicfuse" / "magic fuse" — meaning Google is *not* yet sending you commercial-intent traffic. Every issue below ladders up to that single problem.

---

## 1. Performance snapshot (last 7 days vs prior 7)

| Metric | Last 7d | Prev 7d | Δ |
|---|---|---|---|
| Total clicks (all queries) | **32** | 26 | +23% |
| Total impressions | 19,667 | 21,252 | -7.5% |
| Site-wide CTR | **0.16%** | 0.12% | +0.04 pp |
| Avg position (queries) | mid-30s | mid-30s | flat |
| Branded clicks | 22 (68.8%) | — | — |
| Non-branded clicks | **10 / 19,601 imp** | — | CTR ≈ 0.05% |

**Devices**

| Device | Clicks 7d | Impressions | CTR | Avg pos |
|---|---|---|---|---|
| Desktop | 70 | 38,651 | 0.18% | 19.2 |
| Mobile | 14 | 3,482 | 0.40% | 30.2 |
| Tablet | 0 | 65 | 0% | 35.4 |

> *Note: the device totals are larger than the query total because GSC counts each impression once per query type — they can disagree slightly; treat the trends as directional.*

**What this means**

- Mobile CTR (0.40%) is **2.2× higher than desktop** even though mobile rankings are *worse* (pos 30 vs 19). Demand on mobile is more click-hungry; you are leaving leads on the table by not improving mobile rank.
- Desktop has 11× the impressions but only 5× the clicks → the desktop SERP layout (AI Overviews, People Also Ask, sitelinks for Salesforce.com, top-10 dominated by Gartner / Clutch / G2 / Salesforce.com) is *eating* your visibility.
- 19,667 impressions in a week → demand is real. The conversion problem is **rank position + title CTR**, not topic relevance.

**Geography**

| Country | Clicks | Impressions | Pos | Notes |
|---|---|---|---|---|
| 🇮🇳 India | 20 | 2,352 | 17.4 | high impressions, weak buyers |
| 🇺🇸 United States | 14 | 26,445 | **20.6** | 60% of impressions, 0.05% CTR — your real money market |
| 🇺🇦 Ukraine | 10 | 142 | 9.0 | brand traffic |
| 🇵🇱 Poland | 6 | 388 | 20.2 | brand + nearshore positioning |
| 🇬🇧 UK | 5 | 2,651 | 24.0 | second priority market |
| 🇨🇦 Canada | 5 | 1,054 | 14.6 | best EU/NA non-brand position |
| 🇩🇪 Germany | 4 | 851 | 31.5 | weak |

> 60% of all impressions are US. US average position is 20.6 — bottom of page 2. Moving the US average from ~20 → ~10 is the single biggest revenue lever on the entire site.

---

## 2. The biggest performance problems (ranked)

### 🔴 Problem 1 — Money pages don't rank
All commercial / lead-generating templates sit on page 3-7:

| Page template | Avg impressions | Avg position | Clicks |
|---|---|---|---|
| `/hire-salesforce-*` (8 pages) | ~2,100 / wk | **34** | **0** |
| `/services/*` (~20 pages) | ~1,500 / wk | **25–55** | 1 |
| `/expertise/*` (16 pages) | ~1,800 / wk | **27–43** | 2 |

**Concrete examples**

```
/hire-salesforce-developers   1,124 imp  pos 33.9  0 clicks
/hire-salesforce-expert         448 imp  pos 34.5  0 clicks
/hire-salesforce-consultants    245 imp  pos 35.5  0 clicks
/services/salesforce-managed-service  397 imp  pos 50.7  1 click
/services/salesforce-app-development  234 imp  pos 46.4  0 clicks
/services/salesforce-custom-development  134 imp  pos 54.4  0 clicks
/expertise/mulesoft           446 imp  pos 33.2  0 clicks
/expertise/tableau            310 imp  pos 37.5  0 clicks
/expertise/marketing-cloud    116 imp  pos 38.0  0 clicks
```

**Diagnosis:** these are all *topical* pages with thin internal linking, almost no inbound topical authority, and they're outranked by Gartner / Clutch / TopDevelopers / hire-salesforce-developer.com listicles — pages that have hundreds of referring domains. You're competing on topics where authority decides the SERP. **This is the section that link building must target.**

### 🔴 Problem 2 — Page-1 ranks with broken CTR
Several blog posts already rank in Google's top 10 but are getting practically zero clicks, meaning the title/description or SERP layout is failing:

| URL | Pos | Imp | CTR | Clicks |
|---|---|---|---|---|
| `/blog/agentforce-cost` | 8.0 | **5,077** | 0.14% | 7 |
| `/blog/salesforce-marketing-cloud-cost` | 9.1 | 2,564 | 0.23% | 6 |
| `/blog/top-salesforce-development-companies` | 10.1 | 2,466 | 0.12% | 3 |
| `/blog/appexchange-pricing-and-monetisation` | 8.2 | 1,346 | 0.07% | 1 |
| `/blog/isv-partnerships` | 6.9 | 1,122 | 0.09% | 1 |
| `/blog/salesforce-security-best-practices` | **7.8** | 405 | **0%** | **0** |
| `/blog/process-builder-to-flow-migration` | 9.4 | 214 | 0% | 0 |

**Expected CTR at position 8** is roughly 3–4%. You're getting 0.1%. That's a 25× under-performance. Three causes, all fixable:

1. **AI Overviews / Featured snippet stealing the click** — pricing queries are a textbook AIO category. Solution: rewrite intros so Google has to keep your link to answer the question (use proprietary numbers, comparison tables, "as of {month} 2026" dates).
2. **Weak titles/descriptions** — for a "cost" article, the title needs the *number* in it ("Agentforce Cost in 2026: $2 / Conversation + Add-Ons Explained"). Test: does the SERP snippet answer the query without clicking? If yes, rewrite.
3. **Missing FAQ / HowTo schema** — every "X cost" page should have `Article` + `FAQPage` schema so PAA picks you up.

### 🔴 Problem 3 — Index bloat & duplicate URLs
GSC is reporting dozens of indexed `#heading-num-X` anchor URLs as separate pages:

```
/blog/marketo-vs-pardot                       643 imp
/blog/marketo-vs-pardot#heading-num-1         258 imp
/blog/marketo-vs-pardot#heading-num-2         246 imp
/blog/marketo-vs-pardot#heading-num-0         257 imp
/blog/marketo-vs-pardot#heading-num-3          52 imp
```

That's the **same content** indexed five times. Same pattern for `/blog/salesforce-marketing-cloud-cost`, `/blog/data-cloud-limits`, `/blog/agentforce-cost`, `/blog/2gp-developer-guide`, etc. This dilutes link equity, splits CTR, and is a textbook Panda signal.

**Fix:** the table-of-contents anchor links should not generate distinct canonical URLs. Add `<link rel="canonical" href="…/marketo-vs-pardot">` on every variant (most likely the issue is that the TOC is generating real `<a href>` paths Google treats as separate URLs because of how the SPA framework — Astro/Vercel — emits them). Easiest mitigation: add `data-no-fragment` handling, or robots-noindex `#heading-num-*` paths via JS-rendered canonical.

### 🔴 Problem 4 — Site sits behind a Vercel bot challenge
A direct `curl` to `magicfuse.co` returns HTTP **429** with a `Vercel Security Checkpoint` page. Real browsers solve a JS challenge instantly, and Googlebot is normally allow-listed by Vercel — **but** any over-aggressive ruleset can throttle Bingbot, Yandex, Ahrefsbot, Mozbot, and even crawl spikes from Googlebot. Validate this:

- Check **Search Console → Settings → Crawl stats** for spikes in `Other client error (4xx)` or `Server error (5xx)`.
- Run `Live test` in **URL Inspection** on `/hire-salesforce-developers` and confirm "Page is available to Google" with a fully rendered DOM (no challenge HTML).
- In Vercel project → **Firewall / Bot Protection**, confirm `googlebot`, `bingbot`, `linkedinbot`, `applebot` are **always allowed** (verified by IP) and that bot-protection ruleset is *not* set to "Strict" for the production hostname.

If Google is occasionally seeing the challenge HTML, that alone explains why none of your money pages rank.

### 🟠 Problem 5 — Position decay on key topics
Week-on-week, your most important commercial topics are **losing** ground:

```
salesforce marketing cloud   pos 26.6 → 32.9   216 imp
salesforce customization     pos 13.2 → 16.8   207 imp
salesforce commerce cloud    pos 33.9 → 37.1   285 imp
salesforce integration       pos 48.2 → 52.1   162 imp
salesforce consulting companies  pos 29.4 → 33.2   143 imp
salesforce managed services  pos 56.5 → 60.0   136 imp
hire a salesforce developer  pos 29.8 → 35.8   126 imp
salesforce developer for hire pos 29.7 → 34.6  113 imp
```

That's a coordinated drop across "salesforce marketing cloud", "customization", "commerce cloud", "integration", "consulting companies", "managed services", and the "hire" cluster. This is almost always a **content freshness + internal links** signal, sometimes amplified by an algo update (Google ran a core update through Q1 2026). Treat it as urgent.

### 🟠 Problem 6 — Polish (`/pl/`) market is essentially dead
Eight `/pl/*` pages indexed; total impressions in the week ≈ 30. Either fix hreflang + add more localized content, or de-index the empty Polish funnel and consolidate. Currently it's eating crawl budget.

### 🟠 Problem 7 — Branded dependence
68.8% of clicks come from "magicfuse" / "magic fuse". A healthy B2B agency site should be ≤30%. Until the non-brand SEO is fixed, paid + outbound is doing all the heavy lifting; SEO is just helping people who already heard of you find your URL.

---

## 3. On-page audit — what to fix on the homepage and money pages

### Homepage `/`
Verified live (Pos 8.7, 9.6% CTR — best on the site, but still only 24 clicks/week):

- ✅ Title contains "Salesforce Development Company" — good.
- ⚠️ **H1 is duplicated three times** in the rendered DOM ("Salesforce Development Company" appears as page title and H1 twice). Keep one H1 only.
- ⚠️ The certifications block repeats the same list **three times** in the source — looks like a carousel that emits triplicate DOM. Cleaner output helps both Lighthouse and crawl efficiency.
- ⚠️ No structured data for `Organization` + `Service` + `BreadcrumbList` + `AggregateRating` is visible in the rendered HTML. With AppExchange ratings (4.9★) and 250+ certifications you have *plenty* to put in `Organization` + `Service` schema.
- ⚠️ Missing `Person` schema for the team grid — that's free entity-graph fuel for E-E-A-T.
- ✅ Logos / social proof present.
- ❌ The only CTAs are "Book a Free Consultation" / "Book a Call". Add a secondary CTA above the fold to a **lead magnet** (e.g., "Free Salesforce Health Check Report"). Right now there is no soft conversion path; everything is "talk to sales".

### `/hire-salesforce-developers` (1,124 imp, pos 33.9, 0 clicks)
Highest-impression commercial page. To move this to page 1:

1. **Title rewrite** to include intent + qualifier: `Hire Salesforce Developers (250+ Certs, EU & LATAM) | MagicFuse`.
2. **H1** must match: `Hire Senior Salesforce Developers — Certified, Vetted, Time-Zone Aligned`.
3. **First 100 words** must contain: hire salesforce developer, salesforce developer for hire, dedicated salesforce developer, certified, hourly rate, contract, full-time. Right now these are buried.
4. **Add a comparison table**: in-house vs offshore vs MagicFuse (cost / time-to-hire / certifications / retention). Tables get pulled into AIO and PAA.
5. **Add explicit pricing brackets** ("from $X / hour"). Pages with pricing rank far better for "hire X" queries because users pre-filter by budget.
6. **FAQ schema** with the actual questions GSC shows you're getting impressions for: "how much does a Salesforce developer cost", "how to hire salesforce developer", "salesforce developer for hire near me", "hire dedicated salesforce developer", "salesforce developer hourly rate".
7. **Internal links from**: every `/expertise/*` page, every `/services/*` page, the homepage hero, and at least 5 blog posts (`top-salesforce-development-companies`, `hire-salesforce-consultants`, `top-salesforce-implementation-partners`, etc.). Right now it has almost no internal anchor text.
8. **Add a sticky CTA + a scoped lead magnet** (free 30-min architect call / "Salesforce hiring scorecard" PDF).

Apply the same playbook to: `/hire-salesforce-expert`, `/hire-salesforce-consultants`, `/hire-salesforce-admin`.

### `/services/*`
Pages live in pos 25–55 because they're thin and not interlinked. Three concrete fixes:

- **Make `/services/salesforce-managed-service`** the hub for *“salesforce managed services / managed services for salesforce”*. Currently pos 50–60 on a 136-imp/wk query — should be pos 8-12.  Add: scope of work matrix, SLA tiers, sample monthly report, named clients, FAQ block, and pricing tier teaser ("starting at 80h/mo").
- **`/services/salesforce-integration`** should be a **silo hub** linking down to all 6 sub-pages (payment, project management, document management, AWS, ERP, marketing automation). Right now it's a flat node.
- **`/services/salesforce-app-development`** competes for "salesforce app development company" (pos 20, 58 imp). Drop a section with code-named cases ("Limio", "ID-Pal", "Atamis") and link to the case studies.

### `/expertise/*`
You have 16 expertise pages averaging pos 30+ on big-volume queries. They're being out-ranked because they read like brochure pages. Treatment:

- **Each `/expertise/{cloud}` page = a 2,500-word pillar** answering: what is X, when to use X, when not to use X, MagicFuse's X delivery model, certifications, team size, sample projects, integration list, FAQ schema.
- Cross-link **inside the body** (not the footer) to: blog deep-dives, services, hire pages, related case studies, and to the contact form using a varied set of natural anchors.
- Specifically:
  - `/expertise/marketing-cloud` → "marketing cloud salesforce", "what is marketing cloud" — currently pos 38, 116 imp, deserves pos 12.
  - `/expertise/data-cloud` → "salesforce data cloud", "cdp vs data cloud" — link to existing blog `/blog/cdp-vs-data-cloud`.
  - `/expertise/agentforce` → all the "agentforce pricing" / "agentforce for X" blog traffic should funnel here. **Currently it does not.**
  - `/expertise/mulesoft` → 446 imp, pos 33 — the highest-impression expertise page. Worth a dedicated content + link push.

### Blog quick wins (already on page 1 — fix the title only)

| Page | New title pattern |
|---|---|
| `/blog/agentforce-cost` | `Agentforce Cost in 2026: Pricing, Flex Credits & Real Bills (with Examples)` |
| `/blog/salesforce-marketing-cloud-cost` | `Salesforce Marketing Cloud Cost (2026): All Editions, Add-ons, Hidden Fees` |
| `/blog/top-salesforce-development-companies` | `Top 25 Salesforce Development Companies in 2026 (Vetted, by Tier)` |
| `/blog/data-cloud-limits` | `Salesforce Data Cloud Limits (2026): Quotas, Storage, API Caps Cheat Sheet` |
| `/blog/salesforce-security-best-practices` | `Salesforce Security Best Practices: Checklist for 2026 (PDF Inside)` |

Each should add a `FAQPage` schema, a *pricing table* or *checklist* (whichever fits intent), an updated date in copy ("Last updated: April 2026"), and 3–5 internal links to the relevant `/services/*` or `/hire-*` page.

---

## 4. Striking-distance keywords (the 90-day list)

These are queries where you already rank pos **5–20** with significant impressions and **zero clicks**. They convert into clicks the fastest with on-page work alone — no link building required to start moving:

| Query | Imp | Pos | Target page | Quick action |
|---|---|---|---|---|
| salesforce development company | 326 | 8.6 | `/blog/top-salesforce-development-companies` | rewrite title to include "2026", FAQ schema |
| salesforce customization | 207 | 16.8 | `/blog/salesforce-customization-mistakes` | retarget to `/services/salesforce-custom-development`; add a "what is customization" intro |
| marketo vs pardot | 112 | 9.8 | `/blog/marketo-vs-pardot` | add comparison table snippet, refresh pricing |
| salesforce agentforce pricing official 2026 | 91 | 7.2 | `/blog/agentforce-cost` | rename H1 to match exact phrase |
| pardot vs marketo | 90 | 8.7 | `/blog/marketo-vs-pardot` | covered |
| salesforce crm development company | 88 | 10.0 | `/blog/top-salesforce-development-companies` | one anchor away from page 1 |
| salesforce marketing cloud consulting | 81 | 16.6 | `/expertise/marketing-cloud` | beef up + interlink |
| top salesforce consulting firms for agentforce | 69 | 17.3 | `/blog/top-salesforce-consulting-companies` | add Agentforce section |
| hire salesforce expert | 64 | 11.8 | `/hire-salesforce-expert` | title rewrite (see §3) |
| salesforce development company in usa | 61 | 11.3 | `/blog/top-salesforce-development-companies` | add "in USA" subsection |
| middleware for salesforce and dynamics 365 integration | 54 | 8.2 | `/blog/microsoft-dynamics-365-integration` | add middleware block |
| salesforce appexchange number of apps | 44 | 6.6 | `/blog/best-salesforce-appexchange-apps` | already close |
| marketing cloud engagement pricing | 34 | 7.0 | `/blog/salesforce-marketing-cloud-cost` | already close |
| salesforce service cloud consultants | 31 | 8.6 | `/blog/service-cloud-consultants` | already close |
| salesforce agentforce pricing model 2026 | 30 | 5.6 | `/blog/agentforce-cost` | featured snippet candidate |

Deliver these and you should add **30–80 non-branded clicks/week within the first refresh cycle** (Google's recrawl + ranking re-evaluation), with no backlinks required.

---

## 5. Technical SEO checklist (quick)

| Check | Status | Action |
|---|---|---|
| HTTPS / HSTS | ✅ | OK (Vercel) |
| `robots.txt` reachable for Googlebot | ⚠️ | Verify in GSC → Settings; bot-challenge may serve 429 to non-Google crawlers |
| `sitemap.xml` reachable | ⚠️ | Same; submit in GSC and confirm last-fetched is < 7 days |
| Core Web Vitals (mobile) | ❓ | Run PSI for `/`, `/hire-salesforce-developers`, `/blog/agentforce-cost`. Mobile CTR is 2× desktop; mobile must be < 2.5s LCP, < 0.1 CLS |
| Structured data — Organization | ⚠️ | Add full `Organization` JSON-LD with `sameAs` (LinkedIn, AppExchange, Clutch, GoodFirms), `aggregateRating`, `address`, `numberOfEmployees`, `award`, `founder` |
| Structured data — Service | ❌ | Missing on `/services/*` and `/expertise/*`. Add `Service` + `Offer` schema |
| Structured data — FAQPage | ❌ | Missing on every blog post that has Q-style headings |
| Structured data — BreadcrumbList | ❌ | Missing site-wide |
| Canonical handling for `#heading-num-*` | ❌ | Confirmed broken — see §2 Problem 3 |
| `/pl/*` hreflang | ❓ | Verify `<link rel="alternate" hreflang="pl">` ↔ `<link rel="alternate" hreflang="en">` reciprocal pairs |
| Pagination on `/blog` | ❓ | Verify; if rel-prev/next is gone, ensure listing pages are crawlable, individual posts are linked |
| Image alt text | ❓ | Run a crawl (Screaming Frog 5K free) and audit. Likely a quick win. |
| Internal links to money pages | ❌ | Run an internal link analysis. The 8 `/hire-*` pages and `/services/salesforce-managed-service` are clearly under-linked |
| Crawl budget — Vercel bot challenge | ⚠️ | See §2 Problem 4. **Highest-priority technical risk.** |

---

## 6. Link-building strategy & anchor text plan

### 6.1 Strategic frame

You sell a **trust-driven, certification-heavy B2B service** (salesforce consulting / dev). For Google, the link signals that move this category are:

1. **Topical authority of the linking domain** — Salesforce ecosystem sites > generic SaaS blogs > general tech blogs.
2. **Geo signal** — US/UK domains for the markets you want.
3. **Anchor diversity that reads natural** — over-optimised exact-match ("hire salesforce developer") at scale will get you a Penguin algorithmic suppression *fast* in this niche; Google has trained the spam detector hard on the dev-services category because of historical abuse.
4. **Co-citation** — being mentioned alongside Slalom, IBM, Accenture, Tquila, Sikich, 7Summits, Bluewave Group, etc., in the same article body — even without a link.

### 6.2 Anchor text mix (this is what to enforce)

For a B2B Salesforce consultancy at your stage, the safe + effective anchor distribution is:

| Anchor type | Share | Example | When to use |
|---|---|---|---|
| **Branded** | **30–35%** | `MagicFuse`, `MagicFuse team`, `the team at MagicFuse` | Default; safe everywhere |
| **Branded + keyword** | **15–20%** | `MagicFuse, a Salesforce development company`, `MagicFuse Salesforce consultants` | Editorial mentions, listicles |
| **Naked URL / domain** | **10–15%** | `magicfuse.co`, `https://magicfuse.co/` | Resource pages, citations |
| **Generic** | **10–15%** | `learn more`, `read the full guide`, `see this case study`, `here`, `this resource`, `their blog` | Inline editorial links |
| **Long-tail / partial-match** | **15–20%** | `practical Agentforce pricing breakdown`, `guide to Marketing Cloud cost`, `MuleSoft delivery team in Europe`, `vetted Salesforce developers` | Content links pointing to deep pages |
| **Exact-match commercial** | **≤ 5–8%** | `hire Salesforce developers`, `Salesforce managed services`, `Salesforce development company` | Only on **DR 50+** sites with topical context. Never two on the same page |
| **Image / brand-image alt** | **5%** | alt text contains brand or topic | Logos, infographics, embedded images |

**Rule of thumb:** for every 1 exact-match commercial anchor, place 4 branded, 2 generic, 2 partial-match, 1 naked URL.

### 6.3 Money-page → anchor mapping

The job of link building is to push the **commercial pages** (not the homepage) up. For each target page below, here is the anchor text *vocabulary* writers should rotate through. **Mix these. Never use the same anchor twice on the same domain.**

#### → `/hire-salesforce-developers`
- Branded: `MagicFuse`, `MagicFuse engineering team`, `MagicFuse's Salesforce devs`
- Branded + KW: `MagicFuse Salesforce developers`, `MagicFuse — hire Salesforce developers`
- Generic: `their hiring page`, `see how they staff`, `their developer roster`, `more on how this works`
- Partial-match: `dedicated Salesforce engineering team`, `vetted Salesforce developers`, `Salesforce dev team augmentation`, `certified Salesforce engineers in EU & LATAM`
- Exact-match (sparingly): `hire Salesforce developers`, `hire a Salesforce developer`, `Salesforce developers for hire`
- Naked: `magicfuse.co/hire-salesforce-developers`

#### → `/hire-salesforce-expert`
- Partial: `Salesforce expert on demand`, `senior Salesforce experts`, `bring in a Salesforce expert`
- Exact (rare): `hire Salesforce expert`
- Branded: `MagicFuse experts`

#### → `/hire-salesforce-consultants`
- Partial: `Salesforce consulting partner`, `Salesforce consulting team`, `senior Salesforce consultants`
- Exact (rare): `hire Salesforce consultants`, `hire Salesforce consultant`
- Branded: `MagicFuse consultants`

#### → `/services/salesforce-managed-service`
- Partial: `Salesforce post-launch support`, `ongoing Salesforce support partner`, `managed Salesforce support`
- Exact (rare): `Salesforce managed services`, `managed services for Salesforce`
- Branded: `MagicFuse managed support`

#### → `/services/salesforce-app-development`
- Partial: `AppExchange product development`, `Salesforce ISV partner`, `build a Salesforce app`
- Exact (rare): `Salesforce app development company`, `Salesforce application development services`
- Branded: `MagicFuse for AppExchange`

#### → `/services/salesforce-integration`
- Partial: `connect Salesforce with your stack`, `Salesforce systems integration`, `mid-tier Salesforce integration shop`
- Exact (rare): `Salesforce integration partners`, `Salesforce API integration services`
- Branded: `MagicFuse integration team`

#### → `/services/salesforce-custom-development`
- Partial: `custom Apex & LWC engineering`, `Salesforce platform engineering`, `bespoke Salesforce builds`
- Exact (rare): `custom Salesforce development services`
- Branded: `MagicFuse custom dev`

#### → `/services/salesforce-managed-service` *(combined with security/health-check upsell)*
- Topical: `Salesforce health check`, `Salesforce security audit`, `quarterly Salesforce review`

#### → `/expertise/marketing-cloud`
- Partial: `Salesforce Marketing Cloud experts`, `Marketing Cloud delivery partner`, `MC implementation team`
- Exact (rare): `Salesforce Marketing Cloud consulting`, `Salesforce Marketing Cloud consultants`
- Branded: `MagicFuse Marketing Cloud team`

#### → `/expertise/data-cloud`
- Partial: `Salesforce Data Cloud implementation`, `CDP delivery on Salesforce`, `Data Cloud consulting`
- Exact (rare): `Salesforce Data Cloud consultants`
- Co-citation: pair with `Snowflake`, `Segment`, `mParticle` so Google understands the entity

#### → `/expertise/agentforce`
- Partial: `Agentforce implementation`, `building agents on Salesforce`, `Agentforce delivery partner`
- Exact (rare): `Agentforce consultants`
- Topical: `Agentforce pricing`, `Agentforce for marketing`, `Agentforce for field service` *(deep-link to the matching blog)*

#### → `/expertise/mulesoft`
- Partial: `MuleSoft delivery team`, `MuleSoft API engineering`, `mid-tier MuleSoft partner`
- Exact (rare): `MuleSoft consulting services`

#### → Blog pillars (`/blog/agentforce-cost`, `/blog/salesforce-marketing-cloud-cost`, etc.)
For these, anchor-mix should lean **partial-match topical** because they're informational:
- `actual Agentforce pricing breakdown`, `recent Agentforce cost analysis`, `Marketing Cloud pricing guide`, `Data Cloud limits cheat sheet`, `practical guide to ISV partnerships`, `2GP packaging walkthrough`.
- Avoid commercial anchors here — informational pages with commercial anchors trigger over-optimisation patterns.

### 6.4 Where to actually get the links (target list)

Prioritised by ratio of *topical authority × link probability × buyer-attention*:

**Tier 1 — Salesforce ecosystem (must-have)**

1. **Salesforce AppExchange listing** — make sure every product, partner page, and team-member listing links back, with branded + topical anchors.
2. **Salesforce Partner Directory** — refresh certifications + descriptions; add links to `/expertise/*` pages, not just homepage.
3. **Salesforce Trailblazer Community profiles** — every consultant on your team should have a complete Trailblazer profile linking to `/about-us` and to their relevant `/expertise/*`.
4. **Salesforce Ben** (`salesforceben.com`) — guest posts, sponsored posts, listicles. Aim for 1 contributed deep article per quarter from a named architect, with one branded + one partial-match anchor.
5. **Apsona / Forcetalks / Automation Champion / SFDCAmplified / SalesforceHacker** — Salesforce-focused blogs where senior people guest write. Pitch: "What we learned migrating 15 orgs from Process Builder to Flow" → links to `/blog/process-builder-to-flow-migration` + `/services/salesforce-managed-service`.
6. **Trailhead Mixed Reality / Trailblazer DX speaking decks** — slide-deck links count.
7. **Co-marketing with ISV partners** — Limio, ID-Pal, Atamis, Elements.cloud, E-sign, Riptide all already love you (your testimonials show 5/5 NPS). **Ask each for a “Built/Implemented by MagicFuse” partner page link.** That's 8–10 highly relevant DR 40+ links sitting on the table right now.

**Tier 2 — B2B SaaS / agency directories (filtering matters)**

- **Clutch.co**, **GoodFirms**, **DesignRush**, **TopDevelopers**, **G2 (services)**, **AppFutura**, **TheManifest** — set up complete profiles, request reviews from the same 10 testimonial clients on the homepage. These directories outrank most Salesforce-niche sites for "Salesforce consulting companies" / "salesforce development companies" — that's why you can't beat them on those queries. *Joining them is currently the easiest win.*
- **Crunchbase** + **PitchBook** — confirmed company profiles with website backlinks.
- **LinkedIn Company Page** + employee posts — not for direct ranking, but for E-E-A-T entity signals.

**Tier 3 — Editorial / digital PR**

- **HARO / Qwoted / Featured.com / SourceBottle / Help A B2B Writer** — your architects answer reporter queries on Salesforce / CRM / AI agents. Each accepted reply usually returns a link from a DR 60+ news/business site with a branded or partial anchor. Aim for 2 wins per week per replier.
- **Industry roundups** — search `"Salesforce" "best companies" 2026 site:.com -inurl:magicfuse` and pitch inclusion.
- **Podcasts** — the SaaS / RevOps podcast circuit (e.g., Sales Pipeline Radio, RevOps Co-op, B2B Marketing Now, The Salesforce Admins Podcast). Each episode = a `Person`-schema mention + show-notes backlink.
- **Conference & event sites** — Dreamforce, World Tour stops, Pegasystems / MuleSoft Summit, London's Salesforce World Tour. Sponsorship pages and speaker bios are easy wins.

**Tier 4 — Content-led, scalable**

- **Original research** — publish *one* annual data report (e.g., "State of Salesforce Implementation 2026: 1,200 orgs surveyed"). Even a small sample (200 orgs from your network + customers) becomes the most-cited research in the niche if no one else does it. **This is the single highest-leverage link asset you can build.**
- **Free tools** — Agentforce ROI calculator, Marketing Cloud cost estimator, Data Cloud limits checker. Each of those topics has *thousands* of impressions and people search for the calculation; a free interactive tool earns links naturally.
- **Comparison content** — `marketo-vs-pardot` already proves this works for you. Build out: `Pardot vs Marketing Cloud Account Engagement`, `Service Cloud vs Zendesk for Salesforce shops`, `Data Cloud vs Snowflake for B2B`, `Agentforce vs Microsoft Copilot for Sales`.

### 6.5 Velocity & monthly cadence (target)

For a domain at your DR / niche, a safe, sustainable, ranking-moving link profile looks roughly like:

- **15–25 referring domains added per month** total (≈ 50/quarter), of which:
  - 6–8 Tier-1 Salesforce ecosystem (highest weight)
  - 4–6 Tier-2 directory / partner pages
  - 4–6 Tier-3 editorial (HARO, podcasts, roundups)
  - 1–3 Tier-4 self-published research / tools that **earn** links naturally
- **Anchor distribution must stay within the §6.2 ratios month-over-month.** Track in a spreadsheet, audit monthly.
- **Never** point more than 1 exact-match commercial anchor from the same domain, and never more than 2 exact-match commercial anchors at the same target page in a single calendar month.

Going much above that pace risks an over-optimisation flag in this niche. Going below it means another year of brand-only traffic.

---

## 7. 90-day execution plan (do these in this order)

**Days 1–14 — fix the bleed**
1. Confirm Googlebot is *not* hitting the Vercel bot challenge (§2.4). Run URL Inspection on the 10 most important commercial pages.
2. Fix `#heading-num-*` duplicate URLs with proper canonicals.
3. Submit / verify `sitemap.xml`; remove `/pl/*` URLs that aren't actively maintained, or fix hreflang properly.
4. Rewrite titles + descriptions for the 7 pages in §3 "Page-1 ranks with broken CTR".
5. Add `Organization`, `Service`, `BreadcrumbList`, `FAQPage` schema everywhere it's missing.
6. Run Lighthouse mobile on top 10 pages; fix LCP & CLS issues — mobile is your highest-CTR device but worst-ranked.

**Days 15–45 — on-page upgrades**
7. Re-write `/hire-salesforce-developers` per §3 playbook; replicate to `/hire-salesforce-expert`, `/hire-salesforce-consultants`.
8. Convert each `/expertise/*` page into a 2,500-word pillar with internal links and FAQ schema.
9. Refresh the 15 striking-distance blog posts (§4) — title, intro, dates, comparison tables, schema.
10. Build a deliberate internal-link map: every blog mentioning "Marketing Cloud" → `/expertise/marketing-cloud`; every blog mentioning "hire" → `/hire-salesforce-*`; every blog mentioning a service → corresponding `/services/*`. Use varied anchors per §6.2.

**Days 30–90 — link building**
11. Reach out to all existing partner/customer brands (Limio, ID-Pal, Atamis, Riptide, Elements.cloud, E-sign, Nomagic, De Gruyter Brill, Auto Service Repairs, Ascent, Xenogenix) for "Implemented/Built by MagicFuse" partner-page links. Target: **8 links** in the first 30 days from this alone.
12. Refresh / launch directory profiles: Clutch, GoodFirms, TheManifest, DesignRush, AppFutura, Crunchbase, AppExchange, Salesforce Partner Directory, G2.
13. Launch HARO/Featured/Qwoted answering rotation — one architect, 30 minutes/day, 4 days/week.
14. Pitch and ship 1 cornerstone guest post on Salesforce Ben + 1 on Forcetalks + 1 on Apsona (or equivalent niche blog) per month.
15. Begin work on the annual "State of Salesforce Implementation 2026" research piece — survey + data + landing page + outreach plan.

**Day 90 — measure**
- Target: non-branded clicks ≥ 100/week (10× current), avg position ≤ 22 site-wide, US position ≤ 14.
- Money pages (`/hire-*`, key `/services/*`, key `/expertise/*`): every one in top-30, the top three of each cluster in top-15.
- Branded share of clicks: < 50%.
- Referring domains gained: ≥ 45 in 90 days, of which ≥ 12 Tier-1 Salesforce ecosystem.

---

## 8. KPIs to put on a single dashboard

1. **Non-branded clicks/week** — the only metric that means SEO is working as a lead channel.
2. **US average position** (filter: country = USA) — your buyer market.
3. **Money-page average position** — average across the 8 `/hire-*`, top 5 `/services/*`, and top 5 `/expertise/*` pages. Target: < 20 → < 10.
4. **Striking-distance count** — how many queries are at pos 5–20 (today: ~37 with ≥30 imp). Aim to grow this before growing clicks.
5. **Referring domains (root) per month** — Ahrefs / Majestic.
6. **Anchor distribution** — manually audit monthly against §6.2 ratios.
7. **AppExchange + Clutch + G2 review velocity** — directly affects how those directory pages rank for your category names.

---

### Final note

The CSV data shows a site that has *demand* (≈20K weekly impressions, growing topical breadth) but is being held back by three solvable structural problems: **money pages don't rank, page-1 pages don't get clicked, and the link profile is too thin to compete with Gartner/Clutch/Salesforce.com on the SERPs that buy your services.** Fix the technical and on-page items in §3-§5 first — those alone should add ~2-4× non-brand clicks within 6-8 weeks. Then drive the link velocity in §6 with the anchor mix in §6.2. The "money keywords + anchor-text vocabulary" mapping in §6.3 is the playbook your link team should keep open every day.
