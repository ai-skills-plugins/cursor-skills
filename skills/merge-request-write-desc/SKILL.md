---
description: Generate a concise merge request description summarizing staged changes vs. v3
---

## Objectives

draft a clear, concise merge request description for the current branch and save it to `./ai-agent/merge-requests/<YYYYMMDD>-<HHmmss>-<commit-branch-name>.md` with minimal required input.

## Pull Request Description Section

### Must Have

- **Summary**
  - 1–3 sentences describing what this branch changes.
- **Changes**
  - Bullet list of the main code or behaviour changes.
- **Testing**
  - How this was tested and current status.

### Additional

- Add any extra sections you need beyond the items above.

### If the changes includes UI changes

- Add a **Screenshots** section:
  - Include before/after screenshots if relevant.

## Optional Context by Prompt

- If the prompt with this command includes the word `TASK`:
  - Add a **Task** section before **Summary** with only a placeholder for the link.
