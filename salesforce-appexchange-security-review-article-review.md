# Editorial Review: "Salesforce AppExchange Security Review: How to Prepare and Pass [2026 Guide]"

## Reviewer: Senior Salesforce Technical Writer
## Date: April 28, 2026

---

## Part 1: Meta Tags Assessment

### Meta Title
**Current:** `Salesforce AppExchange Security Review: 2026 Guide` (53 chars)

**Assessment:** Good length (under 60 chars). Includes the primary keyword "Salesforce AppExchange Security Review" upfront, which is ideal for SERP click-through. The year tag adds freshness. Works well.

**Minor suggestion:** Consider testing `Salesforce AppExchange Security Review: Complete 2026 Guide` (58 chars) for a slightly stronger value proposition while still fitting the recommended 50-60 character range.

### Meta Description
**Current:** `Step-by-step guide to the Salesforce AppExchange security review process. Checklist, pricing, common pitfalls, scanner tools, and expert tips.` (152 chars)

**Assessment:** Solid. Within the 150-160 char sweet spot. Hits key search intent signals: "step-by-step," "checklist," "pricing," "pitfalls," "scanner tools." The word "expert tips" adds authority. Reads naturally and would perform well in SERPs.

**Minor suggestion:** You could A/B test adding a concrete number like "15+ checklist items" for extra specificity, but it's already strong as-is.

---

## Part 2: Factual Accuracy Check (Against Official Salesforce Documentation)

### ACCURATE Claims

1. **$999 per-attempt fee for paid apps** - CONFIRMED. Per Salesforce's official Trailhead documentation and the March 2023 fee restructuring announcement: "For every paid solution you sell on AppExchange, we ask for a $999 fee payment for the initial submission and for any subsequent attempts." This is correct.

2. **Free apps don't pay the review fee** - CONFIRMED. Free apps are exempt, though they must request a fee waiver code via a Partner Support case (the submission system still prompts for payment).

3. **~50% first-attempt failure rate** - CONFIRMED. Multiple official and partner sources corroborate this: Salesforce's own Dreamforce 2015 presentation stated "50% of all apps fail the first time through Security Review," and the Trailhead module states "Most submissions pass on the second attempt." Third-party partners like Aquiva Labs cite "Salesforce estimates 50 percent of applications fail the first time."

4. **Chimera scanner retired** - CONFIRMED. The Partner Security Portal now shows: "Chimera is no longer supported." Multiple sources confirm it was decommissioned in the Summer '25 timeframe. The recommendation to switch to OWASP ZAP or Burp Suite is also correct per official guidance.

5. **Checkmarx (Source Code Scanner) is mandatory with 3 free scans per review** - CONFIRMED. The Partner Security Portal documentation states: "Partners scanning for the AppExchange Security Review can use 3 free scans per review." And: "It is compulsory for any security review submission that would include a Salesforce package or component."

6. **No fee for resubmission if only false-positive justifications (no code changes)** - CONFIRMED per multiple third-party sources citing official Salesforce policy.

7. **Periodic re-reviews every 6 months to 2 years** - CONFIRMED. Official documentation states: "Time elapsed since the last review (could be six months to two years)." Trailhead says: "Typically, AppExchange solutions are reviewed for security once a year."

8. **CRUD/FLS violations as the top failure reason** - CONFIRMED. Official Salesforce Developer blog and multiple partner sources cite this as the most common issue.

9. **Common vulnerability categories (SOQL injection, XSS, sharing model violations, etc.)** - CONFIRMED. All of these are documented in official Salesforce security review guidance.

10. **Security Review Wizard submission process** - CONFIRMED. The submission interface is indeed a wizard accessed via the Partner Console under Technologies > Solutions > Start Review.

### INACCURATE or MISLEADING Claims (Requiring Correction)

#### 1. CRITICAL: $150 Annual Listing Fee - INCORRECT
**Article states:** "Annual listing fee: $150 per app" for both paid and free apps.

**Fact:** The $150 annual listing fee was **eliminated** as of March 16, 2023, as part of the fee restructuring. The official Salesforce announcement explicitly states: "The $150 annual fee is eliminated." This is confirmed by the Salesforce Developers Blog, the Medium post from Tarun Gupta (Salesforce), and Stack Exchange answers citing the official Partner Community announcement.

**Required fix:** Remove the $150 annual listing fee row from the pricing table entirely. The current fee structure is simply $999 per attempt for paid apps, no fee for free apps.

#### 2. MISLEADING: Submission Interface Name
**Article states:** "Partner Community Publishing Console (Submission Wizard)"

