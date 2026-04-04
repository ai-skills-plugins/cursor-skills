---
description: Refine user prompt and generate an implementation plan saved to ai-agent/implementations.
---

- investigate the user request to understand the current state and requirements.
- Ask clarifying questions to the user to refine the prompt if any details or scenario contexts are missing or ambiguous.
- Once the requirements are clear, create an implementation plan using the standard `implementation_plan.md` artifact.
- When implementation begins, break the work into small checkpoints. Each checkpoint must contain exactly one single complete feature. A complete feature implies exactly **one action goal** (the API route, its Action class, and its test(s)) per the `docs/architecture.md` Git commit discipline for Atomic commits. Do not combine multiple unrelated actions into one checkpoint. Each complete feature must definitively include tests when applicable. Strictly follow this rule.
- Stop and wait for user evaluation once a checkpoint or step is completed. NEVER commit the changes yourself using git commit. Let the user manually commit the changes for each atomic step.
- Save the finalized implementation plan under `ai-agent/implementations/` with a descriptive filename (e.g. `{{plan_name}}.md`). Do not use a top-level `implementations/` folder.
- Update the `task.md`
- DO NOT PROCEED to change the code
