# Failure Modes

This document is a pre-mortem for consciousness measurement. It lists ways a method can look scientifically impressive while failing to support the intended experiential claim.

## F1. Target substitution

The study begins with one target and ends by interpreting the result as another.

Example: a marker predicts responsiveness and is later described as a measure of phenomenal presence.

Prevention: declare the target before analysis and bind every claim to the M0-M7 ladder.

## F2. Circular validation

The candidate measure helps define the reference label used to validate itself.

Prevention: use independent target anchors and document label provenance.

## F3. Report contamination

A neural signature attributed to experience is driven by decision, memory, speech, button press, or report preparation.

Prevention: matched no-report or delayed-report controls and temporal decomposition.

## F4. Unconscious-processing mimic

A candidate marker is produced by sensory, semantic, or task processing that can occur without reportable experience.

Prevention: negative controls designed to reproduce processing without the declared experiential target.

## F5. Arousal confounding

A measure tracks wakefulness, vigilance, autonomic activation, or medication effects rather than the experiential target.

Prevention: manipulate and model arousal separately.

## F6. False negative from inability to respond

A person fails a behavioral or active neural task because of motor, language, memory, sensory, or attention limitations.

Prevention: alternative response channels, passive paradigms, quality control, repeat testing, and an inconclusive state.

## F7. False positive from nonspecific physiology

A pupil, skin, cardiac, respiratory, or neural response is treated as consciousness-specific even though it can arise from nonconscious processing.

Prevention: specificity controls and multimodal triangulation.

## F8. Hidden channel dependence

Multiple correlated channels are multiplied as if they were independent, producing extreme but unjustified posterior confidence.

Prevention: explicit dependence models and sensitivity bounds.

## F9. Dataset leakage

Information from the test participant, test site, or outcome leaks into preprocessing, feature selection, or model tuning.

Prevention: participant-grouped splits, held-out sites, frozen pipelines, and provenance logs.

## F10. Site shortcut

The model learns scanner, amplifier, acquisition, or clinical-site features associated with labels.

Prevention: held-out-site validation, harmonization checks, and site-prediction diagnostics.

## F11. State-specific shortcut

A model distinguishes one anesthetic drug from wakefulness and is misinterpreted as a general consciousness measure.

Prevention: multiple mechanistically distinct state manipulations and cross-state transport testing.

## F12. Threshold reification

An empirical cutoff from one implementation is treated as a universal natural boundary.

Prevention: report the population, algorithm, preprocessing, hardware, and validation context of every threshold.

## F13. Scalar collapse

Meaningful dissociations among report, behavior, neural, perturbational, and physiological channels are averaged into one score.

Prevention: preserve the CEP vector and discordance before allowing a scalar summary.

## F14. Missingness as absence

A missing or uninterpretable channel silently becomes zero evidence.

Prevention: model missingness, report acquisition failure, and preserve `inconclusive`.

## F15. Overfitted phenomenal geometry

The mapping between neural and phenomenal structures is optimized on the same pairs used to claim correspondence.

Prevention: held-out experience pairs, held-out participants, null mappings, and preregistered metrics.

## F16. Stimulus-structure confound

Neural and phenomenal geometries align because both reflect stimulus similarity rather than experience.

Prevention: compare stimulus-only geometry, ambiguous-percept conditions, and within-stimulus experiential changes.

## F17. Theory immunization

A failed prediction is reinterpreted after the fact so that the theory cannot lose.

Prevention: preregister proposition-level predictions, pass/fail regions, and auxiliary assumptions.

## F18. Theory overkill

Failure of one operationalization is described as falsification of an entire broad theory family.

Prevention: state exactly which proposition and assumptions failed.

## F19. Ontological promotion

A reliable predictive relation is described as proof that a physical quantity is identical to experience.

Prevention: keep prediction, causation, structural correspondence, and ontological identity separate.

## F20. Cross-substrate copying

A human neural threshold is applied to infants, animals, organoids, or AI without a validated invariance argument.

Prevention: domain-specific validation and explicit substrate assumptions.

## F21. Ethical asymmetry hidden by accuracy

A classifier with acceptable average accuracy has an unacceptable false-negative cost in a vulnerable population.

Prevention: report error types separately and define the scientific-evidence threshold separately from the ethical-precaution threshold.

## F22. Irreproducible flexibility

Many preprocessing pipelines, electrodes, regions, windows, metrics, or seeds are tried but only the favorable result is reported.

Prevention: discovery-confirmation separation, full analysis inventory, and frozen confirmatory code.

## Required use

Every preregistered study should identify the failure modes most relevant to its design. Every result that reaches M3 or higher should report which failure modes were tested directly and which remain unresolved.
