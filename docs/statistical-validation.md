# Statistical Validation Plan

## 1. Separate discovery from confirmation

Exploratory feature engineering occurs only in discovery data. Confirmatory evaluation uses frozen pipelines and held-out participants/sites.

## 2. Hierarchical structure

Repeated measures are nested within participant and site. Models must respect this dependence rather than treating every trial as independent.

## 3. Calibration over accuracy

For probabilistic outputs, evaluate:

- reliability/calibration curves;
- Brier score;
- log score;
- calibration intercept/slope;
- decision-curve analysis only for defined clinical decisions.

## 4. Identification and sensitivity analysis

When latent-state inference depends on assumptions, report how conclusions change under:

- different priors;
- channel dependence;
- misclassification rates;
- missing-not-at-random reports;
- site effects;
- assay sensitivity bounds.

## 5. Multimodal fusion

A multimodal model must beat strong single-channel baselines prospectively and must demonstrate that improvement is not due to data leakage.

## 6. Negative tests

The model must explicitly search for:

- false positives during validated unconscious conditions;
- false negatives during clearly reportable experience;
- signatures reproduced by attention or motor preparation alone;
- site/scanner-specific shortcuts.

## 7. Multiple comparisons

High-dimensional neural analyses require preregistered families, multiplicity control, or hierarchical inference. Selective reporting of favorable electrodes, regions, time windows, or metrics is not acceptable.

## 8. Sample-size planning

Sample size is determined per primary endpoint using:

- target effect size or minimum clinically/scientifically important effect;
- repeated-measures correlation;
- site heterogeneity;
- desired confidence interval width;
- expected missingness/uninterpretable recordings;
- external validation sample requirements.

## 9. Abstention

A scientifically responsible classifier needs an abstain/inconclusive state. Forced binary prediction is inappropriate when data quality or model support is insufficient.
