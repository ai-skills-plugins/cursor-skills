---
description: Implement a solution from an implementation plan, then review, test, and fix up to 3 times on failure.
---

# Implement, Review, Test, and Validate

**Re-entry**: prior implement/tasks done → start at step 2 (Review).

## Context budget (mandatory)

- One checkpoint per turn; never bundle checkpoints.
- Read only: named plan path + that checkpoint section + listed scope files. No whole-plan skim, no repo-wide explore, no AGENTS/ADR re-read unless checkpoint cites one.
- If user omits scope files: open checkpoint section only; derive file list from it; then read those paths. Still no broad search.
- Prefer `Read`/`Grep` on known paths over `Task`/explore. Cap discovery: stop once edit targets are identified.
- Do not restate plan, conventions, or prior chat into tool prompts.
- Bloated parent chat + one checkpoint: continue in parent if files already warm; else new chat with plan path + checkpoint id only (not a sub-agent by default).

## 1. Implement

- Input: latest plan (`ai-agent/implementations/*.md` or provided) + optional checkpoint id/title.
- Before coding: scan scope for similar existing fns/helpers that could absorb the change via refactor (vs new parallel code).
- If refactor fits: draft short pseudocode of the refactor; ask user approve/deny before writing code. Do not implement until answered.
- Strict that checkpoint's scope + project conventions only.
- Checkpoint = one atomic feature unit (route + Action + tests); no cross-checkpoint bundling.
- Prefer extend existing tests; avoid new files/duplicate setup for same surface.
- Commits:
  - Prefer commit over no commit unless the change is very simple (typo, one-liner, trivial config).
  - Structural prep first, separate commit, before feature work (e.g. Request→ServiceAction, rename, move, extract/split). Litmus: could land alone, tests green, no new product behavior → separate commit. Do not mix with new behavior.
  - No checkpoints in plan: invent atomic commit units yourself when justified (independent features/fixes/surfaces); one commit per unit after its review+test gate. Skip inventing units only for very simple changes.
  - Single checkpoint: do not commit unless user explicitly asked.
  - Multiple checkpoints: auto-commit after each checkpoint passes its review+test gate, before the next checkpoint starts. NEVER commit multiple checkpoints into one commit.

## 2. Review

- Run `v3-review` skill on the checkpoint's git-tracked changes (not a general review skill).
- Scope: staged + unstaged for this checkpoint only; fix Critical/High before tests.
- No full-plan re-read.

## 3. Test

- Targeted first: filter to checkpoint's test class/name (`php artisan test --filter=…`, `pest -f`, `bun test` path, `vitest` path).
- Full project suite only after targeted green, or when no filter exists / user requires suite.
- All pass → stop; wait for user verify (single checkpoint / very simple). Otherwise auto-commit per the Commits rule above (invented units or multiple checkpoints), then continue the next unit/checkpoint if any. Failure → step 4.

## 4. Fix and Retry (max 3)

- Root-cause from failure messages/logs only → minimal fix → re-run targeted tests.
- Cap 3 attempts per checkpoint.
- After 3 failures: stop; report scope done, remaining failures (last errors), fixes tried, next steps. No success claim.

## Constraints

- No scope creep; minimal failure fixes.
- Use project standard test command family; no skip/substitute.
- Omit trivial/skippable issues from user report.
- Return contract: files changed, test command + result, blockers only. No narrative dump.

## Execution venue

- Default: parent chat (warm plan/conventions).
- Sub-agent only when: parallel independent checkpoints (near-zero file overlap), or parent context so large that reads thrash and isolation is required.
- Sub-agent prompt: plan path, checkpoint id, scope file list, this command, return contract. No pasted plan body if path suffices.
- Skip sub-agent for one-checkpoint or mid-flight steering in-thread.
- Parallel sub-agents: never when shared models/routes/migrations; parent merges/verifies only.