**Fact:** The official name is the **AppExchange Partner Console** (under the Publishing tab), and the review-specific interface is the **AppExchange Security Review Wizard** (or simply "Security Review Wizard"). The article conflates these into a made-up hybrid name. The submission flow is: Partner Community > Publishing > Partner Console > Technologies tab > Solutions tab > Start Review > Security Review Wizard.

**Required fix:** Use "AppExchange Partner Console" for the console and "Security Review Wizard" for the submission wizard, per official Salesforce terminology.

#### 3. MISLEADING: Review Timeline - Understated
**Article states:** "4-6 Weeks" for security testing.

**Fact:** Official Salesforce documentation says "A solution typically takes 4-5 weeks to get through the review process" (Trailhead), but the Salesforce Developers Blog says "there is a queue time of six to nine weeks." Multiple partner sources report 6-8 weeks as the realistic range, with some reviews taking up to 3 months. The Sliick guide notes "Sometimes, the wait time can be longer than 6 weeks depending on demand, especially during the lead up to Dreamforce."

**Required fix:** Change to "4-6 weeks (though 6-9 weeks is common during peak periods)" or "typically 4-8 weeks" to be more accurate and set realistic expectations.

#### 4. UNVERIFIABLE: AI/ML Security Evaluation as a Formal New Requirement
**Article states:** This is presented as a distinct, formal new requirement with specific test criteria (adversarial input attacks, insecure model training, unauthorized access to AI models).

**Fact:** While Salesforce has indeed begun examining AI-related security concerns (Synebo confirms "SF quietly expanded its checks for AI-related security issues: AI-driven logic, sensitive-data handling, and inference risks"), this is **not** a formally published, standalone requirement with defined test criteria. The article presents specific test categories (adversarial input attacks, insecure model training) as if they are documented Salesforce requirements, but these are not found in official Salesforce documentation. The article should distinguish between confirmed expanded scrutiny and speculative test categories.

**Required fix:** Soften the language. Instead of presenting specific test categories as established requirements, note that Salesforce has expanded scrutiny of AI/ML features and recommend documenting data flows proactively. Cite this as an emerging trend rather than a codified checklist.

#### 5. UNVERIFIABLE: Zero-Trust as a Formal New Requirement
**Article states:** "Salesforce now recommends that AppExchange apps implement zero-trust security principles" as a new, specific requirement.

**Fact:** While Synebo confirms "The review now favors a zero-trust mindset," this is a general approach shift, not a formal published requirement. The article presents it as a distinct new section of the review, which overstates the case. Zero-trust principles (MFA, least privilege, continuous monitoring) were always part of good security practice and have always been checked in the review. The article's treatment makes it sound like a new, distinct evaluation category rather than an intensification of existing checks.

**Required fix:** Frame this as an intensified emphasis rather than a brand-new formal requirement. Something like "The review increasingly applies zero-trust principles to evaluation, meaning..."

#### 6. UNVERIFIABLE: Performance Security Testing as a Formal New Requirement
**Article states:** "Salesforce has introduced performance-focused security testing" as a new category.

**Fact:** The only source for this specific claim is MagicFuse's own blog post (the company publishing this article). No official Salesforce documentation, Trailhead module, or independent third-party source confirms "performance security testing" as a distinct, new evaluation category. While Salesforce certainly tests for governor limit violations and bulk processing issues (these have always been part of the review), presenting this as a formally introduced new testing category is unsubstantiated.

**Required fix:** Either remove this section or clearly label it as a best practice recommendation from MagicFuse rather than a confirmed Salesforce requirement. Alternatively, reframe it around governor limits and bulk processing best practices, which are genuinely part of the review.

#### 7. MINOR: Salesforce Code Analyzer Omission
**Article states:** In the scanner table, Salesforce Code Analyzer is listed as "Good complement to Checkmarx" and a development tool.

**Fact:** As of 2024-2025, Salesforce Code Analyzer scan reports are **mandatory** for managed package submissions, not merely a complement. The official documentation states: "As an AppExchange partner submitting your managed package for security review, you must scan it with the Salesforce Code Analyzer and provide test results in your solution's AppExchange Security Review submission. This scan is in addition to the scan that you must complete using the Source Code Scanner [Checkmarx]."

**Required fix:** Update the scanner table to reflect that Salesforce Code Analyzer is now **mandatory** for managed package submissions, not just recommended. It should be listed alongside Checkmarx as a required tool, not below it as a nice-to-have.

#### 8. MINOR: Submission Verification Timeline
**Article states:** "1-2 Business Days" for submission verification.

**Fact:** Multiple sources say this can take "a few days" (Salesforce Developer Blog) or "1-2 weeks" (Sliick, citing official guidance). The Partner Console guide says the ops team review plus passing to ProdSec "can take two to four weeks." One to two business days significantly understates this phase.

