---
description: Improve code structure and readability without changing behavior.
---

# Objective: System Optimization
Optimize existing code for maximum maintainability and structural integrity while preserving identical functional behavior.

1. **Pre-Refactor Check**:
   - Consult `.cursorrules` to ensure alignment with project-specific design patterns (e.g., Service layer, Component-based architecture).
   - Map existing dependencies to avoid unintended side effects across the stack (back-end vs front-end).

2. **Core Principles**:
   - **SOLID & Design Patterns**: Prioritize the Single Responsibility Principle. Decompose large methods/classes into focused units.
   - **Minimal Diff Principle**: Produce the smallest meaningful change. Avoid "noise" changes that complicate future reviews.
   - **DRY & Clarity**: Eliminate duplication and replace magic numbers/strings with named constants.

3. **Verification**:
   - Behavior must remain 100% identical.
   - Verify that refactored code passes existing tests across the relevant stack.
   - **Architect's Audit**: Does this refactor reduce technical debt or just move it?

4. **Constraints**:
   - Do NOT add new features.
   - If a breaking change is necessary for structural reasons, request explicit approval via `notify_user` first.
