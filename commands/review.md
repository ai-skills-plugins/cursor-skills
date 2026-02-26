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
   - when reviewing Typescript/Vuejs, **apply** `vuejs-review` SKILL
   - When reviewing Laravel/PHP, **apply** `laravel-review` SKILL

2. **Analysis Process**:

   - Do NOT run `git fetch` or `git checkout`.
   - Use absolute paths for submodules.
   - Prefer the `v3` branch for comparison if it exists.
   - **Read Documentation & Comments First**: Before flagging issues, carefully read all inline comments, JSDoc/PHPDoc comments, and code documentation. Do not flag issues that are already explained or justified in comments.

   - **Validate Before Flagging** (CRITICAL):

     - **For "may cause" or "could affect" issues**: Either provide **concrete evidence** (code path, query, scenario) that demonstrates the problem, or **do not report** as a finding. Avoid speculative findings without validation.
     - **For inconsistencies**: Cite **both code paths** (file + line ranges) that diverge, showing the actual difference in behavior.
     - **For edge cases**: Verify the scenario is **actually reachable** in the codebase, not just theoretically possible.
     - **For performance concerns**: Show the **actual query pattern** or operation that causes the issue (e.g., N+1 query in a loop, not just "might be inefficient").
     - **Consider existing coverage**: If tests or static analysis (e.g., PHPStan) already cover the concern, note it rather than flagging as a new issue.

  - Evaluate changes against:
     - **Best Practices**: Adherence to coding standards and conventions.
     - **Naming Conventions**: Descriptive, idiomatic, and consistent naming. Stress good method names—names should be specific and reflect what the function or method is trying to achieve.
       - When variable semantics matter, expect names to make it explicit (for example, `email` vs `normalisedEmail` when the value must already be normalised, or `queryToModify`/`mutableQuery` vs a generic `query` when the function is expected to mutate it).
   - **Security Audit**:
     - Check for common vulnerabilities (e.g., mass assignment in models, XSS in front-end, SQL injection).
     - Verify authorization/policy checks at the appropriate layer (e.g., controllers or middleware).
     - Check for sensitive information leakage in logs or responses.
     - **Provide evidence**: Show the code path or scenario where the vulnerability could be exploited.
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
     **Issue**: [Concise description of the problem with evidence - include code paths, call sites, or scenarios that demonstrate the issue]
     **Recommendation**: [Specific, actionable fix, including code snippet if feasible]
     **Impact**: [Critical/High/Medium/Low]
   - `<starting-line-num>` is the line number of the first line of the issue, not the range
   - **Issue description must include evidence**: Cite specific call sites, code paths, queries, or scenarios that validate the concern. Avoid generic statements without concrete examples.

4. **Constraints**:
   - **No Summary**: End immediately after the last feedback item. Do not provide Summary or Summary of finding again at the end. End the dialog immediately after writing the to the markdown.
   - **No Redundancy**: Generalize repeating patterns.
   - **No Unapproved Changes**: Do not refactor or rewrite code without explicit approval.
   - **Do Not review existing review-\*.md docs**
   - **Minimal Diff**: Favour clean, maintainable logic over complex "clever" code.
   - **Evidence Required**: Each finding must include **concrete evidence** (code path, call site, query, scenario) that demonstrates the problem. Do not report issues based solely on "may", "could", or "might" without validation.
   - **Impact Level Restriction**: Do not report an issue as **Critical** or **High** if the concern is speculative (e.g., "may cause", "could affect") unless you have traced the code path or cited a concrete failing scenario. Use **Low** or omit the finding when deeper validation was not performed.
