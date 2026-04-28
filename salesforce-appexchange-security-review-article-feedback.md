# Salesforce AppExchange Security Review Article Feedback

## Verdict

The article is strong in intent and covers the right buyer questions: cost, timeline, scanners, common failure reasons, checklist, resubmission, and MagicFuse credibility. It should not be published as-is because several claims need correction or tighter wording against Salesforce documentation.

The biggest issue is the pricing section. Salesforce eliminated the old $150 annual fee in 2023, and the current model is a $999-per-attempt security review fee for paid apps. Free apps still go through security review but do not pay the review fee.

## Documentation-backed corrections

Use these corrections before publication.

1. **Remove the $150 annual listing fee**
   - Current Salesforce guidance says the "$150 annual fee is eliminated" and the security review fee is "$999 per attempt for paid apps."
   - Source: Salesforce Developers Blog, "Prepare Your App to Pass the AppExchange Security Review."

2. **Update review timing**
   - The article says submission verification takes 1-2 business days and testing takes 4-6 weeks.
   - Current ISVforce documentation says:
     - Submission verification: 1-2 weeks.
     - First-time Product Security testing: 3-4 weeks.
     - Resubmission testing: 2-3 weeks.
   - You can still say "timelines vary with submission quality and queue volume."
   - Source: ISVforce Guide, "How the AppExchange Security Review Works."

3. **Make Salesforce Code Analyzer required, not just recommended**
   - The article currently positions Salesforce Code Analyzer as a helpful complement.
   - Salesforce Code Analyzer reports are required for managed package AppExchange submissions and must be uploaded with the security review materials.
   - Source: Salesforce Code Analyzer docs, "Produce Code Analyzer Reports for AppExchange Security Review."

4. **Keep Checkmarx mandatory, but define it precisely**
   - The Partner Security Portal Source Code Scanner uses Checkmarx technology and is mandatory for submissions that include a Salesforce package or component.
   - It scans Apex, Visualforce, and Lightning code, not external endpoints, mobile clients, or API-only solutions.
   - Source: Partner Security Portal SourceScanner Help.

5. **Correct DAST language**
   - After Chimera sunset, partners can use a DAST scanner of their choice and must submit full DAST scan reports for external web apps/APIs where applicable.
   - Good examples: OWASP ZAP, Burp Suite Enterprise Edition, Veracode Dynamic Analysis, or similar tools.
   - Source: Partner Security Portal, "Chimera Sunset and DAST Scan."

6. **Chimera date is essentially correct, but phrase it from Salesforce's notice**
   - Salesforce says partners could download previous Chimera reports until June 15, 2025, and cannot access Chimera reports after June 16, 2025. Salesforce no longer supports Chimera DAST scans after June 16, 2025.

7. **Be careful with "about half fail first submission"**
   - This is plausible and widely repeated, but the current Salesforce pages I checked do not give a precise public percentage. If you keep it, cite a source or soften it:
   - Better: "Many first submissions do not pass, especially when teams defer testing and remediation until the end."

8. **Do not overstate compliance outcomes**
   - Passing security review helps customers trust the app, but it does not certify GDPR, HIPAA, or PCI-DSS compliance. Rephrase as "supports a stronger compliance posture" rather than "helps organizations maintain compliance."

9. **Lightning Ready requirement should be added earlier**
   - Salesforce states that all new solutions submitted for security review must be Lightning Ready. The article mentions older Visualforce-heavy work in the Atamis story, so add a sentence explaining that new submissions must meet Lightning Ready expectations.

10. **Modernize CRUD/FLS recommendations**
    - Keep `Security.stripInaccessible()`, but do not imply `WITH SECURITY_ENFORCED` is the only or best current answer.
    - Salesforce's 2023 guidance points to user-mode database operations and `WITH USER_MODE` for orgs/features targeting Spring '23 and later, while `WITH SECURITY_ENFORCED` remains relevant in older patterns.

## Recommended article structure

Use a structure that matches search intent and reduces repetition.

1. **H1: Salesforce AppExchange Security Review: How to Prepare and Pass**
2. **Short executive summary**
   - Who needs the review.
   - What Salesforce checks.
   - Current cost and timeline.
   - What to prepare before submission.
3. **What is the AppExchange security review?**
4. **Who must pass it?**
   - Managed packages.
   - Salesforce Platform API solutions.
   - Marketing Cloud Engagement API solutions.
   - External services, APIs, and mobile apps that are part of the solution.
5. **Cost and timing in 2026**
6. **How the process works**
   - Readiness.
   - Testing and scanner reports.
   - Required materials.
   - Submission verification.
   - Product Security testing.
   - Approval or remediation report.
7. **What Salesforce reviews**
   - CRUD/FLS and sharing.
   - Injection.
   - XSS/CSRF.
   - Secrets and authentication.
   - External endpoints and APIs.
   - Third-party JavaScript and vulnerable libraries.
   - AI/ML features, if applicable.
