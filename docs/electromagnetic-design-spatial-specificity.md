# Electromagnetic Design and Spatial Specificity Program

## Research III V31-V35

V16-V30 established sensor-level electromagnetic observables, forward and inverse source limits, covariance-aware residual geometry, inverse resolution, Fisher information, temporal aliasing, and singular-direction noise amplification.

V31-V35 add a measurement-design layer:

> Given a declared electromagnetic forward and inverse model, how should spatial specificity, source distinguishability, sensor design, nuisance rejection, and forward-model uncertainty be quantified before any source-space pattern is given an experiential interpretation?

These results are analytic or deterministic synthetic measurement-design results. They are not human empirical data, and they do not establish that consciousness or qualia have been directly measured.

---

## V31. Point-spread and cross-talk functions

For a linear forward operator \(\mathbf L\) and a linear inverse operator \(\mathbf G\),

\[
\widehat{\mathbf j}
=
\mathbf G\mathbf y,
\qquad
\mathbf y
=
\mathbf L\mathbf j+\boldsymbol\eta.
\]

Ignoring noise for the resolution calculation,

\[
\widehat{\mathbf j}
=
\mathbf G\mathbf L\mathbf j.
\]

Define the linear inverse resolution matrix

\[
\boxed{
\mathbf R=\mathbf G\mathbf L
}.
\]

Let \(\mathbf e_k\) denote the \(k\)-th source basis vector.

### Point-spread function

For a unit source at location \(k\),

\[
\mathbf j=\mathbf e_k,
\]

the reconstructed source is

\[
\widehat{\mathbf j}
=
\mathbf R\mathbf e_k.
\]

Therefore the point-spread function is the \(k\)-th column of the resolution matrix:

\[
\boxed{
\operatorname{PSF}_k
=
\mathbf R_{:,k}
}.
\]

It answers the question:

> If source \(k\) alone is active, where does the inverse method spread that source?

### Cross-talk function

The \(i\)-th reconstructed coefficient is

\[
\widehat j_i
=
\mathbf e_i^\top\mathbf R\mathbf j.
\]

Therefore the cross-talk function for reconstructed coefficient \(i\) is the \(i\)-th row of the resolution matrix:

\[
\boxed{
\operatorname{CTF}_i^\top
=
\mathbf R_{i,:}
}.
\]

It answers:

> Which true source locations can leak into reconstructed coefficient \(i\)?

PSF and CTF are different objects in general. A visually focal map does not by itself imply low cross-talk.

### Canonical V31 result

For source index 1, the deterministic construction gives

\[
\operatorname{PSF}_1
=
(0.1,\ 0.7,\ 0.1,\ 0)^\top
\]

and

\[
\operatorname{CTF}_1
=
(0.2,\ 0.7,\ 0.2,\ 0).
\]

After removing the target component, the leakage norms are

\[
\|\operatorname{PSF}_{1,\mathrm{off}}\|_2
=
0.1414213562
\]

and

\[
\|\operatorname{CTF}_{1,\mathrm{off}}\|_2
=
0.2828427125.
\]

The construction deliberately separates spread from cross-talk so that a single generic "resolution" number cannot hide their different meanings.

---

## V32. Noise-aware source distinguishability

Suppose two candidate sources predict sensor topographies

\[
\boldsymbol\ell_1
\quad\text{and}\quad
\boldsymbol\ell_2
\]

under positive-definite sensor covariance \(\mathbf C\).

Their covariance-aware squared separation is

\[
\boxed{
d_C^2
=
(\boldsymbol\ell_1-\boldsymbol\ell_2)^\top
\mathbf C^{-1}
(\boldsymbol\ell_1-\boldsymbol\ell_2)
}.
\]

Let

\[
\mathbf W=\mathbf C^{-1/2}.
\]

Then

\[
d_C^2
=
\|
\mathbf W(\boldsymbol\ell_1-\boldsymbol\ell_2)
\|_2^2.
\]

Thus distinguishability is Euclidean separation after whitening, not raw sensor-space separation before noise geometry is accounted for.

### Gaussian interpretation

For two Gaussian sensor models with equal covariance,

\[
\mathbf y\mid H_1
\sim
\mathcal N(\boldsymbol\ell_1,\mathbf C),
\qquad
\mathbf y\mid H_2
\sim
\mathcal N(\boldsymbol\ell_2,\mathbf C),
\]

