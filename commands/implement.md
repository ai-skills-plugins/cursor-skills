---
description: Implement a solution from an implementation plan, then review, test, and fix up to 3 times on failure.
---

# Implement, Review, Test, and Validate

**Re-entry**: prior implement/tasks done → start at step 2 (Review).

## 1. Implement

- Input: latest plan (`ai-agent/implementations/*.md` or provided).
- Strict plan scope + project conventions only.
- Checkpoint = one atomic feature unit (route + Action + tests); no cross-checkpoint bundling.
- Prefer extend existing tests; avoid new files/duplicate setup for same surface.
- Commits:
  - Single checkpoint: do not commit unless user explicitly asked.
  - Multiple checkpoints: auto-commit after each checkpoint passes its review+test gate.

## 2. Review

- Self-review vs plan: correctness, naming/structure, edges, auth/sensitive exposure.
- Fix before tests.

## 3. Test

- Run project test suite (`bun test`, `php artisan test`, `pest`, `vitest`).
- All pass → stop; wait for user verify/commit. NEVER `git commit`. Failure → step 4.

## 4. Fix and Retry (max 3)

- Root-cause from messages/logs → minimal fix → re-test.
- Cap 3 attempts per implementation.
- After 3 failures: stop; report scope done, remaining failures (last errors), fixes tried, next steps. No success claim.

## Constraints

- No scope creep; minimal failure fixes.
- Use project standard test command; no skip/substitute.
- Omit trivial/skippable issues from user report.

## Execution venue

- Default: parent chat (warm plan/conventions).
- Sub-agent when: parent context large, isolation wanted, or parallel independent checkpoints.
- Sub-agent prompt self-contained: plan path, this command, scope, return contract (files, test result, failures).
- Skip sub-agent for one-checkpoint or mid-flight steering in-thread.
