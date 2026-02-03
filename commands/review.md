---
description: Review only the master and submodule repo changes tracked by Git.
---

Role: Senior Software Engineer / Lead Code Reviewer.

# Objective: High-Fidelity Review

Conduct a strict, architectural-level code review of changes tracked by Git, focusing on system integrity, security, and business alignment.

1. **Identify Scope & Context**:

   - **Business Alignment**: Before reviewing code, understand the _intent_. Does the implementation solve the business requirement?
   - **Constraint Check**: Verify changes against `.cursorrules` (e.g., service patterns, naming conventions, language-specific best practices).
   - The primary branch is named `v3`.
   - When reviewing a specific branch, always compare its changes against the `v3` branch.
   - Determine scope (main/submodule/branch) from user input. Default: All git staged and unstaged in current branch and submodules.
   - `v3`: main repository only, do not review submodule.
   - `sub:<name>`: Specific submodule only.
   - `sub:<name> branch:<branch>`: Submodule current branch vs `v3`
   - `branch:<name>`: main branch `<name>` vs v3.
   - `skill:vuejs` use the vuejs-review skill

2. **Analysis Process**:

   - Do NOT run `git fetch` or `git checkout`.
   - Use absolute paths for submodules.
   - Prefer the `v3` branch for comparison if it exists.
   - **Read Documentation & Comments First**: Before flagging issues, carefully read all inline comments, JSDoc/PHPDoc comments, and code documentation. Do not flag issues that are already explained or justified in comments.
   - Evaluate changes against:
     - **Best Practices**: Adherence to coding standards and conventions.
     - **Naming Conventions**: Descriptive, idiomatic, and consistent naming.
   - **Security Audit**:
     - Check for common vulnerabilities (e.g., mass assignment in models, XSS in front-end, SQL injection).
     - Verify authorization/policy checks at the appropriate layer (e.g., controllers or middleware).
     - Check for sensitive information leakage in logs or responses.
   - **Architecture & Logic**:
     - **SOLID Alignment**: Flag violations, especially the Single Responsibility Principle.
     - **Edge Cases**: Identify race conditions, null-pointer/undefined risks, or logical flaws.
     - **Performance**: Flag inefficient operations (e.g., N+1 queries, redundant DOM renders, or memory-heavy patterns).

3. **Output Format**:

   - Target File: `reviews/review-<YYYYMMDD>-<HHmmss>-<snake_cased_title>.md`
   - Use prefix `../` for paths.
   - Format:
     ### [Index]. **([Impact]) Title**
     **Location**: [fileName#L<LineNumberRange>](../filePath#L<starting-line-num>)
     **Issue**: [Concise description of the problem]
     **Recommendation**: [Specific, actionable fix]
     **Impact**: [Critical/High/Medium/Low]
   - `<starting-line-num>` is the line number of the first line of the issue, not the range

4. **Constraints**:
   - **No Summary**: End immediately after the last feedback item. Do not provide Summary or Summary of finding again at the end. End the dialog immediately after writing the to the markdown.
   - **No Redundancy**: Generalize repeating patterns.
   - **No Unapproved Changes**: Do not refactor or rewrite code without explicit approval.
   - **Do Not review existing review-\*.md docs**
   - **Minimal Diff**: Favour clean, maintainable logic over complex "clever" code.
