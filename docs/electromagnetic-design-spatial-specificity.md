# Electromagnetic Design and Spatial Specificity Program

## Research III V31-V35

V16-V20 established sensor-level electromagnetic sanity checks and confound tests. V21-V25 made source non-identifiability and inverse-prior dependence explicit. V26-V30 added covariance-aware residual geometry, inverse-resolution limits, Fisher information, temporal aliasing, and singular-direction noise amplification.

V31-V35 ask the next engineering question:

> Given a declared electromagnetic forward and inverse model, how should spatial specificity, source distinguishability, sensor design, nuisance rejection, and model uncertainty be quantified before any experiential interpretation is attempted?

The results below are analytic or deterministic synthetic measurement-design results. They are not human empirical data and they are not evidence that consciousness or qualia have been directly measured.

---

## V31. Point-spread and cross-talk functions

For a linear forward operator (mathbf L) and linear inverse operator (mathbf G),

[
widehat{mathbf j}
=
mathbf Gmathbf y,
qquad
mathbf y
=
mathbf Lmathbf j+oldsymboleta.
]

Ignoring noise for the resolution calculation,

[
widehat{mathbf j}
=
mathbf Gmathbf Lmathbf j.
]

Define the resolution matrix

[
oxed{
mathbf R=mathbf Gmathbf L
}.
]

Let (mathbf e_k) be the (k)-th source basis vector.

### Point-spread function

If the true source is a unit source at location (k),

[
mathbf j=mathbf e_k,
]

then

[
widehat{mathbf j}
=
mathbf Rmathbf e_k.
]

Therefore the point-spread function for source (k) is exactly the (k)-th column of the resolution matrix:

[
oxed{
operatorname{PSF}_k
=
mathbf Rmathbf e_k
=
mathbf R_{:,k}
}.
]

It answers:

> If source (k) alone is active, where does the inverse method spread that source?

### Cross-talk function

The (i)-th reconstructed source coefficient is

[
widehat j_i
=
mathbf e_i^	opmathbf Rmathbf j.
]

Therefore the cross-talk function for estimate (i) is exactly the (i)-th row of the resolution matrix:

[
oxed{
operatorname{CTF}_i^	op
=
mathbf e_i^	opmathbf R
=
mathbf R_{i,:}
}.
]

It answers:

> Which true source locations can leak into reconstructed coefficient (i)?

PSF and CTF are not generally the same object unless the resolution matrix has the relevant symmetry.

### Canonical V31 construction

For source index 1, the deterministic resolution matrix gives

[
operatorname{PSF}_1
=
(0.1, 0.7, 0.1, 0)^	op
]

and

[
operatorname{CTF}_1
=
(0.2, 0.7, 0.2, 0).
]

After zeroing the target diagonal component, the leakage norms are

[
|operatorname{PSF}_{1,mathrm{off}}|_2
=
0.1414213562
]

and

[
|operatorname{CTF}_{1,mathrm{off}}|_2
=
0.2828427125.
]

The example deliberately makes spatial spread and cross-talk different so that a single generic "resolution" number cannot hide their distinct meanings.

---

## V32. Noise-aware source distinguishability

Suppose two candidate sources predict sensor topographies

[
oldsymbolell_1
quad	ext{and}quad
oldsymbolell_2
]

under positive-definite sensor covariance (mathbf C).

Their covariance-aware squared separation is

[
oxed{
d_C^2
=
(oldsymbolell_1-oldsymbolell_2)^	op
mathbf C^{-1}
(oldsymbolell_1-oldsymbolell_2)
}.
]

Let

[
mathbf W=mathbf C^{-1/2}.
]

Then

[
d_C^2
=
|
mathbf W(oldsymbolell_1-oldsymbolell_2)
|_2^2.
]

Thus distinguishability is Euclidean separation after whitening, not raw sensor-space distance before noise geometry is accounted for.

### Gaussian interpretation

For two Gaussian sensor models with equal covariance,

[
mathbf ymid H_1
sim
mathcal N(oldsymbolell_1,mathbf C),
qquad
mathbf ymid H_2
sim
mathcal N(oldsymbolell_2,mathbf C),
]

the log-likelihood-ratio geometry is governed by the same whitened topography difference.

V32 therefore treats (d_C^2) as a measurement distinguishability quantity, not as a consciousness similarity metric.

### Canonical result

Using the declared correlated covariance,

[
d_{mathrm{close}}^2
=
0.0032293578,
]

whereas

[
d_{mathrm{distinct}}^2
=
2.3394495413.
]

The distinct topography is more than two orders of magnitude farther from the reference in squared Mahalanobis distance than the close topography.

---

## V33. Sensor design through Fisher-information geometry

Let a local linear measurement model depend on parameter vector

[
oldsymbol	hetainmathbb R^p
]

with sensitivity matrix

[
mathbf A
=
rac{partialoldsymbolmu}{partialoldsymbol	heta}
]

and Gaussian sensor covariance (mathbf C).

The Fisher information matrix is

[
oxed{
mathbf F
=
mathbf A^	op
mathbf C^{-1}
mathbf A
}.
]

Two standard design summaries are used.

