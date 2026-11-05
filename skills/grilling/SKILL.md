---
name: grilling
description: Grill the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.
---

- Cover every design-branch decision; settle blocking dependencies before dependents.
- Codebase-discoverable facts: look up; do not ask. Decisions stay the user's: pose and wait.
- Pre-grill: decide simple items; batch-list each as `decision — one-line rationale`; wait for confirm. Confirm → complex grill. Do not interleave simple confirms with complex questions. Rejected batch item → open question.
- Pre-grill soundness (Grok 4.7 High Fast): before presenting the batch, validate decisions with that model. Disagreement → fine-tune and reconfirm until agree. Max 3 attempts. No agreement on which is best → log disagreement; ask user which to take.
- Open question (one complex-grill question or one post-lock gap per turn), order:
  - Recommended solution: concrete proposal acceptance would lock.
  - Reasons selected: why it wins (bullets). This is the discussion.
  - Alternatives record: `option — why not selected` for each credible alternative; keep in this turn. No peer write-up, example, or extra question. Omit only when none exist; do not invent.
  - Define uncommon term only when the choice depends on it.
  - Wait for accept, override, or edit.
- Open-question soundness: same Grok 4.7 High Fast loop as pre-grill (validate → fine-tune on disagree → max 3 → else log and ask user) before presenting recommendation + alternatives.
- Lock accepted recommendation or user override. Alternative records stay on the question turn. Locked-understanding list = accepted decisions only.
- On convergence: locked shared understanding, bullets only.
- Ask to review that understanding for coherence/gaps. Wait yes/no.
- Review declined: stop gap-raising; ask explicit confirm before enacting.
- Review accepted: one issue per turn only if the lock may cause undesired future impact. Same open-question presentation. Do not restate the locked understanding. Amend lock from feedback. Continue until issues exhausted or user stops.
- Reprint lock list at final confirm. Enact only after user confirms shared understanding (post-review confirm, or review declined plus explicit confirm).

## Open-question format (locked)

- Recommended: proposal → reasons-selected bullets → `option — why not selected` record → wait.
- Why selected: recommendation + explicit why on the decision turn; alternatives retained as same-turn record (not a second question); override uses recorded options; same shape for grill and post-lock gaps; reason bullets carry trade-offs so alternatives stay one line; pre-grill stays confirm batch (full format only on promote-on-reject).
- Alternatives record:
  - Equal-weight menu with per-option trade-offs/examples — rejected: competes with recommendation; crowds one-question turn.
  - Recommendation + reasons only; drop alternatives — rejected: record lost; override needs re-generation.
  - Recommendation now; alternatives only after reject — rejected: record absent from decision turn; options can drift.
  - Two turns (discuss then log alternatives) — rejected: one decision spans two turns; confirm possible before record exists.
  - Full open-question format on every pre-grill item — rejected: collapses pre-grill gate; promote-on-reject covers contest.
  - Prose discussion + bare alternative names — rejected: reasons must be listed; names without why-not are not a selection record.
