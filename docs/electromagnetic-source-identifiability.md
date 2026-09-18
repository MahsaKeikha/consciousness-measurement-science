# Electromagnetic Source Identifiability Program

## Research III V21-V25

V16-V20 established a sensor-level electromagnetic measurement layer: physical field sanity checks, normalized organization descriptors, matched-power non-identifiability, common-mode confounding, and frequency-specific structure.

V21-V25 move one level deeper.

The central question is no longer only:

> What structure is present in the recorded electromagnetic signals?

It is also:

> What can those measurements identify about the underlying source distribution, and which conclusions depend on reference choice, forward-model geometry, regularization, modality, or model error?

The starting point is the standard linearized measurement form

\[
\mathbf y = \mathbf L\mathbf j + \boldsymbol\eta,
\]

where:

- \(\mathbf y\) is an EEG- or MEG-like sensor measurement;
- \(\mathbf j\) is a vector of candidate source amplitudes;
- \(\mathbf L\) is the lead-field or forward operator;
- \(\boldsymbol\eta\) contains measurement noise and model mismatch.

The program is deliberately theory-neutral. It does not assume that reconstructed neural current is consciousness, that an electromagnetic field is consciousness, or that a unique neural source can be inferred merely because one inverse algorithm returns one image.

## Why this layer matters

EEG and MEG source imaging require a forward model and an inverse method. The inverse problem is generally non-unique unless additional assumptions or priors are imposed. Head geometry, conductivity, sensor placement, source orientation, noise, regularization, and modality sensitivity all affect what can be reconstructed.

For Research III, that means an electromagnetic consciousness-measurement program must distinguish at least three objects:

\[
\text{sensor data}
\neq
\text{reconstructed source}
\neq
\text{experiential target}.
\]

A source estimate can be useful evidence while remaining model-dependent.

---

## V21. Common-reference invariance of pairwise EEG differences

Scalp electric potential is reference-dependent. If a common reference waveform \(r(t)\) is added to every sensor,

\[
x'_k(t)=x_k(t)+r(t),
\]

then individual channel values change.

But any pairwise difference satisfies

\[
x'_i(t)-x'_j(t)
=
x_i(t)-x_j(t).
\]

Equivalently, if \(\mathbf D\) is a difference operator satisfying

\[
\mathbf D\mathbf 1=0,
\]

then

\[
\mathbf D(\mathbf x+r\mathbf 1)
=
\mathbf D\mathbf x.
\]

### Canonical result

The deterministic V21 sweep adds the same reference waveform with scale from 0 to 100. The maximum pairwise-difference discrepancy remains below approximately

\[
1.4\times10^{-14},
\]

which is floating-point roundoff for this construction.

### Interpretation

Reference-sensitive voltage values should not be confused with reference-invariant relational information.

This does **not** mean that EEG source localization is reference-free. The source inverse still depends on the forward model, montage implementation, preprocessing, and inverse assumptions.

---

## V22. Lead-field null-space non-identifiability

Suppose the lead field has a nontrivial right null space:

\[
\ker(\mathbf L)\neq\{0\}.
\]

For any nonzero

\[
\mathbf v\in\ker(\mathbf L),
\]

and any source vector \(\mathbf j\),

\[
\mathbf L(\mathbf j+\mathbf v)
=
\mathbf L\mathbf j.
\]

Therefore two distinct source configurations can produce exactly the same ideal sensor measurement.

### Canonical construction

The V22 operator has

\[
3\text{ sensors},\qquad
6\text{ source dimensions},
\]

with

\[
\operatorname{rank}(\mathbf L)=3,
\qquad
\operatorname{nullity}(\mathbf L)=3.
\]

The canonical alternative source differs from the declared source by Euclidean norm 1 while producing zero sensor residual:

\[
\|\mathbf j'-\mathbf j\|_2=1,
\qquad
\|\mathbf L\mathbf j'-\mathbf L\mathbf j\|_2=0.
\]

### Result

\[
\boxed{
\text{perfect sensor fit does not imply unique source identification}
}
\]

This is a measurement-identifiability statement, not a criticism of all source localization. Practical inverse methods deliberately add anatomical, statistical, spatial, temporal, sparsity, minimum-norm, or other constraints. V22 makes the role of those added assumptions explicit.

