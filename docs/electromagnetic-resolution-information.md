# Electromagnetic Resolution and Information Limits

## Research III V26-V30

V21-V25 established that source reconstruction depends on forward geometry, null spaces, modality, regularization, reference handling, and model perturbation. V26-V30 add a second measurement-theory layer: correlated noise geometry, finite inverse resolution, information bounds, temporal sampling ambiguity, and worst-case inverse noise amplification.

The central model remains

\[
\mathbf y = \mathbf L\mathbf j + \boldsymbol\eta,
\]

where \(\mathbf y\) is a sensor measurement, \(\mathbf L\) is the forward or lead-field operator, \(\mathbf j\) is a candidate source vector, and \(\boldsymbol\eta\) represents noise or mismatch.

These stages ask a narrower question than a consciousness theory:

> Given a declared electromagnetic measurement model, what information is recoverable in principle, what information is lost, and which numerical effects can create false confidence?

The results are analytic or deterministic synthetic measurement results. They are not human empirical evidence that consciousness has been measured.

---

## V26. Correlated sensor noise and whitening

When sensor noise has covariance \(\mathbf C\), ordinary Euclidean residual energy does not represent the likelihood geometry unless \(\mathbf C\) is proportional to the identity.

For residual

\[
\mathbf r = \mathbf y - \mathbf L\mathbf j,
\]

the covariance-weighted residual energy is

\[
Q(\mathbf r)
=
\mathbf r^\top \mathbf C^{-1}\mathbf r.
\]

Let

\[
\mathbf W = \mathbf C^{-1/2}
\]

be the symmetric inverse square root. Since

\[
\mathbf W^\top\mathbf W = \mathbf C^{-1},
\]

we obtain the exact identity

\[
\boxed{
\mathbf r^\top\mathbf C^{-1}\mathbf r
=
\|\mathbf C^{-1/2}\mathbf r\|_2^2
}.
\]

### Canonical result

The deterministic V26 construction gives

\[
Q = 0.027382585751978907
\]

and

\[
\|\mathbf C^{-1/2}\mathbf r\|_2^2
=
0.027382585751978935,
\]

with an absolute difference of approximately

\[
2.78\times10^{-17}.
\]

The difference is floating-point roundoff.

### Measurement consequence

Noise covariance is part of the measurement model. Correlated sensor noise can change the effective geometry of fit, detection, and source estimation even when raw channel amplitudes are unchanged.

Whitening does not create information. It expresses the same covariance-weighted geometry in Euclidean coordinates.

---

## V27. Resolution matrix, source leakage, and a rank barrier

For a linear inverse operator \(\mathbf G\),

\[
\widehat{\mathbf j}=\mathbf G\mathbf y.
\]

Under noiseless data \(\mathbf y=\mathbf L\mathbf j\),

\[
\widehat{\mathbf j}
=
\mathbf G\mathbf L\mathbf j.
\]

Define the inverse resolution matrix

\[
\boxed{
\mathbf R = \mathbf G\mathbf L
}.
\]

Then

\[
\widehat{\mathbf j}=\mathbf R\mathbf j.
\]

Ideal identity resolution would require

\[
\mathbf R=\mathbf I.
\]

For the Tikhonov inverse used in the canonical validation,

\[
\mathbf G_\lambda
=
(\mathbf L^\top\mathbf L+\lambda\mathbf I)^{-1}\mathbf L^\top,
\]

so

\[
\mathbf R_\lambda
=
(\mathbf L^\top\mathbf L+\lambda\mathbf I)^{-1}
\mathbf L^\top\mathbf L.
\]

The repository records two direct diagnostics:

\[
E_I
=
\frac{\|\mathbf R-\mathbf I\|_F}{\sqrt n}
\]

and

\[
F_{\mathrm{off}}
=
\frac{
\|\mathbf R-\operatorname{diag}(\mathbf R)\|_F^2
}{
\|\mathbf R\|_F^2
}.
\]

The second quantity records off-diagonal resolution energy, a direct form of source leakage or cross-talk in this construction.

### Proposition V27-A. Underdetermined linear inverses cannot have identity resolution

If \(\mathbf L\in\mathbb R^{m\times n}\) with \(m<n\), then for every linear inverse operator \(\mathbf G\),

