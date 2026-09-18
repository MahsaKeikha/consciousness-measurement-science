# Research III Formal Validation V1-V25

This is the compact entry point to the executable mathematical research layer of Research III.

Research III separates a declared latent measurement target from the observable channels used to study it. The validation program asks whether an inference is identifiable, finite-sample valid, robust to dependence and transport failure, stable under inversion, honest about missingness and site heterogeneity, precise enough for its intended use, and protected against invalid selection at release time.

These are **analytic and synthetic validation results**. They test the measurement machinery. They are not human empirical evidence that consciousness has been measured.

## Reader path

1. [Validation Atlas](docs/validation-atlas.md) for the complete visual V1-V25 sequence.
2. [Formal Validation V1-V5](docs/formal-validation-program.md) for identification, coverage, transport, dependence, and structural testing.
3. [Formal Validation V6-V10](docs/formal-validation-program-v6-v10.md) for finite calibration uncertainty, missingness, conditioning, heterogeneous sites, and abstention.
4. [Formal Validation V11-V15](docs/formal-validation-program-v11-v15.md) for exact resolution laws, multisite identification, design sample size, and independent release gating.
5. [Electromagnetic Field Program V16-V20](docs/electromagnetic-field-program.md) for physical EM observables, organization descriptors, non-identifiability, and confound stress tests.
6. [Electromagnetic Source Identifiability V21-V25](docs/electromagnetic-source-identifiability.md) for reference invariance, lead-field null spaces, inverse regularization, multimodal complementarity, and forward-model perturbation.
7. [Machine-readable results](results/README.md) for the canonical CSV and JSON records.
8. [V1-V5 runner](scripts/run_validation_program.py), [V6-V10 runner](scripts/run_robustness_validation.py), [V11-V15 runner](scripts/run_identification_design_validation.py), [V16-V20 runner](scripts/run_electromagnetic_validation.py), and [V21-V25 runner](scripts/run_electromagnetic_inverse_validation.py) to regenerate the result record and figures.
9. [Source package](src/consciousness_measurement) and [tests](tests) for the executable implementation and regression checks.

## Twenty-five formal stages

| Stage | Scientific question | Main mathematical object | Executable evidence |
|---|---|---|---|
| **V1** | When can an imperfect binary channel identify latent prevalence? | exact inverse through sensitivity and specificity | `latent_measurement.py`, theorem tests |
| **V2** | What remains valid with finite deployment data and bounded calibration? | partial-identification interval plus Hoeffding coverage | coverage CSV, identification and coverage figures |
| **V3** | What happens when calibration changes across conditions? | exact transport-bias equation | transport stress grid and bias surface |
| **V4** | How badly can naive multimodal independence fail? | exact correlated-channel counterexample | dependence stress CSV and posterior comparison figure |
| **V5** | Does the structural-alignment test control false positives and gain power? | permutation null and planted-signal power | null/power simulation and figure |
| **V6** | How much uncertainty comes from finite sensitivity/specificity calibration samples? | simultaneous calibration/proxy confidence box | calibration-size experiment and figure |
| **V7** | What can be inferred when deployment outcomes are missing without MAR assumptions? | sharp worst-case proxy and latent identified sets | missingness sweep and figure |
| **V8** | When is the inverse numerically unstable? | exact local derivatives and condition factor `1/J` | Youden-margin sweep and conditioning figure |
| **V9** | Can pooled data identify average prevalence across differently calibrated sites? | sharp two-site identified set and constructive counterexample | site-mixture CSV and identification band |
| **V10** | When should the system refuse to release a precise estimate? | predeclared interval-width rule with marginal erroneous-release control | abstention frontier plus conditional-coverage diagnostic |
| **V11** | Exactly how do arbitrary missingness and channel strength combine? | sharp interior width law `missing_fraction / J` | deterministic missingness-information grid and figure |
| **V12** | When does one pooled multisite rate identify the population-average latent prevalence? | necessary-and-sufficient equal-Youden condition | theorem tests and multisite design grid |
| **V13** | What is the sharp target set when pooled multisite identification fails? | exact K-site linear-program solution | fractional-knapsack solver, sharp-width result record and figure |
| **V14** | How large must the deployment sample be for a declared latent resolution? | closed-form Hoeffding design law | sample-size grid and resolution figure |
| **V15** | How can a release gate preserve confirmatory conditional coverage? | independent pilot-gated release theorem | fixed-seed pilot/confirmatory experiment and figure |
| **V16** | Are the physical EM calculations dimensionally and directionally correct? | electromagnetic energy density and Poynting vector | exact analytic sanity checks |
| **V17** | Which organization descriptors survive global gain changes? | normalized spectral, phase, covariance-rank, and singular-entropy features | deterministic gain sweep |
| **V18** | Can field power identify spatial phase organization? | matched-power constructive counterexample | exact channel-power match with distinct phase structure |
| **V19** | Can shared contamination mimic global EM organization? | common-mode confound construction | deterministic nuisance-amplitude stress test |
| **V20** | Can one scalar summarize field organization across frequencies? | frequency-specific phase-organization construction | two-frequency synthetic counterexample |
| **V21** | Which EEG relations survive a change of common reference? | pairwise-difference invariance under common additive rereferencing | deterministic reference-amplitude sweep |
| **V22** | Can ideal sensor data uniquely identify an underlying source distribution? | lead-field rank-nullity and exact right-null-space construction | distinct sources with zero sensor residual |
| **V23** | How strongly does inverse regularization select the reconstructed source? | Tikhonov inverse and singular-direction filter factors | deterministic regularization path |
| **V24** | Can complementary EEG/MEG operators reduce source ambiguity? | null-space intersection of stacked forward operators | deterministic single- versus multimodal rank/nullity record |
| **V25** | How does forward-model error propagate to sensor predictions? | operator-norm perturbation inequality | deterministic forward-model perturbation grid |

