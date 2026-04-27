---
name: api-flow-for-frontend-developer
description: Reverse engineer backend commits into frontend implementation tasks by inferring API signatures, validation rules, error handling, and integration steps. Use when the user shares a backend git commit diff, commit hash, or backend change summary and asks for a frontend technical task/spec.
---

# Commit to Task

## Purpose

Convert backend commit changes into a frontend-facing implementation guide that is practical, testable, and strictly grounded in the backend evidence.

## Trigger Conditions

Apply this skill when the user:

- Provides a backend commit diff, commit hash, or backend PR summary.
- Asks for frontend implementation tasks/spec from backend changes.
- Requests API contracts, validations, error mappings, or mock response data inferred from backend code.

## Input Requirements

Collect or confirm:

- Commit reference (`hash`, diff, or patch text).
- Backend framework context (if known).
- Any target frontend conventions (TypeScript, schema library, API client style).

If commit details are missing, ask for the commit hash or raw diff before producing the final task.

Default invocation path for backend evidence:

- Run `bash skills/api-flow-for-frontend-developer/scripts/get_sysref_v3_api_diff.sh --commit <hash>` to auto-locate the `*sysref-v3-api*` repo and return the git patch.
- For branch comparison, run `bash skills/api-flow-for-frontend-developer/scripts/get_sysref_v3_api_diff.sh --range <base>...HEAD`.
- If no commit/range is provided, the script returns `HEAD` by default.

## Output Format

Return markdown using exactly these sections:

1. `🔍 API Signature (Inferred from Commit)`
2. `🛡️ Validation & Constraints`
3. `🧪 Testing & Integration`
4. `🚀 Quick-Start Mock`

Use precise wording:

- Mark inferred details as `Inferred`.
- Mark uncertain behavior as `Assumption`.
- Do not invent fields, routes, or status codes that are unsupported by the commit.

## Workflow

### 1) Inspect backend evidence

From the commit, identify:

- Route declarations and HTTP methods.
- Controller/action handlers and middleware/auth guards.
- DTO/entity/model fields and serialization shape.
- Validation decorators/rules and custom validators.
- Exception classes, error handlers, and mapped HTTP status codes.
- Default values, fallbacks, and conditional branches that affect client behavior.

Preferred evidence source:

- Use the output from `scripts/get_sysref_v3_api_diff.sh` as the primary commit evidence.

### 2) Produce API Signature section

For each endpoint impacted:

- Endpoint and method.
- Required headers:
  - infer `Content-Type` from body parser/upload usage.
  - infer auth header requirements from middleware/guards.
- TypeScript request/response interfaces based on DTOs/entities in the diff.

Prefer exact property names and optionality from backend structures.

Apply strict exposure filtering:

- Expose only contracts the frontend must know to call/render the API:
  - request body DTOs accepted by public endpoints
  - response DTOs/shapes returned to clients
  - externally visible query/path params used by routes
- Do not expose backend-internal structures unless they leak to API contract:
  - ORM entities used only for persistence
  - internal service-layer DTOs/mappers
  - private/internal-only fields not serialized in response
  - audit/system metadata not required by frontend behavior

If a DTO contains both public and internal fields, include only the public subset and add a short note: `Internal fields omitted`.

### 3) Produce Validation & Constraints section

List frontend-validatable rules from backend code:

- required/optional
- min/max length
- regex/pattern constraints
- enum/value restrictions
- format constraints (email, uuid, date, etc.)

Map exception pathways to frontend handling:

- Exception name -> expected HTTP code -> user-facing handling hint.

### 4) Produce Testing & Integration section

Include:

- Concrete implementation steps for frontend integration.
- Verification checklist for browser Network tab:
  - Request payload shape
  - Headers
  - Response preview/body structure
  - Error response handling
- Edge cases and gotchas derived from conditional logic/defaulting.

### 5) Produce Quick-Start Mock section

Generate:

- `const mockData` aligned to the inferred response interface.
- Only include fields present in backend return shape.
- Use realistic placeholder values that match backend types.

## Quality Bar

Before finalizing, verify:

- Every claim traces to commit evidence.
- Uncertain items are clearly labeled.
- Interfaces are syntactically valid TypeScript.
- Only frontend-relevant interfaces are shown; internal-only DTOs are omitted.
- Validation rules are actionable on the frontend.
- Error mappings are explicit enough for UI branching.

## Response Template

Use this template for final output:

````markdown
## 🔍 API Signature (Inferred from Commit)

### Endpoint

- `METHOD /path`

### Headers

- `Content-Type: ...`
- `Authorization: Bearer <token>` (Inferred)

### TypeScript Interfaces

```ts
interface RequestBody {
  // ...
}

interface ApiResponse {
  // ...
}
```

### Exposure Notes

- Only frontend-relevant contracts are listed.
- Internal DTOs/entities are intentionally omitted.
````

## 🛡️ Validation & Constraints

### Frontend Validation

- `fieldName`: required, maxLength 255
- `email`: must be valid email format

### Error Codes

- `UserNotFoundException` -> `404` -> show "User not found" state

## 🧪 Testing & Integration

### Implementation Steps

1. Update API service call.
2. Add client-side validation schema.
3. Map error responses to UI states.

### Verification (Network Tab)

- Request Payload: matches `RequestBody`
- Request Headers: includes expected auth/content type
- Response Preview: matches `ApiResponse`

### Edge Cases

- If `id` is null, backend defaults to `...` (Assumption if not explicit)

## 🚀 Quick-Start Mock

```ts
const mockData: ApiResponse = {
  // ...
};
```

```

```
