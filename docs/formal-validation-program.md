# Formal Validation Program V1-V5

## Purpose

Research III needs mathematical objects that can fail, code that reproduces those objects, and validation experiments that distinguish a sound measurement argument from an attractive score. This document defines the first five formal validation stages.

The latent variable below is a **declared binary measurement target**. The mathematics does not establish that the target is consciousness, does not provide direct access to qualia, and does not turn a proxy into an ontological measurement. The scientific burden of target validity, calibration, transport, and interpretation remains explicit.

## V1. Point identification through an imperfect binary channel

Let

\[
T\in\{0,1\}
\]

be a declared latent target and

\[
Y\in\{0,1\}
\]

an observable binary evidence channel. Define

\[
\alpha=P(Y=1\mid T=1),\qquad
\beta=P(Y=0\mid T=0),
\]

and latent prevalence

\[
\pi=P(T=1).
\]

The observable positive rate is

\[
q=P(Y=1)
=\alpha\pi+(1-\beta)(1-\pi).
\]

Writing the Youden information coefficient as

\[
J=\alpha+\beta-1,
\]

gives

\[
q=(1-\beta)+J\pi.
\]

### Proposition V1

If \(J>0\) and \(\alpha,\beta\) are known in the declared validation domain, then \(\pi\) is point identified by

\[
\boxed{
\pi=\frac{q+\beta-1}{\alpha+\beta-1}
}
\]

provided the observed \(q\) is compatible with the calibration model.

### Proof

The law of total probability gives

\[
q=P(Y=1\mid T=1)P(T=1)+P(Y=1\mid T=0)P(T=0).
\]

Substituting \(P(Y=1\mid T=1)=\alpha\), \(P(Y=1\mid T=0)=1-\beta\), and \(P(T=0)=1-\pi\) yields

\[
q=\alpha\pi+(1-\beta)(1-\pi)
=(1-\beta)+(\alpha+\beta-1)\pi.
\]

Because \(J>0\), division by \(J\) is valid and gives the stated inverse. QED.

### Scientific meaning

The denominator \(J\) is an identifiability margin. As \(J\to0\), inversion becomes unstable. A channel with sensitivity plus specificity close to one cannot support stable latent inversion even with arbitrarily large sample size.

## V2. Partial identification and finite-sample uncertainty

Calibration is rarely point known. Let

\[
\alpha\in[\alpha_L,\alpha_U],\qquad
\beta\in[\beta_L,\beta_U],\qquad
q\in[q_L,q_U],
\]

with

\[
\kappa=\alpha_L+\beta_L-1>0.
\]

The implementation returns a conservative outer identification interval using interval arithmetic. Define

\[
N=q+\beta-1,
\qquad
J=\alpha+\beta-1.
\]

Then

\[
N\in[q_L+\beta_L-1,\ q_U+\beta_U-1]
\]

and

\[
J\in[\alpha_L+\beta_L-1,\ \alpha_U+\beta_U-1].
\]

Therefore a valid outer interval is

\[
\boxed{
\Pi_{\rm out}
=
\left[
\max\left(0,\frac{q_L+\beta_L-1}{\alpha_U+\beta_U-1}\right),
\min\left(1,\frac{q_U+\beta_U-1}{\alpha_L+\beta_L-1}\right)
\right].
}
\]

This interval is deliberately conservative because specificity appears in both numerator and denominator. It is an outer set, not a claim of sharpness.

### Proposition V2: finite-sample coverage

Suppose \(Y_1,\ldots,Y_n\) are independent Bernoulli observations with mean \(q\), the true \((\alpha,\beta)\) lies inside the declared calibration box, and \(\kappa>0\). Let

\[
\hat q=\frac{1}{n}\sum_{i=1}^n Y_i,
\qquad
\epsilon_n(\delta)=\sqrt{\frac{\log(2/\delta)}{2n}}.
\]

By Hoeffding's inequality,

\[
P\left(|\hat q-q|\le\epsilon_n(\delta)\right)\ge 1-\delta.
\]

