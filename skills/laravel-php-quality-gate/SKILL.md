---
name: laravel-php-quality-gate
description: >-
  After Laravel/PHP code changes, run `php artisan test` then `composer phpstan`
  then `composer pint`; on failure, fix and commit one issue at a time. Use after
  PHP edits, when /implement finishes a Laravel PHP checkpoint, or when the user
  asks for the Laravel quality gate / phpstan / pint post-change check.
disable-model-invocation: true
---

# Laravel PHP quality gate

## Trigger

- After Laravel/PHP change this wave (`app/`, `tests/`, `routes/`, `database/`, `config/`, `packages/**/*.php`, related PHP)
- Mandatory from `/implement` when targeted tests green + PHP files changed
- Skip if wave touch no PHP

## Commands (strict order)

Laravel app root. Prefer project PHP (`AGENTS.md`); else `/opt/homebrew/bin/php` then `php`.

1. `php artisan test`
2. `composer phpstan`
3. `composer pint`

No reorder/skip/substitute. Stop at first fail.

## Failure loop

Fail at step N:

1. Diagnose from that cmd output only; minimal fix
2. Commit that fix alone — skill mandate overrides "commit only when asked"
3. Re-run step N→3; no advance past red
4. Repeat till N green → continue chain
5. Same error after 3 fix attempts → stop; report cmd, last errors, commits, next steps. No success claim

Multi independent fails in one gate → fix+commit one-at-a-time; re-run gate after each.

Pint auto-fix → run pint → commit format dirt alone → re-run pint confirm clean.

## Commit rules

- One commit per discrete fix (test / phpstan / pint). No bundle
- Message = why (failing test name / phpstan rule+path / pint format)
- Git safety protocol else (no amend/force/hooks-skip unless user ask)
- Feature/checkpoint commit = `/implement` only; this skill commits gate fixes (+ pint dirt) only

## Return contract

- Each cmd + pass/fail
- Commits (short hash + subject) or none
- Blockers only if stop early