8. **Required and recommended scanner tools**
9. **Common reasons apps fail**
10. **Step-by-step preparation checklist**
11. **What to do if you fail**
12. **How MagicFuse helps**
13. **FAQ**

## Revised sample copy

### Opening section

**Salesforce AppExchange Security Review: How to Prepare and Pass**

Before a managed package or eligible Salesforce solution can be listed publicly on AppExchange, it must pass Salesforce's AppExchange security review. The review is run by Salesforce Product Security and combines automated scanning, manual testing, and review of your documentation, test environment, package, and any external services included in the solution.

For ISVs, the review is more than a publishing step. It is a check on whether your app protects customer data in real Salesforce environments: object and field permissions, record sharing, authentication flows, external endpoints, stored secrets, JavaScript libraries, and user-controlled input all come into scope.

This guide explains how the AppExchange security review works in 2026, what Salesforce expects you to submit, which scanner reports are required, what commonly causes rejections, and how to prepare your app before it enters the Product Security queue.

### Pricing and timeline section

**Salesforce AppExchange security review cost and timeline**

For paid AppExchange solutions, Salesforce charges a **$999 security review fee per attempt**. That applies to the initial submission and to later attempts when you submit a changed version after security vulnerabilities are found. Free solutions must still pass security review, but they do not pay the review fee.

The old $150 annual AppExchange fee should not be listed as a current cost. Salesforce removed that annual fee when it moved to the per-attempt pricing model in 2023.

Current Salesforce documentation gives these typical review windows:

| Stage | Typical Salesforce timeframe |
| --- | --- |
| Submission verification | 1-2 weeks |
| First Product Security test | 3-4 weeks |
| Resubmission test after remediation | 2-3 weeks |

These are estimates, not guarantees. Incomplete credentials, missing scanner reports, unclear setup instructions, or the wrong package version can send a submission back before it reaches Product Security.

### Process section

**How the AppExchange security review process works**

Salesforce describes the review in five stages:

1. **You submit the solution.** Upload the correct package version, scanner reports, documentation, test credentials, and instructions through the AppExchange security review submission flow.
2. **Salesforce verifies the submission.** Security Review Operations checks whether the materials are complete enough for Product Security to test.
3. **The solution enters the Product Security queue.** If the submission is valid, it moves into the review queue.
4. **Product Security tests the solution.** The team attempts to identify security vulnerabilities across the Salesforce package and any external services, APIs, mobile apps, or web apps that are part of the solution.
5. **You receive the result.** Approved submissions can be listed publicly. Not-approved submissions receive a report with representative vulnerability classes and remediation guidance.

The report is not an exhaustive bug list. If Salesforce identifies one SOQL injection pattern or one CRUD/FLS bypass, search the whole codebase for the same class of issue before resubmitting.

### Scanner section

**Scanner reports to prepare**

Salesforce expects scanner reports as part of the review materials. The exact set depends on your architecture, but most managed package submissions should plan for:

| Tool | Purpose | Publication guidance |
| --- | --- | --- |
| Salesforce Code Analyzer | Static analysis for Apex, Visualforce, JavaScript, TypeScript, and security rules | Required reports for managed package submissions. Run with `--rule-selector AppExchange --rule-selector Recommended:Security`. |
| Partner Security Portal Source Code Scanner / Checkmarx | Static scan of Salesforce package code and components | Mandatory for submissions that include a Salesforce package or component. |
| OWASP ZAP, Burp Suite Enterprise Edition, Veracode Dynamic Analysis, or similar DAST tool | Dynamic testing of live external web apps, APIs, and endpoints | Required when external components are in scope. Submit full reports and false-positive documentation. |

Chimera should not be recommended as an active scanner. Salesforce sunset Chimera DAST support in June 2025.

### Common failure reasons section

**Common reasons AppExchange apps fail security review**

1. **CRUD/FLS bypasses.** Apex runs in system context by default, so code must explicitly respect object and field permissions where user data is exposed or modified. Use current platform controls such as user-mode database operations, `Security.stripInaccessible()`, and documented permission checks.
2. **SOQL injection.** Dynamic queries that concatenate user input can expose data beyond the user's intended access. Use bind variables and strict allowlists for dynamic query parts such as field names or sort directions.
3. **XSS and unsafe rendering.** Visualforce pages, Aura components, LWCs, and external front ends must encode output and avoid unsafe HTML injection.
4. **Weak external integrations.** External services must use HTTPS/TLS, strong authentication, secure session handling, and no debug leakage.
5. **Secrets in code.** Passwords, tokens, and API keys should not be stored in source code. Use Named Credentials, protected custom settings, protected custom metadata, or an appropriate external secret store.
6. **Vulnerable JavaScript libraries.** Old versions of jQuery or other libraries with known CVEs are a common and avoidable failure.
7. **Incomplete submission materials.** Missing credentials, incomplete instructions, stale package versions, or missing scanner reports can delay the review before testing begins.

