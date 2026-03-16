---
name: merge-request-write-desc
description: Generate a concise merge request description from staged changes. Use when drafting an MR/PR description or summarizing branch changes vs. base.
---

## Output

Save the MR description to:

`./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md`

## MR description sections

**Required**

- **Summary** — 1–3 sentences on what this branch changes.
- **Changes** — Bullet list of main code or behaviour changes, ordered **sequentially** to reflect how the flow evolves (earliest/entrypoint changes first, follow‑up/dependent changes after). For closely related steps in the same flow, either:
  - use **sub‑bullets** under a main bullet, or
  - use `>` within a single bullet (e.g. `validate input > call service > persist result`) to show the progression.
- **Testing** — How it was tested and current status.

**Optional**

- Add **Screenshots** (with before/after if relevant) when the change includes UI.
- If the user’s prompt contains `TASK`, add a **Task** section before Summary with a placeholder for the link.

**Suggested commit message** (append or use separately)

- Header: `<type>: <short-description>` (e.g. feat, fix, refactor, docs, chore).
- **Changes** — Bulleted technical modifications.
- **Rationale** — Brief benefit (consistency, performance, debt reduction).
- **Testing** — Steps to verify.
