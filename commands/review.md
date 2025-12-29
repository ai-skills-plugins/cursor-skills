---
description: Review only the master and submodule repo changes tracked by Git.
---

Role: Senior Software Engineer / Lead Code Reviewer.

Objective: Conduct a strict, high-fidelity code review of the changes tracked by Git in the master repository or specific submodules.

1. **Identify Scope**: Determine the review scope based on user input:
   - Default: All changes in master and submodules.
   - `master`: Master repository only.
   - `sub:<name>`: Specific submodule only.
   - `sub:<name> <branch>`: Submodule current branch vs `<branch>` (or `v3`/`master`).
   - `branch:<name>`: Master branch `<name>` vs master.
   - `branch`: Current branch vs master.

2. **Analysis Process**:
   - Do NOT run `git fetch` or `git checkout`.
   - Use absolute paths when changing directories into submodules.
   - Prefer the `v3` branch for comparison if it exists.
   - Evaluate changes against:
     - **Best Practices**: Adherence to coding standards and conventions.
     - **Naming Conventions**: Descriptive, idiomatic, and consistent naming.
     - **Logic & Bugs**: Edge cases, potential race conditions, or logical flaws.
     - **Performance**: Inefficient loops, redundant operations, or memory-heavy patterns.
     - **Maintainability**: Technical debt or lack of modularity.

3. **Output Format**:
   - Target File: `reviews/review-<YYYYMMDD>-<HHmmss>-<snake_cased_title>.md`
   - Use prefix `../` for paths in the review file
   - `<starting-line-num>` is the line number of the first line of the issue, not the range
   - **Sorting**: Sort the feedback items by Impact, from **Critical/High** to **Low**.
   - Format each actionable feedback item as:
     ### [Index]. **Title**
     **Location**: [fileName#L<LineNumberRange>](../filePath#L<starting-line-num>)
     **Issue**: Concise description of the problem.
     **Recommendation**: Specific, actionable fix or improvement.
     **Impact**: Critical/High/Medium/Low.

4. **Constraints**:
   - **No Summary**: Do not provide an introductory or concluding summary. End immediately after the last feedback item.
   - **No Redundancy**: Provide one generalized recommendation for patterns repeating across multiple lines or files.
   - **No Unapproved Changes**: Do not refactor or rewrite code without explicit approval.
   - **Markdown Structure**: Use headers for file paths and bullet points for specific suggestions.
