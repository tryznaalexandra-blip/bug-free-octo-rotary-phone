# Lost SQL Nurture Strategy — Active Campaign

## Data Summary

Based on analysis of ~300 lost SQL deals, here's the breakdown by lost reason:

| Lost Reason | Count (approx) | Recovery Potential | Nurture? |
|---|---|---|---|
| Client is not ready yet | ~70 | HIGH | YES |
| Not relevant anymore | ~55 | LOW | Light |
| TM has no resources | ~45 | N/A (internal) | Internal flag |
| Found another contractor | ~40 | MEDIUM | YES |
| No answer | ~35 | MEDIUM-HIGH | YES |
| Budget too low | ~18 | MEDIUM | YES |
| Project too small | ~8 | LOW | Light |
| TM has no expertise | ~8 | N/A (internal) | Internal flag |
| We are too expensive | ~4 | MEDIUM | YES |
| Not mature client | ~5 | MEDIUM | YES |
| Hired internally | ~3 | LOW | Light |
| Other (legal, recruitment fail, etc.) | ~10 | LOW | NO |

---

## Priority Segments to Nurture (Easy Wins First)

### Segment 1: "Client is Not Ready Yet" (~70 contacts) — HIGHEST PRIORITY
These people wanted to work with you but timing was off. Easiest to win back.

### Segment 2: "No Answer / Ghosted" (~35 contacts)
They went silent. A fresh, low-pressure approach can re-open conversations.

### Segment 3: "Budget Too Low / Too Expensive" (~22 contacts)
They liked you but couldn't afford it. Show ROI and flexible options.

### Segment 4: "Found Another Contractor" (~40 contacts)
They chose someone else. Stay top of mind for when they need help again.

### Segment 5: "Not Mature Client" (~5 contacts)
They weren't ready for the engagement level. Educate them over time.

---

## Easy Topic Ideas That Work

These are simple, proven content topics you can create quickly without heavy production:

### Topic Pool A: Quick Value Content (use across all segments)
1. **"3 Signs Your Salesforce Org Needs Professional Help"** — checklist-style, easy to write
2. **"What to Look for When Hiring a Salesforce Consultant"** — positions you as the expert even if they choose someone else
3. **"5 Quick Salesforce Wins You Can Do This Week"** — actionable tips, builds trust
4. **"How [Client Name] Saved X Hours/Month with a Simple Salesforce Fix"** — short case study
5. **"The Real Cost of Delaying Your Salesforce Project"** — creates urgency without pressure

### Topic Pool B: Objection-Busting (segment-specific)
6. **"Starting Small: How a 2-Week Sprint Can Transform Your Salesforce"** — for budget/too expensive segment
7. **"Is Your Business Ready for Salesforce Help? A Simple Self-Assessment"** — for not-ready/not-mature segment
8. **"What Happens When Your Salesforce Contractor Doesn't Work Out"** — for found-another-contractor segment
9. **"Why Companies Come Back to Us After Trying Other Options"** — subtle, for contractor-switchers
10. **"Salesforce ROI Calculator: Is It Worth the Investment?"** — for budget-conscious segment

### Topic Pool C: Seasonal / Timely (use as one-offs)
11. **"Planning Your Q[X] Salesforce Roadmap"** — quarterly, always relevant
12. **"[Year] Salesforce Release: What It Means for Your Business"** — tied to SF releases
13. **"End of Year: 3 Salesforce Projects to Start Before Q1"** — seasonal urgency

---

## Active Campaign Automation Flows

### Flow 1: "Not Ready Yet" Warm Nurture (DEPLOY FIRST)

**Tag in Active Campaign:** `lost-sql-not-ready`
**Goal:** Keep them warm until they ARE ready, then hand off to sales.

