# Research III Validation Atlas

## From equations to failure tests to reproducible results

This page is the visual research record for the executable mathematical layer of Research III. It complements the nine foundational architecture figures with **ten validation-result figures** generated from deterministic analytic and synthetic experiments.

Use this page in order. Each stage states the scientific question, the mathematical object, the failure condition, the executable source, and the canonical result artifact. The figures summarize computations; they do not replace the equations or the machine-readable result files.

> **Boundary:** all results on this page validate the measurement framework under declared synthetic or analytic conditions. They are not human empirical evidence that consciousness has been measured.

---

## V1. Point identification through an imperfect channel

**Question:** when does an observable binary channel identify the prevalence of a declared latent target?

\[
q=(1-\beta)+(\alpha+\beta-1)\pi.
\]

For \(J=\alpha+\beta-1>0\),

\[
\pi=\frac{q+\beta-1}{J}.
\]

**Failure condition:** at \(J=0\), the observable rate is independent of the latent prevalence. V8 later quantifies how instability grows as \(J\) approaches zero.

Audit: [V1-V5 derivation](formal-validation-program.md), [`latent_measurement.py`](../src/consciousness_measurement/latent_measurement.py), [`test_latent_measurement.py`](../tests/test_latent_measurement.py).

---

## V2. Finite-sample partial identification

**Question:** does the interval retain the target when the deployment rate is estimated from finite data and calibration is known only inside a declared box?

![Finite-sample identification width](figures/finite_sample_identification.svg)

The interval contracts with sample size but does not collapse calibration uncertainty into a false point estimate.

![Finite-sample coverage](figures/finite_sample_coverage.svg)

The fixed-seed simulation checks empirical coverage against the declared nominal guarantee.

Audit: [`finite_sample_coverage.csv`](../results/finite_sample_coverage.csv), [`validation_summary.json`](../results/validation_summary.json), [`simulation_validation.py`](../src/consciousness_measurement/simulation_validation.py).

---

## V3. Measurement transport and calibration shift

**Question:** what bias is introduced if sensitivity or specificity changes across conditions but the analyst reuses baseline calibration?

Under invariant calibration,

\[
\Delta\pi=\frac{\Delta q}{J}.
\]

When calibration changes, the bias is

\[
\operatorname{Bias}
=
\frac{(J_1-J_0)\pi_1+(\operatorname{FPR}_1-\operatorname{FPR}_0)}{J_0}.
\]

![Calibration transport stress](figures/transport_bias_surface.svg)

**Failure condition:** state, intervention, hardware, site, or population shift changes channel calibration.

Audit: [`transport_stress.csv`](../results/transport_stress.csv), [`latent_measurement.py`](../src/consciousness_measurement/latent_measurement.py).

---

## V4. Conditional-dependence stress test

**Question:** what happens when multimodal likelihood ratios are multiplied as if channels were conditionally independent but the channels share dependence?

![Dependence stress](figures/dependence_stress.svg)

The construction preserves the declared channel marginals while increasing shared dependence. The canonical all-positive example moves from the independence posterior near `0.997` toward an exact posterior of `0.84` under maximal shared dependence.

**Failure condition:** duplicated or correlated evidence is counted as independent information.

Audit: [`dependence_stress.csv`](../results/dependence_stress.csv), [`partial_identification.py`](../src/consciousness_measurement/partial_identification.py), [`simulation_validation.py`](../src/consciousness_measurement/simulation_validation.py).

---

## V5. Structural-alignment null and power behavior

**Question:** does the preregisterable relational-geometry permutation statistic control false positives under a null construction and gain power when a correspondence is planted?

![Structural alignment power](figures/structural_alignment_power.svg)

The canonical simulation reports null rejection near the declared 0.05 level and increasing rejection under stronger planted alignment.

**Failure condition:** apparent structural similarity can be reproduced under label permutation, leakage, or an overly flexible mapping.

Audit: [`structural_alignment_power.csv`](../results/structural_alignment_power.csv), [`structural_alignment.py`](../src/consciousness_measurement/structural_alignment.py).

---

# Robustness layer V6-V10

V6-V10 move beyond the idealized assumption that calibration is known, deployment outcomes are complete, inversion is well-conditioned, sites are homogeneous, and every run must emit an estimate.

---

## V6. Finite calibration-sample uncertainty

**Question:** how much uncertainty remains when sensitivity and specificity themselves come from finite reference samples?

For three simultaneous Bernoulli estimates, allocating \(\delta/3\) to each Hoeffding event gives

\[
\epsilon(n,\delta/3)=\sqrt{\frac{\log(6/\delta)}{2n}}.
\]

![Finite calibration sample uncertainty](figures/calibration_sample_uncertainty.svg)

In the canonical run, mean outer-interval width decreases from about `0.960` at 50 calibration observations per class to about `0.281` at 2,500.

**Engineering implication:** reference-sample size is part of the final uncertainty budget.

