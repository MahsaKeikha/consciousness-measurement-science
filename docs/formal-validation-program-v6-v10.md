# Formal Validation Program V6-V10

## Purpose

V1-V5 established a first theorem-to-code validation layer for Research III. V6-V10 extend the framework into additional failure regimes that matter for a real measurement system: finite calibration data, arbitrary missing observations, weak-channel conditioning, heterogeneous sites, and explicit abstention when the evidence cannot support a predeclared resolution.

The latent variable remains a **declared measurement target**. None of the results below are human consciousness measurements. They are analytic and synthetic validation results for the measurement machinery itself.

The common binary measurement model is

\[
q=P(Y=1)=(1-\beta)+(\alpha+\beta-1)\pi,
\]

where

- \(\pi=P(Z=1)\) is the prevalence of the declared latent target;
- \(\alpha=P(Y=1\mid Z=1)\) is sensitivity;
- \(\beta=P(Y=0\mid Z=0)\) is specificity;
- \(J=\alpha+\beta-1\) is the Youden information margin;
- \(Y\) is an observable binary channel and \(Z\) is the declared latent target.

When \(J>0\), the point inverse under known calibration is

\[
\pi=\frac{q+\beta-1}{J}.
\]

V6-V10 ask what remains justified once the idealized assumptions behind that formula are weakened.

---

# V6. Finite calibration samples

## Question

What if the proxy rate, sensitivity, and specificity are all estimated from finite samples rather than treated as known constants?

Let

\[
\hat q=\frac{X_q}{n_q},\qquad
\hat\alpha=\frac{X_\alpha}{n_\alpha},\qquad
\hat\beta=\frac{X_\beta}{n_\beta}.
\]

For any Bernoulli proportion \(p\), Hoeffding's inequality gives

\[
P(|\hat p-p|>\epsilon)\le 2e^{-2n\epsilon^2}.
\]

To obtain a simultaneous failure probability no larger than \(\delta\) for the three estimated quantities, allocate \(\delta/3\) to each component. Then

\[
\epsilon(n,\delta/3)
=
\sqrt{\frac{\log(6/\delta)}{2n}}.
\]

Define simultaneous boxes

\[
q\in Q=[q_L,q_U],\quad
\alpha\in A=[\alpha_L,\alpha_U],\quad
\beta\in B=[\beta_L,\beta_U].
\]

By the union bound,

\[
P(q\in Q,\alpha\in A,\beta\in B)\ge 1-\delta.
\]

The finite-sample latent identified set is then

\[
\Pi(Q,A,B)
=
\left\{
\frac{q+\beta-1}{\alpha+\beta-1}:
q\in Q,\alpha\in A,\beta\in B,
\alpha+\beta-1>0
\right\}\cap[0,1].
\]

The implementation computes a conservative outer interval by evaluating the admissible boundary/corner extrema and clipping to the probability unit interval.

## Proposition V6

If the simultaneous calibration box contains the true triple \((q,\alpha,\beta)\), the true latent prevalence \(\pi\) belongs to \(\Pi(Q,A,B)\). Therefore the finite-sample outer interval covers the target with probability at least \(1-\delta\), subject to the declared measurement model and positive-information restriction.

### Proof

On the event

\[
(q,\alpha,\beta)\in Q\times A\times B,
\]

the true parameter triple is one of the admissible triples used to construct \(\Pi(Q,A,B)\). Substituting the true triple into the inverse measurement equation returns the true \(\pi\). Therefore \(\pi\in\Pi(Q,A,B)\). The simultaneous event occurs with probability at least \(1-\delta\) by the union bound applied to the three Hoeffding events. \(\square\)

## Deterministic simulation

The canonical run fixes the deployment sample size and varies the number of positive and negative reference cases used to estimate sensitivity and specificity. The result is deliberately conservative: the identified interval is broad when calibration data are scarce and narrows as the reference sample grows.

![Finite calibration sample uncertainty](figures/calibration_sample_uncertainty.svg)

Canonical machine-readable result: [`../results/calibration_sample_uncertainty.csv`](../results/calibration_sample_uncertainty.csv).

In the fixed-seed run, mean interval width decreases from approximately **0.960 at 50 calibration observations per class** to **0.281 at 2,500 per class**. Conditional coverage is 1.0 throughout this declared stress grid.

### Interpretation

Calibration sample size is part of the measurement uncertainty budget. Treating a sensitivity or specificity estimate as exact can make a latent estimate appear much more precise than the evidence warrants.

---

# V7. Arbitrary missing outcomes

## Question

What can be identified if some deployment outcomes are missing and no missing-at-random assumption is allowed?

