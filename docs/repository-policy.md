# Repository Policy

This repository uses the same publication discipline across research text, code, tests, schemas, figures, examples, and automation.

## Reader-facing contract

The root README is the canonical public entry point. Every major research object must be discoverable from it, and relative links must resolve to tracked files.

Reader-facing claims must remain synchronized with the underlying formal specification, software, schemas, examples, and tests.

The documentation map in `docs/README.md` provides the canonical reading order.

## Scientific claim discipline

Every scientific claim must identify:

- measurement target;
- population and context;
- evidence level M0-M7;
- assumptions;
- validation domain;
- identifiability status;
- external-validation status;
- falsification condition;
- explicit nonclaims.

The repository must not silently promote a correlation into a causal, ontological, clinical, or direct-qualia claim.

The M0-M7 ladder, Consciousness Evidence Profile, Assumption Registry, Failure Modes, preregistration contract, and Claim Registry define the allowed language for future results.

## Specification versus validation

Documents must distinguish:

- a method being specified;
- a method being implemented;
- a method being tested on retrospective data;
- a method being prospectively validated;
- a method being externally validated;
- a method being clinically validated.

Completing documentation does not count as empirical validation.

## Negative-evidence policy

A negative or missing channel can support absence only when the relevant sensitivity, interpretability, and validation-domain conditions are satisfied.

Otherwise the channel is missing, uninterpretable, or inconclusive.

No code path, schema, or reader-facing document may silently convert uninterpretable data into negative evidence for absence.

## Text style contract

Tracked text must not contain Unicode en dash or em dash characters. Use ordinary punctuation or the ASCII hyphen-minus character.

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
- JSON examples validate against their declared schemas where a schema is provided;
- SVG figures parse as XML;
- relative Markdown links resolve;
- no prohibited Unicode dash appears in tracked text.

Empirical releases have additional requirements in `docs/reproducibility.md`.

## Machine-readable object contract

The repository currently defines:

- `schemas/cep.schema.json` for Consciousness Evidence Profiles;
- `schemas/claim.schema.json` for claim records;
- examples under `examples/`;
- future stable claim records under `claims/`.

Schema changes that alter scientific meaning require synchronized updates to:

- examples;
- documentation;
- tests;
- software structures where applicable.

## Failure policy

A failed or uninterpretable scientific result remains visible. It must not be rewritten as support by changing the target after results are known.

A data-quality failure is reported as uninterpretable, not as evidence of absent consciousness.

A theory-specific failure records which prediction or auxiliary assumption failed. It is not automatically promoted to a statement that an entire theory is false.

## Data policy

Participant data are not committed to the public repository unless explicit consent, governance, licensing, and privacy conditions permit it.

Public datasets should be retrieved from authoritative sources with version and checksum tracking where practical.

Controlled data remain in approved storage. The public repository should contain data-access statements, synthetic examples, and reproducible code rather than unauthorized copies.

## Change policy

When a change modifies any of the following, related reader-facing documentation and tests must be updated in the same change:

- measurement target;
- claim ladder;
- CEP schema;
- claim schema;
- assumption registry;
- validation rule;
- negative-evidence rule;
- experimental interpretation;
- clinical boundary;
- theory falsification rule.

## Release principle

A release tag represents the state of the repository, not a declaration that all proposed scientific milestones have been achieved. Release notes should distinguish implemented infrastructure from empirically supported results.