the log-likelihood-ratio geometry is governed by the same whitened topography difference.

V32 treats \(d_C^2\) as a measurement distinguishability quantity, not as a consciousness distance.

### Canonical V32 result

The declared correlated-noise construction gives

\[
d_{\mathrm{close}}^2
=
0.0032293578,
\]

while the distinct comparison gives

\[
d_{\mathrm{distinct}}^2
=
2.3394495413.
\]

The distinct topography is more than two orders of magnitude farther from the reference in squared Mahalanobis distance than the close topography.

---

## V33. Sensor design through Fisher-information geometry

Let a local linear measurement model depend on

\[
\boldsymbol\theta\in\mathbb R^p
\]

with sensitivity matrix

\[
\mathbf A
=
\frac{\partial\boldsymbol\mu}{\partial\boldsymbol\theta}
\]

and Gaussian sensor covariance \(\mathbf C\).

The Fisher information matrix is

\[
\boxed{
\mathbf F
=
\mathbf A^\top
\mathbf C^{-1}
\mathbf A
}.
\]

Two standard design summaries are used.

### D-optimal information

\[
\boxed{
D
=
\log\det\mathbf F
}
\]

when \(\mathbf F\) is positive definite.

This measures local information volume in parameter space.

### E-optimal information

\[
\boxed{
E
=
\lambda_{\min}(\mathbf F)
}.
\]

This measures the weakest locally informed parameter direction.

### Canonical counterexample: equal sensor count does not imply equal information

The redundant three-sensor design is

\[
\mathbf A_R
=
\begin{pmatrix}
1 & 0\\
1 & 0.02\\
1 & -0.02
\end{pmatrix}.
\]

With identity covariance,

\[
\mathbf F_R
=
\begin{pmatrix}
3 & 0\\
0 & 0.0008
\end{pmatrix},
\]

so

\[
\det\mathbf F_R=0.0024,
\qquad
\lambda_{\min}(\mathbf F_R)=0.0008.
\]

The complementary three-sensor design is

\[
\mathbf A_C
=
\begin{pmatrix}
1 & 0\\
0 & 1\\
1/\sqrt 2 & 1/\sqrt 2
\end{pmatrix},
\]

which gives

\[
\mathbf F_C
=
\begin{pmatrix}
1.5 & 0.5\\
0.5 & 1.5
\end{pmatrix}.
\]

Hence

\[
\det\mathbf F_C=2
\]

and

\[
\lambda_{\min}(\mathbf F_C)=1.
\]

The traces are nearly equal:

\[
\operatorname{tr}(\mathbf F_R)=3.0008,
\qquad
\operatorname{tr}(\mathbf F_C)=3.
\]

Yet their weakest-direction information differs by a factor of

\[
\frac{1}{0.0008}=1250.
\]

Sensor count and total sensitivity do not determine identifiability. Directional complementarity matters.

---

## V34. Nuisance-subspace information loss

Work in whitened sensor coordinates. Let

\[
\mathbf s
\]

be the whitened target topography and let the columns of

\[
\mathbf N
\]

span a nuisance subspace.

The orthogonal projector onto the nuisance subspace is

\[
\mathbf P_N
=
\mathbf N\mathbf N^+,
\]

where \(\mathbf N^+\) is the Moore-Penrose pseudoinverse.

The projector onto its orthogonal complement is

\[
\boxed{
\mathbf P_\perp
=
\mathbf I-\mathbf N\mathbf N^+
}.
\]

After exact nuisance projection, the retained target information is

\[
\boxed{
I_{\mathrm{ret}}
=
\|\mathbf P_\perp\mathbf s\|_2^2
}.
\]

The retained fraction is

\[
\boxed{
\rho_{\mathrm{ret}}
=
\frac{
\|\mathbf P_\perp\mathbf s\|_2^2
}{
\|\mathbf s\|_2^2
}
}.
\]

### Proposition V34-A. Exact one-dimensional nuisance law

Assume \(\mathbf s\) and a unit nuisance vector \(\mathbf n\) form angle \(\theta\). Then

\[
\mathbf P_\perp
=
\mathbf I-\mathbf n\mathbf n^\top.
\]

Since

\[
\mathbf n^\top\mathbf s
=
\|\mathbf s\|_2\cos\theta,
\]

