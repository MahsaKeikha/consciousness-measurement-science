# Evidence-to-Claim Audit

This page connects the main Research III scientific objects so that a reader can audit how an observable result is allowed to become a scientific claim.

## Audit chain

A defensible claim should expose the following sequence:

1. **Declared target** - presence, global state, content, phenomenal structure, or capacity.
2. **Observable evidence** - report, behavior, neural data, perturbational response, physiology, and context.
3. **Quality and confound record** - acquisition validity, missingness, communication capacity, artifacts, and context.
4. **Assumptions** - dependence, calibration, transport, measurement invariance, sensitivity, and causal interpretation.
5. **Identification status** - point identified, partially identified, or not identified under the declared assumptions.
6. **Validation domain** - participants, sites, states, tasks, hardware, and interventions for which the claim has actually been evaluated.
7. **Falsification condition** - what observation would count against the model or theory claim.
8. **Claim ceiling** - the strongest M0-M7 statement that survives all previous steps.
9. **Explicit nonclaims** - stronger interpretations that remain unsupported.

## Compact audit matrix

| Audit object | Required question | Failure mode if omitted | Primary record |
|---|---|---|---|
| Target | What exactly is being inferred? | state, content, structure, and capacity are silently conflated | [Measurement Framework](measurement-framework.md) |
| Evidence | Which observable channels carry the inference? | one convenient biomarker is treated as the target itself | [CEP Specification](measurement-instrument-spec.md) |
| Quality | Is the channel interpretable in this case? | failed acquisition is misread as negative evidence | [Failure Modes](failure-modes.md) |
| Assumptions | What must be true for the inference to hold? | a hidden bridge is smuggled into the analysis | [Assumption Registry](assumption-registry.md) |
| Identification | Is the target uniquely determined? | a broad compatible set is reported as one estimate | [Partial Identification](partial-identification.md) |
| Validation | Where has the relation been tested? | in-domain performance is promoted to universal validity | [Statistical Validation](statistical-validation.md) |
| Falsification | What could prove the current model wrong? | a flexible theory is protected from adverse evidence | [Falsification Matrix](falsification-matrix.md) |
| Claim level | Which statement is licensed now? | correlation becomes mechanism or ontology | [Claim Registry](claim-registry.md) |
| Nonclaims | What remains unresolved? | readers infer a stronger conclusion than the data support | [Epistemic Boundaries](epistemic-boundaries.md) |

## Example claim progression

A hypothetical state marker could move through the claim ladder only by accumulating distinct evidence:

- **M0:** the marker differs between two experimental conditions;
- **M1:** a locked model predicts a validated report or behavioral target out of sample;
- **M2:** the prediction generalizes across participants or sites in a declared domain;
- **M3:** it transports across distinct manipulations of consciousness;
- **M4:** it survives confound controls and causal perturbation tests;
- **M5:** a multimodal model identifies or bounds a declared experiential target under explicit assumptions;
- **M6:** a preregistered physical structure predicts held-out phenomenal structure;
- **M7:** one theory-specific preregistered prediction survives while relevant rivals fail.

The ladder is cumulative in evidential burden, not necessarily a mandatory linear sequence for every project. A result at one level cannot be described using a stronger level's language unless the additional obligations are satisfied.

## Negative evidence audit

A negative result is interpretable as evidence against presence or content only if the relevant assay has demonstrated sensitivity in the current validation domain, acquisition quality is adequate, the subject or system could in principle express the measured response, major confounds are controlled, and the false-negative behavior is characterized. Otherwise the allowed output is inconclusive.

## Structural arm audit

For phenomenal-structure claims, the audit chain must additionally expose:

- how phenomenal relations were elicited;
- reliability of those relations;
- how the physical or neural geometry was constructed;
- how the mapping family was selected;
- which relations were reserved for held-out evaluation;
- the preregistered distortion metric;
- the null or rival mapping comparison;
- the exact statement that low or high distortion licenses.

Low distortion supports a declared correspondence model. High distortion rejects that model. Neither result alone establishes that physical structure is identical to experience.

## Clinical boundary

Clinical or noncommunicative settings increase the cost of every missing audit step. Discordance among behavior, task-based brain responses, resting-state measures, perturbational responses, and physiology should be represented as uncertainty or model conflict rather than forced into a binary answer.

Nothing in this audit framework is a clinical decision rule or a substitute for specialist evaluation.
