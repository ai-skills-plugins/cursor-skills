---
name: vuejs-review
description: conventions for reviewing .vue file
---

- Before report `Missing Null Check`, confirm if a `v-if` condition already ensures the variable is not null.
- If a computed property is used where a constant would suffice, suggest this as feedback.
