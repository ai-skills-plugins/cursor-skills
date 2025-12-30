---
description: Systematically investigate an issue to find its root cause.
---

# Objective: Root Cause Integrity
Systematically isolate the source of a failure using data-driven investigation.

1. **Environment & Data Gathering**:
   - Identify relevant logs for the current stack (e.g., `storage/logs/laravel.log` for PHP, browser console for JS, or build logs for TS/CSS).
   - Use language-appropriate debugging tools and terminal commands to gather output.
   - Use grep/codebase search to trace the data flow from the entry point (API, UI, Command) to the failure.

2. **Investigation Artifact**:
   - Create an internal "Investigation Plan" (markdown) to track:
     - Observed symptoms.
     - Commands executed and their results.
     - Verified vs. falsified hypotheses.

3. **Analysis & Verification**:
   - Systematically prove the root cause. If it's a bug, identify the exact commit or logic change where it was introduced if possible.
   - Propose a fix *only* after the root cause is 100% isolated and understood across the relevant stack.

4. **Architect's Requirement**:
   - Distinguish between "symptoms" and "root causes." Ensure the proposed solution fixes the cause, not just the symptom.
   - Consider cross-language side effects (e.g., how a PHP back-end change affects a TS front-end).