---

## V23. Regularization sensitivity

A standard L2-regularized inverse solves

\[
\widehat{\mathbf j}_{\lambda}
=
\arg\min_{\mathbf j}
\left[
\|\mathbf L\mathbf j-\mathbf y\|_2^2
+
\lambda\|\mathbf j\|_2^2
\right].
\]

For \(\lambda>0\),

\[
\boxed{
\widehat{\mathbf j}_{\lambda}
=
(\mathbf L^\top\mathbf L+\lambda\mathbf I)^{-1}
\mathbf L^\top\mathbf y
}
\]

and, under the singular value decomposition

\[
\mathbf L=\mathbf U\boldsymbol\Sigma\mathbf V^\top,
\]

each singular direction is weighted by the Tikhonov filter factor

\[
g_{\lambda}(s)
=
\frac{s}{s^2+\lambda}.
\]

### Canonical result

Across

\[
\lambda\in
\{10^{-6},10^{-4},10^{-2},10^{-1},1\},
\]

the source estimate norm decreases while the sensor residual increases.

In the canonical record:

- estimate norm decreases from approximately 1.547 to 0.577;
- measurement residual increases from approximately \(1.43\times10^{-5}\) to 0.521.

### Result

The reconstructed source is not determined by the measurement alone. It also depends on the inverse regularization rule.

That dependence should be exposed in any consciousness-related analysis that moves from EEG or MEG sensors into source space.

---

## V24. EEG/MEG complementarity as null-space reduction

Let

\[
\mathbf L_E
\]

be an EEG-like forward operator and

\[
\mathbf L_M
\]

a complementary MEG-like operator acting on the same source vector.

The stacked observation operator is

\[
\mathbf L_{EM}
=
\begin{bmatrix}
\mathbf L_E\\
\mathbf L_M
\end{bmatrix}.
\]

Its null space is

\[
\ker(\mathbf L_{EM})
=
\ker(\mathbf L_E)
\cap
\ker(\mathbf L_M).
\]

Therefore adding a genuinely complementary modality cannot increase the common null space and may reduce it.

### Canonical construction

The deterministic V24 record has:

\[
\operatorname{nullity}(\mathbf L_E)=3,
\]

\[
\operatorname{nullity}(\mathbf L_M)=3,
\]

but

\[
\operatorname{nullity}(\mathbf L_{EM})=1.
\]

### Result

Complementary electric and magnetic measurements can reduce source ambiguity.

But the canonical stacked operator still has a nonzero nullity, so:

\[
\boxed{
\text{multimodal measurement can improve identifiability without guaranteeing uniqueness}
}
\]

This is more precise than saying that one modality is universally superior.

---

## V25. Forward-model perturbation bound

Let the true operator differ from the assumed forward operator by

\[
\Delta\mathbf L.
\]

Then the sensor prediction changes by

\[
\Delta\mathbf y
=
\Delta\mathbf L\,\mathbf j.
\]

The spectral operator norm gives

\[
\boxed{
\|\Delta\mathbf y\|_2
\le
\|\Delta\mathbf L\|_2
\|\mathbf j\|_2
}
\]

by submultiplicativity.

### Canonical result

Across perturbation operator norms from 0.001 to 0.1, every deterministic test satisfies the bound.

The canonical ratio

\[
\frac{
\|\Delta\mathbf L\mathbf j\|_2
}{
\|\Delta\mathbf L\|_2\|\mathbf j\|_2
}
\]

is approximately 0.479 in the nonzero perturbation rows.

### Interpretation

Head-model error, conductivity error, sensor-geometry error, or other forward-model mismatch propagates into sensor predictions in a mathematically bounded way.

However, source-estimation error can be more strongly amplified when the inverse is ill-conditioned. A small sensor residual therefore does not establish that the assumed source model is uniquely correct.

---

## What V21-V25 establish

The current deterministic record establishes five measurement-science facts inside the declared linear constructions:

1. common rereferencing preserves pairwise sensor differences;
2. a lead-field null space creates exact source non-identifiability;
3. regularization changes the selected source estimate;
4. complementary modalities can reduce shared source ambiguity;
5. forward-model perturbations obey an operator-norm sensor-error bound.

These results are directly relevant to any electromagnetic consciousness program because they define what must be separated before an experiential interpretation is attempted.