Construct

\[
Q_n=
[\max(0,\hat q-\epsilon_n),\min(1,\hat q+\epsilon_n)]
\]

and pass \(Q_n\) through the outer identification map above. Then the resulting latent interval contains the true \(\pi\) with probability at least \(1-\delta\), conditional on the declared calibration box containing the true calibration.

### Proof

With probability at least \(1-\delta\), Hoeffding's inequality places the true \(q\) inside \(Q_n\). On that event, the true \(q,\alpha,\beta\) all lie inside the interval box used by the outer-identification map. Interval arithmetic therefore contains the value of the rational map at the true parameter point. Hence the true \(\pi\) lies in the returned interval on an event with probability at least \(1-\delta\). QED.

### Simulation check

The fixed-seed validation run uses true \(\pi=0.40\), sensitivity 0.84, specificity 0.91, a +/-0.02 calibration box, 2,500 repetitions per sample size, and nominal coverage 0.95.

| n | empirical coverage | mean interval width |
|---:|---:|---:|
| 50 | see generated CSV | 0.606 approximately |
| 100 | see generated CSV | generated |
| 250 | see generated CSV | generated |
| 500 | see generated CSV | generated |
| 1000 | see generated CSV | generated |
| 2500 | see generated CSV | 0.169 approximately |

The exact machine-readable values are in `results/finite_sample_coverage.csv` and `results/validation_summary.json`.

![Finite-sample identification width](figures/finite_sample_identification.svg)

![Finite-sample coverage](figures/finite_sample_coverage.svg)

## V3. Intervention contrasts and measurement invariance

Consider two conditions \(z\in\{0,1\}\) with latent prevalences \(\pi_0,\pi_1\). Under invariant calibration,

\[
q_z=(1-\beta)+J\pi_z.
\]

Subtracting the conditions gives

\[
\Delta q=J\Delta\pi.
\]

### Proposition V3

If sensitivity and specificity are invariant across the two conditions and \(J>0\), then

\[
\boxed{
\Delta\pi=\frac{\Delta q}{J}.
}
\]

This makes measurement invariance an explicit identification assumption rather than an implicit convenience.

### Exact bias under calibration shift

Let baseline calibration be \((\alpha_0,\beta_0)\) and condition-1 calibration be \((\alpha_1,\beta_1)\), with

\[
J_z=\alpha_z+\beta_z-1,
\qquad
\operatorname{FPR}_z=1-\beta_z.
\]

If the analyst incorrectly corrects both conditions using the baseline \(J_0\), the contrast bias is exactly

\[
\boxed{
\operatorname{Bias}
=
\frac{(J_1-J_0)\pi_1+(\operatorname{FPR}_1-\operatorname{FPR}_0)}{J_0}.
}
\]

The validation grid in `results/transport_stress.csv` verifies that zero calibration shift gives exactly zero bias and quantifies the bias away from invariance.

![Calibration transport stress](figures/transport_bias_surface.svg)

## V4. Conditional-dependence stress test for multimodal fusion

Multiplying channel likelihood ratios assumes conditional independence. Research III already exposes that assumption in the software API. V4 makes the failure mode quantitative.

For channel \(m\), let

\[
p_m^{(1)}=P(Y_m=1\mid T=1),
\qquad
p_m^{(0)}=P(Y_m=1\mid T=0).
\]

Define a dependence mixture indexed by \(\rho\in[0,1]\):

- with probability \(1-\rho\), channels use independent uniform random variables;
- with probability \(\rho\), all channels use one shared uniform random variable.

This construction preserves every marginal channel probability exactly. For the all-positive pattern,

\[
P(Y_1=\cdots=Y_M=1\mid T=t)
=
\rho\min_m p_m^{(t)}
+(1-\rho)\prod_m p_m^{(t)}.
\]

The corresponding posterior is therefore available in closed form. At \(\rho=0\), it equals naive independence fusion. As \(\rho\) increases, repeated evidence becomes less independent and naive multiplication can become severely overconfident.