\[
\operatorname{rank}(\mathbf R)
=
\operatorname{rank}(\mathbf G\mathbf L)
\le
\operatorname{rank}(\mathbf L)
\le m<n.
\]

But

\[
\operatorname{rank}(\mathbf I_n)=n.
\]

Therefore

\[
\boxed{
\mathbf R\neq\mathbf I_n
}.
\]

This conclusion does not depend on which linear inverse method is chosen.

### Proposition V27-B. Rank-only lower bound on normalized identity error

Let \(r=\operatorname{rank}(\mathbf R)\). The best rank-\(r\) approximation to \(\mathbf I_n\) in Frobenius norm leaves \(n-r\) unit singular values unresolved. Therefore

\[
\|\mathbf R-\mathbf I_n\|_F
\ge
\sqrt{n-r},
\]

and hence

\[
\boxed{
E_I
\ge
\sqrt{\frac{n-r}{n}}
}.
\]

For the canonical V27 system,

\[
n=6,
\qquad
r\le3,
\]

which gives

\[
E_I
\ge
\sqrt{\frac{3}{6}}
=
\frac{1}{\sqrt2}
\approx
0.7071067812.
\]

The smallest-regularization V27 result is

\[
E_I
=
0.7071067916,
\]

which lies extremely close to this rank-only lower bound.

### Canonical regularization path

Across \(\lambda\in\{10^{-4},10^{-2},10^{-1},1\}\), the identity error rises from approximately 0.707107 to 0.809089, while the off-diagonal leakage fraction remains near 0.49 to 0.50.

The scientific point is not that one regularization value is universally correct. The point is that a low sensor residual does not imply identity source resolution, and rank alone can impose a nonzero error floor before noise or modeling error is considered.

---

## V28. Fisher information and the Cramer-Rao lower bound

Consider a scalar source amplitude \(a\) with known sensor topography \(\boldsymbol\ell\),

\[
\mathbf y
\sim
\mathcal N(
a\boldsymbol\ell,
\mathbf C
).
\]

The log likelihood, up to constants independent of \(a\), is

\[
\log p(\mathbf y\mid a)
=
-\frac12
(\mathbf y-a\boldsymbol\ell)^\top
\mathbf C^{-1}
(\mathbf y-a\boldsymbol\ell).
\]

Differentiating with respect to \(a\),

\[
\frac{\partial}{\partial a}
\log p(\mathbf y\mid a)
=
\boldsymbol\ell^\top
\mathbf C^{-1}
(\mathbf y-a\boldsymbol\ell).
\]

The scalar Fisher information is therefore

\[
\boxed{
\mathcal I(a)
=
\boldsymbol\ell^\top
\mathbf C^{-1}
\boldsymbol\ell
}.
\]

For any unbiased estimator satisfying the usual regularity conditions,

\[
\boxed{
\operatorname{Var}(\widehat a)
\ge
\frac{1}{\mathcal I(a)}
}.
\]

### Closed form for the canonical common-noise model

For \(p\) sensors, let

\[
\boldsymbol\ell=\mathbf 1
\]

and

\[
\mathbf C
=
(1-\rho)\mathbf I
+
\rho\mathbf 1\mathbf 1^\top.
\]

The common direction \(\mathbf 1\) is an eigenvector of \(\mathbf C\) with eigenvalue

\[
1+(p-1)\rho.
\]

Hence

\[
\boxed{
\mathcal I
=
\frac{p}{1+(p-1)\rho}
}
\]

and

\[
\boxed{
\operatorname{CRLB}
=
\frac{1+(p-1)\rho}{p}
}.
\]

For \(p=4\), the canonical sweep gives:

| Common-noise correlation \(\rho\) | Fisher information | CRLB variance |
|---:|---:|---:|
| 0.0 | 4.000000 | 0.250000 |
| 0.3 | 2.105263 | 0.475000 |
| 0.6 | 1.428571 | 0.700000 |
| 0.9 | 1.081081 | 0.925000 |

As correlated noise increases along the measured topography, information about the common amplitude decreases and the best possible unbiased variance bound rises.

This is a fundamental information statement for the declared Gaussian model, not an algorithm comparison.

---

