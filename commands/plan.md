---
description: Refine user prompt and generate an implementation plan saved to implementations folder.
---

1. /investigate the user request to understand the current state and requirements.
2. Ask clarifying questions to the user to refine the prompt if any details or scenario contexts are missing or ambiguous.
3. Once the requirements are clear, create an implementation plan using the standard `implementation_plan.md` artifact.
4. Save a copy of the finalized implementation plan to the `implementations` folder with a descriptive name: `cp {{implementation_plan_path}} implementations/{{plan_name}}.md`
5. Update the `task.md` to reflect the transition to the execution phase.
6. Do not update or change existing code