**Required fix:** Change to "a few business days to 1-2 weeks" to be more accurate.

#### 9. MINOR: MFA Guidance Contradiction
**Article states (in the checklist):** "MFA enforced where applicable."

**Fact:** While MFA is generally a good security practice, the Salesforce security review specifically requires that **2FA/MFA should be disabled** on test org credentials so the testing team can log in. The Salesforce Developer Blog explicitly states: "Access to test org is validated - 2FA/MFA should be disabled, so the testing team can log in to test." This is an important nuance the article misses.

**Required fix:** Add a note in the documentation/submission section that MFA must be disabled on test credentials provided to the security review team, even though MFA enforcement is a security best practice for production.

---

## Part 3: Structural and Editorial Assessment

### Overall Structure
The article follows a logical progression: What > Pricing > Process > What's New > Failure Reasons > Preparation > Checklist > Failure Recovery > CTA. This is a strong structure for a comprehensive guide.

### Strengths
1. **Practical case studies** - The Atamis and Elements.cloud examples add credibility and differentiate this from generic guides.
2. **Pricing table** - Clear, scannable format (though needs the $150 correction).
3. **Scanner comparison table** - Useful for ISVs evaluating their tooling.
4. **Actionable checklist** - The checkbox-style checklist is immediately usable.
5. **FAQ section** - Good for featured snippets and voice search.
6. **Honest tone** - Acknowledging the ~50% failure rate and budgeting for resubmission builds trust.

### Weaknesses
1. **"What's New" section credibility** - Two of the three "new" items (zero-trust and performance testing) are not well-sourced from official Salesforce documentation. Only the Chimera retirement is solidly verifiable. This weakens the article's authority for a 2026 Guide.

2. **Missing: Salesforce Code Analyzer as mandatory** - This is a significant omission for a 2026 guide. The article treats it as optional when it's now required.

3. **Missing: AgentExchange** - As of April 2026, Salesforce launched AgentExchange, a unified marketplace combining AppExchange, Slack Marketplace, and the Agentforce ecosystem. A 2026 guide should at least mention this development and its potential impact on the security review landscape.

4. **Missing: Lightning Ready certification requirement** - The Sliick guide notes: "All new solutions submitted for review must be certified as Lightning Ready." This is not mentioned in the article.

5. **Missing: Version submission guidance** - The Salesforce Developer Blog has important guidance: "Submit a point release (e.g., 16.7→16.8, etc.), not a patch release (16.7.1234)." This is a practical tip that catches many ISVs off guard.

6. **Excessive keyword stuffing** - Phrases like "security review," "security vulnerabilities," "Salesforce AppExchange security review," and "security issues" are repeated excessively. Some paragraphs read more like SEO filler than expert guidance. A senior Salesforce writer would vary the language more naturally.

7. **Missing: Attestation process for version updates** - The article doesn't mention that new package versions no longer need full security review; you just complete a quick attestation. This is important information for ISVs planning their release cadence.

---

## Part 4: Real-World Example (Structured Text)

Below is a rewritten example section demonstrating how a senior Salesforce writer would restructure the "How the Process Works" section with a concrete, real-world example woven in:

---

### How the Salesforce AppExchange Security Review Process Works (Rewritten Example)

The security review follows five stages. Here's how each one played out for a recent ISV client building a procurement solution on Salesforce.

**Stage 1: Preparation (Your Responsibility)**

We started by mapping every integration point in the application: Apex callouts to an external pricing engine, a Visualforce-based document generator, and a Lightning Web Component for workflow approvals. For each, we listed the data flowing through it and identified where user input could be manipulated.

Then we ran Salesforce Code Analyzer (`sf code-analyzer run --rule-selector AppExchange --rule-selector Recommended:Security`) and Checkmarx scans via the Partner Security Portal. The first Checkmarx scan returned 47 findings. Thirty-one were genuine issues, mostly CRUD/FLS violations in utility classes that queried records without `WITH SECURITY_ENFORCED`. Sixteen were false positives where `stripInaccessible()` was applied downstream but the scanner couldn't trace the flow.

We fixed the genuine issues, documented each false positive with code references and explanations, and re-scanned. The second scan was clean except for the documented false positives.

For the external pricing engine, we ran OWASP ZAP against the API endpoints since Chimera was retired in June 2025. ZAP flagged a missing Content-Security-Policy header and an open redirect on the OAuth callback URL. Both were fixed before submission.

**Stage 2: Submission (Partner Console)**

We submitted through the AppExchange Partner Console (Technologies > Solutions > Start Review), which launched the Security Review Wizard. The wizard walked us through:

