---
name: merge-request-write-desc
description: Generate a concise merge request description from staged changes. Use when drafting an MR/PR description, summarizing branch changes vs. base, or when the user says create pr / pr (creates the PR via forgejo-cli).
disable-model-invocation: true
---

## Output

- Save to `./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md`

## Workflow

- Diff base: branch `v3` → normal merge base/upstream; else → `v3`
- Analyse commits + diff vs base
- Write MR sections below; optional sections only when relevant
- Save to output path
- **Create commit** only if prompt contain `create commit`
- **Create PR** only if prompt contains `create pr` or `pr` (case-insensitive):
  - Title = **Git commit title** value
  - Push branch first
  - Repo root: `fj pr create "<title>" --body-file "./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md"`; append `--base v3` when current branch ≠ `v3`
  - On failure: report stderr; no blind retry

## MR Description Sections

**Required**

- Title
  - Format: `<flags> <type>: <short-description>`
  - Types: `add` | `fix` | `update` | `refactor` | `docs` | `chore` (match repo style from `git log`)
  - **Backend (API) prefix flags** — prepend applicable flags immediately before `<type>` (combine when multiple apply):
    - `[M]` — new database migration
    - `[C]` — new Laravel Command
    - `[DS]` — database seeding required post-deploy
    - `[B]` — change to existing API or existing request param
- **Summary** — 1–2 imperative sentences; user/business impact; plain language
- **Action** — include only when title has `[M]`, `[C]`, and/or `[DS]`; place immediately after Summary; list concrete post-deploy/run commands (one bullet per command; derive from diff — migration class, artisan signature, seeder class):
  - `[M]` → `php artisan migrate`
  - `[C]` → `php artisan <command-signature>` (exact signature from the new Command)
  - `[DS]` → `php artisan db:seed --class=<SeederClass>` (or the project’s documented seed command for that change)
- **Changes** — execution order (entrypoint → downstream); sub-bullets or `>` chain per flow
- **Commit framing checklist** — from `git status`, `git diff`, `git log`: intent → type; scope + why over mechanics
- **Testing** — API (PHP): frontend-consumer scenario only — payload, response shape/status, key errors; omit internals

**Optional**

- **Task** — prompt contains `TASK` → section before Summary with placeholder link
- **Screenshots** — UI affected only
