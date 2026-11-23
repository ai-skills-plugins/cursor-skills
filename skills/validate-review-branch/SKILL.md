---
name: validate-review-branch
description: >-
  Validate claims on new commits of a review/source branch; cherry-pick
  oldest-first onto current only when every claim valid; then push. Fire on
  /validate-review-branch or validate-and-cherry-pick from given branch onto
  current.
disable-model-invocation: true
---

# Validate review branch

Source branch required (arg or ask once). Target = current branch. Manual only.

## Preconditions -> fail any = stop

1. Git repo. `HEAD` on branch (not detached).
2. Clean tree ignore submodules:

```bash
git status --porcelain --ignore-submodules=all
```

Non-empty -> stop. No stash. Submodule dirt alone -> ignore, proceed.

3. Resolve `SOURCE_REF`: local `SOURCE` else `git fetch origin SOURCE` then `origin/SOURCE`. Missing -> stop.
4. New commits oldest-first:

```bash
git rev-list --reverse --no-merges HEAD.."SOURCE_REF"
```

Empty -> report "nothing to cherry-pick"; stop; no push.

5. Merges in range -> refuse:

```bash
git rev-list --merges HEAD.."SOURCE_REF"
```

Any hits -> list + stop. No cherry-pick merges.

6. Show candidates:

```bash
git log --reverse --no-merges --oneline HEAD.."SOURCE_REF"
```

## Validate claims (before any cherry-pick)

Per candidate sha, oldest -> newest. Inspect message + full diff:

```bash
git show --stat --patch <sha>
```

Claim valid only if all hold:

- Subject/body match what diff actually does
- Diff coherent for claimed intent; no contradicting/unrelated silent churn
- No secrets / credentials / private keys introduced
- Not empty or no-op while claiming a real change

Any sha fails -> abort + report (failed sha, subject, why invalid). Zero cherry-picks. No push. Stop.

All valid only -> proceed Apply.

## Apply

Oldest -> newest. Per sha: `git cherry-pick <sha>`.

Conflict or non-zero -> `git cherry-pick --abort` now; report failed sha + subject + conflict summary; stop; no push. No resolve. No `--continue`. No ask-to-fix mid-run.

## Push

All picks OK only -> `git push` (current upstream). No `--force` / `--force-with-lease`.

No upstream -> stop + report; keep local picks; user set upstream / name remote+branch. Push fail -> report; no force retry.

## Report

Emit: source ref, current branch, claim-validation outcome, picked commits (hash + subject) or abort reason, push result if reached.

## Never

- Cherry-pick before every claim validated
- Cherry-pick after any claim invalid
- Force push
- Push after validation fail or abort
- Touch source branch
- Rebase/reset current as part of this skill
- Invent default source
- Enter / sync / update / commit inside submodules