Audit: [`calibration_sample_uncertainty.csv`](../results/calibration_sample_uncertainty.csv), [`measurement_robustness.py`](../src/consciousness_measurement/measurement_robustness.py).

---

## V7. Arbitrary missing outcomes

**Question:** what can be said when some deployment outcomes are missing and no missing-at-random assumption is imposed?

For \(s_o\) observed positives among \(n_o\) observed outcomes from \(N\) intended measurements,

\[
q\in\left[\frac{s_o}{N},\frac{s_o+N-n_o}{N}\right].
\]

These proxy-rate bounds are sharp under unrestricted missing outcomes.

![Missingness identification loss](figures/missingness_identification_loss.svg)

The canonical latent interval reaches width `0.400` at 30% unrestricted missingness.

**Engineering implication:** missing observations widen the permitted claim; they are not encoded as negative evidence.

Audit: [`missingness_stress.csv`](../results/missingness_stress.csv), [`measurement_robustness.py`](../src/consciousness_measurement/measurement_robustness.py).

---

## V8. Inverse conditioning

**Question:** how strongly do small measurement errors amplify when the channel has a weak information margin?

\[
\frac{\partial\pi}{\partial q}=\frac1J,
\qquad
\frac{\partial\pi}{\partial\alpha}=-\frac{\pi}{J},
\qquad
\frac{\partial\pi}{\partial\beta}=\frac{1-\pi}{J}.
\]

![Inverse conditioning by Youden margin](figures/inverse_conditioning_youden.svg)

At \(J=0.05\), proxy-rate error is amplified 20-fold. At \(J=0.90\), the amplification is about 1.11-fold.

**Engineering implication:** an algebraically invertible channel can still be scientifically unusable because the inverse is ill-conditioned.

Audit: [`conditioning_stress.csv`](../results/conditioning_stress.csv), [`measurement_robustness.py`](../src/consciousness_measurement/measurement_robustness.py).

---

## V9. Heterogeneous-site non-identifiability

**Question:** does one pooled observable rate identify the average latent prevalence when sites have different calibration channels?

For two sites,

\[
\bar q
=
\frac{c_1+c_2}{2}
+
\frac{J_1\pi_1+J_2\pi_2}{2},
\]

which generally identifies a calibration-weighted combination rather than

\[
\bar\pi=\frac{\pi_1+\pi_2}{2}.
\]

![Two-site partial identification](figures/two_site_partial_identification.svg)

At pooled rate `0.45`, the canonical construction admits average latent prevalence from about `0.375` to `0.5625`.

**Engineering implication:** site-specific calibration can determine which population quantity is mathematically identifiable.

Audit: [`two_site_nonidentifiability.csv`](../results/two_site_nonidentifiability.csv), [`measurement_robustness.py`](../src/consciousness_measurement/measurement_robustness.py).

---

## V10. Resolution-based abstention

**Question:** when should the pipeline refuse to emit a precise latent estimate?

For interval \(I_n=[L_n,U_n]\), define

\[
w_n=U_n-L_n,
\]

and release only when

\[
w_n\le\omega.
\]

![Resolution abstention frontier](figures/resolution_abstention_frontier.svg)

With predeclared \(\omega=0.28\), the canonical simulation releases 0% of runs at `n=750`, about 44.4% at `n=1000`, and 100% at `n=1500`.

**Engineering implication:** `inconclusive` is a valid scientific state. A pipeline should not manufacture precision merely because downstream software expects a number.

Audit: [`resolution_abstention_frontier.csv`](../results/resolution_abstention_frontier.csv), [`robustness_simulations.py`](../src/consciousness_measurement/robustness_simulations.py).

---

# Reproducibility map

| Layer | Reproduce | Code | Tests | Machine-readable record |
|---|---|---|---|---|
| V1-V5 | `python scripts/run_validation_program.py` | `latent_measurement.py`, `simulation_validation.py` | `test_latent_measurement.py`, `test_simulation_validation.py` | V1-V5 CSV/JSON files in `results/` |
| V6-V10 | `python scripts/run_robustness_validation.py` | `measurement_robustness.py`, `robustness_simulations.py` | `test_measurement_robustness.py`, `test_robustness_simulations.py` | V6-V10 CSV/JSON files in `results/` |
| Whole repository | `make check` | all source modules | complete pytest suite | repository policy and CI record |

Canonical seeds are `20260917` for V1-V5 and `20260918` for V6-V10.

---

# How to read the result figures

A result figure supports only the narrow mathematical or computational statement produced by its declared experiment. Before using one in a paper or presentation, verify:

1. the declared target and measurement model;
2. the assumptions used by the theorem or simulation;
3. the exact code path that generated the result;
4. the machine-readable input/output record;
5. the failure condition being tested;
6. the strongest claim the result can support;
7. the explicit nonclaim.

For Research III, a successful synthetic test validates an inference procedure under known conditions. It does not validate a consciousness biomarker in people or systems. That later empirical burden remains separate and visible.
