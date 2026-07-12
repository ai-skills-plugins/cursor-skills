---
description: Implement a solution from an implementation plan, then review, test, and fix up to 3 times on failure.
---

# Implement, Review, Test, and Validate

**Re-entry**: If implementation/tasks already done, start at step 2 (Review).

## 1. Implement

- Input: latest implementation plan (`ai-agent/implementations/*.md` or provided plan).
- Implement strictly per plan; project conventions; change only plan scope.
- Checkpoint scope: smallest complete feature unit per atomic commit (route + Action + tests for one feature; no cross-checkpoint bundling).
- Tests: extend existing test files/cases when coverage fits; avoid new files or duplicate setup for the same surface.

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
