---
name: v3-review
description: >
  Architectural review of git-tracked master/submodule changes vs v3.
  Fire on /v3-review, implement-review gates, or "review branch changes".
disable-model-invocation: true
---
Review git-tracked diffs for business fit, integrity, security. Enforce `.cursorrules`.

## Scope

- Base: `v3`.
- Compare:
  - `v3` -> main only; exclude submodules
  - `branch:<name>` -> main `<name>` vs `v3`
  - `sub:<name>` -> that submodule only
  - `sub:<name> branch:<branch>` -> submodule `<branch>` vs `v3`
- Default: staged + unstaged current branch + submodules.
- Never `git fetch` / `git checkout`. Absolute submodule paths. Prefer `v3` target when present.
- PHP/Laravel -> `laravel-review`. TS/Vue -> `vuejs-review`.

## Evidence

- Finding needs call path / call site / query / reachable scenario.
- Speculative risk -> omit.
- Inconsistency -> cite both paths.
- Edge -> prove reachability.
- Perf -> cite concrete query/op.
- Existing test/static/tool coverage of same rule -> coverage note, not defect.

## Dimensions

Standards; naming; security (mass assign, XSS, SQLi, auth/policy, leak); arch/logic (SOLID/SRP, race/null, waste); smell baseline (Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest). Repo docs override.

Feature-test low-signal (diff touches `tests/Feature` / Pest `it()`): enforce `docs/ADR/feature-testing.md` Low-signal ban + `AGENTS.md` Tests; flag Medium (drop or fold) — omit-keeps after ignore-body/identity freeze; second verb/entry same helper/gate; missing-id 404 when peer/other-org already smokes scoped load; privilege map cloned across CRUD; cross-file topic dup; subset happy of fuller sibling; null/empty or model field-echo; default sort/pagination.

## Inline docs

- Read PHPDoc/JSDoc/comments first.
- Doc justifies issue + call-site semantics unchanged -> skip.
- Doc justifies omission (e.g. "no port") but new/changed caller **persists, returns to client, or replaces stored value** with rebuilt/transformed output -> **do not skip**; reopen as finding.

## Transform / rebuild gates

Fire when diff touches decompose->recompose (e.g. `parse_url` + string rebuild), encode/normalise helpers, or extract of same.

### Parse->rebuild inventory

- Checklist keys: `scheme`, `user`, `pass`, `host`, `port`, `path`, `query`, `fragment`.
- Dropped key + product does not explicitly strip **or** any persist/return caller needs it -> Medium+.
- Rebuild helper used for storage/API return missing non-default-port (and prefer userinfo) unit case -> Medium.

### Validate-only -> persist amplification

- Extract/reuse transformer: compare old vs new call sites.
- Old = validate-only (encode then discard / only `FILTER_VALIDATE_*`); new = persist / API return / replace stored value -> re-audit data-loss edges that were harmless under validate-only.
- Latent drop that now corrupts stored value -> Medium+ (not "legacy intentional").

## Impact gating

- Report **Critical | High | Medium**. Omit Low entirely.
- Unverified/speculative -> never Critical/High.
- Chat gate language: "no findings ≥ Medium" / "N Medium+" — **never** summarize as "no Critical/High" alone when Medium exists or was not audited.
- ≥1 finding after gate -> write review file. Zero ≥ Medium -> write nothing; state that in chat.

## Output

- Path: `./ai-agent/reviews/review-<YYYYMMDD>-<HHmmss>-<snake_cased_title>.md`
- Links: `../` prefix.
- Finding shape: `### [Index]. **([Impact]) Title`** / `**Location**: [fileName#L<LineNumberRange>](../../filePath#L<starting-line-num>)` / `**Issue**` / `**Recommendation**` / `**Impact**: Critical|High|Medium`
- `starting-line-num` = first line of issue range.
- End after last finding. No summary. Collapse repeated patterns.
- No refactor without approval. Skip existing `review-*.md`. Prefer minimal diffs.

## Post-file

After writing review file (skip if none): related feature/unit tests for modified classes + static analysis. Failures confirm findings / expose false positives.

## Prompt `fix`

Apply recommended fixes. One commit per fix; next only after prior succeeds. Subject `([Impact]) Title`. Body = Location / Issue / Recommendation as implemented.

## Delegate (do not duplicate specialty)

- Logic bugs / missing error handling / typos / unhandled edges; encode/normalise **persist** paths -> `/review-bugbot` (pre-push).
- Auth/login, DB queries, new third-party deps, secrets, injection, broken authz -> `/review-security` (optional threat-model).
- Architecture / business fit / conventions / smells / multi-repo submodule -> stay here.
