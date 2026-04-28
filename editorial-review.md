# Editorial Review: "Salesforce AppExchange Security Review: How to Prepare and Pass [2026 Guide]"

**Reviewer role:** Senior Salesforce content writer / ISV editor
**Goal of this review:** (1) fact-check the draft against current Salesforce documentation; (2) propose a tighter structure; (3) provide rewritten "real text" examples for the weakest sections; (4) leave editorial comments the writer can act on.

---

## 1. Executive verdict

The draft is *publishable with edits*. Voice and positioning are strong (case-led, ISV-credible). The main risks are:

1. **A factual error in the pricing table** that will undermine credibility for any reader who actually publishes on AppExchange.
2. **Outdated Apex security guidance** (`WITH SECURITY_ENFORCED` is still valid, but Salesforce now explicitly recommends `WITH USER_MODE` / `as user` for code targeting Spring '23+ orgs — which any 2026 review submission is).
3. **Weak structural signals**: H2/H3 hierarchy is flat, the checklist is buried below "what to do if you fail", and the case study is mixed into the explanatory body in a way that hurts skimmability.
4. **Some claims that should be sourced or softened** ("about half of all initial submissions fail", "most pass on the second attempt") — these are repeated in Salesforce's own materials but should be attributed once.

Below: fact-check, then proposed structure, then rewritten passages with inline editorial comments.

---

## 2. Fact-check against Salesforce documentation

I cross-referenced every concrete claim in the draft against (a) Salesforce Developers, (b) the Salesforce Security Guide Spring '26, (c) the Partner Security Portal, (d) Trailhead's Security Review Submission Process module, and (e) the Spring '26 / Summer '25 release-note coverage.

### 2.1 Pricing — needs correction

| Claim in draft | Status | Source / what's actually true |
|---|---|---|
| "$999 per submission" for paid apps | **Correct.** | Trailhead (ISV Security Review module) and the 2023 Salesforce Developers blog post on the per-attempt fee model both state $999 per attempt. ([developer.salesforce.com](https://developer.salesforce.com/blogs/2023/04/prepare-your-app-to-pass-the-appexchange-security-review)) |
| "Annual listing fee — $150 per app" | **Incorrect / outdated.** | Salesforce **eliminated the $150 annual listing fee on March 16, 2023**, when it moved to the per-attempt model. There is no $150/yr listing fee in 2026. Some bloggers still mention it because the original press from 2014 referenced it, but Salesforce's own 2023 announcement says: "The $2,550 initial review fee is eliminated. The $150 annual fee is eliminated. The security review fee is $999 per attempt." This needs to come out of the table. |
| "No fee (fee waiver code available)" for free apps | **Correct.** | Free apps can request a fee waiver; Salesforce reserves the right to revisit this policy. Acknowledge that explicitly so the article ages well. |
| "Resubmission (false-positive justifications only, no code changes) — No additional fee" | **Correct.** | Confirmed by Salesforce Stack Exchange answer citing the Trailhead module: re-submitting the same package with false-positive explanations is not a new attempt. |
| "Periodic re-review every 6 months to 2 years" | **Mostly correct, but soften.** | Salesforce describes periodic re-reviews triggered by risk factors and changes; the 6-months-to-2-years cadence is widely repeated in partner community posts but is not a fixed contractual interval. Phrase as "periodically — Salesforce determines the cadence based on risk factors and the changes you've shipped." |

> **EDITORIAL COMMENT (high priority):** Removing the $150 annual line is non-negotiable. Anyone who has actually paid Salesforce since 2023 knows there is no annual listing fee, and leaving it in will get the article called out in comments / LinkedIn. Replace that row with a row about the **PNR (Percentage Net Revenue) royalty** — that is the real recurring cost partners care about, and it is the most common gap in articles like this.

### 2.2 Process timing — generally correct, can be sharper

- "Submission Verification (1–2 Business Days)" — matches Salesforce's published guidance.
- "Security Testing (4–6 Weeks)" — matches; Salesforce communicates this as a typical, not guaranteed, window.
- "About half of all initial submissions fail" / "most pass on the second attempt" — both phrasings appear in Salesforce's own materials (Trailhead module says "Most submissions pass on the second attempt"). Attribute once and move on.

### 2.3 Apex guidance — partially out of date

The draft says:

> "use `WITH SECURITY_ENFORCED` in SOQL queries, call `stripInaccessible()` in Apex before returning data, and use `Schema.DescribeSObjectResult` for runtime permission checks."

This is the **pre–Spring '23 playbook**. Salesforce's *current* recommendation, as documented in the LWC Developer Guide → "Secure Apex Classes" page and reiterated in the AppExchange security review prep blog:

- **Preferred:** `WITH USER_MODE` on SOQL/SOSL, and `insert as user` / `Database.insert(records, AccessLevel.USER_MODE)` on DML. This enforces object, field, *and* record-level security in one clause and reports all FLS errors (not just the first), and it covers `WHERE` and `ORDER BY` clauses, which `WITH SECURITY_ENFORCED` does not.
- **Use `Security.stripInaccessible()`** when you want graceful degradation instead of a `QueryException`.
- **Use `WITH SECURITY_ENFORCED`** only when you have to support orgs older than Spring '23 (rare in 2026).
- **`Schema.DescribeSObjectResult` / `isAccessible()`** is now explicitly described by Salesforce as "legacy" with "many more lines of boilerplate code." Recommend it only when neither of the above fits.

> **EDITORIAL COMMENT (high priority):** This is the single most common sign that a "2026 guide" has been recycled from a 2022 draft. If you tell ISVs to default to `WITH SECURITY_ENFORCED` in 2026, a Salesforce reviewer reading the article will quietly close the tab. Lead with `WITH USER_MODE`, mention `stripInaccessible()` as the graceful-degradation pattern, and demote `WITH SECURITY_ENFORCED` to a one-line "still valid; required if you target pre-Spring '23 orgs." See rewritten code block in §4.

### 2.4 Tooling — Chimera retirement is correct

- **Chimera DAST scanner retired June 16, 2025** — confirmed by the partners.salesforce.com community post and the Partner Security Portal banner ("Chimera is no longer supported"). The draft's date and recommendation (OWASP ZAP / Burp Suite as replacements) are both consistent with Salesforce's own guidance and Aquiva Labs' Summer '25 readout.
- **Checkmarx — 3 free scans per review** — confirmed on the Source Scanner Customer Portal. Add the constraint that the **packaging org must be linked to the Partner publisher account** and that scans must be submitted from an **Author Apex account on a business email domain** — that's where ISVs most often trip up before they even reach the queue.
- **Salesforce Code Analyzer** — the draft positions it as "free, good complement to Checkmarx." Correct. Optionally mention it is the open-source SF CLI plugin (`sf scanner run`) and is the engine Salesforce itself recommends running pre-commit / in CI.

### 2.5 Spring '26 platform changes the article should at least nod to

The draft's "What's New (2025–2026)" section talks about AI/ML scrutiny, zero trust, and performance testing — fine, but it misses two Spring '26 release-note items that *directly* affect what passes review:

1. **Connected Apps creation is restricted as of Spring '26.** New integrations must use **External Client Apps (ECAs)**. Existing Connected Apps continue to work, and Connected Apps inside managed packages remain supported, but architects designing a *new* AppExchange integration should plan for ECAs. This is from the Salesforce Security Guide v66.0 (Spring '26) and the Spring '26 Architect Highlights.
2. **Shorter certificate lifespans.** From March 2026, new CA-signed certs are capped at ~200 days, dropping to ~100 days in 2027. Self-signed certs are exempt. This matters for any ISV with external endpoints (which the draft already calls out as a common rejection cause).

> **EDITORIAL COMMENT:** Adding even two sentences on each of these makes the "2026 Guide" framing earn its name. As written, the "what's new" section could have been published in 2024.

### 2.6 Other small fact-check notes

- **"managed packages, Lightning components, OmniStudio solutions, and apps with external endpoints or web apps"** — accurate scope. Consider adding **2GP (Second-Generation Managed Packages)** and **Agentforce / AgentExchange** explicitly, since Salesforce now uses the consolidated AgentExchange brand and 2GP is the default packaging story for new ISVs.
- **OWASP Top 10 mapping** — the draft maps "Injection → SOQL injection, Broken Access Control → CRUD/FLS / sharing, Security Misconfiguration → org settings / protected custom settings." That mapping is accurate and well chosen; keep it.
- **"managed package and ID stay the same … no additional fee"** — accurate per the Trailhead module language ("If we discover security vulnerabilities in your submission, then you fix and resubmit, that's another attempt"), with the false-positive-only carve-out the draft already mentions.

---

## 3. Proposed structure (senior-writer cut)

The draft's outline is fine but flat. Here is the structure I'd ship, with the rationale for each move:

```
H1  Salesforce AppExchange Security Review: How to Prepare and Pass [2026 Guide]

    [Lede: keep the Atamis story, but tighten to 2 short paragraphs.]
    [Trust block: 11 years, 11+ ISV projects, 270+ certifications — one line, not two.]
    [Promise: what the reader will be able to do after reading.]

H2  What the AppExchange security review actually is
    H3  What Salesforce tests for
    H3  Who has to pass it (managed 1GP/2GP, LWC, OmniStudio, Agentforce/AgentExchange, anything with external endpoints)

H2  What it costs in 2026
    [Corrected pricing table — see §4.1]
    H3  The hidden cost most articles miss: PNR (revenue share)
    H3  Budget rule of thumb: assume one resubmission

H2  How the review process works, stage by stage
    H3  Stage 1 — Preparation
    H3  Stage 2 — Submission via the Publishing Console
    H3  Stage 3 — Submission verification (1–2 business days)
    H3  Stage 4 — Security testing (4–6 weeks)
    H3  Stage 5 — Results and report

H2  What's new for 2026 (this is where you earn the year in the title)
    H3  External Client Apps replace Connected Apps (Spring '26)
    H3  Certificate lifespans shrink to ~200 days
    H3  AI / ML scrutiny expanded
    H3  Performance security testing for high-volume apps
    H3  Chimera retired — what to use instead
    H3  Zero-trust expectations

H2  The eight reasons most apps fail (ranked)
    H3  CRUD/FLS violations
    H3  SOQL injection
    H3  XSS in Visualforce / LWC
    H3  Insecure auth and session handling
    H3  Sharing-model violations
    H3  Insecure external endpoints
    H3  Incomplete documentation
    H3  Vulnerable third-party libraries  <-- add; this is a common 2026 finding

H2  How to prepare, step by step
    H3  Build security in from day 1
    H3  Read the four documents that actually matter
    H3  Run the right scanners at the right time
    H3  Document false positives properly (with template)
    H3  Run Salesforce Health Check
    H3  Build a clean test environment
    H3  Book office hours

H2  The pre-submission checklist
    [Move the checklist UP — it is the most-saved, most-shared part of an article like this. Putting it before the failure-recovery section means readers who bounce still get the highest-utility piece.]

H2  If you fail: what to do next
    H3  Read the report like a security engineer, not a project manager
    H3  Search for the *class* of issue, not just the instance
    H3  Manual pen-test the gaps automated tools missed
    H3  Resubmit cleanly

H2  Case studies — what we've seen ship
    H3  Atamis (procurement)
    H3  Elements.cloud
    H3  [one more if you can — diversity of industries reads better]

H2  How MagicFuse helps ISVs through the review
    [Keep short — readers know it's a CTA section.]

H2  FAQs
```

Two structural moves are doing most of the work:

1. **Pull the checklist above the failure-recovery section.** A checklist is bookmark bait. Burying it ~80 % of the way down the article wastes its SEO and link-magnet value.
2. **Group the case studies.** Right now Atamis is in the lede, Elements.cloud is in the MagicFuse section, and there's a vague "we've seen similar patterns" sentence in between. Either lead with one case and consolidate the others into a dedicated "case studies" H2, or move all of them into the MagicFuse section and tighten the lede. Don't do both.

---

## 4. Rewritten passages (real text examples)

Below: the four sections that most need the rewrite, with comments on what changed and why.

### 4.1 Pricing table — corrected

> **EDITORIAL COMMENT:** Replaces the inaccurate "$150 annual listing fee" row with a more useful PNR (revenue share) row and a "fee waiver" footnote for free apps.

**Real text example:**

> ## What the security review costs in 2026
>
> Salesforce moved to a per-attempt fee model on March 16, 2023, eliminating the old $2,550 initial fee and the $150 annual listing fee. The current structure is simpler — and easier to underestimate.
>
> | Cost | Paid apps | Free apps |
> |---|---|---|
> | Initial security review | $999 per attempt | No fee (waiver code via Partner support case) |
> | Resubmission with code changes | $999 per attempt | No fee |
> | Resubmission with false-positive explanations only (no code changes) | No additional fee | No additional fee |
> | Periodic re-review (Salesforce-initiated, code changes required) | $999 per attempt | No fee |
> | AppExchange revenue share (PNR) | Tiered — typically 15–25 % of net revenue, with marginal-PNR reductions as you scale | N/A |
> | Annual listing fee | **None** (eliminated March 2023) | None |
>
> Two costs catch first-time ISVs off-guard:
>
> 1. **Resubmission attempts.** If Salesforce finds a vulnerability and you ship a code fix, that is a new $999 attempt. Given the ~50 % first-attempt pass rate Salesforce itself cites, budget for at least two attempts on your first listing.
> 2. **PNR (Percentage Net Revenue).** This is not a security-review fee, but it is the recurring cost ISVs forget when they price their app. The standard AppExchange rate has historically been a 15–25 % share of net revenue, with Salesforce's Marginal PNR Model reducing the marginal rate once you cross specific revenue thresholds. Confirm your rate in your Partner Application Distribution Agreement (PADA) — every ISV's contract is slightly different.
>
> Salesforce also conducts periodic re-reviews. There is no fixed cadence; Salesforce decides based on the changes you have shipped, the risk profile of your app, and how long it has been since the last review. Plan for at least one full re-review cycle within the first two years on the listing.

**What changed:**
- Removed the false $150/year row.
- Added a PNR row (the cost ISVs actually feel).
- Removed the "every 6 months to 2 years" hard interval — it is community lore, not policy.
- Footnoted the free-app waiver instead of treating it as a permanent line item; Salesforce reserves the right to revisit.

---

### 4.2 Apex security guidance — modernized

> **EDITORIAL COMMENT:** This is the highest-leverage rewrite in the article. The current text recommends a 2022-era pattern. Lead with `WITH USER_MODE`; demote `WITH SECURITY_ENFORCED`; mention `stripInaccessible()` as the graceful-degradation option.

**Real text example (replaces the "CRUD/FLS Violations" subsection):**

> ### CRUD/FLS violations — the #1 cause of rejections
>
> Apex runs in system mode by default. That means your code can read and write any object and any field, regardless of what the running user is allowed to see in the UI. If you do not explicitly enforce object permissions, field-level security (FLS), and sharing, your code will leak data the user's profile is supposed to restrict — and Salesforce reviewers flag this more than any other issue.
>
> **In 2026, the recommended pattern is `WITH USER_MODE` for queries and `as user` for DML.** Both were generally available in Spring '23 and are now the default Salesforce-recommended approach. Use them whenever your package targets Spring '23 (API v57.0) or newer — which any new AppExchange submission does.
>
> Query in user mode:
>
> ```apex
> // Enforces object, field, AND record-level security in one clause.
> // Reports ALL FLS errors (not just the first), and applies to WHERE / ORDER BY.
> List<Account> accounts = [
>     SELECT Id, Name, Industry
>     FROM Account
>     WHERE Industry = :industry
>     WITH USER_MODE
> ];
> ```
>
> DML in user mode:
>
> ```apex
> // Honors the running user's create/update permissions on every field.
> insert as user accounts;
>
> // Or, with the explicit AccessLevel parameter:
> Database.insert(accounts, AccessLevel.USER_MODE);
> ```
>
> Graceful degradation with `stripInaccessible()` (use when you do not want a `QueryException` to surface):
>
> ```apex
> List<Account> accounts = [SELECT Id, Name, Industry FROM Account];
>
> SObjectAccessDecision decision = Security.stripInaccessible(
>     AccessType.READABLE,
>     accounts
> );
>
> if (!decision.getModifiedIndexes().isEmpty()) {
>     // Decide whether to silently drop fields, log, or throw a friendlier error.
> }
>
> return decision.getRecords();
> ```
>
> **What about `WITH SECURITY_ENFORCED`?** Still valid, still passes review, but it only enforces FLS on the `SELECT` and `FROM` clauses, ignores `WHERE` and `ORDER BY`, and reports only the first inaccessible field. Use it only if you must support orgs older than Spring '23. The legacy `Schema.DescribeSObjectResult.isAccessible()` pattern is no longer recommended for new code — Salesforce's own documentation now describes it as boilerplate-heavy and reserves it for cases the newer clauses cannot cover.
>
> If you change one thing in your codebase before submitting: do this.

**What changed:**
- Replaces the `WITH SECURITY_ENFORCED`-first recommendation with `WITH USER_MODE`-first.
- Adds three concrete code blocks (real text the reader can paste), which is what every developer-facing 2026 guide should do.
- Keeps `WITH SECURITY_ENFORCED` and `DescribeSObjectResult` as fallback positions, framed honestly.

---

### 4.3 "What's new (2025–2026)" — earns the year

> **EDITORIAL COMMENT:** Add the two Spring '26 items the draft is missing — Connected Apps → External Client Apps, and shorter certificate lifespans. Both are documented in Salesforce's Spring '26 release notes and the Spring '26 Security Guide (v66.0).

**Real text example (new subsections to add to the existing "What's new" H2):**

> ### External Client Apps replace Connected Apps (Spring '26)
>
> Starting Spring '26, Salesforce disabled the creation of new Connected Apps in all orgs by default. Existing Connected Apps continue to work — including those installed via managed packages — but new integrations should be built as **External Client Apps (ECAs)**.
>
> For ISVs designing a new AppExchange integration in 2026, this means:
>
> - Use ECAs for any new inbound integration. They support only modern OAuth flows and remove legacy patterns like the username/password flow.
> - If your managed package already creates a Connected App, you can keep shipping it — Salesforce explicitly carves out package-installed Connected Apps. But plan a migration path; the long-term direction is clear.
> - Audit every Connected App in your packaging org for OAuth flow types, scope, and secret-storage. Anything still using the username/password flow needs to be re-architected before submission.
>
> Salesforce also continues to phase out the legacy SOAP `login()` call and is deprecating session IDs in outbound messages. If your app still authenticates against either, the security review team will flag it.
>
> ### Certificate lifespans are shrinking
>
> Effective March 2026, new CA-signed certificates are capped at roughly 200 days, dropping to roughly 100 days in 2027. Self-signed internal SSO certificates are not affected.
>
> If your app has external-facing endpoints — or relies on mutual TLS, SAML, or API integration certificates — automate certificate rotation now. The security review will not fail you for a long-lived cert today, but a forgotten cert that expires three weeks after listing is an avoidable customer-facing outage.

**What changed:**
- Adds two genuinely 2026-specific items so the "[2026 Guide]" tag in the H1 is earned.
- Frames each from the ISV's point of view ("here's what to do") instead of just summarizing the release note.

---

### 4.4 Lede — tightened

> **EDITORIAL COMMENT:** The current lede works, but it buries the promise of the article behind two long paragraphs and a credibility block. Tighten to three short paragraphs: hook → stake → promise.

**Real text example:**

> # Salesforce AppExchange Security Review: How to Prepare and Pass [2026 Guide]
>
> When we picked up Atamis — a procurement platform built mostly in Visualforce by a team without deep Salesforce experience — the product worked, but the codebase was nowhere near AppExchange-ready. We restructured the architecture, raised test coverage, prepared the false-positive documentation, and walked the team through submission. Atamis passed and now ships with strong AppExchange reviews.
>
> Not every team gets that on the first try. Roughly half of all initial submissions fail the Salesforce AppExchange security review. Each rejection on a paid solution costs **$999**, delays your launch by weeks, and gives competitors a head start. The good news, per Salesforce's own ISV training: **most submissions pass on the second attempt** — once developers know exactly where to focus.
>
> This guide covers the security review process as it actually works in 2026: what the Salesforce Product Security team tests for, what changed in Spring '26, the eight failure modes that account for almost every rejection we see, and the pre-submission checklist we run on every ISV engagement. It draws on 11+ ISV projects (Elements.cloud, Atamis, and others) and 150+ Salesforce engagements over 11 years.

**What changed:**
- Drops the "11+ ISV projects and 150+ Salesforce engagements" until the third paragraph so the reader hits the *promise* before the *credibility*.
- Attributes the "most pass on the second attempt" line to Salesforce's own training, which is where it actually comes from.
- Bolds the two numbers a hurried reader needs to remember ($999, second attempt).

---

## 5. Section-by-section editorial comments

These are the smaller calls — none are blockers, but most of them are the difference between a good article and a sourced, citation-worthy one.

### Lede / case study placement
- Replace with the tightened version in §4.4.
- "Atamis, a procurement platform built by someone without deep Salesforce experience" — say "a team without deep Salesforce experience." "Someone" reads slightly dismissive.

### "What Is the Salesforce AppExchange Security Review?"
- Add **2GP** and **Agentforce / AgentExchange** to the list of listing types. Both are in scope as of 2026 and not naming them dates the article.
- "Salesforce-specific risks like CRUD/FLS violations and unsafe use of protected custom settings" — good. Optionally add **insecure use of custom metadata for secrets** and **session-keep-alive abuse**, both common 2026 findings.

### "Pricing and Fees"
- Replace with §4.1.
- Move from "Pricing and Fees" to "What it costs in 2026." Reads less like a brochure.

### "How the Salesforce AppExchange Security Review Process Works"
- Stages are clear. Two improvements:
  - **Stage 2 (Submission):** explicitly call out that the **packaging org must be linked to the Partner publisher account** before Checkmarx will give you the 3 free scans, and that **scans must be submitted by an Author Apex account on a business email domain**. These are the most common pre-submission tripwires.
  - **Stage 5 (Results):** the line "the report lists vulnerability classes, not every single instance" is genuinely useful and should be a callout box, not a parenthetical sentence.

### "What's New (2025–2026)"
- Add the two Spring '26 items in §4.3.
- "AI and ML Security Evaluation" — the framing is right. Add one concrete artifact: a **data-flow diagram** for any AI feature is something the security team explicitly asks for. That makes the advice operational.
- "Zero-Trust Security Requirements" — fine, but Salesforce frames this less as a hard requirement and more as a recommended posture. Consider softening "Salesforce now recommends" to "Salesforce's published guidance increasingly aligns with…".

### "Common Reasons Apps Fail"
- **CRUD/FLS** — replace with §4.2.
- **SOQL Injection** — accurate. Add `Database.query` with bind variables (Spring '24+ supports `Database.queryWithBinds`) as the modern dynamic-SOQL pattern.
- **XSS** — accurate. Add a sentence on **`lwc:dom="manual"` and `innerHTML` in LWC** as the LWC-equivalent footgun, since the current text only mentions Visualforce's `escape="false"`.
- **Insecure Authentication** — strong. Add a line on **External Client Apps** as the 2026-forward path (links to §4.3).
- **Sharing Model Violations** — accurate.
- **Incomplete Documentation** — accurate. Worth listing the *exact* artifacts Salesforce expects: usage doc, scanner reports, false-positive doc, valid admin credentials with My Domain enabled, and a 2-minute walkthrough video for any non-trivial business flow. The video tip is in Salesforce's own guidance and is rarely mentioned in third-party articles.
- **Insecure External Endpoints** — add a line on certificate lifespans (links to §4.3).
- **Add a ninth section: Vulnerable third-party libraries / dependencies.** Salesforce checks JS bundles in LWC and Aura against the National Vulnerability Database; outdated jQuery / Lodash / Moment versions are a recurring 2026 finding.

### "How to Prepare … Step by Step"
- Strong. Two adds:
  - In **"Run Security Scanners Early and Often,"** add **`sf scanner run`** (the SF CLI command) as the concrete invocation for Salesforce Code Analyzer. The article currently says "free, run frequently as you code," but never names the command.
  - In **"Prepare Test Environments and Documentation,"** add the My Domain step before Lightning components, and add **enable Multi-Factor Authentication** on the admin user before sharing credentials. Salesforce reviewers flag MFA-disabled review-credentials in 2026.

### "Salesforce Security Review Checklist"
- Move this section *up* in the article (see §3 structure).
- Add lines:
  - Code Security: "WITH USER_MODE used in new queries; WITH SECURITY_ENFORCED only where legacy support requires it."
  - External Components: "Certificate rotation policy documented; no cert exceeds 200 days as of March 2026."
  - Documentation: "2-minute walkthrough video included for any non-trivial flow."

### "What to Do If Your App Fails"
- Strong. The "they list classes of vulnerability, not every instance" insight should be a callout, not a sentence inside a paragraph.
- Add: **"Run the same scanner against your fix branch before resubmitting."** It is the single highest-leverage prevention against a third attempt.

### "How MagicFuse Helps"
- Tighten by 30 %. Specifically: the "11+ years … 270+ certifications … 80+ certified specialists … peaked at 70 … currently around 30 developers" passage is *dense* with numbers and slows the reader right at the conversion moment. Pick two numbers, not five.
- The Atamis story is now told twice (lede + this section). Keep it once — in the case-studies H2 — and reference it lightly here.

### FAQs
- "How much does the Salesforce security review cost?" — fix the $150 annual fee here too. It appears nowhere in the FAQ now, which is good; just make sure the table and the answer match.
- "What scanners are required?" — add `sf scanner run` and link to the Salesforce Code Analyzer GitHub.
- Add an FAQ: **"Do I need to redo the security review for every package version?"** — short answer: no, not until Salesforce explicitly demands a re-review, with the exception of significant metadata changes. This is the question every ISV manager asks at week 2.

---

## 6. SEO / metadata

- **Meta title (53 chars)** — "Salesforce AppExchange Security Review: 2026 Guide" — good, well within the 50–60 char window.
- **Meta description (152 chars)** — "Step-by-step guide to the Salesforce AppExchange security review process. Checklist, pricing, common pitfalls, scanner tools, and expert tips." — fine. If you want to lean harder on the 2026 freshness, swap "expert tips" for "Spring '26 changes" so the SERP snippet shows the year. New version (151 chars):
  > Step-by-step guide to the Salesforce AppExchange security review in 2026. Checklist, pricing, common pitfalls, scanner tools, Spring '26 changes.
- **H1** — keep.
- **Internal links** — make sure "AppExchange Security Review Guide (developer.salesforce.com)" links to the *current* Trailhead module URL (the path `trailhead.salesforce.com/content/learn/modules/isv_security_review/` is stable).
- **Schema** — if your CMS supports it, add `FAQPage` JSON-LD on the FAQ section. With this many questions and this much keyword overlap, the SERP gain is non-trivial.

---

## 7. Two-line ship/no-ship summary

**Ship after:** (a) fix the $150 annual fee error in the pricing table, (b) lead Apex guidance with `WITH USER_MODE`, (c) add the two Spring '26 items (ECAs + cert lifespans), (d) move the checklist above the "what to do if you fail" section.

Everything else in this review is polish — high-value polish, but polish. The article is fundamentally well-positioned and well-voiced; it just needs to be brought into 2026.