## Core measurement equations

For latent prevalence \(\pi\), sensitivity \(\alpha\), specificity \(\beta\), observable positive rate \(q\), and Youden information margin \(J=\alpha+\beta-1\),

\[
q=(1-\beta)+J\pi,
\qquad
\pi=\frac{q+\beta-1}{J},\quad J>0.
\]

Finite-sample rate uncertainty uses

\[
\epsilon_n(\delta)=\sqrt{\frac{\log(2/\delta)}{2n}}.
\]

Local inverse conditioning is

\[
\frac{\partial\pi}{\partial q}=\frac1J,
\qquad
\frac{\partial\pi}{\partial\alpha}=-\frac{\pi}{J},
\qquad
\frac{\partial\pi}{\partial\beta}=\frac{1-\pi}{J}.
\]

V11 makes the missingness penalty exact in the interior. If \(m\) of \(N\) intended outcomes are unrestricted missing values,

\[
\boxed{
W_{\mathrm{miss}}=\frac{m/N}{J}
}
\]

before parameter-boundary clipping.

For \(K\) sites with weights \(w_i\), site-specific Youden margins \(J_i\), and known false-positive intercepts,

\[
\bar q
=
\sum_i w_i(1-\beta_i)
+
\sum_i w_iJ_i\pi_i.
\]

V12 proves that the population average

\[
\bar\pi=\sum_iw_i\pi_i
\]

is identified from this single pooled rate for every feasible site-prevalence vector if and only if

\[
\boxed{J_1=J_2=\cdots=J_K.}
\]

When the margins differ, V13 computes the sharp identified interval exactly rather than substituting a pooled point estimate.

For point-known calibration, V14 gives the sufficient deployment size for latent interval width at most \(\omega\):

\[
\boxed{
 n
\geq
\frac{2\log(2/\delta)}{J^2\omega^2}.
}
\]

V15 separates the pilot decision from the confirmatory interval. If the release event \(G\) is determined only from pilot data independent of confirmatory data, and \(C\) is the confirmatory coverage event, then

\[
\boxed{
P(C\mid G)=P(C)
}
\]

whenever \(P(G)>0\).

These equations are useful only inside their declared calibration, sampling, independence, and identification assumptions. The repository therefore tests both the successful regime and the failure regime instead of presenting an inverse formula as a universal consciousness score.

## Electromagnetic measurement equations

For a measured electric field \(\mathbf E\) and magnetic field \(\mathbf B\), V16 implements the vacuum physical sanity checks

\[
u=\frac12\left(\epsilon_0\lVert\mathbf E\rVert^2+\frac{\lVert\mathbf B\rVert^2}{\mu_0}\right),
\qquad
\mathbf S=\frac1{\mu_0}\mathbf E\times\mathbf B.
\]

For multichannel measurements \(X_k(t)\), the EM program then studies normalized spectral entropy, frequency-specific sensor-phase concentration, covariance effective rank, singular-value entropy, and common-mode fraction. V18 proves constructively that matched channel power does not identify spatial phase organization, and V19 demonstrates that shared contamination can create spurious sensor-wide phase concentration.

These quantities are candidate electromagnetic observables, not consciousness scores.

For source-space electromagnetic inference, V21-V25 use the linear forward model

\[
\mathbf y=\mathbf L\mathbf j+\boldsymbol\eta.
\]