Suppose \(N\) measurements were intended, \(n_o\) outcomes are observed, and \(s_o\) of the observed outcomes are positive. Let \(m=N-n_o\) be the number missing. The total number of positives \(S\) must satisfy

\[
s_o\le S\le s_o+m.
\]

Therefore the full-sample proxy rate is sharply bounded by

\[
\boxed{
q\in
\left[
\frac{s_o}{N},
\frac{s_o+m}{N}
\right].
}
\]

No distributional or missingness-model assumption is needed for this statement.

## Proposition V7

The bounds above are sharp under unrestricted missing outcomes.

### Proof

The lower endpoint is achieved by assigning every missing outcome the value zero. The upper endpoint is achieved by assigning every missing outcome the value one. Every intermediate value corresponding to an integer number of positive missing outcomes is attainable. No tighter universal bounds are possible without additional assumptions. \(\square\)

With known calibration, propagate this interval through the inverse map:

\[
\Pi_{\mathrm{miss}}
=
\left\{
\frac{q+\beta-1}{J}:q\in[q_L,q_U]
\right\}\cap[0,1].
\]

Since the inverse is increasing in \(q\) when \(J>0\), the endpoints are simply the transformed proxy-rate endpoints.

![Missingness identification loss](figures/missingness_identification_loss.svg)

Canonical machine-readable result: [`../results/missingness_stress.csv`](../results/missingness_stress.csv).

In the canonical setup, unrestricted **10% missingness** widens the latent interval to approximately **0.133**, **30% missingness** widens it to **0.400**, and **50% missingness** widens it to approximately **0.667**.

### Interpretation

Missing data are not evidence of absence. When missing outcomes could plausibly be either positive or negative, the scientifically correct object is an identified set whose width records the information that was lost.

---

# V8. Inverse conditioning and information margin

## Question

How stable is the latent inverse to small errors in observed rate or calibration?

For

\[
\pi(q,\alpha,\beta)
=
\frac{q+\beta-1}{J},
\qquad J=\alpha+\beta-1,
\]

the local sensitivities are

\[
\frac{\partial\pi}{\partial q}=\frac{1}{J},
\]

\[
\frac{\partial\pi}{\partial\alpha}
=-\frac{\pi}{J},
\]

and

\[
\frac{\partial\pi}{\partial\beta}
=\frac{1-\pi}{J}.
\]

## Proposition V8

The inverse problem becomes arbitrarily ill-conditioned as \(J\to0^+\). At \(J=0\), the latent prevalence is not identifiable from the proxy rate.

### Proof

The derivative with respect to \(q\) is exactly \(1/J\), so the amplification of a small proxy-rate perturbation diverges as \(J\to0^+\). If \(J=0\), then

\[
q=(1-\beta)+J\pi=1-\beta,
\]

which no longer depends on \(\pi\). Thus every \(\pi\in[0,1]\) produces the same observable rate and the latent prevalence cannot be identified from \(q\). \(\square\)

![Inverse conditioning by Youden information margin](figures/inverse_conditioning_youden.svg)

Canonical machine-readable result: [`../results/conditioning_stress.csv`](../results/conditioning_stress.csv).

For a fixed proxy-rate perturbation of 0.02, the canonical sweep shows latent error of approximately **0.40 when \(J=0.05\)**, compared with approximately **0.022 when \(J=0.90\)**.

### Interpretation

A weak channel is not merely less discriminating. It can make inverse inference numerically unstable. The information margin therefore belongs in any engineering specification that converts a calibrated observable into a latent estimate.

---

# V9. Two-site pooled non-identifiability

## Question

Can a pooled observable rate identify the average latent prevalence if sites use different measurement channels?

For two equally weighted sites,

\[
q_1=c_1+J_1\pi_1,
\qquad
q_2=c_2+J_2\pi_2,
\]

with

\[
c_s=1-\beta_s,
\]

the pooled observable rate is

\[
\bar q
=
\frac{q_1+q_2}{2}
=
\frac{c_1+c_2}{2}
+
\frac{J_1\pi_1+J_2\pi_2}{2}.
\]

The target average prevalence is

\[
\bar\pi=\frac{\pi_1+\pi_2}{2}.
\]

Unless \(J_1=J_2\), the pooled equation identifies a weighted combination of \(\pi_1\) and \(\pi_2\), not their simple average.

## Proposition V9

With heterogeneous site calibration, the same pooled observable rate can correspond to distinct average latent prevalences.

### Constructive proof

Choose two admissible site calibrations with unequal information margins. Fix a pooled proxy rate \(\bar q\). The equation

\[
J_1\pi_1+J_2\pi_2
=
2\bar q-(c_1+c_2)
\]

