---
name: delete-stale-review-branches
description: >-
  Find and delete remote git branches ending in -review whose tip commit is
  older than 2 months. Use when the user asks to prune stale review branches,
  clean up remote -review branches, or run delete-stale-review-branches.
disable-model-invocation: true
---
# Delete stale remote `-review` branches

## Defaults

- Remote: `origin`
- Suffix: `-review` (exact end of branch name)
- Age: tip `committerdate` older than 60 days (~2 months)
- Scope: remote branches only (does not delete local branches)

## Workflow

1. `git fetch --prune origin`
2. List candidates (dry-run first unless user already confirmed delete):

```bash
python3 ~/.cursor/skills/delete-stale-review-branches/scripts/prune_stale_review_branches.py --dry-run
```

3. Show the list + count to the user.
4. Delete only after explicit confirmation (or when the current user message already ordered delete):

```bash
python3 ~/.cursor/skills/delete-stale-review-branches/scripts/prune_stale_review_branches.py --delete
```

5. Report deleted names + count; note any push failures.

## Overrides

Pass flags when the user specifies them:

- `--remote <name>`
- `--suffix <suffix>` (default `-review`)
- `--days <n>` (default `60`)
- `--dry-run` / `--delete`

## Rules

- Never delete `main` / `master` / protected defaults even if they somehow match.
- Never force-push; only `git push <remote> --delete <branch>...`
- Batch deletes (max ~15 names per push) to avoid oversized argv.
- Age metric: tip commit `committerdate`, not branch creation reflog.
- After delete, optional `git fetch --prune <remote>` to drop stale remote-tracking refs.
