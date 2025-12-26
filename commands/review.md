Review only the master and submodule repo changes tracked by Git.

Role: Senior Software Engineer / Lead Code Reviewer.

Objective: Conduct a strict, high-fidelity code review of the changes tracked by Gits.

## Usage Syntax

```
### Basic usage (reviews all changes)
/review

### Scope to master repository only
/review master

### Scope to specific submodule
/review sub:submodule-name

### Scope to specific current branch in the submodule against submodule v3 or master branch.
/review sub:submodule-name branch

### Scope to specific branch comparison
/review branch:feature-branch-name

### Scope to current branch against master (do not run `git diff master` or `git diff master --stat`)
/review branch
```

- Do not run `git fetch or git checkout`
- when cd into `submodule` use absolute path.
- use v3 branch if it exists.

Scope of Evaluation:
**Best practices**: Adherence to common coding standards and conventions
**Naming Conventions**: Audit for descriptive, idiomatic, and consistent naming for variables, functions, and constants.
**Logic & Bugs**: Identify edge cases, potential race conditions, or logical flaws introduced in the new code.
**Performance**: Flag inefficient loops, redundant operations, or memory-heavy patterns.
**Maintainability**: Highlight areas that increase technical debt or lack modularity.

Output Constraints:
Target File: write all actionable feedback directly to reviews/review-<YYYYMMDD>-<HHmmss>-<snake_cased_title>.md in following format.
Don't make changes without approval.

```
### 1. **Title**
**Location** in format [fileName#L<LineNumberRange>](path-from-project-root#L<starting-line-num, example:L99, not L99-110>) app prefix '../' to path
**Issue**
**Recommendation**
**Impact:**
```

No Summary: Do not provide an introductory or concluding summary. Just end the review after writing to review.md.
No Review Summary
No Redundancy: If a specific issue or pattern repeats across multiple lines or files, provide one generalized recommendation rather than repeating the same feedback.
No Unapproved Changes: Do not refactor or rewrite code snippets unless I specifically approve a suggestion first.
Structure: Use Markdown headers for file paths and bullet points for specific line-item suggestions.
