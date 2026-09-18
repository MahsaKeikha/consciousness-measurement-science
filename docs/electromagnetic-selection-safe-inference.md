# Multiplicity and Selection-Safe Electromagnetic Inference

## Research III V41-V45

V36-V40 established exact scalar-amplitude inference under known covariance, finite inverse-covariance bias, Gaussian source-discrimination error, an independent-search FWER baseline, and sandwich variance under covariance mismatch.

V41-V45 address the next statistical problem:

> How should an electromagnetic study control multiplicity, avoid same-data selection bias, and preserve valid confirmatory inference when many candidate sources, times, frequencies, or preprocessing choices are searched?

These stages are analytic or fixed-seed synthetic inference results. They are not human empirical data and they do not identify consciousness or qualia.

---

## V41. Bonferroni FWER control under arbitrary dependence

Let \(A_k\) be the false-positive event for comparison \(k\), with

\[
P(A_k)\le \frac{\alpha}{K}.
\]

No independence assumption is required.

By the union bound,

\[
P\left(
\bigcup_{k=1}^{K} A_k
\right)
\le
\sum_{k=1}^{K} P(A_k)
\le
K\frac{\alpha}{K}
=
\alpha.
\]

Therefore

\[
\boxed{
\operatorname{FWER}
\le
\alpha
}
\]

for any dependence structure among the \(K\) tests.

For two-sided standard-normal statistics, choose threshold

\[
\boxed{
t_{\alpha,K}^{\mathrm{Bonf}}
=
\Phi^{-1}
\left(
1-\frac{\alpha}{2K}
\right).
}
\]

The corresponding union-bound FWER is

\[
K\cdot
2\left[
1-\Phi(t_{\alpha,K}^{\mathrm{Bonf}})
\right]
=
\alpha.
\]

### Canonical V41 thresholds

At \(\alpha=0.05\),

\[
\begin{array}{c|c|c}
K & t_{\alpha,K}^{\mathrm{Bonf}} & \text{independent exact FWER}\\
\hline
1 & 1.959963985 & 0.0500000000\\
10 & 2.807033768 & 0.0488898695\\
100 & 3.480756404 & 0.0487824698\\
1000 & 4.055626981 & 0.0487717646
\end{array}
\]

The union-bound guarantee is exactly 0.05 up to floating-point roundoff. Under independence, the realized FWER is slightly smaller because Bonferroni is conservative.

The scientific point is narrow but important:

> A search-wide error guarantee can be valid without assuming independent source statistics.

---

## V42. Holm step-down testing

Let ordered raw p-values satisfy

\[
p_{(1)}
\le
p_{(2)}
\le
\cdots
\le
p_{(K)}.
\]

Holm's sequentially rejective procedure compares

\[
p_{(i)}
\]

to

\[
\frac{\alpha}{K-i+1}.
\]

Equivalently, the Holm adjusted p-value for ordered position \(i\) is

\[
\boxed{
\widetilde p_{(i)}
=
\min\left[
1,
\max_{1\le j\le i}
(K-j+1)p_{(j)}
\right].
}
\]

A hypothesis is rejected when its adjusted p-value is at most \(\alpha\).

Holm controls strong family-wise error under arbitrary dependence while being uniformly no less powerful than single-step Bonferroni.

### Canonical V42 example

Take

\[
(p_1,p_2,p_3,p_4)
=
(0.001,\ 0.016,\ 0.017,\ 0.5).
\]

The Holm adjusted p-values are

\[
(0.004,\ 0.048,\ 0.048,\ 0.5).
\]

At \(\alpha=0.05\), Holm rejects the first three hypotheses.

Single-step Bonferroni uses threshold

\[
\frac{0.05}{4}
=
0.0125
\]

and rejects only the first.

Thus the canonical example gives

\[
\boxed{
3\ \text{Holm rejections}
\quad\text{versus}\quad
1\ \text{Bonferroni rejection}.
}
\]

The gain does not come from weakening the family-wise error target. It comes from using the ordered evidence structure.

---

## V43. Exact sign-flip maximum-statistic inference

Suppose each observation row is a multivariate source statistic and the global null implies row-wise sign symmetry.

Let the data matrix be

\[
\mathbf X
\in
\mathbb R^{n\times K}.
\]

Define the maximum absolute mean statistic

\[
\boxed{
T(\mathbf X)
=
\max_{1\le k\le K}
\left|
\frac{1}{n}
\sum_{i=1}^{n}
X_{ik}
\right|.
}
\]

For sign vector

\[
\mathbf s
\in
\{-1,+1\}^{n},
\]

let

