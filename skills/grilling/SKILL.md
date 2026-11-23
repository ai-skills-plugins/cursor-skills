---
name: grilling
description: Grill the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.
disable-model-invocation: true
---

- Cover every design-branch decision; settle blocking dependencies before dependents.
- Codebase-discoverable facts: look up; do not ask. Decisions stay the user's: pose and wait.
- No pre-grill. No simple-batch confirm.
- One-shot soundness (Grok 4.7 High Fast): single call, whole decision set. Input = decisions + brief context/constraints. Output package:
  - default locks: obvious picks seed locked-understanding (`decision — one-line rationale`); no user turn
  - open: recommended + reasons + `option — why not selected` alts each
  - Disagree → fine-tune inside that call until agree. Max 3. No agreement which best → log disagreement; ask user which to take.
  - One fat call. Prefer over many thin. No per-question spawn.
- Present (parent only; no re-Task / no re-summarize plan into new soundness call): open questions one per turn from package, full format. Skip default locks unless user contests later.
- Re-soundness only when: package missing alts for contested default; user override invents option not in package; user asks challenge/validate again. Else present package as-is.
- Open question (one grill question or one post-lock gap per turn), order:
  - Recommended solution: concrete proposal acceptance would lock.
  - Reasons selected: why it wins (bullets). This is the discussion.
  - Alternatives record: `option — why not selected` for each credible alternative; keep in this turn. No peer write-up, example, or extra question. Omit only when none exist; do not invent.
  - Define uncommon term only when the choice depends on it.
  - Wait for accept, override, or edit.
- Lock accepted recommendation or user override. Contested default → same open-question path. Alternative records stay on the question turn. Locked-understanding list = accepted decisions only (defaults + locked opens).
- On convergence: locked shared understanding, bullets only.
- Ask to review that understanding for coherence/gaps. Wait yes/no.
- Review declined: stop gap-raising; ask explicit confirm before enacting.
- Review accepted: one issue per turn only if the lock may cause undesired future impact. Same open-question presentation. Do not restate the locked understanding. Amend lock from feedback. Continue until issues exhausted or user stops.
- Reprint lock list at final confirm. Enact only after user confirms shared understanding (post-review confirm, or review declined plus explicit confirm).

## Open-question format (locked)

- Recommended: proposal → reasons-selected bullets → `option — why not selected` record → wait.
- Why selected: recommendation + explicit why on the decision turn; alternatives retained as same-turn record (not a second question); override uses recorded options; same shape for grill and post-lock gaps; reason bullets carry trade-offs so alternatives stay one line; defaults seed lock from one-shot (no batch confirm).
- Alternatives record:
  - Equal-weight menu with per-option trade-offs/examples — rejected: competes with recommendation; crowds one-question turn.
  - Recommendation + reasons only; drop alternatives — rejected: record lost; override needs re-generation.
  - Recommendation now; alternatives only after reject — rejected: record absent from decision turn; options can drift.
  - Two turns (discuss then log alternatives) — rejected: one decision spans two turns; confirm possible before record exists.
  - Pre-grill / simple-batch confirm gate — rejected: ceremony after one-shot; defaults seed lock; contest → open Q.
  - Per-open-Q fresh soundness spawn — rejected: re-reads context; one-shot package + targeted recheck-on-contest only.
  - Prose discussion + bare alternative names — rejected: reasons must be listed; names without why-not are not a selection record.
