# Electromagnetic Sparse Identifiability and Nuisance-Aware Information

## Research III V36-V40

V31-V35 made spatial specificity, sensor design, nuisance projection, and forward-model uncertainty explicit. V36-V40 ask a narrower next question:

> If an electromagnetic source model is assumed to be sparse, what can the declared sensing operator actually guarantee about uniqueness, conditioning, nuisance-adjusted information, and the value of an additional measurement?

The key phrase is **if a sparse model is assumed**. Sparsity is an additional structural assumption. It is not created by the inverse problem and it is not established by observing that a sparse algorithm returns a focal map.

All V36-V40 results are analytic or deterministic synthetic measurement-design results. They are not human empirical data and they are not evidence that consciousness or qualia have been directly measured.

---

## V36. Mutual coherence and the Welch floor

Let the normalized columns of a sensing or lead-field dictionary be

[
widetilde{mathbf L}
=
[
widetilde{oldsymbolell}_1,ldots,widetilde{oldsymbolell}_n
],
qquad
|
widetilde{oldsymbolell}_j
|_2
=
1.
]

Define the mutual coherence

[
oxed{
mu(mathbf L)
=
max_{i
eq j}
left|
widetilde{oldsymbolell}_i^	op
widetilde{oldsymbolell}_j
ight|
}.
]

This is the largest absolute pairwise similarity between normalized source topographies.

A small value means that no pair of declared source columns is too similar in the measurement geometry. A large value means that at least one pair is difficult to distinguish by column direction alone.

For (n>m), the Welch bound gives

[
oxed{
mu
ge
sqrt{
rac{n-m}{m(n-1)}
}
}
]

for (n) unit vectors in an (m)-dimensional measurement space.

### Canonical V36 construction

The V36 regular-simplex dictionary has

[
m=4,
qquad
n=5,
qquad
operatorname{rank}(mathbf L)=4.
]

Its five normalized columns form a regular simplex in (mathbb R^4), so every distinct pair has inner product magnitude

[
rac14.
]

Therefore

[
mu
=
0.25.
]

The Welch floor is

[
sqrt{
rac{5-4}{4(5-1)}
}
=
rac14
=
0.25.
]

Thus the canonical simplex construction attains the Welch bound exactly.

The coherent comparison dictionary has the same dimensions and rank but contains one column nearly parallel to the first basis direction:

[
mu
approx
0.9949371890.
]

This comparison makes a measurement-design point: equal matrix size and equal rank do not imply equal sparse-source separability.

---

## V37. Coherence-based sufficient sparse-uniqueness guarantee

For a normalized dictionary with mutual coherence (mu>0), the classical coherence condition gives the sufficient sparsity requirement

[
oxed{
k
<
rac12
left(
1+rac1mu
ight)
}.
]

Inside the standard exact sparse linear model, this condition guarantees uniqueness of the sufficiently sparse representation under the classical coherence result. Related results also connect coherence conditions to recovery by basis pursuit and greedy algorithms.

The condition is **sufficient, not necessary**.

Failure of the inequality does not prove non-uniqueness. It means only that this particular worst-case certificate no longer guarantees uniqueness.

### Canonical V37 results

For the regular simplex,

[
mu=0.25,
]

so

[
k
<
rac12(1+4)
=
2.5.
]

The largest positive integer guaranteed by this strict inequality is

[
oxed{k=2}.
]

For the coherent comparison dictionary,

[
mu
approx
0.9949371890,
]

so

[
k
<
1.0025442867.
]

The largest guaranteed positive integer sparsity is therefore only

[
oxed{k=1}.
]

The construction does not claim that every two-source case in the coherent dictionary is non-identifiable. It shows that the coherence certificate has almost completely collapsed.

---

## V38. Restricted Gram conditioning from coherence

Select a support (S) with

[
|S|=k.
]

Let

[
mathbf L_S
]

be the normalized subdictionary and

[
mathbf G_S
=
mathbf L_S^	opmathbf L_S
]

its Gram matrix.

The diagonal entries equal one and the off-diagonal entries have magnitude at most (mu). Gershgorin's theorem therefore gives

[
oxed{
1-(k-1)mu
le
lambda(mathbf G_S)
le
1+(k-1)mu
}
]

for every eigenvalue, with nonnegativity of the Gram matrix providing zero as a trivial lower floor when the algebraic lower bound is negative.

When

[
(k-1)mu<1,
]

the support Gram matrix is guaranteed positive definite, and

[
sigma_{min}^2(mathbf L_S)
ge
1-(k-1)mu.
]

A corresponding condition-number bound is

[
kappa_2(mathbf L_S)
le
sqrt{
rac{
1+(k-1)mu
}{
1-(k-1)mu
}
}.
]