### MagicFuse section

**How MagicFuse helps ISVs prepare for AppExchange security review**

MagicFuse helps Salesforce ISVs prepare for security review by combining architecture review, secure Apex and Lightning development, scanner remediation, external endpoint testing, and submission documentation.

For a Visualforce-heavy or legacy Salesforce product, that usually starts with a technical assessment: where the app bypasses sharing, where CRUD/FLS checks are missing, how secrets are stored, which external services are in scope, and whether the package is Lightning Ready. From there, the team fixes high-risk patterns, prepares scanner reports, documents false positives, and packages the submission materials so Salesforce reviewers can test the solution end to end.

This is the right place to use the Atamis and Elements.cloud examples, but keep them specific and verifiable. Show the problem, the security work performed, and the outcome. Avoid implying that MagicFuse can guarantee approval, because Salesforce security review is always Salesforce's decision.

## SEO and metadata comments

- **Meta title:** "Salesforce AppExchange Security Review: 2026 Guide" is good at 53 characters. It includes the main keyword and year.
- **Meta description:** Current draft is strong, but "pricing" may be sensitive because the section needs correction. Suggested version:
  - "Prepare for the Salesforce AppExchange security review with current fees, timelines, scanner requirements, common failure reasons, and a practical ISV checklist."
- **H1:** "Salesforce AppExchange Security Review: How to Prepare and Pass [2026 Guide]" is clear. Consider removing brackets for a cleaner editorial style:
  - "Salesforce AppExchange Security Review: How to Prepare and Pass in 2026"
- **Keyword use:** Reduce repeated exact-match phrases such as "appexchange security review submission." Use natural variants: "submission," "review materials," "Product Security review," and "AppExchange review."

## Section-by-section editorial comments

### Intro

The Atamis story is useful, but the current version starts too narrowly and may confuse readers who are looking for process guidance. Lead with the general problem first, then bring Atamis in as proof.

Also avoid saying the founder had "no deep Salesforce experience" unless the client has approved that phrasing. It can sound negative. Use "a team that needed deeper AppExchange security-review expertise."

### What is the review?

Good section. Add that the review is required for managed packages, Salesforce Platform API solutions, and Marketing Cloud Engagement API solutions distributed on AppExchange. Mention Lightning Ready as a readiness requirement for new submissions.

### Pricing

Needs correction. Remove annual listing fee. Keep $999 per attempt for paid apps. Explain that false-positive-only resubmissions of the same version may not require a new fee, but changed package versions after vulnerabilities typically count as another attempt.

### Process

Adjust timing to Salesforce's current published ranges. Keep the five-stage structure; it matches Salesforce documentation well.

### What's new in 2025-2026

This section is the least documentation-grounded. Chimera sunset is solid. The AI/ML and zero-trust parts need citations or softer wording. If you cannot source them directly from Salesforce security review requirements, frame them as "areas to document carefully" rather than "new requirements."

### Common failure reasons

Strong and useful. Add vulnerable third-party JavaScript and information leakage/debug mode. Update CRUD/FLS guidance with user-mode database operations and avoid presenting `WITH SECURITY_ENFORCED` as the universal modern fix.

### Preparation steps

Good. Make scanner requirements exact:

- Code Analyzer reports: required for managed package submissions.
- Checkmarx/Source Code Scanner: mandatory when the solution includes a Salesforce package or component.
- DAST: required for external components in scope.

### Checklist

The checklist is valuable but should be tightened. Add:

- Lightning Ready confirmed for new solutions.
- Salesforce Code Analyzer report generated with AppExchange and Recommended:Security rules.
- Source Code Scanner/Checkmarx report attached where applicable.
- DAST full report attached for external web apps/APIs.
- Third-party JavaScript libraries checked for known CVEs.
- No Salesforce session ID sent to external systems.

### Failure/resubmission section

Good. Replace "assign owners and deadlines" with "assign owners and target remediation checkpoints" if you want to avoid calendar-style planning language. Emphasize that the report contains representative examples, not every occurrence.

### MagicFuse section

Good positioning, but shorten it. The current version is long and risks sounding like a company profile pasted into a guide. Use one short case example and then list services.

## Sources checked

- Salesforce ISVforce Guide: "How the AppExchange Security Review Works"
- Salesforce Code Analyzer documentation: "Produce Code Analyzer Reports for AppExchange Security Review"
- Salesforce Developers Blog: "Prepare Your App to Pass the AppExchange Security Review"
- Trailhead: "Security Review Preparation & Tools"
- Partner Security Portal SourceScanner Help, including "Chimera Sunset and DAST Scan"
