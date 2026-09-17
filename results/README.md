# Formal validation results

This directory contains deterministic analytic and synthetic validation outputs for Research III.

These files are **not human empirical data** and must not be described as evidence that consciousness has been measured. They test whether the proposed inferential machinery behaves correctly under known data-generating conditions.

## Generated outputs

- `finite_sample_coverage.csv`: empirical coverage and interval width versus sample size.
- `dependence_stress.csv`: exact posterior versus naive conditional-independence fusion as dependence increases.
- `transport_stress.csv`: exact bias when sensitivity or specificity changes across conditions.
- `structural_alignment_power.csv`: null rejection and synthetic power for the relational-geometry permutation statistic.
- `validation_summary.json`: compact machine-readable summary of the canonical run.

## Reproduce

```bash
python scripts/run_validation_program.py
```

Canonical seed: `20260917`.