\[
\mathbf X_{\mathbf s}
=
\operatorname{diag}(\mathbf s)\mathbf X.
\]

The exact sign-flip orbit contains

\[
2^n
\]

datasets.

The randomization p-value is

\[
\boxed{
p_{\mathrm{flip}}
=
\frac{
\#\left\{
\mathbf s:
T(\mathbf X_{\mathbf s})
\ge
T(\mathbf X)
\right\}
}{
2^n
}.
}
\]

Under the declared sign-symmetry null, the observed sign configuration is exchangeable over this finite orbit. Therefore the rank-based randomization p-value is finite-sample valid for the maximum statistic.

### Canonical V43 construction

The deterministic matrix contains

\[
n=6
\]

rows and

\[
K=2
\]

source coordinates, so the orbit size is

\[
2^6=64.
\]

The observed statistic is

\[
T_{\mathrm{obs}}
=
1.0083333333.
\]

Exactly two sign configurations meet or exceed it, giving

\[
\boxed{
p_{\mathrm{flip}}
=
\frac{2}{64}
=
0.03125.
}
\]

This result is exact for the declared finite sign orbit. It does not justify sign-flip testing when the row-wise symmetry assumption is false.

---

## V44. Exact post-selection coverage collapse under same-data reuse

Let

\[
Z_1,\ldots,Z_K
\]

be independent standard-normal null statistics.

Suppose an ordinary symmetric marginal interval has coverage

\[
c.
\]

Equivalently, its null statistic remains inside the marginal acceptance threshold with probability \(c\).

Now select

\[
J
=
\arg\max_k |Z_k|
\]

and report the ordinary marginal interval for the selected coordinate using the same data.

The selected interval covers zero exactly when every searched coordinate remains inside the marginal acceptance threshold.

Under independence,

\[
P(\text{selected interval covers }0)
=
P\left(
\max_k |Z_k|
\le t_c
\right)
=
c^K.
\]

Therefore

\[
\boxed{
C_{\mathrm{selected}}
=
c^K
}
\]

and

\[
\boxed{
P_{\mathrm{FP,selected}}
=
1-c^K.
}
\]

### Canonical V44 result

For marginal coverage

\[
c=0.95,
\]

the exact selected-coordinate coverage is

\[
\begin{array}{c|c|c}
K & 0.95^K & 1-0.95^K\\
\hline
1 & 0.95 & 0.05\\
10 & 0.5987369392 & 0.4012630608\\
100 & 0.0059205292 & 0.9940794708\\
1000 & 5.2918227\times10^{-23} & \approx 1
\end{array}
\]

At \(K=100\), a nominal 95 percent interval reused after max-absolute selection covers the null value only about 0.59 percent of the time.

This is an exact independent-null result. It formalizes the danger of using the same noisy search to select a source and then treating its ordinary marginal uncertainty as confirmatory.

---

## V45. Independent holdout restores selected-coordinate Type I error

Now separate discovery and confirmation.

Let the discovery data select an index

\[
J
=
g(D_{\mathrm{disc}})
\]

using any measurable search rule.

Let the confirmatory statistics

\[
Z^{\mathrm{conf}}_1,\ldots,Z^{\mathrm{conf}}_K
\]

be independent of the discovery data and satisfy the null law

\[
Z^{\mathrm{conf}}_k
\sim
\mathcal N(0,1)
\]

for every \(k\).

Conditional on the selected index \(J=j\),

\[
P\left(
|Z^{\mathrm{conf}}_J|>z_{1-\alpha/2}
\mid
J=j
\right)
=
\alpha.
\]

Averaging over the discovery-selected index gives

\[
\boxed{
P\left(
|Z^{\mathrm{conf}}_J|>z_{1-\alpha/2}
\right)
=
\alpha.
}
\]

Thus independent confirmation restores nominal selected-coordinate Type I error regardless of how many discovery coordinates were searched, provided the confirmatory null model and independence assumptions hold.

### Canonical V45 simulation

The fixed-seed simulation uses

\[
K=100,
\qquad
50{,}000\ \text{trials},
\qquad
\alpha=0.05.
\]

Same-data reuse gives empirical false-positive rate

\[
0.99382,
\]

close to the exact value

\[
1-0.95^{100}
=
0.9940794708.
\]

Independent holdout confirmation gives empirical false-positive rate

\[
0.04986,
\]

close to the exact conditional and unconditional value

\[
0.05.
\]

The fixed-seed simulation checks the implementation against the analytic result.

---

## Combined inference chain

V41-V45 create a selection-safe inference chain:

\[
\text{arbitrary-dependence multiplicity control}
\rightarrow
\text{step-down multiplicity}
\rightarrow
\text{dependence-aware randomization}
\rightarrow
\text{post-selection failure}
\rightarrow
\text{independent confirmation}.
\]

The chain makes several distinctions explicit:

\[
\text{marginal significance}
\neq
\text{search-wide significance},
\]

\[
\text{selected estimate}
\neq
\text{valid selected uncertainty},
\]

\[
\text{same-data reuse}
\neq
\text{independent confirmation},
\]

and

\[
\text{statistical significance}
\neq
\text{consciousness measurement}.
\]

---

## What V41-V45 establish

Inside the declared analytic and fixed-seed synthetic constructions:

1. Bonferroni controls family-wise error by the union bound without requiring independence;
2. the two-sided Bonferroni Gaussian threshold is
   \[
   \Phi^{-1}\left(1-\frac{\alpha}{2K}\right);
   \]
3. Holm adjusted p-values provide strong family-wise error control while improving on single-step Bonferroni in the canonical example;
4. exact row-wise sign-flip enumeration gives a finite randomization p-value for the declared maximum statistic under sign symmetry;
5. same-data max-absolute selection reduces naive independent-null coverage exactly to
   \[
   c^K;
   \]
6. independent confirmation restores selected-coordinate Type I error to \(\alpha\) under the declared independence and null assumptions.

## What V41-V45 do not establish

They do not establish:

- that Bonferroni or Holm is optimal for every electromagnetic analysis;
- that source statistics are independent;
- that sign-flip symmetry holds after arbitrary preprocessing;
- that permutation validity survives data-dependent preprocessing unless the full pipeline is included in the randomization;
- that independent discovery and confirmation are available in every dataset;
- that a statistically significant source is a consciousness source;
- that multiplicity correction solves forward-model, inverse-model, confounding, calibration, or target-identification problems;
- that synthetic false-positive calibration replaces human or clinical validation.

---

## Prospective empirical controls

A future electromagnetic source-search study should preregister or report, as applicable:

- the complete search family across source, time, frequency, state, preprocessing, model, and hyperparameter choices;
- whether multiplicity control is single-step, step-down, maximum-statistic, randomization-based, or otherwise dependence-aware;
- the assumptions needed for the chosen correction;
- whether selection and estimation reuse the same data;
- whether source localization, frequency-band choice, ROI choice, or preprocessing was selected before or after observing the target contrast;
- whether confirmatory data are genuinely independent of discovery;
- whether all preprocessing and source-reconstruction steps are repeated inside a permutation or randomization loop when required for validity;
- marginal and search-wide uncertainty;
- sensitivity of conclusions to alternative justified multiplicity families;
- explicit separation of exploratory and confirmatory claims.

A result should be weakened when search multiplicity is incompletely declared, selection and inference reuse the same noise without correction, or the randomization assumptions do not match the acquisition pipeline.

---

## Literature anchors

- Holm S. *A Simple Sequentially Rejective Multiple Test Procedure*. Scandinavian Journal of Statistics. 1979;6(2):65-70.
- Nichols TE, Holmes AP. *Nonparametric permutation tests for functional neuroimaging: a primer with examples*. Human Brain Mapping. 2002;15(1):1-25. doi:10.1002/hbm.1058.
- Kriegeskorte N, Simmons WK, Bellgowan PSF, Baker CI. *Circular analysis in systems neuroscience: the dangers of double dipping*. Nature Neuroscience. 2009;12(5):535-540. doi:10.1038/nn.2303.

These references support the multiplicity, randomization, and selection-bias framework. They do not imply that the V41-V45 synthetic validations are empirical evidence about consciousness.

---

## Reproducibility

Source:

- src/consciousness_measurement/electromagnetic_selection.py
- src/consciousness_measurement/electromagnetic_selection_simulations.py

Tests:

- tests/test_electromagnetic_selection.py
- tests/test_electromagnetic_selection_simulations.py

Runner:

~~~bash
python scripts/run_electromagnetic_selection_validation.py
~~~

Machine-readable outputs:

- results/v41_bonferroni_arbitrary_dependence.csv
- results/v42_holm_step_down.csv
- results/v43_sign_flip_max_statistic.csv
- results/v44_post_selection_coverage.csv
- results/v45_independent_holdout.csv
- results/electromagnetic_selection_validation_summary.json

Canonical figure:

![Multiplicity and selection-safe electromagnetic inference V41-V45](figures/v41_v45_electromagnetic_selection_validation.svg)

V41-V45 remain analytic or fixed-seed synthetic inference results. They are not human empirical data, and they are not human empirical evidence that consciousness has been measured.