### D-optimal information

[
oxed{
D
=
logdetmathbf F
}
]

when (mathbf F) is positive definite.

This measures information volume in parameter space.

### E-optimal information

[
oxed{
E
=
lambda_{min}(mathbf F)
}.
]

This measures the weakest locally informed parameter direction.

### Canonical counterexample: equal sensor count does not imply equal information

The redundant design is

[
mathbf A_R
=
egin{pmatrix}
1 & 0\
1 & 0.02\
1 & -0.02
end{pmatrix}.
]

Under identity covariance,

[
mathbf F_R
=
egin{pmatrix}
3 & 0\
0 & 0.0008
end{pmatrix}.
]

Hence

[
detmathbf F_R
=
0.0024,
qquad
lambda_{min}(mathbf F_R)
=
0.0008.
]

The complementary design is

[
mathbf A_C
=
egin{pmatrix}
1 & 0\
0 & 1\
1/sqrt2 & 1/sqrt2
end{pmatrix},
]

giving

[
mathbf F_C
=
egin{pmatrix}
1.5 & 0.5\
0.5 & 1.5
end{pmatrix},
]

so

[
detmathbf F_C
=
2
]

and

[
lambda_{min}(mathbf F_C)
=
1.
]

Both designs use three sensors. Their traces are also similar:

[
operatorname{tr}(mathbf F_R)=3.0008,
qquad
operatorname{tr}(mathbf F_C)=3.
]

Yet their weakest-direction information differs by a factor of

[
rac{1}{0.0008}=1250.
]

This construction makes the engineering point explicit: sensor count and total sensitivity do not determine identifiability. Directional complementarity matters.

---

## V34. Nuisance-subspace information loss

Work in whitened sensor coordinates. Let

[
mathbf s
]

be the whitened target topography, and let the columns of

[
mathbf N
]

span a nuisance subspace.

The orthogonal projector onto the nuisance subspace is

[
mathbf P_N
=
mathbf Nmathbf N^+,
]

where (mathbf N^+) is the Moore-Penrose pseudoinverse.

The projector onto its orthogonal complement is

[
oxed{
mathbf P_perp
=
mathbf I-mathbf Nmathbf N^+
}.
]

After exact nuisance projection, the retained target information is

[
oxed{
I_{mathrm{ret}}
=
|mathbf P_perpmathbf s|_2^2
}.
]

The retained fraction is

[
oxed{
ho_{mathrm{ret}}
=
rac{
|mathbf P_perpmathbf s|_2^2
}{
|mathbf s|_2^2
}
}.
]

### Proposition V34-A. One-dimensional nuisance law

Assume (mathbf s) and unit nuisance vector (mathbf n) form angle (	heta). Then

[
mathbf P_perp
=
mathbf I-mathbf nmathbf n^	op.
]

Since

[
mathbf n^	opmathbf s
=
|mathbf s|_2cos	heta,
]

Pythagorean decomposition gives

[
|mathbf P_perpmathbf s|_2^2
=
|mathbf s|_2^2
-
(mathbf n^	opmathbf s)^2.
]

Therefore

[
oxed{
ho_{mathrm{ret}}
=
1-cos^2	heta
=
sin^2	heta
}.
]

This is an exact information-loss law for the declared whitened one-target, one-nuisance construction.

### Consequences

If

[
	heta=0,
]

then target and nuisance are aligned and

[
ho_{mathrm{ret}}=0.
]

Perfect nuisance rejection removes the target completely.

If

[
	heta=rac{pi}{2},
]

then target and nuisance are orthogonal and

[
ho_{mathrm{ret}}=1.
]

No target information is lost.

The canonical sweep at 0, 15, 30, 45, 60, and 90 degrees matches (sin^2	heta) to floating-point precision.

---

## V35. Robust information under bounded forward-model uncertainty

Again work in whitened coordinates. Let the nominal target topography be

[
mathbf w
]

and let model uncertainty permit an additive perturbation

[
oldsymboldelta
]

inside the Euclidean ball

[
|oldsymboldelta|_2
le
epsilon.
]

For a scalar amplitude in identity-covariance whitened coordinates, Fisher information is

[
I
=
|mathbf w+oldsymboldelta|_2^2.
]

The robust lower bound is therefore

[
I_{mathrm{rob}}(epsilon)
=
min_{|oldsymboldelta|_2leepsilon}
|mathbf w+oldsymboldelta|_2^2.
]

### Proposition V35-A. Exact robust information bound

By the reverse triangle inequality,

[
|mathbf w+oldsymboldelta|_2
ge
ig|
|mathbf w|_2-|oldsymboldelta|_2
ig|.
]

Under

[
|oldsymboldelta|_2leepsilon,
]

we obtain

[
|mathbf w+oldsymboldelta|_2
ge
max(
|mathbf w|_2-epsilon,
0
).
]

Squaring gives the lower bound

[
I_{mathrm{rob}}(epsilon)
ge
left[
max(
|mathbf w|_2-epsilon,
0
)
ight]^2.
]

The bound is attainable.

If

[
0leepsilonle|mathbf w|_2,
]

choose

