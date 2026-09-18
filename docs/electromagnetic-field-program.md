# Electromagnetic Field Measurement Program

## Research III V16-V20

This program adds electromagnetic observables as a **candidate evidence channel** inside the existing Research III measurement architecture.

The scientifically supportable claim is narrow:

> Electromagnetic recordings can quantify physical and neural field dynamics. Those observables can be tested as predictors, correlates, or causal-response markers for a declared consciousness target after calibration and validation.

The program does **not** assume that electromagnetic field strength, power, coherence, complexity, or any other field descriptor is consciousness itself. It also does not assume that an electromagnetic theory of consciousness is correct.

That distinction is essential. EEG and MEG are established measurements of electrical and magnetic consequences of neural population activity, and perturbational EEG methods have shown useful state-sensitive validation. Electromagnetic-field theories of consciousness are active theoretical proposals, but they are not established measurement laws.

## Measurement model

Let the underlying electromagnetic state over space and time be

\[
\mathcal F(\mathbf r,t)=\{\mathbf E(\mathbf r,t),\mathbf B(\mathbf r,t)\}.
\]

A sensor array does not observe the full field directly. It observes a hardware- and geometry-dependent projection

\[
\mathbf X(t)=\mathcal M(\mathcal F)(t)+\boldsymbol\eta(t),
\]

where \(\mathcal M\) contains sensor transfer functions, source-to-sensor geometry, referencing, filtering, shielding, and other acquisition effects, and \(\boldsymbol\eta\) collects environmental and instrumental contamination.

The first Research III electromagnetic feature vector is

\[
\Phi_{EM}
=
\left(
H_f,
C_\phi,
r_{\mathrm{eff}},
H_{SV},
\rho_{CM}
\right),
\]

where:

- \(H_f\) is normalized spectral entropy;
- \(C_\phi\) is sensor-phase concentration at a preregistered frequency;
- \(r_{\mathrm{eff}}\) is covariance effective rank;
- \(H_{SV}\) is normalized singular-value entropy of the sensor-time matrix;
- \(\rho_{CM}\) is the common-mode variance fraction.

These are **field-organization descriptors**. They are not consciousness scores.

## V16. Physical-field sanity layer

For electric field \(\mathbf E\) and magnetic field \(\mathbf B\), the code implements the vacuum electromagnetic energy density

\[
u
=
\frac{1}{2}
\left(
\epsilon_0\lVert \mathbf E\rVert^2
+
\frac{\lVert \mathbf B\rVert^2}{\mu_0}
\right)
\]

and Poynting vector

\[
\mathbf S
=
\frac{1}{\mu_0}\mathbf E\times\mathbf B.
\]

These functions are physical unit and implementation checks. They are **not** asserted to be direct scalp-brain quantities in conductive biological tissue, where a forward model and medium properties are required.

## V17. Gain-invariant organization features

A useful organization descriptor should not change simply because the amplifier gain or global signal scale changes.

For nonzero scalar \(a\),

\[
H_f(a\mathbf X)=H_f(\mathbf X),
\qquad
C_\phi(a\mathbf X)=C_\phi(\mathbf X),
\]

and covariance effective rank and normalized singular entropy are likewise invariant to global amplitude scaling.

The deterministic V17 record verifies this across gains 0.1, 1, and 10.

## V18. Matched-power non-identifiability

V18 constructs two eight-sensor fields with identical single-frequency power in every channel.

One field is phase aligned:

\[
x_k(t)=\sin(2\pi f t).
\]

The second is phase balanced:

\[
x_k(t)=
\sin\left(
2\pi f t+\frac{2\pi k}{K}
\right).
\]

Channelwise Fourier power is the same, yet

\[
C_\phi^{\mathrm{aligned}}=1,
\qquad
C_\phi^{\mathrm{balanced}}\approx0.
\]

The canonical run has maximum relative channel-power difference below \(3\times10^{-16}\), while phase concentration changes from 1 to numerical zero.

### Result

**Power alone does not identify spatial field organization.**

This is directly relevant to consciousness measurement because a field-based research program that reports only amplitude or band power can miss relational structure that is mathematically distinct at the same power.

## V19. Common-mode confound

A shared environmental source, reference artifact, field spread, or other common input can create apparent sensor-wide organization.

The synthetic stress test adds

\[
x'_k(t)=x_k(t)+a\,c(t)
\]

to an otherwise phase-balanced array.

As shared amplitude \(a\) rises from 0 to 2, raw phase concentration rises from numerical zero to about 0.935, even though the underlying sensor-specific phase pattern was not changed.

After exact common-mode removal in this deliberately controlled construction, the concentration returns to numerical zero.

### Result

**Sensor-level phase organization is not interpretable without nuisance, reference, field-spread, and environmental controls.**

Common-average removal is used here only as a synthetic diagnostic. It is not proposed as a universal correction for EEG or MEG.

## V20. Frequency-specific field structure

A single multichannel signal can be strongly aligned at one frequency and phase balanced at another.

