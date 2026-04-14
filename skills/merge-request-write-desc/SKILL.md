---
name: merge-request-write-desc
description: Generate a concise merge request description from staged changes. Use when drafting an MR/PR description or summarizing branch changes vs. base.
---

## Output

Save the MR description to:

`./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md`

## Workflow

1. Determine the diff base:
   - If current branch is `v3`, use its normal merge base/upstream.
   - If current branch is not `v3`, use `v3` as the base branch for summary and change analysis.
2. Analyze commits and code changes against the selected base.
3. Write a concise, customer-relevant MR description using the required sections below.
4. Add optional sections only when relevant.
5. Save the final content to the output path.

## MR Description Sections

**Required**

- **Summary** — 1-3 sentences on what this branch changes and why it matters.
- **Changes** — Bulleted main changes ordered sequentially by flow (entrypoint to downstream effects). For related steps in one flow:
  - use sub-bullets, or
  - use `>` in one bullet (example: `validate input > call service > persist result`).
- **Testing** — How it was validated and current status.
  - For API (PHP) changes, include a frontend developer test scenario focused on consumer-facing behavior:
    - request payload
    - expected response shape/status
    - key error cases
  - Only include what testers need to validate behavior; omit internal implementation details.

**Optional**

- **Task** — If the prompt contains `TASK`, add this section before Summary with a placeholder link.
- **Screenshots** — Add before/after screenshots when UI is affected.

## Suggested Commit Message

Append this only when requested by the user.

- Header: `<type>: <short-description>` (example: feat, fix, refactor, docs, chore).
- **Changes** — Bulleted technical modifications.
- **Rationale** — Brief value or motivation.
- **Testing** — Steps to verify.
