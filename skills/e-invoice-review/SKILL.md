---
name: malaysia-e-invoice-review
description: Specialized reviewer for Malaysia LHDN E-Invoice integration. Use when reviewing e-invoice code, LHDN API integration, or order transaction e-invoicing workflows.
---

# E-Invoice Review

## Implementation Overview

Verify the code adheres to these four pillars of the LHDN workflow:

- Tokens must be cached/persisted to avoid frequent login API calls.
- Must follow a "Submit -> Get SubmissionID -> Poll Status" flow.
- Cancellation is ONLY allowed for e-invoices that have been submitted to LHDN.
- LHDN details (QR codes/UUIDs) must be hidden in views until the invoice is submitted.

## Instruction

- Ensure e-invoice implementation files are organized under a dedicated directory (e.g. vi-e-invoice) to keep them under a package.
- E-invoice must relate to OrderTransaction instead of Order. **Flag as Critical** if e-invoice primarily uses Order.
- Admin and Customer e-invoice endpoints must be under order-transaction resource path, not under orders (e.g. `POST order-transactions/e-invoice`, not `POST orders/e-invoice`). Flag if e-invoice routes are registered under an orders route group, since e-invoice is payment transaction-scoped.
- Admin-level queries must be scoped by organisation, Customer-level queries must be scoped by customerId. **Flag as Critical** if missing `organisation_id` (Admin) or `customer_id` (Customer) filters.
- Compare the outbound JSON/XML payload logic against [LHDN API Specs](https://sdk.myinvois.hasil.gov.my/api/).
- Compile all findings into a `e-invoice-review-report.md`. Do not list "Pass" or "Correct" items. Only include critical issues, potential bugs, and areas of concern that may lead to integration failure or non-compliance with LHDN requirements. Provide recommendations for each issue identified, referencing specific sections of the LHDN documentation where applicable.

## Common Issues & Red Flags

- Flag any call to the Login API that does not check a cache first.
- Flag missing mandatory fields required by the [LHDN Codes](https://sdk.myinvois.hasil.gov.my/codes/).
- Ensure `submissionID` is saved _before_ the async status check job is dispatched.
- Flag miscalculation of e-invoice amount details.

## External References

- Integration Practices: https://sdk.myinvois.hasil.gov.my/integration-practices/
- Sample: https://sdk.myinvois.hasil.gov.my/sample/
- Platform API: https://sdk.myinvois.hasil.gov.my/api/
- E-Invoice API: https://sdk.myinvois.hasil.gov.my/einvoicingapi/
- Main SDK: https://sdk.myinvois.hasil.gov.my/
