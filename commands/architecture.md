---
description: Analyze this repository's architecture, file structure, and coding conventions; generate then simplify architecture.md for future agents.
disable-model-invocation: true
---
# Objective: Create and Simplify architecture.md

Analyze the repository, produce an `architecture.md` that future agents can follow strictly, then review and trim it so only essential information remains (to reduce context size).

---

## Phase 1: Analyze

- **Scope**: The **project root** of the current workspace (the repo being worked on), not the `.cursor` folder.
- **Gather**:
  1. **Tech stack**: Languages, frameworks, runtimes, package managers, key libraries (from lockfiles, config files, `package.json`, `composer.json`, etc.).
  2. **Build/run commands**: How to install deps, build, test, lint, run dev/prod (from scripts, CI config, or docs).
  3. **File structure**: Main directories and their purpose (e.g. `src/`, `app/`, `tests/`, config locations).
  4. **Coding conventions**: Style (from configs like `.editorconfig`, `eslint`, `phpcs`, `prettier`), naming patterns, where business logic vs. UI vs. tests live.
  5. **Architectural patterns**: App structure (MVC, layers, modules), how config/env is loaded, how tests are organized.
- **Output**: Use this analysis to draft `architecture.md` in the **project root** (e.g. workspace root of the actual project).

---

## Phase 2: Generate architecture.md

- **Location**: Create or overwrite `architecture.md` at the **repository root** of the project being analyzed.
- **Content** (include only what exists; do not invent):
  - **Tech stack**: Bullet list of core technologies and versions if easily known.
  - **Commands**: Install, build, test, lint, dev server, production run (exact commands).
  - **Directory layout**: Short description of main folders and their role.
  - **Conventions**: Naming, file placement, style tools and rules agents should follow.
  - **Patterns**: How the codebase is structured (e.g. MVC, feature modules, API vs UI).
- **Tone**: Direct, imperative, so an agent can "follow strictly." Prefer lists and tables over long prose.

---

## Phase 3: Review and Simplify

- **Review**: Re-read the generated `architecture.md` and remove:
  - Redundant or obvious points.
  - Long explanations that don’t change agent behavior.
  - Duplicate info (e.g. same command in two sections).
- **Simplify**:
  - Keep: Tech stack, exact commands, critical paths (where to put code, how to run tests), and non-obvious conventions.
  - Cut: Verbose intros, repeated bullets, and anything that can be inferred from the repo.
- **Result**: A shorter `architecture.md` that still gives future agents everything they need to follow the stack, commands, and patterns strictly, with minimal context.

---

## Constraints

- Analyze the **project repository** (the codebase under development), not the `.cursor` config repo, unless the user explicitly asks to document `.cursor`.
- Do not invent technologies or commands; only document what is present in the repo.
- Write for an agent: concise, actionable, and scoped to what affects implementation and review.
