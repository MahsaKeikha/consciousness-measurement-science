# Electromagnetic Resolution and Information Program

## Research III V26-V30

V16-V20 established sensor-level electromagnetic measurement checks. V21-V25 then made the forward and inverse source-identifiability problem explicit.

V26-V30 ask the next engineering question:

> Even when the measurement and source model are declared, how much resolution and information are actually available, and how can acquisition noise, sampling, and weak singular directions limit the claim?

The program remains theory-neutral. None of these stages treats an electromagnetic statistic, source estimate, or information bound as consciousness itself.

---

## V26. Correlated-noise whitening

Let the sensor model be

[
mathbf y=mathbf Lmathbf j+oldsymboleta,
qquad
oldsymboletasim(0,oldsymbolSigma).
]

For residual

[
mathbf r=mathbf y-mathbf Lmathbf j,
]

the covariance-weighted residual energy is

[
Q
=
mathbf r^	opoldsymbolSigma^{-1}mathbf r.
]

If

[
mathbf W=oldsymbolSigma^{-1/2},
]

then

[
oxed{
Q
=
lVertmathbf Wmathbf rVert_2^2
}
]

because

[
mathbf W^	opmathbf W
=
oldsymbolSigma^{-1}.
]

### Canonical result

The deterministic construction gives

[
Q=0.027382585751978907
]

and

[
lVertmathbf Wmathbf rVert_2^2
=
0.027382585751978935,
]

with absolute identity error

[
2.78	imes10^{-17}.
]

### Interpretation

Residuals should be judged in the noise geometry actually present at the sensors. Treating strongly correlated noise as independent can distort both fit statistics and inverse weighting.

Whitening is not evidence for consciousness. It is a measurement correction.

---

## V27. Resolution matrix and source leakage

For the L2-regularized inverse

[
mathbf W_lambda
=
(mathbf L^	opmathbf L+lambdamathbf I)^{-1}mathbf L^	op,
]

the source-resolution matrix is

[
oxed{
mathbf R_lambda
=
mathbf W_lambdamathbf L
=
(mathbf L^	opmathbf L+lambdamathbf I)^{-1}
mathbf L^	opmathbf L.
}
]

If the true source is (mathbf j), the noise-free reconstruction is

[
widehat{mathbf j}
=
mathbf R_lambdamathbf j.
]

Perfect source resolution would require

[
mathbf R_lambda=mathbf I.
]

In an underdetermined or regularized inverse this generally fails.

Define the normalized identity error

[
E_R
=
rac{
lVertmathbf R_lambda-mathbf IVert_F
}{
sqrt{p}
}
]

for (p) source coordinates, and off-diagonal leakage fraction

[
Lambda_{mathrm{off}}
=
rac{
lVert
mathbf R_lambda-operatorname{diag}(mathbf R_lambda)
Vert_F^2
}{
lVertmathbf R_lambdaVert_F^2
}.
]

### Canonical result

Across

[
lambdain{10^{-4},10^{-2},10^{-1},1},
]

the declared six-source, three-sensor construction has

[
E_R approx 0.707	ext{ to }0.809
]

and

[
Lambda_{mathrm{off}}approx0.485	ext{ to }0.501.
]

### Result

A visually sharp inverse map should not be assumed to have perfect source resolution. The resolution matrix, point-spread behavior, and cross-talk belong in the interpretation.

---

## V28. Fisher information under correlated sensor noise

Consider a scalar source amplitude (a) with known sensor topography (oldsymbolell):

[
mathbf y
=
aoldsymbolell+oldsymboleta,
qquad
oldsymboletasimmathcal N(0,oldsymbolSigma).
]

The Fisher information for (a) is

[
oxed{
mathcal I(a)
=
oldsymbolell^	op
oldsymbolSigma^{-1}
oldsymbolell.
}
]

The Cramer-Rao lower bound is

[
oxed{
operatorname{Var}(widehat a)
ge
rac{1}{mathcal I(a)}.
}
]

For (m) sensors with common topography

[
oldsymbolell=mathbf 1
]

and equicorrelated covariance

[
oldsymbolSigma
=
(1-ho)mathbf I+homathbf 1mathbf 1^	op,
]

the inverse gives the closed-form law

[
oxed{
mathcal I(a)
=
rac{m}{1+(m-1)ho}
}
]

and therefore

[
oxed{
operatorname{CRLB}(a)
=
rac{1+(m-1)ho}{m}.
}
]

For the canonical (m=4) construction,

[
mathcal I(a)
=
rac{4}{1+3ho}.
]

### Canonical result

As common-noise correlation rises from (0) to (0.9),

[
mathcal I(a): 4.0ightarrow1.081081...
]

while

[
operatorname{CRLB}:0.25ightarrow0.925.
]

### Result

More sensors do not automatically mean proportionally more information when their noise is strongly shared.

---

## V29. Exact temporal aliasing counterexample

Sample a cosine at rate (f_s):

[
x_f[n]
=
cosleft(
2pirac{f}{f_s}n
ight).
]

Now consider frequency

[
f'=f_s-f.
]

Then

