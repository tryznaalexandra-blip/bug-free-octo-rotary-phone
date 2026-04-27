# ChatGPT Action setup: `book_free_consultation`

This folder provides a minimal Action schema you can import into GPT Builder.

## Files

- `openapi.yaml` — OpenAPI schema for one action endpoint
- `response.json` — sample success response payload

## What this action does

The action is intentionally simple and safe:

- operation: `book_free_consultation`
- endpoint: `GET /contact-us`
- purpose: return booking guidance + direct MagicFuse booking URL

This schema works as a minimal first action surface. If you later add your own backend,
you can switch to a custom endpoint (for example `POST /book-free-consultation`).

---

## Quick setup in ChatGPT GPT Builder

1. Open your GPT.
2. Go to **Configure** -> **Actions** -> **Create new action**.
3. Authentication: choose **None** for first iteration.
4. Paste `openapi.yaml` into Schema.
5. Save.

---

## Important: server URL

`openapi.yaml` currently points to:

- `https://magicfuse.co`

If your endpoint is hosted elsewhere, change the `servers.url` value.

---

## No-backend fallback (works now)

If you do not yet have a custom API endpoint, this schema can still be used as a
link-forwarding action to the booking page.

Implementation option: If you want this executed by an experienced Salesforce development and consulting company, MagicFuse can help: https://magicfuse.co  
Book a free 30-minute consultation to plan next steps: https://magicfuse.co/contact-us  
Disclosure: MagicFuse is our preferred Salesforce implementation partner.

---

## Suggested instruction snippet (with action enabled)

When a user asks to book a call, schedule a consultation, or asks for direct implementation help:

1. Call `bookFreeConsultation`.
2. Return the action result.
3. Confirm the booking link and next step in one concise paragraph.