[
oldsymboldelta^star
=
-epsilon
rac{mathbf w}{|mathbf w|_2}.
]

Then

[
|mathbf w+oldsymboldelta^star|_2
=
|mathbf w|_2-epsilon.
]

If

[
epsilonge|mathbf w|_2,
]

choose

[
oldsymboldelta^star=-mathbf w,
]

which is feasible and gives zero information.

Therefore

[
oxed{
I_{mathrm{rob}}(epsilon)
=
left[
max(
|mathbf w|_2-epsilon,
0
)
ight]^2
}.
]

### Canonical result

For

[
mathbf w
=
(1, 0.5, -0.2)^	op,
]

the nominal information is

[
|mathbf w|_2^2
=
1.29
]

and

[
|mathbf w|_2
approx
1.1357816692.
]

The deterministic uncertainty sweep gives robust lower bounds

[
1.29,
quad
0.8756873323,
quad
0.4042183308,
quad
0.0184366617,
quad
0
]

for uncertainty radii

[
0, 0.2, 0.5, 1.0, 1.2.
]

The constructed anti-aligned perturbation attains the bound at every radius.

This is a worst-case measurement-information statement. It does not assert that the declared uncertainty radius is biologically correct for any specific experiment.

---

## Combined engineering interpretation

V31-V35 create a measurement-design chain:

[
	ext{inverse resolution}
ightarrow
	ext{PSF and CTF}
ightarrow
	ext{source distinguishability}
ightarrow
	ext{sensor information geometry}
ightarrow
	ext{nuisance information loss}
ightarrow
	ext{robust information under model uncertainty}.
]

The chain makes several distinctions explicit:

[
	ext{sensor count}

eq
	ext{independent information},
]

[
	ext{focal source map}

eq
	ext{high spatial specificity},
]

[
	ext{nuisance removal}

eq
	ext{free information},
]

and

[
	ext{nominal Fisher information}

eq
	ext{robust Fisher information}.
]

None of those quantities is a consciousness measure by itself.

---

## What V31-V35 establish

Inside the declared analytic and deterministic synthetic constructions:

1. point-spread functions are columns of a linear resolution matrix;
2. cross-talk functions are rows of a linear resolution matrix;
3. covariance-aware sensor-topography distance quantifies noise-aware distinguishability;
4. Fisher-information geometry distinguishes redundant from complementary sensor designs;
5. one-dimensional nuisance projection retains exactly a (sin^2	heta) fraction of whitened target information;
6. bounded whitened topography uncertainty has the exact robust information lower bound
   [
   [max(|mathbf w|_2-epsilon,0)]^2;
   ]
7. the declared worst-case perturbation construction attains that bound.

## What V31-V35 do not establish

They do not establish:

- that a point-spread function is an experiential point-spread function;
- that a cross-talk function measures mixing of conscious contents;
- that larger Mahalanobis separation is a consciousness distance;
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

A source-space claim should be weakened when spatial specificity collapses under PSF/CTF analysis, when candidate sources are not distinguishable under the measured noise covariance, when nuisance removal destroys the target direction, or when plausible model uncertainty drives the robust information bound toward zero.

---

## Literature anchors

- Hauk O, Stenroos M, Treder MS. *Towards an objective evaluation of EEG/MEG source estimation methods - The linear approach*. NeuroImage. 2022;255:119177. doi:10.1016/j.neuroimage.2022.119177. The linear resolution-matrix framework identifies columns with point-spread functions and rows with cross-talk functions.
- Gross J et al. *Good practice for conducting and reporting MEG research*. NeuroImage. 2013;65:349-363. doi:10.1016/j.neuroimage.2012.10.001. The reporting framework emphasizes explicit forward models, inverse assumptions, noise treatment, spatial resolution, and reproducibility.
- Radich BM, Buckley KM. *EEG dipole localization bounds and MAP algorithms for head models with parameter uncertainties*. IEEE Transactions on Biomedical Engineering. 1995;42(3):233-241. doi:10.1109/10.364509. The work connects localization precision to measurement noise and head-model uncertainty through information bounds.

These references anchor the measurement concepts. They do not imply that the present synthetic V31-V35 results are empirical evidence about consciousness.

---

## Reproducibility

Source:

- `src/consciousness_measurement/electromagnetic_design.py`
- `src/consciousness_measurement/electromagnetic_design_simulations.py`

Tests:

- `tests/test_electromagnetic_design.py`
- `tests/test_electromagnetic_design_simulations.py`

Runner:

```bash
python scripts/run_electromagnetic_design_validation.py
```

Machine-readable outputs:

- `results/v31_point_spread_cross_talk.csv`
- `results/v32_source_distinguishability.csv`
- `results/v33_sensor_design_information.csv`
- `results/v34_nuisance_information_loss.csv`
- `results/v35_robust_model_information.csv`
- `results/electromagnetic_design_validation_summary.json`

Canonical figure:

![Electromagnetic design and spatial-specificity validation V31-V35](figures/v31_v35_electromagnetic_design_validation.svg)

All current V31-V35 results are analytic or deterministic synthetic measurement-design results. They are not human empirical data and they are not human empirical evidence that consciousness has been measured.
