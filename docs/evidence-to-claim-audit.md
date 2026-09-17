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

## Figure-to-claim traceability

The nine canonical Research III figures are not decorative summaries. Each figure has a specific audit role. The table below states the mathematical or inferential object represented by each visual, the assumptions that must remain visible, the admissible inference, a concrete failure condition, the relevant validation obligation, and the strongest claim family the figure can organize. A figure does not itself supply the empirical evidence needed to reach that ceiling.

| Canonical visual | Mathematical or inferential object | Assumptions that must remain explicit | Admissible inference | Failure condition | Validation obligation | Claim ceiling organized by the visual |
|---|---|---|---|---|---|---|
| [Research program map](figures/research_program_map.svg) | target-conditioned inference chain from observables through assumptions, identification, validation, and claim control | target definition; channel interpretation; transport scope; causal interpretation | specifies which inferential steps must be exposed before a claim is licensed | any target, bridge assumption, or validation step is left implicit | every empirical claim must name its target and validated domain | M0-M7 architecture only; no empirical rung is earned by the map |
| [Target-evidence matrix](figures/target_evidence_matrix.svg) | relation between declared target classes and heterogeneous evidence channels | no channel is assumed universally sufficient; negative evidence requires assay sensitivity | identifies which channels can contribute evidence for a declared target | a channel validated for one target is promoted to another without evidence | target-specific sensitivity, specificity, reliability, and transport checks | normally M0-M4 evidence organization; M5 requires an explicit identification model |
| [Measurement architecture](figures/measurement_architecture.svg) | observable data vector `D=(R,B,N,P,A,I,C)` linked to an unobserved experiential target `E` under assumptions `A` | observability distinction; measurement model; dependence structure; calibration; context | asks what about `E` is identifiable, bounded, predicted, or falsified from `D` under `A` | multiple latent explanations remain compatible but a unique estimate is reported | out-of-sample calibration, confound controls, invariance, transport, and uncertainty assessment | up to M5 when identification obligations are actually satisfied |
| [CEP anatomy](figures/cep_anatomy.svg) | structured record `CEP(s,t,tau,c)=(v,q,u,A,D,Gamma)` | evidence quality and uncertainty cannot be discarded when evidence is aggregated | records evidence, quality, uncertainty, assumptions, validation domain, and allowed claim together | a scalar score hides discordance, missingness, uncertainty, or unsupported assumptions | schema validation plus empirical calibration of every component used inferentially | records the current ceiling `Gamma`; does not independently raise it |
| [Identification and uncertainty pipeline](figures/identification_uncertainty_pipeline.svg) | identified set or region for a target under declared assumptions | model class, dependence restrictions, sensitivity assumptions, missing-data assumptions | distinguishes point identification, partial identification, and abstention | an identification region is collapsed to a point without justification | coverage, sensitivity analysis, dependence robustness, and calibration of uncertainty | M5 only when a declared experiential target is genuinely identified or bounded |
| [Structural measurement pipeline](figures/structural_measurement_pipeline.svg) | held-out comparison between phenomenal relational geometry `(E,d_E)` and physical-neural geometry `(N,d_N)` through a preregistered mapping family `f:N->E` | reliable phenomenal relations; independently constructed geometries; frozen mapping family; held-out relations; declared nulls | supports or rejects a specified structural correspondence model | mapping flexibility, leakage, unreliable phenomenal geometry, or absence of a held-out test can reproduce apparent alignment | preregistered distortion statistic, held-out prediction, permutation/null comparison, reliability and replication | M6 when preregistered physical structure predicts held-out phenomenal structure |
| [Validation program map](figures/validation_program_map.svg) | staged transport and stress-test sequence across participants, sites, states, hardware, interventions, and confounds | validation domains are finite and must not be silently universalized | determines where an empirical relation has survived increasingly demanding tests | performance collapses under a prespecified transport, perturbation, or confound test | participant/site holdout, altered-state transport, causal perturbation, clinical stress tests, and replication as applicable | organizes progression from M1 through M6 depending on the tested object |
| [Theory falsification map](figures/theory_falsification_map.svg) | comparison of preregistered divergent predictions from competing theory commitments | rivals must make genuinely discriminating predictions; analysis choices are frozen before outcome inspection | supports rejection or comparative survival of declared predictions | predictions are non-discriminating, post hoc, or flexible enough to accommodate every outcome | adversarial preregistration, adequate power, manipulation checks, and independent replication | M7 only for a unique preregistered prediction surviving while relevant rivals fail |
| [Measurement claim ladder](figures/claim_ladder.svg) | ordered evidential obligations M0-M7 | higher language requires the additional obligations associated with that rung | constrains wording to the strongest claim justified by the complete record | a result is described with language belonging to a stronger rung | claim record must link evidence, assumptions, identification, validation, and nonclaims | M0-M7 taxonomy; the ladder itself establishes none of the rungs |

### Reading rule

For any figure, ask six questions before treating it as scientific support:

1. What mathematical or inferential object does the figure encode?
2. Which assumptions are required for the arrows or mappings to have inferential meaning?
3. What statement is actually licensed if the represented test succeeds?
4. What observation or diagnostic would make that inference fail or become inconclusive?
5. In which population, state, task, hardware, intervention, or context has the relation been validated?
6. What is the strongest M-level wording allowed after all five previous questions are answered?

If one of these questions has no explicit answer, the visual should be treated as a specification or hypothesis diagram rather than as evidence for the corresponding scientific claim.

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