- **Technical details:** Architecture description, solution type, listing of all external endpoints
- **Documentation upload:** Salesforce Code Analyzer HTML report, Checkmarx scan results, ZAP scan report, false-positive analysis document, user/admin documentation, data flow diagram
- **Test environments:** A Partner Developer Edition org with the managed package installed, two test users (admin and standard), and credentials for the external pricing API. We triple-checked that MFA was disabled on the test org so the review team could log in.
- **Payment:** $999 via credit card

One detail that nearly derailed us: we initially uploaded a patch version (2.3.1) instead of a point release (2.4). The Checkmarx scanner filters out patch releases. We had to create version 2.4 and re-upload.

**Stage 3: Submission Verification (Expect a Few Business Days to 2 Weeks)**

The Security Review Operations team validated our materials. This is not a technical review. They confirmed all required documents were present, credentials worked, and the managed package version was correct. Our submission cleared this gate in five business days.

Had anything been missing, it would have been returned without entering the queue. This does not count as a failed attempt, but it costs time.

**Stage 4: Security Testing (4-8 Weeks)**

Our submission entered the Product Security queue. The assigned reviewer conducted threat modeling, static analysis, dynamic testing, and manual penetration testing across:

- All Apex classes for SOQL injection, CRUD/FLS enforcement, and sharing model violations
- Visualforce pages for XSS and CSRF vulnerabilities
- Lightning Web Components for DOM-based XSS and insecure client-side logic
- The external pricing API for authentication flaws, TLS configuration, and input validation
- OAuth flows for token leakage and session fixation

The review took six weeks. During this period, we heard nothing from Salesforce. No news is normal during this phase.

**Stage 5: Results**

We received a pass. The approval email included next steps for publishing the listing. Had we failed, we would have received a report listing vulnerability classes (not every instance) with descriptions, context, and remediation guidance.

One critical point from experience: the report is representative, not exhaustive. The review team has a finite testing window. If they find one SOQL injection, assume the same pattern exists elsewhere in your codebase. Search for and fix every instance, not just the flagged one.

---

## Part 5: Recommended Corrections (Priority Order)

### Must Fix (Factual Errors)

| # | Issue | Current Text | Corrected Text |
|---|-------|-------------|----------------|
| 1 | $150 annual fee | "Annual listing fee: $150 per app" | Remove this row entirely. The $150 annual fee was eliminated in March 2023. |
| 2 | Salesforce Code Analyzer status | Listed as "Good complement to Checkmarx" | Change to "Mandatory for managed package submissions (in addition to Checkmarx)" |
| 3 | Submission interface name | "Partner Community Publishing Console (Submission Wizard)" | "AppExchange Partner Console (via the Security Review Wizard)" |
| 4 | Submission verification timeline | "1-2 Business Days" | "A few business days to 1-2 weeks" |
| 5 | Review timeline | "4-6 Weeks" | "4-6 weeks (6-9 weeks during peak periods)" |

### Should Fix (Misleading or Unsubstantiated)

| # | Issue | Recommendation |
|---|-------|---------------|
| 6 | AI/ML evaluation section | Soften language; present as emerging scrutiny, not formal checklist |
| 7 | Zero-trust section | Reframe as intensified emphasis, not new formal requirement |
| 8 | Performance testing section | Remove or label as MagicFuse recommendation; not an official Salesforce requirement |
| 9 | MFA in checklist | Add note about disabling MFA on test credentials for the review team |
| 10 | Free app fee waiver process | Note that free apps need to request a waiver code via Partner Support case |

### Nice to Have (Missing Information)

| # | Addition | Why |
|---|---------|-----|
| 11 | Salesforce Code Analyzer as mandatory (expanded) | Major change ISVs need to know |
| 12 | Attestation process for version updates | Saves ISVs from unnecessary resubmissions |
| 13 | Point release vs. patch release guidance | Common gotcha |
| 14 | Lightning Ready certification requirement | Required for all new submissions |
| 15 | AgentExchange mention | Relevant 2026 development |

---

## Part 6: Verdict

**Overall quality: 7/10**

The article is well-structured, actionable, and covers the topic comprehensively. The case studies add genuine credibility, and the checklist format is immediately useful for ISV teams. However, there are factual errors (especially the $150 annual fee and the Code Analyzer omission) and unsubstantiated claims in the "What's New" section that undermine the article's authority as a definitive 2026 guide.

The biggest risk is the $150 annual fee error. An ISV reading this article and budgeting for a fee that doesn't exist will lose trust in the entire guide when they discover the mistake. Fix that first.

With the corrections above applied, this would be an 8.5/10 guide and one of the stronger AppExchange security review resources available.
