# Formal validation results

This directory contains the deterministic analytic and fixed-seed synthetic validation outputs for Research III V1-V15.

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

## Reader-facing interpretation

Use [Research III Formal Validation V1-V15](../VALIDATION.md) for the compact program map, [Validation Atlas](../docs/validation-atlas.md) for the complete visual sequence, and [Formal Validation V11-V15](../docs/formal-validation-program-v11-v15.md) for the new identification and design proofs.

## Verification rule

Downstream prose should cite or compute from the CSV and JSON values rather than retyping rounded numbers from figure labels. The SVG figures are generated summaries of these records, not independent sources of truth.
