---
description: Implement, review, create pr
disable-model-invocation: true
---

run /implement, then /v3-review fix per change. When all tests pass, git push and use /merge-request-write-desc to create pr

## PR link (non-negotiable)

After `create_pull_request` succeeds (or when claiming the PR already landed):

1. Final reply **first line** = full absolute `html_url` only (e.g. `https://code.vilor.com/vilor-internal/sysref-v3-api/pulls/880`).
2. Ban number-only (`#880`, `PR 880`) as the sole reference in that reply or in any later turn that says landed/stop/resume.
3. Restate the full URL on every later turn that mentions that PR. Brief-answer / "don't repeat" rules do not override this.
4. Failure to paste the full URL = incomplete command — fix before ending the turn.

## Commits

- Checkpoint = the smallest independently reviewable/testable unit. Typical: one route + its Action(s) + its tests. Not a whole epic, feature area, or PR.
- ONE checkpoint = ONE git commit. Hard 1:1. NEVER 2+ checkpoints in one commit.
- NEVER combine multiple routes/Actions/tests in one commit, no matter how small or related.
- No plan / non-route work: invent atomic checkpoints before coding. Independent surfaces get separate commits (examples: export command + ADR + its test; one controller/`actionPrivileges` map; generated artefact; glossary/docs submodule). A shared theme ("TypeScript export", "refactor privileges") is NOT one checkpoint.
- "If only one checkpoint: commit once before push" means only when the dirty tree truly is a single unit. It NEVER means "one PR = one commit" or "batch the whole feature then commit once".
- Multi-checkpoint flow: after each checkpoint passes review + targeted tests → commit that unit → only then start the next. `/implement` "NEVER git commit" does not apply under this command.
- Pre-commit / pre-push gate (mandatory): if staged+unstaged changes span more than one checkpoint/surface (e.g. many `Ad*Ctrl` files + command + ADR + generated + docs), STOP. Split into one commit per checkpoint. NEVER squash, amend-together, or dump the dirty tree into one mega-commit.
- Mega-commit ban: a commit that refactors/adds the same pattern across many controllers/classes plus infrastructure in one shot is a failure to invent checkpoints — rewrite history into per-unit commits before push/PR when still local; if already pushed, add a note in the PR and do not repeat.
