# Research III Formal Validation V1-V10

This is the fastest entry point to the executable mathematical research layer of Research III.

Research III separates a declared latent measurement target from the observable channels used to study it. The formal validation program asks whether the proposed inference is identifiable, finite-sample valid, robust to dependence and transport failure, stable under inversion, honest about missingness and site heterogeneity, and capable of abstaining when precision is inadequate.

These are **analytic and synthetic validation results**. They test the measurement machinery. They are not human empirical evidence that consciousness has been measured.

## Reader path

1. [Validation Atlas](docs/validation-atlas.md) for the complete visual V1-V10 sequence.
2. [Formal Validation V1-V5](docs/formal-validation-program.md) for the first theorem and simulation layer.
3. [Formal Validation V6-V10](docs/formal-validation-program-v6-v10.md) for calibration-sample uncertainty, missingness, conditioning, site heterogeneity, and abstention.
4. [Machine-readable results](results/README.md) for the canonical CSV and JSON records.
5. [V1-V5 runner](scripts/run_validation_program.py) and [V6-V10 runner](scripts/run_robustness_validation.py) to regenerate the results and figures.
6. [Source package](src/consciousness_measurement) and [tests](tests) for the executable implementation and regression checks.

## Ten formal stages

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
| **V10** | When should the system refuse to release a precise estimate? | predeclared interval-width release rule with marginal erroneous-release control | abstention frontier plus empirical conditional-coverage diagnostic |

## Core equations

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

These equations are useful only inside their declared calibration and identification assumptions. The repository therefore tests the assumptions and their failure regimes instead of presenting the inverse formula as a universal consciousness score.

## Canonical result record

The committed fixed-seed experiments show, among other checks:

- finite-sample V2 coverage remains conservative while interval width contracts with sample size;
- naive conditional-independence fusion can report about `0.997` where the exact posterior in the declared shared-dependence construction is `0.84`;
- structural-alignment permutation testing stays near the declared null rejection level and reaches high power for strong planted alignment;
- V6 mean width contracts from about `0.960` at 50 calibration examples per class to about `0.281` at 2,500;
- unrestricted 30% missingness expands the canonical latent identified interval to width `0.400`;
- a Youden margin of `0.05` amplifies proxy-rate error by a factor of `20`;
- the same pooled proxy rate `0.45` can correspond to average latent prevalences from about `0.375` to `0.5625` in the canonical two-site construction;
- with maximum allowed interval width `0.28`, the canonical abstention experiment releases no estimates at deployment `n=750`, about 44.4% at `n=1000`, and all at `n=1500`.

For V10, marginal interval coverage controls the probability of an erroneous release, but does not automatically imply the same nominal coverage conditional on release. The simulation therefore reports conditional coverage among released intervals as a diagnostic rather than treating it as a theorem-level consequence.

The exact values are stored under [`results/`](results/). Do not copy rounded prose values into downstream analyses when the machine-readable values are available.

## Reproduce

```bash
python -m pip install -e ".[dev]"
python scripts/run_validation_program.py
python scripts/run_robustness_validation.py
make check
```

The two validation runners regenerate their result tables and SVG figures from fixed seeds. `make check` runs the repository policy, compilation, pytest suite, and Ruff.

## Scientific boundary

Passing these tests means that the mathematics and software behave as declared under the stated synthetic data-generating models. It does not establish empirical calibration for a human, animal, organoid, or artificial system; it does not identify qualia; and it does not settle the ontology of consciousness. Those are separate empirical burdens.
