# Lost SQL Nurture Strategy — ActiveCampaign Playbook

## Data Overview

| Lost Reason | Count | % of Total | Nurture-able? |
|---|---|---|---|
| Not relevant anymore | 48 | 19.4% | Partially (re-engage if context changes) |
| Client is not ready yet | 47 | 19.0% | **Yes — top priority** |
| TM has no resources | 42 | 17.0% | Yes — capacity messaging |
| No answer | 38 | 15.4% | **Yes — re-activation** |
| Found another contractor | 34 | 13.8% | Yes — long-term trust build |
| Budget too low | 17 | 6.9% | Yes — ROI/value framing |
| Project too small | 6 | 2.4% | Yes — smaller entry offers |
| TM has no expertise | 5 | 2.0% | Limited |
| We are too expensive | 2 | 0.8% | Yes — ROI/value framing |
| Other (legal, internal hire, etc.) | 7 | 2.8% | No — suppress |

**Total nurture-able contacts: ~204 out of 247 (83%)**

---

## Strategy Principle: Start Easy, Win Fast

Rather than building 8 different tracks, we focus on **3 topic buckets** that cover 71% of lost deals and are the easiest to re-engage with no awkward "we know you ghosted us" energy.

---

## The 3 Nurture Tracks

### Track 1 — "Not Ready Yet" Re-Engagement
**Targets:** Client is not ready yet (47), TM has no resources (42) = **89 contacts**

These people *wanted* to work with you. The timing was wrong. They are the warmest segment.

**Email topic sequence (5 emails, ~6 weeks):**

| # | Send | Subject Line | Angle |
|---|---|---|---|
| 1 | Day 1 | "Still thinking about [project]? You're not alone." | Normalise that projects get delayed. Share a short case study of a client who paused, came back, and succeeded. |
| 2 | Day 8 | "What's changed in Salesforce since we last spoke" | Educational — 2-3 bullet points on recent SF updates relevant to their space. No pitch. Positions you as the expert who stayed current. |
| 3 | Day 15 | "How other [industry/partner type] teams are handling resource gaps" | Peer benchmarking content. "Here's how teams like yours are moving forward with part-time or phased projects." Subtle answer to the "not ready / no resources" objection. |
| 4 | Day 25 | "Quick question, [First Name]" | Ultra-short. One sentence: "Are you at a point where it makes sense to pick this back up?" CTA: reply yes/no. Triggers sales notification on reply. |
| 5 | Day 42 | "Leaving the door open" | Soft close. "No pressure — just wanted you to know we're here when the time is right. Here's what we're working on lately." Links to recent work or blog post. |

**ActiveCampaign setup notes:**
- Tag: `lost-not-ready`
- Goal: any reply or link click → notify sales owner, pause sequence
- After sequence ends → move to low-frequency newsletter (1x/month)

---

### Track 2 — "No Answer" Re-Activation
**Targets:** No answer (38) = **38 contacts**

These people went cold mid-process. We don't know why. Keep it light, low-pressure, and give them an easy door back in.

**Email topic sequence (3 emails, ~3 weeks):**

| # | Send | Subject Line | Angle |
|---|---|---|---|
| 1 | Day 1 | "Checking in — no worries if things changed" | Acknowledge reality: "We know things get busy / priorities shift." Offer a 15-minute catch-up with zero commitment framing. |
| 2 | Day 10 | "[First Name], one thing that might be useful to you" | Drop one piece of genuinely useful content (a short guide, checklist, or case study) relevant to what they originally enquired about. Pure value, no ask. |
| 3 | Day 21 | "Last check-in from us" | Honest close: "I don't want to keep emailing if it's not useful. Click here if you'd like to stay in touch, or just ignore this and no hard feelings." |

**ActiveCampaign setup notes:**
- Tag: `lost-no-answer`
- Email 3 includes a one-click "yes, keep in touch" link → adds to newsletter, removes from nurture
- No reply after email 3 → suppress from outreach for 90 days, then re-evaluate

---

### Track 3 — "Found Another Contractor" Long-Game
**Targets:** Found another contractor (34) = **34 contacts**

These people chose someone else. They're not hostile — they just went elsewhere. The best play is patience and proof.

**Email topic sequence (4 emails, ~2 months):**

| # | Send | Subject Line | Angle |
|---|---|---|---|
| 1 | Day 1 | "Hope the project went well — here's something we learned recently" | Zero mention of them choosing someone else. Just a warm re-connect with a useful insight or short case study. |
| 2 | Day 20 | "What clients wish they'd known before starting a Salesforce project" | Educational. Things that go wrong, questions to ask, how to evaluate quality of work. Subtly positions your expertise without saying "we're better than whoever you hired." |
| 3 | Day 45 | "If you ever need a second pair of eyes..." | "Sometimes it helps to have someone review what's been built or take over a phase. We're happy to do a free 30-min review call — no agenda, just value." Low-commitment offer. |
| 4 | Day 65 | "Still here if you need us" | Brief, warm, link to a recent case study or client testimonial. Ends the formal sequence on a trust-building note. |

**ActiveCampaign setup notes:**
- Tag: `lost-found-contractor`
- After sequence ends → add to monthly newsletter
- If they book the "review call" → hot lead, notify sales immediately

---

## What NOT to Do

- **Do not** put "Budget too low" contacts into the same track as "Not ready yet" — they need ROI/value framing first, save that for phase 2.
- **Do not** nurture contacts tagged `lost-legal-security`, `company was acquired`, or `we failed` — suppress them.
- **Do not** send more than 1 email per week per contact across all tracks.
- **Do not** start with a pitch. Every sequence starts with empathy or value, not a CTA.

---

## ActiveCampaign Implementation Checklist

```
[ ] Import contacts from PDF, clean and deduplicate
[ ] Add custom field: "Lost Reason" and "Lost Date"
[ ] Create 3 tags: lost-not-ready, lost-no-answer, lost-found-contractor
[ ] Build 3 automations (one per track)
[ ] Set automation trigger: tag applied
[ ] Set goal condition: any reply OR booking link clicked → notify assigned sales rep
[ ] Set suppression: contacts tagged lost-legal or lost-irrelevant
[ ] Schedule send times: Tue-Thu, 9-11am recipient local time
[ ] QA: send test emails for each sequence before going live
```

---

## Phase 2 (after 60 days) — Budget Objection Track

Once Phase 1 is running and generating re-engagement data, add:

- **"Budget too low" + "Too expensive" + "Project too small"** → 25 contacts
- Focus: ROI case studies, phased engagement options, "start small" pilot offers
- Sequence: 3 emails over 5 weeks

---

## Expected Outcomes (conservative)

| Track | Contacts | Target Re-engage Rate | Est. Re-engaged |
|---|---|---|---|
| Not Ready Yet | 89 | 15% | ~13 |
| No Answer | 38 | 8% | ~3 |
| Found Contractor | 34 | 10% | ~3 |
| **Total** | **161** | | **~19 warm leads** |

Even 5-10 genuine re-engagements from this list represents significant pipeline value given the typical deal size for Salesforce implementation/consulting work.
