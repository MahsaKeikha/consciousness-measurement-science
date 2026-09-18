# Finite-Sample Electromagnetic Inference Program

## Research III V36-V40

V16-V35 built a measurement-science chain from sensor-level electromagnetic observables through source identifiability, inverse resolution, information geometry, spatial specificity, nuisance loss, and robust model uncertainty.

V36-V40 add the next statistical layer:

> Once an electromagnetic measurement model is declared, how should estimator uncertainty, finite covariance estimation, source discrimination, multiplicity, and covariance-model mismatch be quantified before a source-space result is treated as reliable evidence?

These are analytic and fixed-seed synthetic inference results. They are not human empirical data and they do not establish that consciousness or qualia have been directly measured.

---

## V36. Efficient scalar-amplitude inference with known covariance

Consider the Gaussian linear measurement model

\[
mathbf y
=
a\boldsymbol\ell
+
\boldsymbol\eta,
qquad
\boldsymbol\eta
sim
mathcal N(mathbf 0,mathbf C),
\]

where

- \(a\) is a scalar source amplitude;
- \(\boldsymbol\ell\) is a declared sensor topography;
- \(\mathbf C\) is a positive-definite sensor covariance.

The generalized least-squares estimator is

\[
\boxed{
widehat a
=
\frac{
\boldsymbol\ell^\top
mathbf C^{-1}
mathbf y
}{
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\ell
}
}.
\]

### Proposition V36-A. Unbiasedness

Substitute the data model:

\[
widehat a
=
\frac{
\boldsymbol\ell^\top
mathbf C^{-1}
(a\boldsymbol\ell+\boldsymbol\eta)
}{
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\ell
}.
\]

Therefore

\[
widehat a
=
a
+
\frac{
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\eta
}{
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\ell
}.
\]

Since

\[
mathbb E[\boldsymbol\eta]
=
mathbf 0,
\]

it follows that

\[
\boxed{
mathbb E[widehat a]=a
}.
\]

### Proposition V36-B. Exact variance

The random part is linear in the Gaussian noise. Its variance is

\[
operatorname{Var}(widehat a)
=
\frac{
\boldsymbol\ell^\top
mathbf C^{-1}
mathbf C
mathbf C^{-1}
\boldsymbol\ell
}{
(
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\ell
)^2
}.
\]

Hence

\[
\boxed{
operatorname{Var}(widehat a)
=
\frac{1}{
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\ell
}
}.
\]

The scalar-amplitude Fisher information is

\[
\boxed{
I(a)
=
\boldsymbol\ell^\top
mathbf C^{-1}
\boldsymbol\ell
}.
\]

Therefore

\[
operatorname{Var}(widehat a)
=
\frac{1}{I(a)}.
\]

The estimator attains the Cramer-Rao lower bound under the declared known-covariance Gaussian model.

### Canonical V36 construction

The deterministic topography and covariance are

\[
\boldsymbol\ell
=
(1, 0.5, -0.2)^\top
\]

and

\[
mathbf C
=
\begin{pmatrix}
1 & 0.3 & 0.1\\
0.3 & 0.8 & 0.2\\
0.1 & 0.2 & 0.6
end{pmatrix}.
\]

The exact information is

\[
I(a)
=
1.2766666667
\]

and the exact estimator variance is

\[
\boxed{
operatorname{Var}(widehat a)
=
0.7832898172
}.
\]

A fixed-seed simulation with true amplitude \(a=1.2\), seed (20260918), and 40,000 Gaussian trials gives

\[
overline{widehat a}
=
1.2090215517,
\]

\[
s_{widehat a}^2
=
0.7844758366,
\]

and empirical coverage of the known-variance 95 percent Gaussian interval

\[
0.947775.
\]

The simulation checks the finite Monte Carlo implementation against the exact analytic law. It does not replace the analytic proof.

---

## V37. Finite-sample inverse-covariance bias

Suppose an independent noise sample produces

\[
mathbf W
sim
operatorname{Wishart}_p(mathbf C,
u)
\]

with dimension \(p\) and degrees of freedom (
u), and define the sample covariance

\[
mathbf S
=
\frac{mathbf W}{
u}.
\]

For

\[

u>p+1,
\]

the inverse-Wishart expectation gives

