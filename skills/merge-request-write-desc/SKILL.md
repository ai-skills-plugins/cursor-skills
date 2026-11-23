---
name: merge-request-write-desc
description: Generate a concise merge request description from staged changes. Use when drafting an MR/PR description, summarizing branch changes vs. base, or when the user says create pr / pr (creates the PR via yp-forgejo MCP).
disable-model-invocation: true
---

## Output

- Prompt contains `pr` (case-insensitive): **do not** write an MR markdown file; pass body inline to yp-forgejo `create_pull_request`
- Otherwise: save to `./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md`

## Workflow

- Diff base: branch `v3` → normal merge base/upstream; else → `v3`
- Analyse commits + diff vs base
- Write MR sections below; optional sections only when relevant
- Save to output path
- **Create commit** only if prompt contain `create commit`
- **Create PR** only if prompt contains `create pr` or `pr` (case-insensitive):
  - Title = **Git commit title** value
  - Push branch first
  - Resolve `owner` / `repo` from Forgejo remote (usually `origin` via `git remote get-url`):
    - SSH `git@<host>:<owner>/<repo>.git`
    - HTTPS `https://<host>/<owner>/<repo>.git`
  - Call MCP `user-yp-forgejo` → `create_pull_request` with:
    - `owner`, `repo`, `title`, `head` = current branch, `body` = full MR markdown
    - `base` = `v3` when current branch ≠ `v3`; otherwise the repo’s default merge base / upstream target used for the diff
  - On failure: report tool error; no blind retry
  - On success: use returned `html_url` (or build `https://<host>/<owner>/<repo>/pulls/<number>` from remote + PR number)
  - **PR URL (non-negotiable):**
    - Final reply MUST open with the full absolute PR URL on its own first line (e.g. `https://code.vilor.com/owner/repo/pulls/631`).
    - Ban: `#631`, `PR 631`, `pulls/631` alone, Forgejo API `url`, or "PR created" without the `html_url`.
    - Every later turn in the same run that mentions that PR (landed, stop, resume, Attention) MUST restate the same full URL — number-only is a failure.
    - Brief-answer / "don't repeat" rules do not override this.
- **No PR:** save to output path after writing sections

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
