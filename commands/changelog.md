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
- Treat behavior-preserving code changes as internal consumption, including class/function/file renames, namespace moves, extraction, consolidation, dead-code removal, and implementation-only restructuring.
- Do not claim customer impact when the commit only changes maintainability, organization, naming, or developer workflow.
- Merge related commits into one concise entry when they share the same user-facing or internal outcome.
- Keep each entry scannable: `- **Heading**: Outcome sentence. (references)`
- Omit empty sections.
