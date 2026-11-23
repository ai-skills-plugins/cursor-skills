---
description: Create or improve automated tests for the codebase.
disable-model-invocation: true
---
# Objective: Quality Assurance & Regression Control
Build a robust safety net of tests that verify both correctness and failure handling.

1. **Strategic Coverage**:
   - **Happy Paths**: Verify standard success scenarios.
   - **Negative Testing**: Crucial—mandate tests for invalid inputs, authorization failures, and boundary conditions (e.g., empty lists, null/undefined values).
   - **Edge Cases**: Check race conditions or time-dependent logic.

2. **Implementation Standards**:
   - **State Validation**: Verify that the system state reflected the change correctly (e.g., database assertions like `assertDatabaseHas` or UI state assertions).
   - Align with project-specific test patterns (e.g., Pest/PHPUnit for back-end, Vitest/Jest for front-end). Use established helpers and factories per `.cursorrules`.

3. **Execution**:
   - Run tests locally to ensure 100% pass rate.
   - Ensure the new tests are "isolated"—they should not depend on external state or other tests.