The canonical two-frequency construction gives

\[
C_\phi(10\,\mathrm{Hz})=1,
\qquad
C_\phi(17\,\mathrm{Hz})\approx0.
\]

### Result

**Electromagnetic organization must be specified in frequency, space, time, and acquisition context. It should not be compressed into an unqualified scalar.**

## Proposed empirical measurement arm

For a human benchmark, the EM arm should be evaluated as part of the existing multimodal program rather than in isolation.

### Acquisition

As feasible:

- high-density EEG with complete reference and impedance metadata;
- MEG or OPM-MEG in shielded and environmentally monitored settings;
- TMS-EEG for perturbational response;
- ECG, EOG, respiration, motion, and environmental field reference channels;
- synchronized report, no-report, stimulus, and state markers.

### Predeclared controls

At minimum:

- line-noise and environmental-field characterization;
- reference/montage sensitivity;
- volume-conduction or field-spread analysis;
- sensor-motion sensitivity;
- source-reconstruction sensitivity where justified;
- amplitude-matched comparisons;
- frequency-specific analyses;
- positive and negative controls;
- repeated-state and held-out participant validation.

### Candidate outcomes

The first empirical study should ask whether a preregistered EM feature vector predicts a **declared target** such as global state, perceptual content, or perturbational capacity better than strong baseline models.

It should not ask whether a large value of one EM statistic means that a subject or system "has more consciousness."

## Extension to nonbiological systems

The same measurement architecture can be applied to artificial or engineered systems only at the level of observables.

For a candidate system:

1. characterize its native electric and magnetic emissions;
2. separate source-generated fields from power-supply, clock, radio, and environmental interference;
3. measure spatial, temporal, spectral, and perturbational organization;
4. test reproducibility under matched computational or behavioral conditions;
5. establish an independent target and validation anchor before making any consciousness-related inference.

High field strength, high coherence, high entropy, or high complexity alone does not establish consciousness.

## Claim ceiling

Before prospective validation, V16-V20 support only:

- **M0 physical/measurement claims** about electromagnetic observables and controlled synthetic differences;
- **measurement-design claims** about invariance, non-identifiability, frequency specificity, and confounding.

They do not yet support M1-M7 empirical consciousness claims.

A future EM result can move upward only through the existing Research III ladder: out-of-sample prediction, transport, confound separation, causal perturbation, multimodal identification, held-out phenomenal-structure prediction, or unique theory discrimination.

## Falsification criteria

The EM arm should be demoted or rejected for a declared target if:

- performance disappears under amplitude matching;
- results collapse after environmental/reference controls;
- the effect is explained by field spread or a common source;
- calibration fails across states, sites, or hardware;
- a strong non-EM baseline performs equally well;
- the feature does not survive held-out participants or conditions;
- perturbation fails to change the feature in the preregistered direction;
- a theory-specific EM prediction fails while a rival prediction survives.

## Literature anchors

- He B et al. Electrophysiological source imaging: a noninvasive window to brain dynamics. The EEG/MEG forward problem relates neuronal current sources to measured electric potentials and magnetic fields.
- Yang Y et al. Overview of magnetoencephalography in basic principle and clinical application. 2024. MEG directly measures magnetic fields generated by neuronal currents with high temporal resolution.
- Casali AG et al. A theoretically based index of consciousness independent of sensory processing and behavior. Science Translational Medicine. 2013;5(198):198ra105. doi:10.1126/scitranslmed.3006294.
- Casarotto S et al. Stratification of unresponsive patients by an independently validated index of brain complexity. Annals of Neurology. 2016;80(5):718-729. doi:10.1002/ana.24779.
- Bastos AM, Schoffelen JM. A tutorial review of functional connectivity analysis methods and their interpretational pitfalls. Common reference, field spread, signal-to-noise, and common-input effects can create misleading connectivity estimates.
- Jones MW, Hunt T. Electromagnetic-field theories of qualia: can they improve upon standard neuroscience? 2023. Reviews multiple EM-field theories and their unresolved strengths and weaknesses.
- Hunt T et al. Editorial: Electromagnetic field theories of consciousness. 2024. Frames EM theories as an active but unsettled theory class.

## Reproducibility

Source:

- `src/consciousness_measurement/electromagnetic_observables.py`
- `src/consciousness_measurement/electromagnetic_simulations.py`

Tests:

- `tests/test_electromagnetic_observables.py`
- `tests/test_electromagnetic_simulations.py`

Runner:

```bash
python scripts/run_electromagnetic_validation.py
```

Canonical machine-readable outputs:

- `results/v17_em_scale_invariance.csv`
- `results/v19_common_mode_confound.csv`
- `results/v20_frequency_specific_structure.csv`
- `results/electromagnetic_validation_summary.json`

Canonical visual:

![Research III V16-V20 electromagnetic validation](figures/v16_v20_electromagnetic_validation.svg)

The entire V16-V20 record is analytic or synthetic. No result in this section is human empirical evidence that consciousness has been measured.