## V29. Temporal aliasing as exact non-identifiability after sampling

Let a real cosine be sampled at rate \(f_s\):

\[
x_f[n]
=
\cos\left(
2\pi f\frac{n}{f_s}
\right).
\]

Now consider the distinct continuous frequency

\[
f'=f_s-f.
\]

At integer sample index \(n\),

\[
\begin{aligned}
x_{f'}[n]
&=
\cos\left(
2\pi(f_s-f)\frac{n}{f_s}
\right)\\
&=
\cos\left(
2\pi n
-
2\pi f\frac{n}{f_s}
\right)\\
&=
\cos\left(
2\pi f\frac{n}{f_s}
\right)\\
&=
x_f[n].
\end{aligned}
\]

Therefore

\[
\boxed{
x_f[n]=x_{f_s-f}[n]
}
\]

for every integer sample index.

### Canonical result

With

\[
f_s=100\text{ Hz},
\qquad
f=17\text{ Hz},
\qquad
f'=83\text{ Hz},
\]

the maximum difference across 200 samples is approximately

\[
1.39\times10^{-13},
\]

again consistent with floating-point roundoff.

### Measurement consequence

A digital record cannot by itself distinguish all continuous-time signals that map to the same sample sequence. Anti-alias filtering, acquisition bandwidth, and sampling assumptions are therefore part of the measurement claim, not implementation details.

---

## V30. Worst-case inverse noise amplification

Let the sensor perturbation be \(\boldsymbol\eta\). For a pseudoinverse reconstruction,

\[
\Delta\widehat{\mathbf j}
=
\mathbf L^+\boldsymbol\eta.
\]

The induced operator norm gives

\[
\boxed{
\|\Delta\widehat{\mathbf j}\|_2
\le
\|\mathbf L^+\|_2
\|\boldsymbol\eta\|_2
}.
\]

If the nonzero singular values of \(\mathbf L\) are

\[
\sigma_1\ge\cdots\ge\sigma_r>0,
\]

then

\[
\boxed{
\|\mathbf L^+\|_2
=
\frac{1}{\sigma_r}
}.
\]

For full-rank square operators this is

\[
\frac{1}{\sigma_{\min}(\mathbf L)}.
\]

### Worst-case equality

Let \(\mathbf u_r\) be the left singular vector associated with \(\sigma_r\). Choosing

\[
\boldsymbol\eta
=
c\mathbf u_r
\]

gives

\[
\mathbf L^+\boldsymbol\eta
=
\frac{c}{\sigma_r}\mathbf v_r,
\]

so

\[
\frac{
\|\mathbf L^+\boldsymbol\eta\|_2
}{
\|\boldsymbol\eta\|_2
}
=
\frac{1}{\sigma_r}
=
\|\mathbf L^+\|_2.
\]

Thus the spectral bound is attainable.

### Canonical result

The deterministic V30 diagonal construction aligns noise with the weakest singular direction.

| Smallest singular value | \(\|\mathbf L^+\|_2\) | Realized amplification |
|---:|---:|---:|
| 1.00 | 1.0000 | 1.0000 |
| 0.30 | 3.3333 | 3.3333 |
| 0.10 | 10.0000 | 10.0000 |
| 0.03 | 33.3333 | 33.3333 |
| 0.01 | 100.0000 | 100.0000 |

The construction reaches the worst-case bound in every row.

### Measurement consequence

Small singular values create directions in which small sensor perturbations can produce large source-space errors. A numerically precise source image can therefore be physically fragile if the inverse problem is poorly conditioned.

---

## Combined interpretation

V26-V30 establish a connected measurement chain:

\[
\text{noise covariance}
\rightarrow
\text{effective sensor geometry}
\rightarrow
\text{inverse resolution}
\rightarrow
\text{information limit}
\rightarrow
\text{sampling ambiguity}
\rightarrow
\text{noise amplification}.
\]

The chain matters because every later interpretation inherits the limitations of the earlier measurement layers.

For a consciousness-related electromagnetic study, at least four distinctions must remain explicit:

\[
\text{physical field or voltage}
\neq
\text{sampled digital record}
\neq
\text{reconstructed source}
\neq
\text{experiential target}.
\]

No result in V26-V30 collapses those distinctions.

---

## What V26-V30 establish

Inside the declared analytic and deterministic synthetic constructions:

1. covariance whitening exactly preserves Mahalanobis residual energy;
2. an underdetermined linear inverse has an unavoidable nonzero resolution error floor;
3. off-diagonal resolution energy makes source leakage visible;
4. correlated sensor noise can lower Fisher information for a target amplitude;
5. distinct continuous frequencies can become exactly indistinguishable after sampling;
6. inverse noise amplification is controlled by the pseudoinverse norm and can attain the singular-value bound.

## What V26-V30 do not establish

They do not establish:

- that EEG, MEG, OPM-MEG, or another electromagnetic modality directly measures consciousness;
- that a reconstructed source is uniquely true;
- that a low residual establishes physiological correctness;
- that source leakage has been eliminated because one inverse method produces a focal map;
- that a Cramer-Rao bound is achieved by a practical estimator;
- that a synthetic covariance model represents every biological noise process;
- that an electromagnetic organization variable is identical to qualia or phenomenal content;
- that analytic or synthetic validation substitutes for preregistered human experiments.

---

## Prospective empirical controls

A future empirical electromagnetic study that relies on source-space structure should report, as applicable:

- sensor noise covariance and how it was estimated;
- whether whitening was applied and from which data partition;
- forward operator rank and singular spectrum;
- inverse operator and regularization rule;
- resolution matrix diagnostics;
- point-spread and cross-talk functions when a linear inverse is used;
- sensor-space and source-space results side by side;
- sampling rate, hardware filters, digital filters, and anti-alias assumptions;
- sensitivity to plausible covariance, head-model, registration, conductivity, and source-orientation perturbations;
- source stability under alternative justified inverse priors;
- held-out participant, session, state, site, and hardware validation where feasible.

A consciousness-related interpretation should be weakened when its apparent effect disappears under a predeclared measurement, resolution, sampling, or conditioning control.

---

## Literature anchors

- Hauk O, Stenroos M, Treder MS. *Towards an objective evaluation of EEG/MEG source estimation methods - The linear approach*. NeuroImage. 2022;255:119177. doi:10.1016/j.neuroimage.2022.119177. Develops resolution-matrix analysis with point-spread and cross-talk functions for linear EEG/MEG source estimation.
- Gross J et al. *Good practice for conducting and reporting MEG research*. NeuroImage. 2013;65:349-363. doi:10.1016/j.neuroimage.2012.10.001. Recommends explicit treatment and reporting of forward models, inverse methods, noise, and spatial-resolution limitations.
- Radich BM, Buckley KM. *EEG dipole localization bounds and MAP algorithms for head models with parameter uncertainties*. IEEE Transactions on Biomedical Engineering. 1995;42(3):233-241. doi:10.1109/10.364509. Derives Cramer-Rao localization bounds under measurement noise and head-model uncertainty.
- Grech R et al. *Review on solving the inverse problem in EEG source analysis*. Journal of NeuroEngineering and Rehabilitation. 2008;5:25. doi:10.1186/1743-0003-5-25. Reviews EEG inverse methods and the role of model assumptions, noise, and head-model error.

These references support the measurement framework. They do not imply that the present synthetic validations are human evidence about consciousness.

---

## Reproducibility

Source:

- `src/consciousness_measurement/electromagnetic_resolution.py`
- `src/consciousness_measurement/electromagnetic_resolution_simulations.py`

Tests:

- `tests/test_electromagnetic_resolution.py`
- `tests/test_electromagnetic_resolution_simulations.py`

Runner:

```bash
python scripts/run_electromagnetic_resolution_validation.py
```

Machine-readable outputs:

- `results/v26_correlated_noise_whitening.csv`
- `results/v27_resolution_leakage.csv`
- `results/v28_fisher_information.csv`
- `results/v29_temporal_aliasing.csv`
- `results/v30_inverse_noise_amplification.csv`
- `results/electromagnetic_resolution_validation_summary.json`

Canonical figure:

![Electromagnetic resolution and information limits V26-V30](figures/v26_v30_electromagnetic_resolution_validation.svg)

All current V26-V30 results are analytic or deterministic synthetic measurement results. They are not human empirical data and they are not human empirical evidence that consciousness has been measured.
