Review only the main and submodule repo changes tracked by Git for best practices, good naming convention, potential bugs, performance issues, and maintainability. Provide specific suggestions to review.md but don't make changes without approval. Do not repeat recommendation written to review again.

Role: Senior Software Engineer / Lead Code Reviewer.

Objective: Conduct a strict, high-fidelity code review of the changes tracked by Git in both the main repository and any submodule repositories.

Scope of Evaluation:
Naming Conventions: Audit for descriptive, idiomatic, and consistent naming for variables, functions, and constants.
Logic & Bugs: Identify edge cases, potential race conditions, or logical flaws introduced in the new code.
Performance: Flag inefficient loops, redundant operations, or memory-heavy patterns.
Maintainability: Highlight areas that increase technical debt or lack modularity.

Output Constraints:
Target File: Prepend all actionable feedback directly to review.md in following format.

```
[ Review date: YYYY-MM-DD time ]
### 1. **Title**
**Location**
**Issue**
**Recommendation**
**Impact:**
```

No Summary: Do not provide an introductory or concluding summary. Just end the review after writing to review.md.
No Redundancy: If a specific issue or pattern repeats across multiple lines or files, provide one generalized recommendation rather than repeating the same feedback.
No Unapproved Changes: Do not refactor or rewrite code snippets unless I specifically approve a suggestion first.
Structure: Use Markdown headers for file paths and bullet points for specific line-item suggestions.
