---
name: sysref-project-development
description: Local end-to-end development and validation for the sysref project.
disable-model-invocation: true
---
# Sysref Project Development

## Local environment URLs

Use these URLs for development and validation:

| App                  | URL                                    |
| -------------------- | -------------------------------------- |
| **Admin (frontend)** | https://v3admin.test.vilor.com:3099    |
| **Customer Portal**  | https://v3customer.test.vilor.com:3098 |
| **API (backend)**    | https://v3api.test.vilor.com           |

## Validating Changes

- Read `.login.dev` for email/password when login is required.
- Use the browser tools or browser agent to navigate and interact.
  **Verify:** UI changes, success messages, or data updates.

### What to Verify

- **Admin UI:** Pages load, forms submit correctly, tables display expected data.
- **Customer Portal:** If there are customer-portal changes, verify at the Customer Portal URL: pages load, login (if required), forms and flows behave as expected.
- **API Flows:** Backend changes work via the admin UI or direct API calls.
