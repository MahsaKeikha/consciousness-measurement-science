# Formal validation results

This directory contains the deterministic analytic and synthetic validation outputs for Research III V1-V10.

These files are **not human empirical data** and must not be described as evidence that consciousness has been measured. They test whether the proposed inferential machinery behaves correctly under known mathematical and synthetic data-generating conditions.

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

## Reader-facing interpretation

Use [Research III Formal Validation V1-V10](../VALIDATION.md) for the compact program map and [Validation Atlas](../docs/validation-atlas.md) for the complete visual sequence with equations, failure conditions, code links, tests, and figure-to-result provenance.

## Verification rule

Downstream prose should cite or compute from the CSV/JSON values rather than retyping rounded numbers from figure labels. The SVG figures are generated summaries of these deterministic records, not independent sources of truth.