## What V21-V25 do not establish

They do not establish:

- that EEG or MEG directly measures consciousness;
- that a reconstructed source is uniquely true;
- that an electromagnetic field is identical to experience;
- that multimodal EEG/MEG removes all inverse ambiguity;
- that minimum-norm, sparse, beamformer, Bayesian, or other inverse solutions are interchangeable;
- that a low source-space residual proves a consciousness mechanism;
- that any current artificial system is conscious because it emits structured electromagnetic fields.

---

## Prospective empirical controls

A serious empirical EM study should report, as applicable:

- sensor geometry and registration;
- electrode reference and rereferencing policy;
- head model and conductivity assumptions;
- forward solver;
- source space and orientation constraints;
- inverse method and prior;
- regularization parameter selection;
- noise covariance;
- sensitivity to plausible head-model perturbations;
- sensitivity to sensor deletion or motion;
- cross-method source stability;
- EEG-only, MEG-only, and combined analyses when available;
- sensor-space results alongside source-space results;
- held-out participant and session validation;
- negative controls and nuisance channels.

A source-space consciousness claim should be weakened if it disappears under reasonable forward-model or inverse-model perturbations.

---

## Literature anchors

- Phillips AR, Vakilna YS, EPMoghaddam D, Banta A, Mosher JC, Aazhang B. *Inferring neural sources from electroencephalography: foundations and frontiers*. Journal of Neural Engineering. 2026;23(1):011002. doi:10.1088/1741-2552/ae3e16. Reviews current EEG forward and inverse modeling, source-estimation limitations, anatomical variability, high-density systems, and multimodal integration.
- Luria G, Viani A, Pascarella A, Bornfleth H, Sommariva S, Sorrentino A. *The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG*. Frontiers in Human Neuroscience. 2024;18:1359753. doi:10.3389/fnhum.2024.1359753. Provides a probabilistic source-localization framework that keeps uncertainty in the reconstructed source explicit.
- Gross J et al. *Good practice for conducting and reporting MEG research*. NeuroImage. 2013;65:349-363. doi:10.1016/j.neuroimage.2012.10.001. Describes the M/EEG inverse problem as fundamentally ill-posed, including limited sensor count, lead-field null spaces, and nonunique source configurations, and recommends explicit reporting of forward models, inverse methods, parameters, and regularization.
- He B, Sohrabpour A, Brown E, Liu Z. *Electrophysiological Source Imaging: A Noninvasive Window to Brain Dynamics*. Annual Review of Biomedical Engineering. 2018;20:171-196. doi:10.1146/annurev-bioeng-062117-120853. Reviews the forward/inverse source-imaging pipeline and the physical relationship between noninvasive electromagnetic measurements and candidate neural generators.
- Grech R et al. *Review on solving the inverse problem in EEG source analysis*. Journal of NeuroEngineering and Rehabilitation. 2008;5:25. doi:10.1186/1743-0003-5-25. Reviews parametric and distributed inverse methods and the role of added assumptions in obtaining source estimates.
- Hu S et al. *Which Reference Should We Use for EEG and ERP practice?* Brain Topography. 2019. Reviews the EEG reference problem and the assumptions behind common rereferencing choices.

The repository uses these references to motivate the measurement problem, not to claim that any one inverse method is uniquely correct.

---

## Reproducibility

Source:

- `src/consciousness_measurement/electromagnetic_inverse.py`
- `src/consciousness_measurement/electromagnetic_inverse_simulations.py`

Tests:

- `tests/test_electromagnetic_inverse.py`
- `tests/test_electromagnetic_inverse_simulations.py`

Runner:

```bash
python scripts/run_electromagnetic_inverse_validation.py
```

Machine-readable outputs:

- `results/v21_reference_invariance.csv`
- `results/electromagnetic_inverse_validation_summary.json`
- `results/v23_regularization_path.csv`
- `results/v24_multimodal_nullity.csv`
- `results/v25_forward_model_perturbation.csv`

Canonical figure:

![Electromagnetic forward and inverse validation V21-V25](figures/v21_v25_electromagnetic_inverse_validation.svg)

All current V21-V25 results are analytic or deterministic synthetic measurement results. They are not human empirical evidence that consciousness has been measured.