### Canonical simplex results

For

[
mu=0.25
]

and

[
k=2,
]

the Gram eigenvalue interval is exactly

[
[0.75, 1.25].
]

The exhaustive support sweep observes

[
lambda_{min}=0.75,
qquad
lambda_{max}=1.25.
]

For

[
k=3,
]

the coherence interval is

[
[0.5, 1.5].
]

The exhaustive support sweep observes

[
lambda_{min}=0.5,
qquad
lambda_{max}=1.25.
]

The lower bound is attained; the upper bound remains conservative.

V38 therefore separates two questions:

1. Is a support covered by a worst-case coherence certificate?
2. What conditioning does the selected support actually have?

The second should be computed directly whenever a support is available.

---

## V39. Nuisance-adjusted Fisher information

Suppose a local linear-Gaussian model contains target parameters

[
oldsymbol	heta
]

and nuisance parameters

[
oldsymbol
u.
]

Partition the Fisher information matrix as

[
mathbf F
=
egin{pmatrix}
mathbf F_{	heta	heta}
&
mathbf F_{	heta
u}
\
mathbf F_{
u	heta}
&
mathbf F_{
u
u}
end{pmatrix}.
]

When the nuisance block is invertible, the Fisher information available for the target after accounting for nuisance uncertainty is the Schur complement

[
oxed{
mathbf F_{mathrm{eff}}
=
mathbf F_{	heta	heta}
-
mathbf F_{	heta
u}
mathbf F_{
u
u}^{-1}
mathbf F_{
u	heta}
}.
]

The implementation uses the Moore-Penrose pseudoinverse for the declared deterministic nuisance block so the same expression is defined in rank-deficient synthetic cases.

### Geometric meaning

In whitened coordinates, nuisance adjustment removes the component of the target sensitivity lying in the nuisance span.

Thus target and nuisance directions that are nearly aligned can destroy target information even when the nominal target sensitivity is large.

### Canonical V39 construction

The nominal scalar target information is one.

For a nuisance subspace orthogonal to the target,

[
I_{mathrm{eff}}=1.
]

For a nuisance direction separated from the target by 30 degrees, together with a second orthogonal nuisance direction,

[
I_{mathrm{eff}}
=
sin^2(30^circ)
=
0.25.
]

When the nuisance span contains the target direction,

[
I_{mathrm{eff}}
=
0.
]

This is the Fisher-information version of the nuisance-projection geometry introduced in V34, now expressed in the general block-information language used for parameter inference and experimental design.

---

## V40. Exact sequential sensor information gain

Let the current positive-definite Fisher information matrix be

[
mathbf F.
]

Consider one additional scalar measurement with parameter sensitivity vector

[
mathbf a
]

and independent noise variance

[
sigma^2.
]

The updated information matrix is

[
oxed{
mathbf F_{mathrm{new}}
=
mathbf F
+
rac{
mathbf amathbf a^	op
}{
sigma^2
}.
}
]

The matrix determinant lemma gives

[
det(mathbf F_{mathrm{new}})
=
det(mathbf F)
left(
1+
rac{
mathbf a^	op
mathbf F^{-1}
mathbf a
}{
sigma^2
}
ight).
]

Therefore the exact D-optimal log-determinant gain is

[
oxed{
Deltalogdetmathbf F
=
log
left(
1+
rac{
mathbf a^	op
mathbf F^{-1}
mathbf a
}{
sigma^2
}
ight).
}
]

The quadratic term

[
mathbf a^	op
mathbf F^{-1}
mathbf a
]

is large when the new measurement points into a direction that is weakly informed by the current design.

### Canonical V40 construction

Start with

[
mathbf F
=
egin{pmatrix}
10 & 0\
0 & 1
end{pmatrix},
qquad
sigma^2=1.
]

A candidate aligned with the already-strong direction gives

[
Deltalogdet
=
log(1.1)
approx
0.0953101798.
]

A 45-degree mixed direction gives

[
Deltalogdet
=
log(1.55)
approx
0.4382549309.
]

A candidate aligned with the weak-information direction gives

[
Deltalogdet
=
log 2
approx
0.6931471806.
]

The determinant-lemma value and the direct log-determinant difference agree to floating-point precision for every candidate.

This makes a design principle explicit:

> The most valuable next measurement is not necessarily the one with the largest raw sensitivity. It can be the one that fills the weakest current information direction.

---

## Combined engineering interpretation

V36-V40 produce the following chain:

[
	ext{normalized lead field}
ightarrow
	ext{mutual coherence}
ightarrow
	ext{sparse uniqueness certificate}
ightarrow
	ext{restricted support conditioning}
ightarrow
	ext{nuisance-adjusted target information}
ightarrow
	ext{incremental sensor information}.
]

