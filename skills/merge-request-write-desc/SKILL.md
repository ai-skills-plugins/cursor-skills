---
name: merge-request-write-desc
description: Generate a concise merge request description from staged changes. Use when drafting an MR/PR description, summarizing branch changes vs. base, or when the user says create pr / pr (creates the PR via forgejo-cli).
disable-model-invocation: true
---

## Output

Save the MR description to:

`./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md`

## Workflow

1. Determine the diff base:
   - If current branch is `v3`, use its normal merge base/upstream.
   - If current branch is not `v3`, use `v3` as the base branch for summary and change analysis.
2. Analyze commits and code changes against the selected base.
3. Writ MR description using the required sections below.
4. Add optional sections only when relevant.
5. Save the final content to the output path.
6. **Create PR** — only when the user prompt contains `create pr` or `pr` (case-insensitive):
   - **Title** — value from the **Git commit title** section.
   - **Base** — if current branch is not `v3`, pass `--base v3`; otherwise omit `--base` (use repo default).
   - Ensure the branch is pushed to the remote before creating the PR.
   - Run from the git repo root (use the Shell tool):

```bash
fj pr create "<title>" --body-file "./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<current-branch-name>.md" [--base v3]
```

   - Omit `[--base v3]` when already on `v3`.
   - On failure, report stderr and do not retry blindly.

## MR Description Sections

**Required**

- **Git commit title**: - `<type>: <short-description>` (example: feat, fix, refactor, docs, chore). plain text, no backticks
- **Summary** — 1-2 concise, end-user-facing sentences in plain language; imperative mood (`add`/`fix`/`update`/`refactor`); state intent and user/business impact.
- **Changes** — ordered by execution flow (entrypoint → downstream); use sub-bullets or `>` chain for a single flow.
- **Commit framing checklist**:
  - analyze `git status`, `git diff`, `git log` for changed files, change type, and repo commit style.
  - choose type by intent: new feature=`add`, bug fix=`fix`, enhancement=`update`, refactor=`refactor`.
  - include scope (affected area/component) and purpose/motivation.
  - prioritize why over mechanics; describe problem solved, not low-level implementation steps.
- **Testing**
  - For API (PHP) changes, include a frontend developer test scenario focused on consumer-facing behavior:
    - request payload
    - expected response shape/status
    - key error cases
  - Only include what testers need to validate behavior; omit internal implementation details.

**Optional**

- **Task** — If the prompt contains `TASK`, add this section before Summary with a placeholder link.
- **Screenshots** — Add before/after screenshots when UI is affected.
