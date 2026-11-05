---
description: Refine user prompt and generate an implementation plan saved to ai-agent/implementations.
---

- Investigate request: current state + requirements.
- **MANDATORY FIRST:** Clarify missing/ambiguous details. One question at a time; wait for answer. Prefer single-select radio options + `Other`.
- Create plan only after all critical clarifications resolved. Use standard `implementation_plan.md` artifact.
- Checkpoints: one complete feature each = one action goal (route + Action + tests) per `docs/architecture.md` atomic-commit discipline. No unrelated actions in one checkpoint. Include tests when applicable.
- Structural prep as its own checkpoint/commit before feature work (e.g. Request→ServiceAction, rename, move, extract/split). Litmus: could land alone, tests green, no new product behavior → separate commit. Do not mix with new behavior.
- After each approved checkpoint: commit that atomic step, then continue. Stop and wait for user evaluation between checkpoints.
- Save under `ai-agent/implementations/` with descriptive name (`{{date}}{{plan_name}}.md`). No top-level `implementations/`.
- New plan file top headers (before title/body):
  ```
  Created: YYYY-DD-MM HH:mm
  Completed Checkpoint: X, YYYY-DD-MM HH:mm
  ```
  Fill `Created` now; leave `Completed Checkpoint` as `—` until done, then set `X` + completion timestamp.
- DO NOT update `task.md`.
- DO NOT change code.
