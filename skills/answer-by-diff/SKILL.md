---
name: answer-by-diff
description: >-
  Answer comparison, option, design, and "what changes" questions with critical
  deltas first: exact before/after snippets, full widened allow-lists, no
  guessing. Use when the user asks to show option A/B, compare approaches,
  explain a proposed change, show what widens/expands, show exact diffs to
  original code, or wants an answer they can get immediately without reading a
  full plan or pseudocode dump.
disable-model-invocation: false
---

# Answer by diff

When answering "what changes / show option / compare / widen / exact" questions:
lead with the smallest set of critical edits to the original code. Exact text.
Reader must not guess or re-derive from a long narrative.

## Hard rules

1. **Critical changes first** - open with the exact before/after (or after-only if new). No preamble, no restated question, no full-flow pseudocode before the deltas.
2. **Exact, not summarised** - paste real identifiers, arrays, keys, signatures. If an allow-list widens, show the **full** resulting list, not "and other fields".
3. **Mark every changed line** - in both Before and After code blocks, annotate the lines that differ so the reader does not have to visually diff. Use trailing end-of-line comments (language-appropriate):
   - `// CHANGED: <short why>` on a line that is edited (Before = old form; After = new form)
   - `// NEW: <short why>` on a line/block that only exists in After
   - `// REMOVED: <short why>` on a line that only exists in Before (or comment above a deleted block)
   - Leave unmarked lines alone - unmarked means unchanged.
   - Prefer contiguous Before/After blocks for the same span; do not hide the edit behind `// ...` with no marker.
4. **One critical unit per numbered section** - e.g. (1) model allow-list, (2) call-site swap, (3) unchanged.
5. **Unchanged last** - short bullet list of what stays as-is. Do not re-explain them.
6. **No whole-plan dump** - full pseudocode only if user asks, and only after the critical deltas (or in a follow-up).
7. **ASCII only** in code/lists: straight quotes, hyphen `-`, `...` not ellipsis char.

## Answer shape (default)

```markdown
Critical deltas only.

### 1. `<path-or-symbol>` — `<what>`

**Before**
\`\`\`php
$this->mergeAddressDiffs(   // CHANGED: rename + widen
    buyer: $buyer,
    validated: $validated,
);
if ($isAuditLog) {   // CHANGED: also require non-empty diffs
    // ...
}
\`\`\`

**After**
\`\`\`php
$this->mergeValidatedAttributeDiffs(   // CHANGED: was mergeAddressDiffs
    buyer: $buyer,
    validated: $validated,
);
// NEW: skip empty audit row
if ($isAuditLog && (! empty($beforeData) || ! empty($afterData))) {
    // ...
}
\`\`\`

### 2. Unchanged

- `symbol` — reason one short clause
```

Omit empty sections. If only one site changes, one numbered block is enough.

## What counts as "critical"

Prefer these over flow prose:

- Allow-lists / consts / `$changeAuditColumns` / select cols / fillable / rules keys
- The exact call swap (`update` -> `fill` + `logUpdate` + `save`, etc.)
- Signature / arg / return shape changes
- Condition that gates create vs skip
- Anything the reader would otherwise infer from a long plan

## Anti-patterns

- Opening with full function pseudocode before showing the 5-line edit
- "basically adds the profile fields" without listing every key
- Diffs that say `// ... more fields` for the widened set
- Contiguous Before/After with no `CHANGED`/`NEW`/`REMOVED` markers (forces visual guessing)
- Restating Option A vs B trade-offs when the user asked for exact widen content
- Mixing "unchanged" explanation into the critical before/after blocks

## When user asks for both exact widen and full flow

1. Critical deltas (this skill) first.
2. Then, only if asked: complete pseudocode in a separate section titled `Full flow` / `Complete pseudocode`.
