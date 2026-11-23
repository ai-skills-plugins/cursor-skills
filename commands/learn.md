---
description: Research and explain code or concepts without making changes.
disable-model-invocation: true
---
# Objective: Deep System Comprehension
Provide high-fidelity explanations of system architecture, data flow, and conceptual logic.

1. **Structural Research**:
   - Consult `.cursorrules` to understand the intended architectural patterns.
   - Trace data flow from Entry Point (Route/Controller) -> Service Layer -> Model/Database.

2. **Architectural Overview**:
   - Don't just explain lines of code; explain the *relationships* between components.
   - Identify potential design bottlenecks or deviations from established project patterns.

3. **Constraints**:
   - Read-only: Search tools only. No edits or terminal execution.
   - Goal: Leave the user with a mental model of the system, not just a technical summary.
