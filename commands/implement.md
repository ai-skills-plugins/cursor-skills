---
description: Implement a solution from an implementation plan, then review, test, and fix up to 3 times on failure.
---

# Implement, Review, Test, and Validate

**Re-entry**: If implementation/tasks already done, start at step 2 (Review).

## 1. Implement

- Input: latest plan (`ai-agent/implementations/*.md` or provided).
- Strict plan scope + project conventions only.
- Checkpoint = one atomic feature unit (route + Action + tests); no cross-checkpoint bundling.
- Prefer extend existing tests; avoid new files/duplicate setup for same surface.
- If work is not atomic and no checkpoint is specified: create own checkpoint list first; execute one checkpoint at a time; each checkpoint = one commit.
- Tests: extend existing test files/cases when coverage fits; avoid new files or duplicate setup for the same surface.
- Commits:
  - Single checkpoint: do not commit unless user explicitly asked.
  - Multiple checkpoints: auto-commit after each checkpoint passes its review+test gate.

## 2. Review

- Self-review before testing: correctness vs plan, naming/structure, edge cases, security (no sensitive exposure, auth where needed).
- Fix issues before running tests.

## 3. Test

- Run project test suite (`bun test`, `php artisan test`, `pest`, `vitest`).
- All pass → stop; wait for user verify/commit. NEVER `git commit`. Failure → step 4.

## 4. Fix and Retry (max 3 attempts)

- On failure: root cause from messages/logs, minimal fix, re-run tests.
- Max **3** attempts per implementation.
- After 3 failures: stop; report implemented scope, remaining failures (last errors), fixes tried, next steps. Do not claim success.

## Constraints

- No scope creep; minimal fixes on failure.
- Project standard test command; do not skip or substitute tests.
- Omit trivial, skippable issues from user-facing report.
