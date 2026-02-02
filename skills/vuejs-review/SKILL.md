---
name: vuejs-review
description: conventions for reviewing .vue file
---

RULES:

- Do not report Missing User-Facing Error Feedback for the HttpClient fetch, it is already handled
- If a computed property is used where a constant would suffice, suggest this as feedback.
- Top-level refs are automatically unwrapped in template expressions (including event handlers). Do not flag template ref assignments like `showModal = false` as errors - `.value` is only required in `<script setup>` sections. However, refs nested as object properties (e.g., `obj.ref.value`) still require `.value` in templates.
- Allow inline arrow function
- Before report `Missing Null Check`, confirm if a `v-if` condition already ensures the variable is not null.
- If the caller uses `v-if` to guarantee the existence of props, do not flag non-reactive prop assignment issues.
- Do not report global type declaratio.
- Prefer import from submodule using the package name (vipaginatedtable, vicommon, vue-iwform). E.g.
  Prefer `import { ConfigTypeEnum } from 'vicommon/utils/apiEnum'` instead of `import { ConfigTypeEnum } from '~/libraries/common/utils/apiEnum'`
- Avoid wrapping HttpClient calls with `try...catch` blocks unless additional error handling is required, as HttpClient already handles error and success toasts.
- Before suggesting to use computed, check if the reactive variable is subjected to change
- Do not report standard practices in reviews (e.g., adding files to .gitignore, standard configuration changes that follow common conventions)

HttpClient.ts related

- should not prompt to use `defaultErrorToastMsg`, it is up to caller
