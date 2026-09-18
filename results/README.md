# Formal validation results

This directory contains the deterministic analytic and fixed-seed synthetic validation outputs for Research III V1-V35.

These files are **not human empirical data** and must not be described as evidence that consciousness has been measured. They test whether the proposed measurement and inference machinery behaves correctly under known mathematical and synthetic data-generating conditions.

## V1-V5 outputs

- `finite_sample_coverage.csv`: empirical coverage and interval width versus deployment sample size.
- `dependence_stress.csv`: exact posterior versus naive conditional-independence fusion as channel dependence increases.
- `transport_stress.csv`: exact bias when sensitivity or specificity changes across conditions.
- `structural_alignment_power.csv`: null rejection and synthetic power for the relational-geometry permutation statistic.
- `validation_summary.json`: compact machine-readable summary of the canonical V1-V5 run.

Reproduce with:

```bash
python scripts/run_validation_program.py
```

Canonical V1-V5 seed: `20260917`.

## V6-V10 outputs

- `calibration_sample_uncertainty.csv`: coverage and interval width when deployment rate, sensitivity, and specificity are all estimated from finite samples.
- `missingness_stress.csv`: sharp worst-case latent interval as unrestricted missing outcomes increase.
- `conditioning_stress.csv`: exact inverse-error amplification as the Youden information margin changes.
- `two_site_nonidentifiability.csv`: sharp average-prevalence identified set from pooled two-site proxy rates under heterogeneous calibration.
- `resolution_abstention_frontier.csv`: fraction of runs meeting a predeclared maximum interval-width criterion, together with empirical conditional coverage among released intervals.
- `robustness_validation_summary.json`: compact machine-readable summary of the canonical V6-V10 run.

For V10, the conditional-coverage column is a simulation diagnostic. Marginal interval coverage bounds the probability of an erroneous release, but does not by itself imply nominal conditional coverage after a data-dependent release rule.

Reproduce with:

```bash
python scripts/run_robustness_validation.py
```

Canonical V6-V10 seed: `20260918`.

## V11-V15 outputs

- `v11_missingness_information_law.csv`: exact interior latent-width law across missingness fractions and Youden information margins.
- `v12_v13_multisite_identification.csv`: sharp population-average identified intervals as site information-margin heterogeneity increases.
- `v14_resolution_sample_size.csv`: sufficient deployment sample sizes for declared latent-width targets under the Hoeffding design law.
- `v15_independent_pilot_gate.csv`: release rate and confirmatory coverage diagnostics for the independent pilot-gated design.
- `identification_design_summary.json`: compact machine-readable summary of the canonical V11-V15 record.

The V15 conditional-coverage values are fixed-seed simulation diagnostics. The theorem-level conditional-coverage result follows from independence between the pilot release event and the confirmatory interval construction, not from the simulated coverage value.

Reproduce with:

```bash
python scripts/run_identification_design_validation.py
```

Canonical V11-V15 seed: `20260919`.

## V16-V20 electromagnetic outputs

- `v17_em_scale_invariance.csv`: gain-invariance check for normalized electromagnetic organization descriptors.
- `v19_common_mode_confound.csv`: deterministic shared-contaminant stress test for sensor-level phase concentration.
- `v20_frequency_specific_structure.csv`: frequency-specific phase-organization counterexample.
- `electromagnetic_validation_summary.json`: compact V16 physical sanity check and V18 matched-power non-identifiability record.

V18 is stored in the summary because it is a constructive two-condition result: channel power is matched to numerical precision while the spatial phase organization changes from fully aligned to phase balanced.

Reproduce with:

```bash
python scripts/run_electromagnetic_validation.py
```

V16-V20 are deterministic and require no random seed. These records validate physical calculations, feature invariance, non-identifiability, and confound behavior. They do not validate an electromagnetic consciousness biomarker.

## V21-V25 electromagnetic source-identifiability outputs

