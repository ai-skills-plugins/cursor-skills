---
name: laravel-review
description: conventions for reviewing Laravel or PHP
---

# Laravel

- Functions returning `void` do not need `@return void` in their PHPDoc.
- When using the `==` operator for comparison, place constants on the left side before the variable, e.g. `'valid' == $submissionStatus`.
- For testing, allow Direct Model Creation instead of always requiring a Factory in test files.
- Do not flag missing UUID validation for fields that are listed in the `$uuids` array property of request classes extending `AppRequest`. The `$uuids` property automatically validates UUID format in `prepareForValidation()` method, so explicit UUID validation is not needed for these fields.
- (High) Do not require imports for classes that are within the same namespace. Only flag missing imports when the class is in a different namespace.
- Do not require a TABLE constant for a model's own table name unless the table name is used elsewhere (e.g. by other models in relationships). A string literal for `$table` in a single model is acceptable.
- When performing multiple Eloquent operations in a loop, if only one entry can be invalid: throw a specific exception for that entry and catch it inside the loop so that the remaining operations can continue (e.g. log or collect the failure and proceed with the next iteration).
- It is acceptable for columns intended for limited values (like enums) to use plain int/string types without explicit database constraints.
- For services without constructor arguments, prefer resolving/instantiating them via the Laravel Service Container (e.g. `app(MyService::class)`) rather than calling `new MyService()` directly
