---
name: merge-request-write-desc
description: Generate a concise merge request description from staged changes. Use when drafting an MR/PR description, summarizing branch changes vs. base, or when the user says create pr / pr (creates the PR via forgejo-cli).
disable-model-invocation: true
---

## Output

- **No PR:** save to `./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md`
- **Create PR:** do not save markdown; pass body inline via `--body`
- **Create PR — report URL:** `fj pr create` prints only `#<number>`; always derive and show the **full PR URL** in the final response (markdown link or bare URL). Never report `#123` alone.

## Workflow

- Diff base: branch `v3` → normal merge base/upstream; else → `v3`
- Analyse commits + diff vs base
- Write MR sections below; optional sections only when relevant
- **Create commit** only if prompt contain `create commit`
- **Create PR** only if prompt contains `create pr` or `pr` (case-insensitive):
  - Title = **Git commit title** value
  - Push branch first
  - Repo root: `fj pr create "<title>" --body "$(cat <<'EOF'
<body>
EOF
)"`; append `--base v3` when current branch ≠ `v3`
  - On failure: report stderr; no blind retry
  - On success: parse PR number from stdout (`#<number>`); build URL from the Forgejo remote (usually `origin` via `git remote get-url`):
    - SSH `git@<host>:<owner>/<repo>.git` → `https://<host>/<owner>/<repo>/pulls/<number>`
    - HTTPS `https://<host>/<owner>/<repo>.git` → `https://<host>/<owner>/<repo>/pulls/<number>`
  - Final output: include the full PR URL (e.g. `https://code.vilor.com/owner/repo/pulls/631`), not just the number
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
- **Screenshots** — UI affected only
