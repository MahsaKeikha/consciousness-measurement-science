# Repository Policy

This repository uses the same publication discipline across research text, code, tests, schemas, figures, and automation.

## Reader-facing contract

The README is the canonical entry point. Every major research object must be discoverable from it, and links must resolve to tracked files. Reader-facing claims must remain synchronized with the underlying formal specification, code, and tests.

## Scientific claim discipline

Every scientific claim must identify its target and evidential scope. The repository must not silently promote a correlation into a causal, ontological, clinical, or direct-qualia claim.

The M0-M7 claim ladder, the Consciousness Evidence Profile specification, the preregistration contract, and the claim registry define the allowed language for future results.

## Text style contract

Tracked text must not contain Unicode en dash or em dash characters. Use ordinary punctuation or the ASCII hyphen-minus character instead.

This rule applies to:

- Markdown documentation;
- Python source and tests;
- YAML workflows;
- JSON schemas and examples;
- TOML and CFF metadata;
- SVG text;
- plain-text policy and license files.

## Reproducibility contract

A change is publishable only when:

- Python tests pass;
- Ruff passes in CI;
- repository policy validation passes;
- JSON files parse;
- SVG figures parse as XML;
- relative Markdown links resolve;
- no prohibited Unicode dash appears in tracked text.

## Failure policy

A failed or uninterpretable scientific result remains visible. It must not be rewritten as support by changing the target after results are known.

A data-quality failure is reported as uninterpretable, not as evidence of absent consciousness.

A theory-specific failure records which prediction or auxiliary assumption failed. It is not automatically promoted to a statement that an entire theory is false.

## Change policy

When a change modifies the measurement target, claim ladder, instrument schema, validation rule, or experimental interpretation, related reader-facing documentation and tests must be updated in the same change.