The chain guards against several common category errors:

[
	ext{sparse algorithm output}

eq
	ext{proof of biological sparsity},
]

[
	ext{focal reconstruction}

eq
	ext{guaranteed unique source},
]

[
	ext{nominal Fisher information}

eq
	ext{nuisance-adjusted Fisher information},
]

and

[
	ext{largest raw sensor response}

eq
	ext{largest incremental information gain}.
]

None of these quantities is a consciousness measure by itself.

---

## What V36-V40 establish

Inside the declared normalized linear and deterministic synthetic constructions:

1. the regular-simplex dictionary attains the Welch coherence floor;
2. the classical coherence certificate guarantees two-sparse uniqueness for the simplex but only one-sparse uniqueness for the coherent comparison;
3. restricted Gram eigenvalues obey the declared coherence bounds;
4. nuisance-adjusted Fisher information is computed by the target-block Schur complement;
5. target information can fall from one to zero when the nuisance span contains the target;
6. one-measurement D-optimal gain is exactly given by the matrix determinant lemma;
7. a measurement aligned with a weak current information direction can add more information than one aligned with an already-strong direction.

## What V36-V40 do not establish

They do not establish:

- that real neural generators are exactly sparse;
- that a sparse prior is correct for a given EEG, MEG, or OPM-MEG experiment;
- that satisfying a coherence bound proves the recovered source is biologically true;
- that violating the coherence bound proves the source is non-unique;
- that mutual coherence captures every source-recovery failure mode;
- that nuisance variables have been completely specified in a real experiment;
- that a D-optimal sensor is optimal for every scientific target;
- that source uniqueness, Fisher information, or sparse recovery identifies consciousness;
- that synthetic guarantees substitute for human empirical, clinical, animal, organoid, or artificial-system validation.

---

## Prospective empirical controls

For a source-space study that invokes sparsity or sparse reconstruction, preregister or report as applicable:

- the source dictionary or lead-field operator and column normalization convention;
- the declared sparse prior and its scientific justification;
- mutual coherence and, where useful, cumulative-coherence or related diagnostics;
- the coherence-based sufficient sparsity threshold;
- actual support-conditioned Gram or singular-value diagnostics for selected supports;
- sensitivity to source-grid density and source orientation;
- sensitivity to head-model, conductivity, sensor-registration, and covariance uncertainty;
- alternative non-sparse inverse analyses;
- nuisance parameterization and nuisance-adjusted target information;
- the objective used for sensor or modality selection;
- incremental information gain for proposed additional measurements;
- held-out participant, session, site, state, and hardware validation.

Sparse-recovery language should be weakened when the scientific sparsity assumption is unsupported, when coherence is high, when selected supports are poorly conditioned, when nuisance adjustment removes the target direction, or when plausible model perturbations erase the apparent information advantage.

---

## Literature anchors

- Donoho DL, Elad M. *Optimally sparse representation in general (nonorthogonal) dictionaries via l1 minimization*. Proceedings of the National Academy of Sciences. 2003;100(5):2197-2202. doi:10.1073/pnas.0437847100.
- Tropp JA. *Greed is Good: Algorithmic Results for Sparse Approximation*. IEEE Transactions on Information Theory. 2004;50(10):2231-2242. doi:10.1109/TIT.2004.834793.
- Mannepalli T, Routray A. *Sparse algorithms for EEG source localization*. Medical & Biological Engineering & Computing. 2021;59(11-12):2325-2352. doi:10.1007/s11517-021-02444-5.

These references anchor sparse-representation and EEG-source methodology. They do not imply that the present V36-V40 deterministic constructions are empirical evidence about consciousness.

---

## Reproducibility

Source:

- `src/consciousness_measurement/electromagnetic_sparse.py`
- `src/consciousness_measurement/electromagnetic_sparse_simulations.py`

Tests:

- `tests/test_electromagnetic_sparse.py`
- `tests/test_electromagnetic_sparse_simulations.py`

Runner:

```bash
python scripts/run_electromagnetic_sparse_validation.py
```

Machine-readable outputs:

- `results/v36_coherence_welch.csv`
- `results/v37_sparse_uniqueness.csv`
- `results/v38_restricted_conditioning.csv`
- `results/v39_nuisance_adjusted_information.csv`
- `results/v40_sequential_sensor_information.csv`
- `results/electromagnetic_sparse_validation_summary.json`

Canonical figure:

![Electromagnetic sparse identifiability and nuisance-aware information V36-V40](figures/v36_v40_electromagnetic_sparse_validation.svg)

All current V36-V40 results are analytic or deterministic synthetic measurement-design results. They are not human empirical data and they are not human empirical evidence that consciousness has been measured.
