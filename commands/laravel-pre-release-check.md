---
description: Pre-release checklist for Laravel changes between production and staging. Runs git log/diff on origin/production..origin/staging and summarizes commits, risky areas, model/API surface, and env/config.
disable-model-invocation: true
---
## Scope

Compare **staging** against **production** using:

- `origin/production..origin/staging` (commits on staging not in production)

Ensure `origin/production` and `origin/staging` exist locally (`git fetch origin` first if refs are missing or stale).

## Output

Save the report to:

`./ai-agent/release/<YYYYMMDD>-<HHmmss>-laravel-pre-release-check.md`

Use this outline:

1. **Step 1 — Commit summary**
2. **Step 2 — Modified code quick pass**
3. **Step 3 — Model / API field exposure**
4. **Step 4 — Environment variables**
5. **Step 5 — Patch / seed console commands to run**
6. **Step 6 — Privilege changes → OrgRoleSeeder**

Under each step, include a short **Summary** of what you found from the actual git output for that step. End the report with a consolidated **Commands to run on deploy** section (see Completion).

## Workflow

Execute the commands below in the repository root, then answer each step from real output (do not invent commits or files).

### Step 1 — Check the summary for list of changes

- **Run:** `git log origin/production..origin/staging --oneline`
- **Summary:** List how many commits, highlight themes (features, fixes, refactors), and call out anything that **might be breaking** (major refactors, renames, removals, auth, billing, exports).
- PR refs: render each as inline-code `#NNN` (backticks per ref), not plain #NNN; digits copied verbatim from the log's `(#…)`.

### Step 2 — Do a quick check on the modified code

- **Run:** `git diff origin/production..origin/staging --stat` (optional: `--name-only` for a file list)
- **Run:** `git diff origin/production..origin/staging` as needed for detail on high-risk paths
- **Summary:** Focus on **public APIs**, **shared services**, and **configuration** changes. Note anything that could break **existing consumers** (route/method changes, response shape, jobs, events, middleware, service bindings).

### Step 3 — Review changes to model fields exposed via admin or customer APIs

- **Use:** The same diff range; prioritize `app/Models`, `app/Http/Resources`, API controllers, transformers, and admin serializers.
- **Summary:** Note removed/renamed **public** or serialized attributes. Mention **regression risk** (example pattern: customer portal or UI expecting a field such as `events.modal_id` — if removed, dependent features break).

### Step 4 — Review for new or changed environment variables

- **Use:** Diff for `.env.example`, `.env.testing`, `config/*.php`, Docker/CI env files, and any docs that list env vars.
- **Summary:** List new/changed/removed variables and whether **documentation** (comments, internal docs, deploy notes) appears updated.

### Step 5 — Find patch/seed console commands to run

- **Run:** `git diff --name-status origin/production..origin/staging -- 'app/Console/Commands' 'packages/*/src/Console/Commands' 'database/seeders' 'database/seeds' 'packages/*/**/Seeders'`
- **Run:** `git diff --name-status origin/production..origin/staging | grep -iE 'console|command|seed'` (catch-all for stragglers).
- Per hit, extract identity: commands → `$signature` + `$description`; seeders → `class … extends Seeder` + `run()` body; resolve seeder invocation name including any `class_alias` registered in service providers.
- Classify each: (a) **must-run** release patch/seed (backfill, data fix, one-off migration-of-data, historical seed); (b) **conditional** — feature-gated, run only if that feature ships this release; (c) **not a run-target** — on-demand dev/admin/support helper.
- Status `A` (new) vs `M` (modified): a modified helper is a run-target only when the change is itself a data patch; refactor-only or delegation changes are **not**.
- Per run-target capture: exact `php artisan` invocation; required/optional args+options; idempotency (safe re-run vs one-shot); prerequisite migration(s); per-tenant/per-org looping need.
- Flag any command requiring `--org-id`/tenant arg as **per-org** — must loop all orgs or the patch/rollup stays empty for the rest.
- **Summary:** ordered run-list (migrate → `composer install` → seeders/backfills → conditional), each with invocation, prerequisite, idempotency, looping; plus a separate list of modified-but-not-run helpers and why they are excluded.

### Step 6 — Detect privilege changes requiring OrgRoleSeeder

- **Run:** `git diff --stat origin/production..origin/staging -- app/Helpers/Privilege.php`
- Any change (new const, `PRIVILEGES_LIST`/`*_GROUP` edit, `getPermissionForXxx` edit) leaves default role privileges stale until reseeded.
- If changed, add a **must-run** reminder to the run-list; idempotent, safe to re-run (updates default privileges without side effects):

```
php artisan db:seed --class=OrgRoleSeeder
```

- **Summary:** state whether `Privilege.php` changed; if so, flag the `OrgRoleSeeder` run as a required follow-up.

## Completion

- End with a **Pre-release verdict**: **Ready** / **Needs follow-up** + **top 3 follow-ups** (if any).
- Then a final **Commands to run on deploy** section consolidating every run-target from Steps 5–6.
- App-level scripts only: `db:seed --class=<Seeder>`, one-off backfills/patch commands, `OrgRoleSeeder` when `Privilege.php` changed (Step 6).
- **Exclude** commands the deploy pipeline auto-runs (dependency install, migrations); state the exclusion inline.
- Order after migrations; copy-ready fenced block; per command, inline note = reason + idempotency + per-org looping.
- Separate fenced block for conditional/feature-gated commands.
- Append a line naming modified-but-not-run helpers (do-not-run).
- Surface any must-run seed/backfill/reseed as a follow-up in the verdict.
- Ensure the final report is written to the output path above.
