# Assumption Registry

A consciousness-measurement claim is only as strong as the assumptions connecting evidence to its experiential target. This registry provides a standard vocabulary for assumptions that must be declared, stress-tested, and linked to every M5-M7 claim and to lower-level claims when relevant.

## A1. Target validity

**Statement:** the declared target corresponds to the scientific construct the study intends to measure.

Threats:

- defining the target by the same biomarker being evaluated;
- switching from presence to responsiveness after observing results;
- treating arousal as equivalent to consciousness.

Required checks:

- independent target definition;
- target-to-observable mapping written before confirmatory analysis;
- explicit neighboring constructs.

## A2. Report validity

**Statement:** when report is used as an anchor, it is sufficiently related to the participant's experience for the stated purpose.

Threats:

- memory decay;
- criterion shifts;
- language limitations;
- demand characteristics;
- deception;
- motor impairment;
- metacognitive noise.

Required checks:

- timing of report;
- confidence or reliability measures where appropriate;
- report-free control analyses;
- task comprehension and motor controls.

## A3. Behavioral capacity

**Statement:** failure of intentional behavior is interpretable because the participant can perceive, understand, remember, and execute the required response.

Threats:

- paralysis;
- aphasia;
- apraxia;
- hearing or vision impairment;
- fatigue;
- fluctuating attention.

Required checks:

- sensory and motor screening;
- alternative response modes;
- repeat testing where fluctuation is plausible.

## A4. Channel sensitivity

**Statement:** a measurement channel has adequate sensitivity to the declared target in the current validation domain.

Threats:

- task-specific false negatives;
- hardware failure;
- preprocessing dependence;
- pathology outside the training domain.

Required checks:

- positive controls;
- false-negative estimates;
- acquisition quality metrics;
- domain-match statement.

## A5. Channel specificity

**Statement:** the signal is not fully explained by neighboring processes such as arousal, attention, memory, motor preparation, sensory strength, or generic task engagement.

Required checks:

- matched confound manipulations;
- negative controls;
- multivariable or causal analyses;
- report/no-report comparison where relevant.

## A6. Channel dependence model

**Statement:** the dependence among evidence channels is represented adequately for fusion.

Threats:

- multiplying correlated likelihood ratios as if channels were independent;
- common dependence on arousal, medication, site, or injury severity.

Required checks:

- explicit dependence model;
- sensitivity analysis to stronger dependence;
- comparison with single-channel baselines.

## A7. Missingness model

**Statement:** missing or uninterpretable evidence does not bias the inference in an unmodeled way.

Threats:

- recordings fail more often in severely impaired participants;
- movement artifact selectively removes responsive trials;
- report is missing when memory is poor.

Required checks:

- failure-to-acquire rate;
- failure-to-interpret rate;
- missingness mechanism analysis;
- sensitivity to missing-not-at-random scenarios.

## A8. Temporal alignment

**Statement:** evidence channels refer to the same target time window or to a justified causal sequence.

Threats:

- delayed report about a rapidly changing state;
- averaging across transitions;
- neural and physiological windows that do not overlap.

Required checks:

- synchronized clocks and event markers;
- declared windows;
- temporal sensitivity analyses.

## A9. Intervention validity

**Statement:** the causal intervention changes the intended mechanism without an uncontrolled alternative pathway accounting for the outcome.

Threats:

- nonspecific arousal;
- pain or sensory confounds;
- downstream motor effects;
- broad pharmacological action.

Required checks:

- manipulation check;
- sham or control intervention where appropriate;
- mediator and side-effect measurements;
- temporal prediction.

## A10. Measurement invariance

**Statement:** the meaning of the measurement is comparable across populations or states where comparison is claimed.

Threats:

- different EEG spectra under different drugs;
- age-related physiology;
- site hardware differences;
- pathology-specific signal generation.

Required checks:

- invariance tests;
- subgroup calibration;
- hardware harmonization;
- held-out-state evaluation.

## A11. Structural comparability

**Statement:** phenomenal and physical-neural relational structures are constructed at compatible granularity and with a defensible correspondence rule.

Threats:

- arbitrary distance metrics;
- circular feature selection;
- alignment driven by stimulus similarity rather than experience;
- overfitting the mapping.

Required checks:

- preregistered metrics;
- held-out pairs and participants;
- stimulus-only controls;
- alternative metric robustness.

## A12. Theory operationalization

**Statement:** a tested empirical prediction accurately represents the theory proposition being evaluated.

Threats:

- vague theory statements;
- post hoc reinterpretation;
- one laboratory's implementation standing in for the full theory.

Required checks:

- proposition written in advance;
- theory proponents or authoritative sources involved where feasible;
- auxiliary assumptions listed;
- failure localized to the tested proposition.

## A13. Reference-standard adequacy

**Statement:** the benchmark used to validate a measure is itself sufficiently reliable for the claimed purpose.

Threats:

- treating behavior as a perfect gold standard in motor impairment;
- treating one brain measure as ground truth for another;
- circular labels derived from the candidate model.

Required checks:

- imperfect-reference analysis;
- multimodal triangulation;
- uncertainty in the reference target carried forward.

## A14. Prior robustness

**Statement:** posterior conclusions are not artifacts of an arbitrary prior in settings where the likelihood is weak.

Required checks:

- prespecified priors;
- sensitivity across plausible priors;
- reporting of likelihood evidence separately where useful.

## A15. Dataset independence

**Statement:** confirmatory data are genuinely independent of model and feature development.

Threats:

- participant overlap;
- repeated tuning on the same test site;
- preprocessing choices informed by test outcomes.

Required checks:

- immutable split definitions;
- participant and site identifiers audited for overlap;
- frozen code or versioned container before confirmatory access.

## Recording assumptions

Every machine-readable claim record should list the relevant assumption IDs, for example:

```json
{
  "assumptions": ["A1", "A4", "A5", "A10", "A15"]
}
```

An assumption is not considered "true" because it is listed. The registry exists so that conclusions can be recomputed or downgraded when an assumption is challenged.
