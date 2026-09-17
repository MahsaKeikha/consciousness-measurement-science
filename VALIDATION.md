# Research III Formal Validation V1-V15

This is the compact entry point to the executable mathematical research layer of Research III.

Research III separates a declared latent measurement target from the observable channels used to study it. The validation program asks whether an inference is identifiable, finite-sample valid, robust to dependence and transport failure, stable under inversion, honest about missingness and site heterogeneity, precise enough for its intended use, and protected against invalid selection at release time.

These are **analytic and synthetic validation results**. They test the measurement machinery. They are not human empirical evidence that consciousness has been measured.

## Reader path

1. [Validation Atlas](docs/validation-atlas.md) for the complete visual V1-V15 sequence.
2. [Formal Validation V1-V5](docs/formal-validation-program.md) for identification, coverage, transport, dependence, and structural testing.
3. [Formal Validation V6-V10](docs/formal-validation-program-v6-v10.md) for finite calibration uncertainty, missingness, conditioning, heterogeneous sites, and abstention.
4. [Formal Validation V11-V15](docs/formal-validation-program-v11-v15.md) for exact resolution laws, multisite identification, design sample size, and independent release gating.
5. [Machine-readable results](results/README.md) for the canonical CSV and JSON records.
6. [V1-V5 runner](scripts/run_validation_program.py), [V6-V10 runner](scripts/run_robustness_validation.py), and [V11-V15 runner](scripts/run_identification_design_validation.py) to regenerate the result record and figures.
7. [Source package](src/consciousness_measurement) and [tests](tests) for the executable implementation and regression checks.

## Fifteen formal stages

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
- under the declared V15 fixed-seed pilot gate, planned confirmatory `n=900` proceeds in `47.625%` of runs, and every identified confirmatory interval in that canonical run covers the true latent prevalence.

The V15 simulation value is a finite fixed-seed check, not the theorem itself. The theorem-level coverage statement follows from independence of the pilot release event and the confirmatory interval construction.

The exact values are stored under [`results/`](results/). Downstream analysis should use the machine-readable records rather than rounded prose values.

## Reproduce

```bash
python -m pip install -e ".[dev]"
python scripts/run_validation_program.py
python scripts/run_robustness_validation.py
python scripts/run_identification_design_validation.py
make check
```

Canonical seeds are `20260917` for V1-V5, `20260918` for V6-V10, and `20260919` for V11-V15 fixed-seed checks.

## Scientific boundary

Passing V1-V15 means that the mathematics and software behave as declared under the stated analytic assumptions and synthetic data-generating models. It does not establish empirical calibration for a human, animal, organoid, or artificial system; it does not identify qualia; and it does not settle the ontology of consciousness. Those remain separate empirical and theoretical burdens.