In the canonical three-channel stress case, naive fusion gives a posterior of about 0.997 for the all-positive pattern, while the exact posterior at full shared dependence is 0.84. This is a deliberate counterexample to the idea that more modalities automatically mean proportionally more independent evidence.

![Conditional dependence stress](figures/dependence_stress.svg)

The existing Frechet-Hoeffding partial-identification code provides a complementary dependence-robust interval when only channel marginals are trusted.

## V5. Structural-alignment null and power behavior

The phenomenal-structure arm requires a falsifiable correspondence statistic rather than a visual similarity argument.

For items \(i=1,\ldots,K\), let latent reference coordinates be

\[
z_i\in\mathbb R^d,
\]

and generate a second representation

\[
x_i
=
\lambda z_i+\sqrt{1-\lambda^2}\,\varepsilon_i,
\qquad
\varepsilon_i\sim\mathcal N(0,I_d),
\]

where \(\lambda\in[0,1]\) is a planted shared-geometry signal.

Build Euclidean distance matrices \(D_Z,D_X\), compute upper-triangle correlation

\[
r=\operatorname{corr}(\operatorname{vec}_\triangle D_Z,
\operatorname{vec}_\triangle D_X),
\]

and obtain a one-sided permutation p-value by relabeling one distance matrix.

### Validation questions

1. At \(\lambda=0\), does the test reject at approximately its nominal alpha rather than inventing correspondence?
2. Does rejection probability increase as shared geometry increases?
3. Does mean held-out relational alignment increase with the planted signal?

The fixed-seed V5 experiment uses 160 replicates per signal level, 20 items, 3 dimensions, and 199 permutations per replicate. The observed null rejection rate is 0.0375 at alpha 0.05, while the strongest planted signal reaches rejection rate 1.0 with mean alignment about 0.799.

![Structural alignment null and power](figures/structural_alignment_power.svg)

These are synthetic validation results. They establish behavior of the statistic under known data-generating conditions. They do not establish that a neural geometry predicts phenomenal geometry in humans. A human-data M6 claim still requires preregistered, held-out empirical validation.

## Reproduction

Run

```bash
python -m pip install -e ".[dev]"
python scripts/run_validation_program.py
pytest -q
```

The validation script uses seed `20260917` and writes:

- `results/finite_sample_coverage.csv`
- `results/dependence_stress.csv`
- `results/transport_stress.csv`
- `results/structural_alignment_power.csv`
- `results/validation_summary.json`
- five generated SVG result figures under `docs/figures/`

A clean rerun should reproduce the same CSV, JSON, and SVG records on the same supported numerical stack.

## Falsification and interpretation rules

The validation program is useful only if failures remain visible.

- If point inversion fails because \(J\le0\), the target is not identified through that channel.
- If the finite-sample interval remains too wide for the intended claim, the correct output is partial identification or abstention.
- If calibration changes across intervention or state, an invariant-calibration contrast is not licensed without sensitivity analysis.
- If channel dependence is not justified, naive likelihood-ratio multiplication is not licensed as a calibrated posterior.
- If the structural permutation test rejects too often under the null, its implementation or inferential calibration must be repaired before empirical use.
- If structural power is poor at scientifically meaningful signal levels, an M6 study is underpowered even if one observed dataset happens to look aligned.

## Literature anchors

The statistical architecture is consistent with established work on latent-class measurement without a perfect reference standard, the consequences of conditional dependence, and partial identification under imperfect reference tests. See Collins and Huynh (2014), Obradovic (2024), and related latent-class literature.

The consciousness-science boundary follows the field's long-standing problem that external measurements, reports, no-report paradigms, and perturbational indices each carry distinct assumptions and validation domains. See Casali et al. (2013), Casarotto et al. (2016), and methodological discussions of no-report paradigms.

The purpose of importing these statistical tools is not to equate consciousness with disease status. It is to use mature measurement theory for the shared inferential problem: a scientifically important target is not directly observed by the external investigator, and imperfect evidence channels must not be treated as a perfect gold standard.