If \(\mathbf v\in\ker(\mathbf L)\), then

\[
\boxed{
\mathbf L(\mathbf j+\mathbf v)=\mathbf L\mathbf j,
}
\]

so a perfect sensor fit need not uniquely identify the underlying source. V23 makes one common regularized inverse explicit:

\[
\boxed{
\widehat{\mathbf j}_{\lambda}
=
(\mathbf L^\top\mathbf L+\lambda\mathbf I)^{-1}
\mathbf L^\top\mathbf y.
}
\]

For complementary operators \(\mathbf L_E\) and \(\mathbf L_M\),

\[
\ker
\begin{bmatrix}
\mathbf L_E\\
\mathbf L_M
\end{bmatrix}
=
\ker(\mathbf L_E)\cap\ker(\mathbf L_M),
\]

so multimodal measurement can reduce, but need not eliminate, source ambiguity. Forward-model perturbations obey

\[
\boxed{
\|\Delta\mathbf L\,\mathbf j\|_2
\le
\|\Delta\mathbf L\|_2\|\mathbf j\|_2.
}
\]

These are source-identifiability and model-sensitivity results. They do not turn a reconstructed source into a direct measurement of consciousness.

## Canonical result record

The committed deterministic and fixed-seed experiments show, among other checks:

- finite-sample V2 coverage remains conservative while interval width contracts with sample size;
- naive conditional-independence fusion can report about `0.997` where the exact posterior in the declared shared-dependence construction is `0.84`;
- V6 mean width contracts from about `0.960` at 50 calibration examples per class to about `0.281` at 2,500;
- unrestricted 30% missingness expands the canonical V7 latent interval to width `0.400`;
- a Youden margin of `0.05` amplifies proxy-rate error by a factor of `20`;
- the same pooled proxy rate `0.45` can correspond to average latent prevalences from about `0.375` to `0.5625` in the canonical two-site construction;
- V11 gives exact interior width `0.133333...` for 10% arbitrary missingness at `J=0.75`;
- the V12-V13 multisite design has zero identified-set width when site information margins are equal and width `0.333333...` at the canonical margin spread `0.30`;
- V14 requires `1,312` deployment observations for the canonical `J=0.75`, width `0.10`, 95% Hoeffding design target;
- under the declared V15 fixed-seed pilot gate, planned confirmatory `n=900` proceeds in `47.625%` of runs, and every identified confirmatory interval in that canonical run covers the true latent prevalence;
- V18 matches channel power to relative error below `3e-16` while phase concentration changes from `1.0` to numerical zero;
- V19 raises raw phase concentration to about `0.935` using only a shared contaminant of amplitude `2.0`, while the controlled common-mode removal construction returns it to numerical zero;
- V20 gives phase concentration `1.0` at 10 Hz and numerical zero at 17 Hz in the same multichannel signal, demonstrating frequency-specific organization;
- V21 preserves pairwise sensor differences to below `1.4e-14` across a 100-fold common-reference amplitude sweep;
- V22 has lead-field rank `3`, nullity `3`, source separation `1`, and exactly zero sensor residual for two distinct source vectors;
- V23 changes the selected source estimate as regularization increases: estimate norm falls from about `1.547` to `0.577` while sensor residual rises from about `1.43e-5` to `0.521`;
- V24 reduces canonical source nullity from `3` for each single modality to `1` for the stacked complementary operator, without reaching uniqueness;
- V25 satisfies the forward-model operator-norm error bound at every tested perturbation scale, with the nonzero canonical mismatch/bound ratio about `0.479`.

The V15 simulation value is a finite fixed-seed check, not the theorem itself. The theorem-level coverage statement follows from independence of the pilot release event and the confirmatory interval construction.

The exact values are stored under [`results/`](results/). Downstream analysis should use the machine-readable records rather than rounded prose values.

## Reproduce

```bash
python -m pip install -e ".[dev]"
python scripts/run_validation_program.py
python scripts/run_robustness_validation.py
python scripts/run_identification_design_validation.py
python scripts/run_electromagnetic_validation.py
python scripts/run_electromagnetic_inverse_validation.py
make check
```

Canonical seeds are `20260917` for V1-V5, `20260918` for V6-V10, and `20260919` for V11-V15 fixed-seed checks. V16-V25 are deterministic and require no random seed.

## Scientific boundary

Passing V1-V25 means that the mathematics and software behave as declared under the stated analytic assumptions and synthetic data-generating models. It does not establish empirical calibration for a human, animal, organoid, or artificial system; it does not identify qualia; and it does not settle the ontology of consciousness. Those remain separate empirical and theoretical burdens.