[
x_{f'}[n]
=
cosleft(
2pi n
-
2pirac{f}{f_s}n
ight)
=
x_f[n].
]

Therefore

[
oxed{
f
quad	ext{and}quad
f_s-f
	ext{ produce identical sampled cosine sequences.}
}
]

### Canonical result

With

[
f_s=100	ext{ Hz},
qquad
f=17	ext{ Hz},
qquad
f'=83	ext{ Hz},
]

the maximum numerical sample difference over 200 samples is

[
1.39	imes10^{-13}.
]

### Result

Continuous-time spectral structure is not identifiable from sampled data without an adequate anti-aliasing and sampling design.

This matters for electromagnetic consciousness studies because apparent frequency-specific structure is only meaningful inside a declared acquisition bandwidth and filtering pipeline.

---

## V30. Singular-direction inverse noise amplification

Let sensor noise perturb the measurement:

[
mathbf y'
=
mathbf y+oldsymboleta.
]

For the Moore-Penrose inverse,

[
deltawidehat{mathbf j}
=
mathbf L^+oldsymboleta.
]

Therefore

[
oxed{
lVert
deltawidehat{mathbf j}
Vert_2
le
lVertmathbf L^+Vert_2
lVertoldsymboletaVert_2.
}
]

If the smallest nonzero singular value of (mathbf L) is (sigma_{min}), then

[
oxed{
lVertmathbf L^+Vert_2
=
rac{1}{sigma_{min}}.
}
]

Noise aligned with the weakest left-singular direction reaches this bound.

### Canonical result

For diagonal operators with

[
sigma_{min}
in
{1,0.3,0.1,0.03,0.01},
]

the exact worst-direction amplification is

[
1,;
3.333...,;
10,;
33.333...,;
100.
]

### Result

A source-space effect can be numerically unstable even when the sensor perturbation is small. Condition and singular-spectrum reporting should therefore accompany source-space consciousness claims.

---

## Scientific interpretation

V26-V30 establish five narrow measurement-engineering results:

1. covariance whitening and weighted residual geometry are equivalent under the declared positive-definite covariance;
2. an underdetermined regularized inverse retains substantial resolution error and source leakage;
3. common correlated sensor noise reduces Fisher information for a common source topography;
4. inadequate temporal sampling creates exact spectral non-identifiability;
5. weak singular directions amplify sensor noise by the pseudoinverse norm.

Together with V16-V25, this creates a three-layer electromagnetic audit:

[
oxed{
	ext{sensor observables}
ightarrow
	ext{source identifiability}
ightarrow
	ext{resolution and information limits}.
}
]

## What V26-V30 do not establish

They do not establish:

- that high Fisher information means greater consciousness;
- that a well-resolved source is a conscious source;
- that whitening creates a consciousness-specific signal;
- that source leakage can be eliminated completely by one inverse method;
- that a frequency peak is meaningful without acquisition-bandwidth validation;
- that a stable inverse reconstruction is ontologically identical to experience.

---

## Empirical controls added by V26-V30

A mature EM study should additionally report:

- sensor-noise covariance estimation procedure;
- whitening or covariance weighting;
- covariance-estimation stability;
- inverse resolution matrix or equivalent point-spread/cross-talk diagnostics;
- singular-value or condition-spectrum diagnostics;
- anti-alias filters and acquisition sample rate;
- analysis bandwidth relative to Nyquist;
- source-space sensitivity to regularization;
- information or uncertainty changes under sensor deletion;
- held-out sensor prediction when source-space models are compared.

A consciousness-related source claim should be weakened if it depends on poorly estimated covariance, severe source leakage, alias-prone acquisition, or a weak singular direction that produces large inverse amplification.

---

## Literature anchors

- Grech R et al. *Review on solving the inverse problem in EEG source analysis*. Journal of NeuroEngineering and Rehabilitation. 2008;5:25. doi:10.1186/1743-0003-5-25. Reviews inverse methods, noise effects, regularization, and spatial-noise prewhitening.
- Hauk O, Stenroos M, Treder MS. *Towards an objective evaluation of EEG/MEG source estimation methods - The linear approach*. NeuroImage. 2022;255:119177. doi:10.1016/j.neuroimage.2022.119177. Develops resolution-matrix, point-spread, and cross-talk evaluation for linear M/EEG source methods.
- Jas M et al. *A reproducible MEG/EEG group study with the MNE software: recommendations, quality assessments, and good practices*. Frontiers in Neuroscience. 2018;12:530. Discusses noise-covariance estimation, whitening, and their effect on source localization.
- Gross J et al. *Good practice for conducting and reporting MEG research*. NeuroImage. 2013;65:349-363. doi:10.1016/j.neuroimage.2012.10.001. Motivates explicit acquisition, filtering, inverse-model, and uncertainty reporting.
- Standard sampled-signal theory gives the Nyquist criterion: analysis frequencies require an acquisition and anti-aliasing design that prevents higher-frequency content from folding into the measured band.

The literature motivates the measurement questions. The V26-V30 equations and deterministic constructions are the repository's own validation record.

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

Canonical records:

- `results/v26_correlated_noise_whitening.csv`
- `results/v27_resolution_leakage.csv`
- `results/v28_fisher_information.csv`
- `results/v29_temporal_aliasing.csv`
- `results/v30_inverse_noise_amplification.csv`
- `results/electromagnetic_resolution_validation_summary.json`

Canonical figure:

![V26-V30 electromagnetic resolution and information validation](figures/v26_v30_electromagnetic_resolution_validation.svg)

The V26-V30 record is deterministic analytic or synthetic validation. It is not human empirical consciousness evidence.