```
Day 0:  [Entry] Contact tagged "lost-sql-not-ready"
        ↓
Day 3:  EMAIL 1 — "Quick question"
        Subject: "Hey {First Name}, quick question"
        Body: Short, personal. "We spoke a while back and the timing
        wasn't right. Totally understand. I put together a quick
        checklist of signs that it might be time to revisit your
        Salesforce setup. No pitch, just useful stuff."
        CTA: Link to Topic #1 (checklist blog/PDF)
        ↓
Day 10: EMAIL 2 — Value drop
        Subject: "5 quick Salesforce wins (takes 10 min each)"
        Body: Share Topic #5 — actionable tips they can use right now.
        Shows you're helpful, not salesy.
        CTA: "Try these and let me know how it goes"
        ↓
Day 21: EMAIL 3 — Social proof
        Subject: "How [Client] fixed their pipeline tracking in 2 weeks"
        Body: Short case study (Topic #4). Keep it brief — problem,
        solution, result in 3 paragraphs.
        CTA: "Want to see if something similar could work for you?"
        ↓
Day 35: EMAIL 4 — Gentle check-in
        Subject: "Still on your radar?"
        Body: "Just checking in. If your Salesforce project is back on
        the table, I'd love to help. If not, no worries — I'll keep
        sending useful stuff your way."
        CTA: "Book a quick 15-min call" (Calendly link)
        ↓
        [IF CLICKED → notify sales, add tag "re-engaged"]
        [IF NO OPEN → wait 30 days → move to Flow 5 (long-term)]
        ↓
Day 50: EMAIL 5 — Planning prompt
        Subject: "Planning your Q{next quarter} Salesforce roadmap?"
        Body: Topic #11 — seasonal planning angle.
        CTA: "Here's a free roadmap template" (lead magnet)
        ↓
Day 65: EMAIL 6 — Final re-engagement
        Subject: "Should I keep you in the loop?"
        Body: "I've been sending you some Salesforce tips. Want to keep
        getting them, or should I stop? Either way is fine."
        CTA: Two buttons — "Keep sending" / "I'm good for now"
        ↓
        [IF "Keep sending" → move to long-term nurture Flow 5]
        [IF "I'm good" or no response → remove from automation, keep in CRM]
```

---

### Flow 2: "No Answer / Ghosted" Re-engagement

**Tag in Active Campaign:** `lost-sql-no-answer`
**Goal:** Get a response — any response. Break the silence.

```
Day 0:  [Entry] Contact tagged "lost-sql-no-answer"
        ↓
Day 2:  EMAIL 1 — Pattern interrupt
        Subject: "Not sure if you saw this"
        Body: Super short. "I know inboxes are crazy. Thought you might
        find this useful — [link to Topic #3: 5 Quick SF Wins].
        No reply needed."
        ↓
Day 9:  EMAIL 2 — Curiosity play
        Subject: "{First Name}, one question"
        Body: "Are you still looking for Salesforce help, or did you
        sort it out? Just want to make sure I'm not bugging you."
        CTA: Three options — "Still looking" / "Found someone" / "Not right now"
        (Use AC's click-based tagging to route responses)
        ↓
        [IF "Still looking" → notify sales immediately]
        [IF "Found someone" → move to Flow 4]
        [IF "Not right now" → continue below]
        ↓
Day 20: EMAIL 3 — Value-only
        Subject: "This saved one of our clients 10 hours/week"
        Body: Quick case study (Topic #4).
        CTA: Soft — "Thought you'd find this interesting"
        ↓
Day 35: EMAIL 4 — Last attempt
        Subject: "Last one from me"
        Body: "I'll stop emailing after this unless you tell me
        otherwise. But if you ever need Salesforce help, here's my
        calendar link. Door's always open."
        CTA: Calendly link
        ↓
        [IF clicked → notify sales, tag "re-engaged"]
        [IF no engagement after 30 days → move to Flow 5 or remove]
```

---

### Flow 3: "Budget Too Low / Too Expensive"

**Tag in Active Campaign:** `lost-sql-budget`
**Goal:** Demonstrate ROI and introduce flexible engagement options.

```
Day 0:  [Entry] Contact tagged "lost-sql-budget"
        ↓
Day 3:  EMAIL 1 — Reframe the cost
        Subject: "The real cost of NOT fixing your Salesforce"
        Body: Topic #5 — frame the cost of inaction. Lost deals,
        manual work, team frustration. Keep it relatable.
        CTA: Link to blog/article
        ↓
Day 12: EMAIL 2 — Flexible options
        Subject: "Starting small with Salesforce (2-week sprints)"
        Body: Topic #6 — introduce the idea of smaller engagements.
        "You don't need a 6-month project. Sometimes a focused 2-week
        sprint on your biggest pain point is all it takes."
        CTA: "See our sprint packages"
        ↓
Day 24: EMAIL 3 — ROI proof
        Subject: "How a $X investment returned $Y for [Client]"
        Body: ROI-focused case study. Numbers talk.
        CTA: "Calculate your potential ROI" (link to Topic #10)
        ↓
Day 40: EMAIL 4 — Check-in
        Subject: "Has anything changed on your end?"
        Body: Friendly check-in. "Budgets shift, priorities change.
        If Salesforce is back on the table, let's talk about what
        we can do within your budget."
        CTA: Book a call
        ↓
        [IF engaged → notify sales]
        [IF no engagement → move to Flow 5]
```

---

### Flow 4: "Found Another Contractor"

**Tag in Active Campaign:** `lost-sql-other-contractor`
**Goal:** Stay top of mind. Be there when the other contractor disappoints.

