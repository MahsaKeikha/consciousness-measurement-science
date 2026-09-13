# Consciousness Evidence Profile (CEP): Measurement Instrument Specification

## Status

**CEP is a research instrument specification, not a validated clinical device.**

The purpose of CEP is to prevent a recurring category error in consciousness science: collapsing heterogeneous evidence about presence, state, content, structure, and capacity into one number before the measurement model has been validated.

CEP therefore begins as a structured evidence object rather than a universal scalar.

## 1. Measurement object

For subject or system \(s\), time window \(t\), target \(\tau\), and context \(c\), define

\[
\operatorname{CEP}(s,t,\tau,c)
=
\left(\mathbf v,\mathbf q,\mathbf u,\mathcal A,\mathcal D,\Gamma\right),
\]

where:

- \(\mathbf v\) is the vector of channel-level evidence values;
- \(\mathbf q\) records data-quality and interpretability flags;
- \(\mathbf u\) records uncertainty for each channel and any fused estimate;
- \(\mathcal A\) is the explicit assumption set required for interpretation;
- \(\mathcal D\) is the validation domain in which the mapping was established;
- \(\Gamma\) is the allowed claim level on the repository's M0-M7 ladder.

The target \(\tau\) must be one of:

1. presence;
2. global state;
3. content;
4. phenomenal structure;
5. capacity.

No CEP result is valid without a declared target.

## 2. Core evidence channels

The initial instrument admits at least the following channel families:

| Symbol | Channel | Example observables | Main failure mode |
|---|---|---|---|
| \(R\) | first-person report | content, confidence, similarity judgment | unavailable, memory/report distortion |
| \(B\) | intentional behavior | command following, forced choice | motor/language failure |
| \(N\) | spontaneous neural data | EEG complexity, spectra, connectivity, fMRI networks | confounding by arousal, pathology, hardware |
| \(P\) | perturbational response | TMS-EEG complexity/effective propagation | stimulation/preprocessing dependence |
| \(A\) | autonomic/ocular physiology | pupil, eye movement, EDA, ECG, respiration | weak specificity, systemic confounds |
| \(X\) | task-evoked covert response | motor imagery EEG/fMRI, semantic signatures | low sensitivity, task comprehension |

A channel is not considered *negative evidence for absence* merely because its detector failed. Negative interpretation requires separately justified sensitivity in the relevant context.

## 3. Required metadata for every channel

Every channel result must carry:

- acquisition protocol and hardware;
- preprocessing version;
- artifact and quality-control status;
- validation population;
- target against which it was validated;
- sensitivity/specificity or calibrated predictive distribution when available;
- missingness mechanism when relevant;
- time stamp and temporal window;
- confounds known to affect the signal;
- whether the channel was used for model discovery or held-out validation.

## 4. Decision states

CEP has four top-level inferential states:

- **evidence-supporting**: data support the declared target claim under stated assumptions;
- **evidence-opposing**: data oppose the target claim under a validated bidirectional measurement model;
- **mixed/dissociated**: channels provide materially conflicting evidence;
- **inconclusive**: data quality, sensitivity, validation domain, or model identifiability is insufficient.

The instrument must never convert `inconclusive` into `absent` for convenience.

## 5. Fusion rule

Let \(Y_k\) denote observations from channel \(k\). A fused latent-state model has the generic form

\[
p(E\mid Y_1,\ldots,Y_K,C)
\propto
p(E\mid C)
\,p(Y_1,\ldots,Y_K\mid E,C).
\]

The factorization

\[
p(Y_1,\ldots,Y_K\mid E,C)=\prod_k p(Y_k\mid E,C)
\]

is **not** assumed by default. Conditional independence is a special model that must be tested or justified. Shared noise, arousal, injury severity, medication, and site effects can create strong dependence between channels.

When dependence is uncertain, the preferred outputs are sensitivity intervals, partial-identification regions, or alternative model results rather than overconfident posterior probabilities.

## 6. Scalar-score gate

A scalar score \(S=g(\operatorname{CEP})\) may be published only after all of the following are satisfied:

1. the target is fixed and explicitly named;
2. the score is prospectively defined before confirmatory testing;
3. calibration is demonstrated on held-out participants;
4. transport is demonstrated at held-out sites;
5. performance is tested across at least two mechanistically different consciousness manipulations;
6. major confounds have dedicated negative controls;
7. an abstention region is prespecified;
8. the scalar adds information beyond its strongest component channel;
9. clinically relevant thresholds, if any, are independently validated;
10. the score's failure modes are published.

Until those conditions are met, the vector profile is scientifically preferable to a single number.

## 7. Example profile schema

```text
target: presence
context: disorders-of-consciousness / bedside day 4
channels:
  behavioral:
    result: no reproducible command following
    quality: adequate
    negative_sensitivity: insufficient for absence claim
  task_eeg:
    result: positive motor-imagery response
    quality: adequate
    validation_domain: covert command following
  resting_eeg:
    result: intermediate complexity
    quality: adequate
  tms_eeg:
    result: unavailable
  autonomic:
    result: interpretable but nonspecific
fusion:
  state: mixed/dissociated
  allowed_claim: evidence for covert cognitive command following
  forbidden_claim: direct measurement of qualia
uncertainty: explicit
assumptions: listed
```

## 8. Validation endpoints

CEP validation should report more than AUROC. At minimum:

- calibration curve and calibration slope/intercept;
- sensitivity and specificity with confidence intervals when a defensible reference is available;
- positive and negative likelihood ratios;
- Brier/log score for probabilistic outputs;
- abstention rate;
- failure-to-acquire and failure-to-interpret rates;
- subgroup/site performance;
- decision-curve analysis only for a prespecified decision context;
- sensitivity to channel dependence and prior assumptions.

## 9. Scientific boundary

CEP is a formalized evidence architecture. Even a perfectly calibrated CEP would establish a reliable relation between measurements and declared experiential targets. It would not, by itself, explain why physical processes are accompanied by experience or establish the ontology of consciousness.
