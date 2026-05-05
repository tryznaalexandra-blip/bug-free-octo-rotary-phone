# Nurture Strategy — Lost SQLs (ActiveCampaign)

Source list: `MF lost SQL - deals-22392613-1740.pdf` (~260 contacts across 9 pages).
Goal: re-engage lost Sales Qualified Leads with low-effort, high-relevance content that maps to *why* the deal was lost. Re-qualify the warm ones, stay top-of-mind for the rest, and feed re-opened opps back to sales.

> Audience signal from the list: mostly B2B SaaS / Salesforce-ecosystem buyers (Sales Ops, RevOps, Founders, IT, Heads of Delivery) in EU + North America, with some APAC. Decision-makers, mid-market.

---

## 1. Segmentation by Lost Reason

Counts are approximate, grouped from the full export. Segments are **ordered by ease of re-engagement** — start at the top, the wins are easiest there.

| # | Segment (AC tag)            | ~Count | Lost reasons rolled up                              | Re-engage difficulty | Why it's easy / hard                                    |
|---|------------------------------|--------|------------------------------------------------------|----------------------|----------------------------------------------------------|
| 1 | `seg-not-ready-yet`          | ~35    | "Client is not ready yet"                           | Easy (warmest)        | They liked us, just timing. Pure waiting game.           |
| 2 | `seg-tm-no-resources`        | ~30    | "TM has no resources" (we couldn't deliver)         | Easy                  | We said no, not them. Our fault to fix.                  |
| 3 | `seg-no-answer`              | ~25    | "No answer"                                         | Easy-medium           | Maybe wrong moment / wrong channel.                      |
| 4 | `seg-not-relevant-anymore`   | ~35    | "Not relevant anymore" / "Not relevant request"     | Medium                | Need is gone today, but situation can change.            |
| 5 | `seg-found-another`          | ~25    | "Found another contractor"                          | Medium                | Competitor displacement — wait for renewal moment.       |
| 6 | `seg-budget-too-low`         | ~12    | "Budget too low" / "We are too expensive"           | Medium                | Show value tier / smaller engagement.                    |
| 7 | `seg-project-too-small`      | ~7     | "Project too small"                                 | Medium                | Refer to partner / reposition for future growth.         |
| 8 | `seg-tm-no-expertise`        | ~8     | "TM has no expertise"                               | Hard                  | Only re-open if we built the capability.                 |
| 9 | `seg-not-mature`             | ~6     | "Not mature client" / "Not mature"                  | Hard                  | Long horizon — educate, don't sell.                      |
| 10| `seg-suppress`               | ~10    | "Hired internally", "Recruitment fail", "Legal/Security issues", "We failed", "Trump", "Interview failed", "company was acquired" | Suppress / manual review | Not worth automating against. |

Apply tags in AC on import. Suppress segment 10 from automated nurture.

---

## 2. Topic Picks — Easy Ones That Map to the Lost Reason

The brief said *"choose topics, but easy ones that might work because of [the lost reasons]"*. So each topic below is intentionally low-effort: short-form, can be repurposed from existing content, and speaks directly to the reason the deal stalled.

### Segment 1 — "Client is not ready yet" → **Readiness content**
These prospects basically said *come back later*. Help them feel ready.

- **T1.1** "5 signs you're ready to scale your Salesforce / RevOps team" (checklist)
- **T1.2** "When does it stop making sense to do this in-house?" (decision matrix)
- **T1.3** Quarterly "What's changed since we spoke" — 1 customer story + 1 product/regulatory update
- **T1.4** A 15-minute "readiness audit" call as the CTA (low commitment)

### Segment 2 — "TM has no resources" → **We have capacity now**
This is *our* fault, not the prospect's. The single best message is "we can do it now."

- **T2.1** "Capacity update — we can take on a [role / project type] starting [month]" (1-line email)
- **T2.2** Case study of a similar client we *did* deliver for
- **T2.3** "Bench spotlight": short profile of a consultant/team available next month
- **T2.4** CTA: re-book the original scoping call

### Segment 3 — "No answer" → **Pattern interrupt + value bait**
They never responded. Don't repeat the same pitch — switch channel and message.

- **T3.1** Single-question email: "Still on your roadmap, or should I close the loop?" (the Breakup email)
- **T3.2** A short benchmark / data point relevant to their industry (1 chart, 1 takeaway)
- **T3.3** LinkedIn touch + email (multi-channel, same week)
- **T3.4** CTA: reply Y/N

### Segment 4 — "Not relevant anymore" → **Adjacent value**
Their need shifted. Show we cover the adjacent problem too.

- **T4.1** "What [their role] are prioritising in [next quarter]" (trend roundup)
- **T4.2** Case study from their industry, different use case than the original
- **T4.3** 1-question survey: "What's on your plate now?" (re-segment them based on reply)

### Segment 5 — "Found another contractor" → **Renewal-window play**
Don't push now; be there when the other contract ends.

- **T5.1** "Switching costs: what to check before renewing your delivery partner" (checklist)
- **T5.2** "Second-opinion audit" offer — 30 min, free, no replacement required
- **T5.3** Customer story of someone who switched *to* us and what changed
- **T5.4** Annual ping ~10–11 months after lost date

### Segment 6 — "Budget too low / Too expensive" → **Lower-tier offer**
Reframe the price by reframing the scope.

- **T6.1** Productised / fixed-price starter package (name it, price it, link it)
- **T6.2** "ROI of [our service] in 90 days" — concrete numbers
- **T6.3** Self-serve / async option if you have one
- **T6.4** CTA: "starter package" call

### Segment 7 — "Project too small" → **Stay in touch for when they grow**
- **T7.1** "How [similar company] grew from X to Y and what they outsourced first"
- **T7.2** Newsletter-only cadence, light touch, quarterly
- **T7.3** Refer-a-partner (if you have a partner network for small jobs)

### Segment 8 — "TM has no expertise" → **Conditional re-open**
Only reach out if we've added that capability. Manually triggered, not in the automated flow.

### Segment 9 — "Not mature client" → **Educational drip**
- **T9.1** "Foundations" series: 4 short emails on the basics of [our domain]
- **T9.2** Free template / starter kit download

---

## 3. Cadence — Default 90-Day Re-Engagement Flow (ActiveCampaign Automation)

Same skeleton for every segment, swap in the segment-specific topics.

```
Day 0   — Email 1: Re-opener tied to the lost reason (segment-specific)
Day 3   — If opened & no click → Email 2: Soft value (Topic .1)
Day 7   — If no open at all   → Email 2 alt: New subject line, same content
Day 14  — Email 3: Case study or social proof (Topic .2)
Day 21  — LinkedIn task created for AE/SDR (manual touch)
Day 30  — Email 4: Direct CTA (book a call / reply Y-N)  (Topic .4)
Day 45  — Email 5: Resource / checklist (Topic .3) — no CTA, pure value
Day 60  — Email 6: Breakup email — "should I close this?"
Day 90  — Move to long-term newsletter list, remove from active nurture
```

**Branching rules in AC:**
- Any reply → remove from automation, notify deal owner, create task "Re-qualify".
- Any link click on a "book a call" CTA → notify deal owner immediately.
- 2+ opens on a single email → bump lead score +5, AE alerted at score ≥ 20.
- 0 opens across 3 emails → cool down 60 days, then move to quarterly newsletter only.

---

## 4. Lead-Scoring Suggestions (AC contact score)

| Action                                  | Points |
|------------------------------------------|--------|
| Email open                               | +1     |
| Email open #2 in same sequence           | +2     |
| Click on case study / blog               | +3     |
| Click on pricing / package page          | +8     |
| Click "book a call" / form started       | +10    |
| Reply to an email (any)                  | +15    |
| 60 days no activity                      | -10    |

Trigger handoff to AE at **score ≥ 20**.

---

## 5. Subject-Line Library (low effort, tested patterns)

Use one per segment, A/B with the variant.

| Segment | Primary subject                                  | Variant                                       |
|---------|---------------------------------------------------|-----------------------------------------------|
| 1       | Worth a 15-min check-in, {{firstname}}?           | Is now a better time than last quarter?       |
| 2       | We've got capacity again — {{org}} still needs us?| Quick update on our team availability         |
| 3       | Should I close the loop?                          | Last note from me, {{firstname}}              |
| 4       | What's changed for {{org}} since we spoke         | New priorities for {{role}} in 2026?          |
| 5       | A second opinion — no switch required             | Before you renew with [contractor]            |
| 6       | A smaller, fixed-price way to start               | What we can do for under [€X]                 |
| 7       | When you're ready to grow past this stage         | A quick note for later                        |
| 9       | A 4-email primer on [topic] for {{org}}           | The basics, in 4 short emails                 |

---

## 6. Implementation Checklist in ActiveCampaign

1. **Import** the cleaned list, dedupe by email (the export has duplicates — e.g. Scott Reynolds, Max Flowerdew, Tom Ellis appear multiple times with different lost reasons; keep the most recent).
2. **Tag every contact** with `lost-sql` + the segment tag from §1.
3. **Add custom fields**: `lost_reason`, `lost_date`, `original_deal_owner`, `org`.
4. **Suppress** segment 10 (`seg-suppress`) from automation. Flag for manual review only.
5. **Build one master automation** with a segment-conditional split at entry. Reuse the cadence in §3, swap content per branch.
6. **Goal step** in AC: "Replied OR booked a call" — exits the automation and notifies the AE.
7. **Suppression rules:** unsubscribed, bounced, currently in another active deal, employee of a competitor.
8. **Reporting**: track per-segment reply rate, meeting-booked rate, re-opened-deal rate, and revenue influenced. Review at 30/60/90 days.

---

## 7. Quick-Start (the easiest things to ship first)

If you can only do three things this week:

1. **Email 1 to Segment 2 (`TM has no resources`)** — "we have capacity now". Highest expected reply rate, lowest content effort, and the reason the deal was lost is fixable on our side.
2. **Breakup email to Segment 3 (`No answer`)** — single sentence, Y/N reply. Cleans the list and surprisingly often re-opens deals.
3. **Readiness checklist to Segment 1 (`Not ready yet`)** — they already liked us; one useful asset keeps us top-of-mind until they are ready.

Everything else can be layered in after these three prove out.
