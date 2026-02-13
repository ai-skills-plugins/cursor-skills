---
description: Implement a solution from an implementation plan, then review, test, and fix up to 3 times on failure.
---

# Implement, Review, Test, and Validate

Execute an implementation plan: implement, self-review, run tests, fix failures (max 3 attempts).

**Re-entry**: If the implementation or tasks are already completed, run the command starting from step 2 (Review).

## 1. Implement

- **Input**: Latest implementation plan (e.g. `implementations/` or provided plan).
- **Action**: Implement strictly per plan. Follow project conventions; change only what the plan specifies.
- **Output**: Generate or modify the necessary files.

## 2. Review

- Self-review before testing: correctness vs plan, naming/structure, edge cases, security (no sensitive exposure, auth where needed).
- Fix any issues found before running tests.

## 3. Test

- Run the project test suite (e.g. `pnpm test`, `php artisan test`, `pest`, `vitest`).
- All pass → done. Any failure → go to step 4.

## 4. Fix and Retry (max 3 attempts)

- On failure: identify root cause from messages/logs, apply minimal fix, re-run tests.
- Repeat at most **3 times** for the same implementation.
- After 3 failed attempts: stop and report what was implemented, what still fails (last errors), fixes tried, and suggested next steps. Do not claim success.

## Constraints

- No scope creep; minimal fixes on failure.
- Use the project’s standard test command; do not skip or substitute tests.