```
Day 0:  [Entry] Contact tagged "lost-sql-other-contractor"
        ↓
Day 7:  EMAIL 1 — No hard feelings
        Subject: "Hope it's going well with your SF project"
        Body: Genuine. "Just wanted to check in and hope your Salesforce
        project is going well. If you ever need a second opinion or
        extra hands, we're here."
        CTA: None — just goodwill
        ↓
Day 30: EMAIL 2 — Helpful resource
        Subject: "What to look for when reviewing your contractor's work"
        Body: Topic #2 — genuinely helpful, positions you as expert.
        Not throwing shade, just being useful.
        CTA: Link to checklist
        ↓
Day 60: EMAIL 3 — Social proof
        Subject: "Why companies come back to us"
        Body: Topic #9 — stories of clients who tried others first.
        Subtle but effective.
        CTA: "Want to chat about your experience?"
        ↓
Day 90: EMAIL 4 — Seasonal
        Subject: "Planning next quarter's Salesforce work?"
        Body: Topic #11. Timely, useful, not pushy.
        CTA: "Let's plan together" (Calendly)
        ↓
        [Continue with Flow 5 quarterly touches]
```

---

### Flow 5: Long-Term Nurture (Catch-All / Ongoing)

**Tag in Active Campaign:** `lost-sql-long-nurture`
**Goal:** Stay on their radar with monthly/quarterly value drops.

```
[Entry] Contacts who completed Flows 1-4 without converting
        ↓
Every 3-4 weeks: ONE email from the Topic Pool rotation

Rotation:
  Month 1: Topic from Pool A (quick value)
  Month 2: Topic from Pool C (seasonal/timely)
  Month 3: Topic from Pool A (different one)
  Month 4: Case study
  Month 5: Topic from Pool C
  Month 6: "Still interested?" check-in with opt-out option

Repeat cycle. Remove after 12 months of zero engagement.
```

---

## Active Campaign Setup Checklist

### Tags to Create
- [ ] `lost-sql-not-ready`
- [ ] `lost-sql-no-answer`
- [ ] `lost-sql-budget`
- [ ] `lost-sql-other-contractor`
- [ ] `lost-sql-not-mature`
- [ ] `lost-sql-long-nurture`
- [ ] `lost-sql-re-engaged` (trigger for sales notification)

### Custom Fields
- [ ] `Lost Reason` (dropdown matching your CRM values)
- [ ] `Original Lost Date` (date field)
- [ ] `Last Engagement Date` (auto-updated)

### Automations to Build (in order)
1. **Import & Tag** — Bulk import contacts, auto-tag by lost reason
2. **Flow 1** — Not Ready Yet nurture (start here, biggest segment)
3. **Flow 2** — No Answer re-engagement
4. **Flow 3** — Budget nurture
5. **Flow 4** — Other Contractor nurture
6. **Flow 5** — Long-term catch-all
7. **Re-engagement Alert** — When any contact clicks a CTA or books a call, notify sales via email/Slack/CRM

### Contact Scoring (optional but recommended)
Set up lead scoring in Active Campaign:
- Opens email: +1 point
- Clicks link: +5 points
- Visits website: +3 points
- Books call: +20 points
- Score > 15: auto-notify sales team

---

## Email Best Practices for These Flows

1. **Keep emails SHORT** — 3-5 sentences max. These are lost leads, not subscribers.
2. **Send from a person, not a brand** — "From: Sarah at [Company]" not "From: [Company] Marketing"
3. **Plain text style** — No fancy templates. Make it look like a real email from a real person.
4. **One CTA per email** — Don't overwhelm. One link, one action.
5. **Personalize** — Use `{First Name}` and reference their company where possible.
6. **Don't sell in every email** — Alternate: value, value, soft ask, value, value, ask.
7. **Respect opt-outs** — Always include unsubscribe. If someone says stop, stop.
8. **Subject lines** — Keep under 6 words. Lowercase feels more personal.

---

## What to Build First (Start This Week)

1. **Import the 70 "not ready yet" contacts** into Active Campaign with the `lost-sql-not-ready` tag
2. **Write Email 1 for Flow 1** (the "quick question" email) — takes 15 minutes
3. **Create a simple checklist** ("3 Signs Your SF Org Needs Help") — can be a Google Doc or simple landing page
4. **Set up the automation** in Active Campaign — Flow 1 only, 6 emails
5. **Hit send** — start with the biggest, easiest segment and learn from it

Then build Flows 2-4 over the following weeks based on what you learn from Flow 1's open/click rates.

---

## Expected Results

| Metric | Conservative | Optimistic |
|---|---|---|
| Open rate | 25-30% | 40-50% |
| Click rate | 3-5% | 8-12% |
| Re-engaged leads (book a call) | 5-8% | 12-15% |
| Converted back to opportunity | 2-3% | 5-8% |

With ~170 contacts in the primary nurture segments, even a conservative 3% conversion = 5 new opportunities from deals you already lost. That's essentially free pipeline.
