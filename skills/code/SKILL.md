---
name: code
description: Karpathy-Inspired Claude Code Guidelines. See https://github.com/multica-ai/andrej-karpathy-skills
---

Merge with project-specific instructions. Trivial tasks: use judgment.

## Think before coding

- State assumptions; ask when uncertain
- Multiple valid interpretations → list all; do not choose silently
- Simpler viable approach → surface it; push back when warranted
- Blocker unclear → stop; name what is unclear; ask

## Simplicity

- Ship minimum code for the request only
- No unrequested features, single-use abstractions, extra configurability, or handling for impossible cases
- Overbuilt solution → cut down (target ~4× reduction when bloated)
- Overcomplicated-by-senior-engineer test before shipping

## Surgical changes

- Edit only what the request requires
- No drive-by fixes to adjacent code, comments, or formatting
- No refactor of unrelated unbroken code
- Match existing style even if you would differ
- Pre-existing dead code → note only; do not delete unless asked
- Remove imports/variables/functions made unused by your diff only
- Every changed line must trace to the user request

## Goal-driven execution

- Turn tasks into explicit, verifiable success criteria before work
- Prefer test-first or check-first formulations (invalid inputs, repro bug, tests green before/after refactor)
- Multi-step work → numbered steps each with a verify check
- Vague success ("make it work") → clarify criteria before implementing

- Changes complete: `/review` → fix issues → run linting and unit test