\[
mathbb E[mathbf W^{-1}]
=
\frac{
mathbf C^{-1}
}{

u-p-1
}.
\]

Because

\[
mathbf S^{-1}
=

umathbf W^{-1},
\]

we obtain

\[
\boxed{
mathbb E[mathbf S^{-1}]
=
\frac{
u}{

u-p-1
}
mathbf C^{-1}
}.
\]

Define the inverse-covariance bias factor

\[
\boxed{
b_{mathrm{inv}}
=
\frac{
u}{

u-p-1
}.
}
\]

This factor is greater than one and approaches one as the noise sample grows.

### Canonical V37 construction

For

\[
p=4,
\]

the exact factors are

\[
\begin{array}{c|c}

u & b_{mathrm{inv}}\\
\hline
6 & 6\\
10 & 2\\
20 & 4/3\\
50 & 10/9
\end{array}
\]

The implication is precise:

> An inverse covariance estimated from a short independent noise record can be systematically too large in expectation even when the covariance estimator itself is unbiased.

This is a statistical measurement issue. It does not imply that any specific empirical covariance estimate has exactly the expectation above unless the Wishart assumptions are appropriate.

---

## V38. Exact Gaussian source-discrimination error

Consider two source hypotheses with equal priors and common covariance:

\[
H_1:
mathbf y
sim
mathcal N(
\boldsymbol\mu_1,
mathbf C
),
\]

\[
H_2:
mathbf y
sim
mathcal N(
\boldsymbol\mu_2,
mathbf C
).
\]

Define the squared Mahalanobis separation

\[
d^2
=
(
\boldsymbol\mu_1-\boldsymbol\mu_2
)^\top
mathbf C^{-1}
(
\boldsymbol\mu_1-\boldsymbol\mu_2
).
\]

Under equal priors and equal covariance, the optimal linear discriminant reduces the problem to one Gaussian coordinate whose means are separated by (d) standard deviations.

The Bayes error is therefore

\[
\boxed{
P_{mathrm{error}}
=
Phileft(-\frac{d}{2}\right)
=
\frac{1}{2}
operatorname{erfc}
left(
\frac{d}{
2sqrt 2
}
\right)
}.
\]

### Canonical V38 sweep

For

\[
d^2
=
0, 0.25, 1, 4, 9,
\]

the exact equal-prior Bayes errors are approximately

\[
0.5,
quad
0.4012936743,
quad
0.3085375387,
quad
0.1586552539,
quad
0.0668072013.
\]

The law converts covariance-aware topographic separation into an explicit best-case classification error under the declared Gaussian assumptions.

It does not state that a low source-discrimination error is evidence of consciousness. It states only that the two declared sensor distributions are statistically distinguishable under the model.

---

## V39. Exact family-wise error control for an independent multi-source search

Let

\[
Z_1,\ldots,Z_K
\]

be independent standard-normal null statistics.

For a two-sided threshold \(t\),

\[
P(|Z_k|\le t)
=
2\Phi(t)-1.
\]

The probability that all \(K\) null statistics remain inside the threshold is

\[
P\left(
\max_k |Z_k|
\le t
\right)
=
\left[
2\Phi(t)-1
\right]^K.
\]

Therefore the family-wise false-positive probability is

\[
\boxed{
\operatorname{FWER}(t,K)
=
1-
\left[
2\Phi(t)-1
\right]^K
}.
\]

To enforce target family-wise error \(\alpha\), solve

\[
1-
\left[
2\Phi(t)-1
\right]^K
=
\alpha.
\]

This gives

\[
2\Phi(t)-1
=
(1-\alpha)^{1/K}
\]

and therefore

\[
\boxed{
t_{\alpha,K}
=
\Phi^{-1}
\left(
\frac{
1+(1-\alpha)^{1/K}
}{
2
}
\right).
}
\]

### Canonical V39 thresholds

At

\[
\alpha=0.05,
\]

the exact independent-test thresholds are approximately

\[
\begin{array}{c|c}
K & t_{0.05,K}\\
hline
1 & 1.959963985\\
10 & 2.799625219\\
100 & 3.473978869\\
1000 & 4.049660550
end{array}
\]

Substitution into the exact FWER formula returns (0.05) to floating-point precision.