- `v21_reference_invariance.csv`: common-reference sweep for pairwise EEG-like sensor differences.
- `electromagnetic_inverse_validation_summary.json`: compact V22 lead-field rank-nullity and exact source non-identifiability record.
- `v23_regularization_path.csv`: deterministic L2-regularization path showing inverse-solution dependence.
- `v24_multimodal_nullity.csv`: single-modality versus stacked-operator rank and nullity.
- `v25_forward_model_perturbation.csv`: deterministic forward-model mismatch and operator-norm bound record.

Reproduce with:

```bash
python scripts/run_electromagnetic_inverse_validation.py
```

V21-V25 are deterministic and require no random seed. They validate reference invariance, source non-identifiability, inverse-prior sensitivity, multimodal null-space reduction, and forward-model perturbation behavior. They do not establish a unique neural source or a consciousness-specific electromagnetic source pattern.

## V26-V30 electromagnetic resolution and information outputs

- `v26_correlated_noise_whitening.csv`: covariance-weighted residual energy and the equivalent whitened residual norm.
- `v27_resolution_leakage.csv`: regularization path for source-resolution trace, off-diagonal leakage, and normalized identity error.
- `v28_fisher_information.csv`: scalar-amplitude Fisher information and Cramer-Rao lower bound as common sensor-noise correlation increases.
- `v29_temporal_aliasing.csv`: exact sampled-cosine aliasing counterexample at 100 Hz sampling.
- `v30_inverse_noise_amplification.csv`: smallest singular value, pseudoinverse norm, and realized worst-direction noise amplification.
- `electromagnetic_resolution_validation_summary.json`: complete machine-readable V26-V30 record, including the V27 rank floor, V28 information curve, and V30 singular-direction amplification.

Reproduce with:

```bash
python scripts/run_electromagnetic_resolution_validation.py
```

V26-V30 are deterministic and require no random seed. They validate noise geometry, inverse resolution limits, information loss under correlated noise, temporal sampling non-identifiability, and singular-direction noise amplification. They do not establish a consciousness-specific information threshold or source-space consciousness measure.

## V31-V35 electromagnetic design and spatial-specificity outputs

- `v31_point_spread_cross_talk.csv`: point-spread and cross-talk values for the canonical asymmetric resolution matrix.
- `v32_source_distinguishability.csv`: covariance-aware squared Mahalanobis distances for close and distinct sensor topographies.
- `v33_sensor_design_information.csv`: determinant, log determinant, minimum eigenvalue, and trace of redundant and complementary Fisher-information designs.
- `v34_nuisance_information_loss.csv`: target information retained after one-dimensional nuisance projection across declared principal angles.
- `v35_robust_model_information.csv`: nominal and worst-case information under bounded whitened topography uncertainty.
- `electromagnetic_design_validation_summary.json`: complete machine-readable V31-V35 design and spatial-specificity record.

Reproduce with:

```bash
python scripts/run_electromagnetic_design_validation.py
```

V31-V35 are deterministic and require no random seed. They validate linear spatial-specificity diagnostics, covariance-aware distinguishability, information-aware sensor design, exact nuisance-subspace information loss, and an exact robust information lower bound. They do not establish a consciousness-specific spatial metric, a consciousness-optimal sensor design, or direct measurement of qualia.

## Reader-facing interpretation

Use [Research III Formal Validation V1-V35](../VALIDATION.md) for the compact program map, [Validation Atlas](../docs/validation-atlas.md) for the complete visual sequence, [Formal Validation V11-V15](../docs/formal-validation-program-v11-v15.md) for the identification and design proofs, [Electromagnetic Field Measurement Program](../docs/electromagnetic-field-program.md) for V16-V20, [Electromagnetic Source Identifiability Program](../docs/electromagnetic-source-identifiability.md) for V21-V25, [Electromagnetic Resolution and Information Program](../docs/electromagnetic-resolution-program.md) for V26-V30, and [Electromagnetic Design and Spatial Specificity Program](../docs/electromagnetic-design-spatial-specificity.md) for V31-V35.

## Verification rule

Downstream prose should cite or compute from the CSV and JSON values rather than retyping rounded numbers from figure labels. The SVG figures are generated summaries of these records, not independent sources of truth.
