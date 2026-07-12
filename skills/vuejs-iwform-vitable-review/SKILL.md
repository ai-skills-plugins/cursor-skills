---
name: vuejs-iwform-vitable-review
description: conventions for reviewing .vue files that use viTable (ViPaginatedTable) or IwForm packages
---

RULES:

## Package Imports

- From app/feature code, import packages (`vipaginatedtable`, `vue-iwform`, `vicommon`) by package name, not relative paths
- Within a package's own source, use relative imports for siblings; package-name self-reference needs an `exports` map (absent in `vue-iwform`)
- When a component can be reused by future projects, consider moving it from project code into packages

## ViPaginatedTable

- Use `ViTableConfig` type with `filters: IwFormInput[]` and optional `columnConfig`
- Filters must include `filter` property: `{ c: 'column', o: 'operator', rel?: 'relation' }`
- Use composables pattern for table logic (extract schema, filters, buttons, modal states)
- Schema: `Record<string, string | ViTableColumnSchema>` (string for simple columns)
- Always use `normaliseTableName()` for `name` prop
- Use `privilegeFunc` prop (don't hardcode privilege checks)
- Use `showCheckbox` conditionally based on privileges
- Use `ViSearchBarConfig` for search (not manual search fields)
- Use `tickedRows` ref with `@rowTicked` handler for checkbox selection

## IwForm

- Use `IwFormConfigParam` type with `formGroups` array
- Prefer composables pattern: return `getForm(formData?)` function handling create/edit modes
- Form groups: use `showDivider`, `foldable`, `css` (e.g., `appFormGridColumnTwo`)
- Form inputs: always `type` and `name`; use `disabled`, `isVisible`, `visibleOnData` for conditional logic
- Select: use `selectConfig.optionConfig` with `constantKey` (constants) or `type: 'api'` with `endpoint`
- Date: use `dateOptions` with `enableRangePicker`, `valueWithTimezone`, `format`
- Use `rules` array for validation (beyond `required` prop)
- Use `formData` prop for initial data; `onSubmit` handler for submission
- Use `isModified` prop to enable submit (or `submitBtnAlwaysEnabled` for filters)
- Use `formConstants` prop for passing constants
- NavigationLayout tabs: use `formConfig`, `formData`, `formConstants` in tab config; increment `formKey` ref when data changes
- Create/edit mode: detect via `Boolean(formData?.id)`; conditionally set `disabled`, `isVisible`, `submitText`

## Anti-Patterns

- ❌ Relative imports for package components from app/feature code (relative is correct within the package's own source)
- ❌ Manual form state management when `isModified` handles it
- ❌ Duplicated form/table config logic (use composables)
- ❌ Missing `normaliseTableName()` for table names
- ❌ Hardcoded privilege checks (use `privilegeFunc`)
- ❌ Missing `formKey` increment in tab-based forms
- ❌ Using `watch` to sync form data (use `formData` prop reactivity)
- ❌ Not handling create/edit modes in form composables
