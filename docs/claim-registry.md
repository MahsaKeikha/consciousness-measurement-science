# Claim Registry

This registry is the repository's guard against overclaiming. Every empirical conclusion should be recorded with a target, evidence level, assumptions, validation domain, falsification condition, and explicit nonclaims.

The prose registry is paired with a machine-readable schema in [../schemas/claim.schema.json](../schemas/claim.schema.json) and a worked example in [../examples/claim_example.json](../examples/claim_example.json).

## Claim ladder

| ID | Candidate claim | Target | Minimum ladder level | Required evidence | Explicitly not implied |
|---|---|---|---|---|---|
| C1 | a feature predicts reportable content | content | M1 | held-out prediction and calibration | direct access to qualia |
| C2 | a feature generalizes across participants or sites | declared target | M2 | locked external validation | causal mechanism or necessity |
| C3 | a marker transports across wake, sleep, anesthesia, or injury | state or presence-related target | M3 | multiple manipulations and controls | universal consciousness scalar |
| C4 | perturbing a candidate mechanism changes the target as predicted | declared mechanism-target relation | M4 | causal manipulation and controls | complete explanation of experience |
| C5 | a multimodal model identifies or bounds a latent target | presence or state | M5 | latent model, explicit assumptions, sensitivity analysis | ontology of consciousness |
| C6 | physical geometry predicts phenomenal geometry | structure | M6 | reliable reports, held-out structural prediction, confound controls | physical geometry is phenomenology |
| C7 | one theory's unique prediction survives an adversarial test | theory comparison | M7 | preregistered divergence and confirmatory data | final theory of consciousness |

## Required fields

Every claim record must contain:

- `claim_id`: stable local identifier;
- `target`: one of presence, global_state, content, structure, capacity, or a clearly justified theory-comparison target;
- `statement`: the exact claim being made;
- `claim_level`: M0 through M7;
- `population`: who or what was studied;
- `contexts`: states, tasks, and acquisition domains;
- `evidence`: datasets and analyses supporting the claim;
- `assumptions`: relevant IDs from the [Assumption Registry](assumption-registry.md);
- `identifiability`: point, interval, partial, or not_identified;
- `external_validation`: whether independent external validation exists;
- `falsification_condition`: what observation would count against the claim;
- `nonclaims`: tempting stronger conclusions that are not licensed;
- `status`: proposed, preregistered, supported, failed, or inconclusive.

## Machine-readable example

```json
{
  "claim_id": "C6-demo-001",
  "target": "structure",
  "statement": "A preregistered neural distance matrix predicts held-out phenomenal similarity structure in the declared benchmark.",
  "claim_level": "M6",
  "population": "healthy adult research participants",
  "contexts": ["visual similarity benchmark"],
  "evidence": {
    "datasets": ["demo-benchmark-v1"],
    "analyses": ["held-out structural alignment"]
  },
  "assumptions": ["A1", "A2", "A10", "A11", "A15"],
  "identifiability": "partial",
  "external_validation": false,
  "falsification_condition": "Held-out structural alignment is indistinguishable from the preregistered null or distortion exceeds the preregistered bound.",
  "nonclaims": [
    "Neural geometry is identical to phenomenology.",
    "The mapping is universal across states or populations."
  ],
  "status": "proposed"
}
```

## Interpretation rules

### A supported lower-level claim cannot be silently promoted

An M1 prediction result is still M1 even if its p-value is extremely small. Claim level is determined by design and validation, not by statistical significance alone.

### A failed claim remains in the registry

Failure is part of the scientific record. The record should be updated to `failed` or `inconclusive` with the relevant evidence rather than deleted.

### A theory failure must be localized

If an M7 prediction fails, record which proposition and auxiliary assumptions were tested. Do not automatically promote a proposition-level failure to a statement that the entire theory family is false.

### Inconclusive is not failed

Insufficient data quality, low assay sensitivity, or a violated assumption can make the claim inconclusive without supporting the opposite claim.

## File organization

Future machine-readable claim records should live under `claims/` with one JSON file per stable claim record. The directory policy is documented in [../claims/README.md](../claims/README.md).
