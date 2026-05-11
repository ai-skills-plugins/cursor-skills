---
description: Turn customer-impacting commit logs into clear release notes
---

- Analyse supplied commit logs and produce grouped changelog notes.
- Preserve original prefix, including brackets and parentheses.
- Preserve trailing references exactly: `(#number, commit-id)` or existing equivalent.
- Rewrite customer-facing entries in plain, outcome-focused language.
- Use title case for readable headings when appropriate.
- Group entries by impact:
  - `Changes to be tested`: user-visible behavior, workflow, UI, API, validation, permission, data, integration, performance, reliability, or release-risk changes.
  - `Changes for internal consumption`: refactors, renames, moves, formatting, cleanup, documentation, tests, tooling, prompts, skills, config, dependency metadata, and other behavior-preserving changes.
- Treat behavior-preserving code changes as internal consumption: renames, namespace moves, extraction, consolidation, dead-code removal, restructuring, integration/service rerouting behind stable contracts; `Changes to be tested` only when identical inputs yield different HTTP/JSON, validation, permissions, or substantive side effects.
- Do not claim customer impact when the commit only changes maintainability, organization, naming, or developer workflow.
- Composer/lockfile edits: default to normal dependency/release rubric; `Changes for internal consumption` only when the diff strictly root-declares or reinstalls packages previously satisfied only transitively (graph hygiene, same effective library) with no deliberate semver move, substitution, or advisory response evident from message/diff.
- Merge related commits into one concise entry when they share the same user-facing or internal outcome.
- One shared `(#…)` or one MR scope → one changelog bullet; anchor text from `Merge pull request … (#…)` / squash-merge head carrying that ref; skip sibling branch commits on that MR unless they add an uncovered deliverable.
- Omit changelog rows for branch-sync-only merges (`Merge branch …`, `Merge remote-tracking branch …`, staging/production propagation) with no exclusive deliverable; never duplicate the same `(#…)` as both that anchor and a branch-tip title.
- Keep each entry scannable: `- **Heading**: Outcome sentence. (references)`
- Omit empty sections.
