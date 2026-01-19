BASE

- rules from ./review.md applied

COMMON RULES

- Do not report Missing User-Facing Error Feedback for the HttpClient fetch, it is already handled
- If a computed property is used where a constant would suffice, suggest this as feedback.
- Top-level refs are automatically unwrapped in template expressions (including event handlers). Do not flag template ref assignments like `showModal = false` as errors - `.value` is only required in `<script setup>` sections. However, refs nested as object properties (e.g., `obj.ref.value`) still require `.value` in templates.

HttpClient.ts related

- **HttpClient.ts**: should not use `defaultErrorToastMsg`.
- Before report `Missing Null Check`, confirm if a `v-if` condition already ensures the variable is not null.