Pythagorean decomposition gives

\[
\|\mathbf P_\perp\mathbf s\|_2^2
=
\|\mathbf s\|_2^2
-
(\mathbf n^\top\mathbf s)^2.
\]

Therefore

\[
\boxed{
\rho_{\mathrm{ret}}
=
1-\cos^2\theta
=
\sin^2\theta
}.
\]

This is an exact information-loss law for the declared one-target, one-nuisance construction.

If

\[
\theta=0,
\]

then target and nuisance are aligned and

\[
\rho_{\mathrm{ret}}=0.
\]

Perfect nuisance rejection removes the target direction completely.

If

\[
\theta=\frac{\pi}{2},
\]

then target and nuisance are orthogonal and

\[
\rho_{\mathrm{ret}}=1.
\]

No target information is lost.

The canonical sweep at 0, 15, 30, 45, 60, and 90 degrees matches \(\sin^2\theta\) to floating-point precision.

---

## V35. Robust information under bounded forward-model uncertainty

Again work in whitened coordinates. Let the nominal target topography be

\[
\mathbf w
\]

and let model uncertainty permit an additive perturbation

\[
\boldsymbol\delta
\]

inside the Euclidean ball

\[
\|\boldsymbol\delta\|_2\le\epsilon.
\]

For a scalar amplitude in identity-covariance whitened coordinates, Fisher information is

\[
I
=
\|\mathbf w+\boldsymbol\delta\|_2^2.
\]

The robust lower bound is

\[
I_{\mathrm{rob}}(\epsilon)
=
\min_{\|\boldsymbol\delta\|_2\le\epsilon}
\|\mathbf w+\boldsymbol\delta\|_2^2.
\]

### Proposition V35-A. Exact robust information bound

By the reverse triangle inequality,

\[
\|\mathbf w+\boldsymbol\delta\|_2
\ge
\big|
\|\mathbf w\|_2-\|\boldsymbol\delta\|_2
\big|.
\]

Under

\[
\|\boldsymbol\delta\|_2\le\epsilon,
\]

we obtain

\[
\|\mathbf w+\boldsymbol\delta\|_2
\ge
\max(
\|\mathbf w\|_2-\epsilon,
0
).
\]

Squaring gives

\[
I_{\mathrm{rob}}(\epsilon)
\ge
\left[
\max(
\|\mathbf w\|_2-\epsilon,
0
)
\right]^2.
\]

The bound is attainable.

For

\[
0\le\epsilon\le\|\mathbf w\|_2,
\]

choose

\[
\boldsymbol\delta^\star
=
-\epsilon
\frac{\mathbf w}{\|\mathbf w\|_2}.
\]

Then

\[
\|\mathbf w+\boldsymbol\delta^\star\|_2
=
\|\mathbf w\|_2-\epsilon.
\]

If

\[
\epsilon\ge\|\mathbf w\|_2,
\]

choose

\[
\boldsymbol\delta^\star=-\mathbf w,
\]

which is feasible and gives zero information.

Therefore

\[
\boxed{
I_{\mathrm{rob}}(\epsilon)
=
\left[
\max(
\|\mathbf w\|_2-\epsilon,
0
)
\right]^2
}.
\]

### Canonical V35 result

For

\[
\mathbf w
=
(1,\ 0.5,\ -0.2)^\top,
\]

the nominal information is

\[
\|\mathbf w\|_2^2=1.29
\]

and

\[
\|\mathbf w\|_2
\approx
1.1357816692.
\]

The deterministic uncertainty sweep gives robust lower bounds

\[
1.29,\quad
0.8756873323,\quad
0.4042183308,\quad
0.0184366617,\quad
0
\]

for uncertainty radii

\[
0,\ 0.2,\ 0.5,\ 1.0,\ 1.2.
\]

The constructed anti-aligned perturbation attains the bound at every radius.

This is a worst-case measurement-information statement. It does not assert that the declared uncertainty radius is biologically correct for any specific experiment.

---

## Combined engineering interpretation

V31-V35 create a measurement-design chain:

\[
\text{inverse resolution}
\rightarrow
\text{PSF and CTF}
\rightarrow
\text{source distinguishability}
\rightarrow
\text{sensor information geometry}
\rightarrow
\text{nuisance information loss}
\rightarrow
\text{robust information under model uncertainty}.
\]

