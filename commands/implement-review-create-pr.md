---
description: Implement, review, create pr
---

run /implement, then /v3-review fix per change. When all tests pass, git push and use /merge-request-write-desc to create pr

## Commits

- always commit single atomic checkpoint when there is more than one check point. NEVER commit multiple checkpoint into one commit.
- Checkpoint = one route + Action + tests (same as `/implement`).
- More than one checkpoint: auto-commit after each checkpoint's review+test gate, before the next checkpoint starts. `/implement` "NEVER git commit" does not apply.
- One checkpoint: commit once before push (this command asked for PR).
- Before push: if uncommitted/staged work covers more than one checkpoint, split into one commit per checkpoint. Do not squash, amend-together, or dump the dirty tree into one commit.
