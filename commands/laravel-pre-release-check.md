---
description: Pre-release checklist for Laravel changes between production and staging. Runs git log/diff on origin/production..origin/staging and summarizes commits, risky areas, model/API surface, and env/config.
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

Under each step, include a short **Summary** of what you found from the actual git output for that step.

## Workflow

Execute the commands below in the repository root, then answer each step from real output (do not invent commits or files).

### Step 1 — Check the summary for list of changes

- **Run:** `git log origin/production..origin/staging --oneline`
- **Summary:** List how many commits, highlight themes (features, fixes, refactors), and call out anything that **might be breaking** (major refactors, renames, removals, auth, billing, exports).

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

## Completion

End with a **Pre-release verdict**: **Ready** / **Needs follow-up** and bullet the **top 3 follow-ups** (if any). Then ensure the final report is written to the output path above.
