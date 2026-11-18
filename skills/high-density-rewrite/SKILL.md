---
name: high-density-rewrite
description: >
  Rewrite Skill/Command docs for agent execution: caveman density, operational
  bullets only, zero human prose. Use when user says "rewrite for skill",
  "remove fluff", "summarize for skills", "high-density rewrite", or attaches
  doc to compress into SKILL.md / command form.
---

Rewrite source into agent-ready Skill/Command. Human prose die. Agent ops stay.

## Audience

Output = machine instruction for agent. Not tutorial. Not blog. Not onboarding.

Agent need: when fire, what do, what never, what decide, what emit.
Agent skip: why-care stories, motivation, soft best-practice, cheerleading.

## Caveman Voice (output)

Match `/caveman` density on rewritten body:

- Drop: articles, filler (just/really/basically/actually/simply), pleasantries, hedging.
- Fragments OK. Short synonyms. Abbreviate common terms (DB/auth/config/req/res/fn/impl).
- Strip conjunctions. Causality via arrows (`X -> Y`). One word when one word enough.
- Pattern: `[thing] [action] [reason]. [next step].`
- Technical terms exact. Code/syntax exact. Errors quoted exact.

## Keep

- Non-obvious ops steps, syntax, flags, paths, tool names
- Hard constraints, refuse/allow boundaries, edge cases
- Decision points + branch outcomes
- Persistence / when-on / when-off rules
- Output contract (shape, forbidden extras)
- Trigger phrases that load skill/command
- Auto-exceptions where terse form risks misread (security, irreversible, ordered sequences)

## Drop

- Examples / "e.g." / walkthroughs / sample dialogues (unless rule inexpressible without one tiny pattern line)
- Definitions agent already know
- Deducible common sense
- Intro/outro, transitions, restated goals
- Motivation, persuasion, "why this matters"
- Redundant section wrappers that add no ops signal

## Compress Moves

- Verbose paragraph -> terse action bullets
- Soft advice -> imperative constraint or delete
- Nested essay -> flat bullets / short headings
- Duplicate rules -> one bullet
- Narrative "if you want X you should Y" -> `Want X -> do Y`

## Structure Target

Prefer caveman-shaped Skill/Command skeleton when source allows:

1. Frontmatter `description` — what + when (triggers)
2. One-line mission (caveman)
3. Persistence / scope (if stateful mode)
4. Rules — keep/drop/do
5. Decision / exception gates
6. Output contract

No filler headings. No "Role" theater. Flat, scannable.

## Output Contract

- Emit only rewritten dense markdown (frontmatter if Skill/Command).
- No methodology restatement. No "here is the rewrite".
- No sample code blocks unless logic otherwise inexpressible.
- Preserve domain-critical correctness; density never drop required constraint.