The chain makes several distinctions explicit:

\[
\text{sensor count}
\neq
\text{independent information},
\]

\[
\text{focal source map}
\neq
\text{high spatial specificity},
\]

\[
\text{nuisance removal}
\neq
\text{free information},
\]

and

\[
\text{nominal Fisher information}
\neq
\text{robust Fisher information}.
\]

None of these quantities is a consciousness measure by itself.

---

## What V31-V35 establish

Inside the declared analytic and deterministic synthetic constructions:

1. point-spread functions are columns of a linear resolution matrix;
2. cross-talk functions are rows of a linear resolution matrix;
3. covariance-aware sensor-topography distance quantifies noise-aware distinguishability;
4. Fisher-information geometry distinguishes redundant from complementary sensor designs;
5. one-dimensional nuisance projection retains exactly a \(\sin^2\theta\) fraction of whitened target information;
6. bounded whitened topography uncertainty has the exact robust information lower bound
   \[
   [\max(\|\mathbf w\|_2-\epsilon,0)]^2;
   \]
7. the declared anti-aligned perturbation attains that bound.

## What V31-V35 do not establish

They do not establish:

- that a point-spread function is an experiential point-spread function;
- that a cross-talk function measures mixing of conscious contents;
- that a larger Mahalanobis separation is a consciousness distance;
- that a D-optimal or E-optimal sensor design is automatically optimal for a consciousness target;
- that nuisance removal is valid without verifying the nuisance model;
- that a nominal forward-model uncertainty ball captures every biological or hardware error;
- that robust Fisher information identifies consciousness;
- that synthetic validation substitutes for human, clinical, animal, organoid, or artificial-system target calibration.

---

## Prospective empirical controls

For a future electromagnetic study using source-space or spatial-specificity claims, preregister or report as applicable:

- the forward operator and its uncertainty model;
- the inverse operator and regularization rule;
- the resolution matrix;
- point-spread and cross-talk functions for relevant source locations;
- the sensor covariance model and how it was estimated;
- source-pair distinguishability under that covariance;
- sensor or modality selection criteria;
- nuisance subspaces and the target information removed by nuisance projection;
- sensitivity to alternative plausible nuisance bases;
- nominal and robust information summaries under predeclared forward-model uncertainty;
- held-out subject, session, site, state, hardware, and analysis-pipeline validation where feasible.

A source-space claim should be weakened when spatial specificity collapses under PSF/CTF analysis, when candidate sources are not distinguishable under measured noise covariance, when nuisance removal destroys the target direction, or when plausible model uncertainty drives the robust information bound toward zero.

---

## Literature anchors

- Hauk O, Stenroos M, Treder MS. *Towards an objective evaluation of EEG/MEG source estimation methods - The linear approach*. NeuroImage. 2022;255:119177. doi:10.1016/j.neuroimage.2022.119177.
- Gross J et al. *Good practice for conducting and reporting MEG research*. NeuroImage. 2013;65:349-363. doi:10.1016/j.neuroimage.2012.10.001.
- Radich BM, Buckley KM. *EEG dipole localization bounds and MAP algorithms for head models with parameter uncertainties*. IEEE Transactions on Biomedical Engineering. 1995;42(3):233-241. doi:10.1109/10.364509.

These references anchor the measurement concepts. They do not imply that V31-V35 are empirical evidence about consciousness.

---

## Reproducibility

Source:

- src/consciousness_measurement/electromagnetic_design.py
- src/consciousness_measurement/electromagnetic_design_simulations.py

Tests:

- tests/test_electromagnetic_design.py
- tests/test_electromagnetic_design_simulations.py

Runner:

~~~bash
python scripts/run_electromagnetic_design_validation.py
~~~

Machine-readable outputs:

- results/v31_point_spread_cross_talk.csv
- results/v32_source_distinguishability.csv
- results/v33_sensor_design_information.csv
- results/v34_nuisance_information_loss.csv
- results/v35_robust_model_information.csv
- results/electromagnetic_design_validation_summary.json

Canonical figure:

![Electromagnetic design and spatial-specificity validation V31-V35](figures/v31_v35_electromagnetic_design_validation.svg)

All current V31-V35 results are analytic or deterministic synthetic measurement-design results. They are not human empirical data, and they are not human empirical evidence that consciousness has been measured.