defines a line segment in the unit square whenever the right-hand side is admissible. Moving along that segment changes

\[
\bar\pi=(\pi_1+\pi_2)/2
\]

unless the segment happens to be parallel to a constant-average line. For \(J_1\ne J_2\), these slopes differ, so two points on the admissible segment generally have different \(\bar\pi\). Therefore the pooled observable alone does not point-identify the average latent prevalence. \(\square\)

The implementation computes the exact extrema of \(\bar\pi\) over the intersection of the linear pooled constraint with \([0,1]^2\).

![Two-site partial identification](figures/two_site_partial_identification.svg)

Canonical machine-readable result: [`../results/two_site_nonidentifiability.csv`](../results/two_site_nonidentifiability.csv).

At the canonical pooled rate \(\bar q=0.45\), the same observable is compatible with an average latent prevalence from approximately **0.375 to 0.5625** under the declared two-site calibration pair.

### Interpretation

Pooling sites before accounting for measurement heterogeneity can erase identifiability. Site-specific calibration is therefore not merely a nuisance covariate. It can change what population quantity is mathematically recoverable.

---

# V10. Resolution-based abstention

## Question

When should a measurement system decline to release a latent estimate?

Let a validated procedure return an identified interval

\[
I_n=[L_n,U_n].
\]

Define its resolution width

\[
w_n=U_n-L_n.
\]

Before observing the data, choose a maximum scientifically acceptable width \(\omega>0\). Define the release rule

\[
R_n=
\begin{cases}
1,&w_n\le\omega,\\
0,&w_n>\omega.
\end{cases}
\]

When \(R_n=0\), the correct output is **abstain / insufficient resolution**, not an arbitrarily selected midpoint.

## Proposition V10

If the underlying interval procedure has coverage at least \(1-\delta\), then every released interval retains that interval's coverage guarantee conditional on the declared procedure; abstention cannot create information that is not present.

The implementation reports both the release rate and conditional coverage among released intervals so that a stringent abstention rule cannot be mistaken for universal performance.

![Resolution abstention frontier](figures/resolution_abstention_frontier.svg)

Canonical machine-readable result: [`../results/resolution_abstention_frontier.csv`](../results/resolution_abstention_frontier.csv).

For the predeclared canonical threshold

\[
\omega=0.28,
\]

the fixed-seed simulation releases approximately **0% at deployment \(n=750\)**, **44.4% at \(n=1000\)**, and **100% at \(n=1500\)** under the declared calibration-sample design.

### Interpretation

A scientifically responsible measurement system should be allowed to say that the available data are too weak for the requested resolution. Abstention is therefore an engineering output, not a software exception.

---

# Cross-stage engineering contract

V6-V10 together define five additional obligations for Research III:

| Stage | Failure regime | Mathematical object | Required software behavior | Scientific lesson |
|---|---|---|---|---|
| V6 | finite calibration data | simultaneous calibration/proxy confidence box | propagate all three uncertainties | reference-data uncertainty belongs in the final claim |
| V7 | arbitrary missing outcomes | sharp missingness identification interval | preserve missing values as uncertainty | missing is not negative evidence |
| V8 | weak measurement channel | inverse sensitivity and condition factor | flag low-information calibration | an invertible formula can still be unstable |
| V9 | heterogeneous sites | site-mixture identified set | retain calibration strata | pooled observables need not identify pooled latent targets |
| V10 | insufficient precision | predeclared resolution threshold | abstain when width is too large | fewer claims can be more scientifically valid |

---

# Reproducibility

The canonical V6-V10 run is generated with

```bash
python scripts/run_robustness_validation.py
```

The runner uses fixed seed `20260918` and writes the machine-readable results under `results/` plus the five SVG scientific figures linked above.

The analytic implementation is in:

- `src/consciousness_measurement/measurement_robustness.py`
- `src/consciousness_measurement/robustness_simulations.py`

The corresponding theorem and simulation tests are:

- `tests/test_measurement_robustness.py`
- `tests/test_robustness_simulations.py`

The repository's normal CI still applies: repository policy, Python compilation, pytest, and Ruff must all pass before this layer is merged.

---

# Scientific boundary

V6-V10 validate properties of an explicit measurement model and its software implementation. They demonstrate what follows mathematically under declared assumptions and how the procedures behave on synthetic data.

They do **not** establish that any current neural, behavioral, physiological, perturbational, or artificial-system channel has the stated calibration for consciousness. They do not validate a human consciousness instrument, identify qualia, prove an ontology, or justify a clinical decision threshold.

Those claims require empirical calibration, preregistered prospective validation, cross-site and cross-state replication, causal interventions where relevant, and target-specific evidence from real subjects or systems.