### Scope of the result

The formula above assumes independent null statistics. Real electromagnetic source searches are usually dependent because of spatial leakage, temporal correlation, inverse regularization, and preprocessing.

Therefore V39 is not proposed as a universal neuroimaging threshold. It is an exact baseline showing why uncorrected location-by-location thresholding cannot be interpreted as family-wise error control.

For dependent searches, an empirical maximum-statistic, random-field, permutation, or other dependence-aware correction should be justified prospectively.

---

## V40. Exact sandwich variance under covariance-model mismatch

Consider a weighted scalar-amplitude estimator

\[
widehat a_{mathbf W}
=
\frac{
\boldsymbol\ell^\top
mathbf W
mathbf y
}{
\boldsymbol\ell^\top
mathbf W
\boldsymbol\ell
},
\]

where

\[
mathbf W
\]

is a symmetric weighting matrix.

The true measurement covariance is

\[
mathbf C.
\]

The random part of the estimator is

\[
\frac{
\boldsymbol\ell^\top
mathbf W
\boldsymbol\eta
}{
\boldsymbol\ell^\top
mathbf W
\boldsymbol\ell
}.
\]

Therefore the exact variance is

\[
\boxed{
operatorname{Var}_{mathrm{true}}
(
widehat a_{mathbf W}
)
=
\frac{
\boldsymbol\ell^\top
mathbf W
mathbf C
mathbf W
\boldsymbol\ell
}{
(
\boldsymbol\ell^\top
mathbf W
\boldsymbol\ell
)^2
}.
}
\]

This is the scalar sandwich variance.

If the weighting matrix is treated as though it were the exact precision matrix, the reported nominal variance would be

\[
\boxed{
operatorname{Var}_{mathrm{nom}}
=
\frac{
1
}{
\boldsymbol\ell^\top
mathbf W
\boldsymbol\ell
}.
}
\]

These are equal when

\[
mathbf W
=
mathbf C^{-1}.
\]

They need not be equal when the covariance model is wrong.

### Canonical V40 construction

For the declared topography and true covariance, three weighting rules give:

\[
\begin{array}{c|c|c|c}
\text{weight model}
&
\text{exact variance}
&
\text{nominal variance}
&
\text{exact/nominal}
\\
hline
\text{oracle precision}
&
0.8779761905
&
0.8779761905
&
1
\\
\text{identity weight}
&
1.06496
&
0.8
&
1.3312
\\
\text{diagonal precision}
&
1.0452329580
&
0.7858546169
&
1.3300589391
end{array}
\]

The oracle weighting is calibrated exactly.

The two misspecified weighting rules understate variance by about 33 percent in this construction.

This result separates two questions that should not be conflated:

1. Does the estimator produce a value?
2. Is the uncertainty attached to that value calibrated under the true covariance?

A source estimate can be numerically stable yet still have a miscalibrated standard error.

---

## Combined inference chain

V36-V40 create a finite-sample inference chain:

\[
\text{efficient estimator}
\rightarrow
\text{finite covariance estimation}
\rightarrow
\text{source discrimination}
\rightarrow
\text{multiple-search control}
\rightarrow
\text{covariance-mismatch calibration}.
\]

The chain makes several distinctions explicit:

\[
\text{point estimate}

eq
\text{calibrated uncertainty},
\]

\[
\text{unbiased sample covariance}

eq
\text{unbiased inverse covariance},
\]

\[
\text{source separation}

eq
\text{zero classification error},
\]

\[
\text{single-test significance}

eq
\text{search-wide significance},
\]

and

\[
\text{nominal precision}

eq
\text{true estimator precision}.
\]

None of these quantities is a consciousness metric by itself.

---

## What V36-V40 establish

Inside the declared analytic and fixed-seed synthetic constructions:

1. the scalar-amplitude GLS estimator is unbiased under the declared Gaussian linear model;
2. its exact variance equals the reciprocal Fisher information and attains the CRLB when covariance is known;
3. the fixed-seed V36 simulation reproduces the analytic variance and approximately reproduces nominal 95 percent coverage;
4. inverse sample covariance has the exact Wishart expectation multiplier (
u/(
u-p-1)) when the declared Wishart assumptions hold;
5. equal-prior common-covariance Gaussian source discrimination has exact Bayes error (Phi(-d/2));
6. independent two-sided multi-source search has exact FWER (1-[2Phi(t)-1]^K);
7. the exact independent-search threshold for target FWER (alpha) is
\[
   Phi^{-1}
   left(
   \frac{
   1+(1-alpha)^{1/K}
   }{2}
   \right);
\]
8. covariance-model mismatch has an exact sandwich variance that can differ materially from nominal inverse-noise uncertainty.

## What V36-V40 do not establish

They do not establish:

- that Gaussian noise is an adequate model for every EEG, MEG, or OPM-MEG experiment;
- that Wishart covariance sampling holds after arbitrary preprocessing or temporal dependence;
- that independent-search FWER formulas are valid for dependent source maps;
- that a low Bayes source-discrimination error is a consciousness classifier;
- that a nominal 95 percent interval has 95 percent coverage when covariance, forward model, inverse regularization, or selection steps are estimated from the same data without accounting for that estimation;
- that synthetic coverage replaces human, clinical, animal, organoid, or artificial-system calibration;
- that any electromagnetic estimator directly measures consciousness or qualia.

---

## Prospective empirical controls

For a future electromagnetic source-inference study, preregister or report as applicable:

- the estimator and its exact weighting convention;
- whether sensor covariance is known, externally estimated, cross-fitted, regularized, or estimated on the same data;
- the number of independent or effective covariance samples;
- uncertainty intervals and the assumptions supporting their coverage;
- calibration checks using held-out or simulated data matched to the acquisition pipeline;
- source-pair discrimination targets and covariance-aware separations;
- the search family used for source, time, frequency, state, and preprocessing comparisons;
- the multiplicity correction and its dependence assumptions;
- maximum-statistic or dependence-aware correction when independent-test formulas are not justified;
- nominal and sandwich uncertainty under plausible covariance-model perturbations;
- sensitivity to forward-model, inverse-regularization, nuisance, and preprocessing choices.

A claim should be weakened when reported uncertainty is not calibrated, covariance estimation is too short or unstable for the precision operation being used, source discrimination remains poor, multiplicity is ignored, or plausible covariance mismatch materially changes the uncertainty.

---

## Literature anchors

- Gross J et al. *Good practice for conducting and reporting MEG research*. NeuroImage. 2013;65:349-363. doi:10.1016/j.neuroimage.2012.10.001. The reporting guidance emphasizes explicit noise treatment, statistical procedures, multiple-comparison control, and reproducibility.
- Brookes MJ et al. *Beamformer reconstruction of correlated sources using a modified source model*. NeuroImage. 2007;34(4):1454-1465. Source reconstruction quality depends on the source and covariance structure assumed by the inverse procedure.
- Nichols TE, Holmes AP. *Nonparametric permutation tests for functional neuroimaging: a primer with examples*. Human Brain Mapping. 2002;15(1):1-25. Maximum-statistic permutation procedures provide family-wise error control without requiring independent voxel or source tests.

These references anchor the measurement and statistical concepts. They do not imply that the present V36-V40 synthetic validations are empirical evidence about consciousness.

---

## Reproducibility

Source:

- `src/consciousness_measurement/electromagnetic_finite_sample.py`
- `src/consciousness_measurement/electromagnetic_finite_sample_simulations.py`

Tests:

- `tests/test_electromagnetic_finite_sample.py`
- `tests/test_electromagnetic_finite_sample_simulations.py`

Runner:

```bash
python scripts/run_electromagnetic_finite_sample_validation.py
```

Machine-readable outputs:

- `results/v36_gls_amplitude_efficiency.csv`
- `results/v37_inverse_covariance_bias.csv`
- `results/v38_gaussian_source_discrimination.csv`
- `results/v39_independent_search_fwer.csv`
- `results/v40_covariance_mismatch_sandwich.csv`
- `results/electromagnetic_finite_sample_validation_summary.json`

Canonical figure:

![Finite-sample electromagnetic inference validation V36-V40](figures/v36_v40_electromagnetic_finite_sample_validation.svg)

V36-V40 remain analytic or fixed-seed synthetic inference results. They are not human empirical data and they are not human empirical evidence that consciousness has been measured.
