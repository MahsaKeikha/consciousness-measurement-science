# Experimental Program

This document translates the repository's measurement framework into a staged empirical program. The order matters: broad claims are not attempted before the measurement targets, failure modes, and validation rules have been specified.

## Phase 0. Measurement specification

Before collecting confirmatory data:

1. define the target: presence, global state, content, structure, or capacity;
2. specify allowed M0-M7 claim levels;
3. list relevant assumptions from the Assumption Registry;
4. list relevant failure modes;
5. preregister the primary endpoint;
6. define theory-specific and theory-neutral analyses separately;
7. define positive and negative controls;
8. define data-quality failure and abstention rules;
9. freeze confirmatory preprocessing.

Output: a complete preregistration and machine-readable proposed claim record.

## Phase 1. Healthy and cross-state benchmark

The first prospective benchmark is specified in [protocol-phase1.md](protocol-phase1.md).

Within-subject or carefully harmonized conditions should include:

- normal wakefulness;
- near-threshold perception;
- masking or rivalry;
- report versus matched no-report conditions;
- NREM and REM sleep with awakening reports;
- medically supervised sedation or anesthesia with more than one mechanism where appropriate;
- dissociative conditions where responsiveness and experience may decouple.

Acquire as feasible:

- high-density EEG;
- ocular and pupillary signals;
- ECG and respiration;
- electrodermal activity;
- synchronized event markers;
- trial-level report and confidence;
- MEG or fMRI subsets;
- TMS-EEG in dedicated sessions.

Primary goal: determine which candidate measurements preserve calibrated relationships with declared targets across dissociations.


## Cross-phase electromagnetic measurement arm

The [Electromagnetic Field Measurement Program](electromagnetic-field-program.md), [Electromagnetic Source Identifiability Program](electromagnetic-source-identifiability.md), [Electromagnetic Resolution and Information Program](electromagnetic-resolution-program.md), [Electromagnetic Design and Spatial Specificity Program](electromagnetic-design-spatial-specificity.md), and [Finite-Sample Electromagnetic Inference Program](electromagnetic-finite-sample-inference.md) form a cross-phase acquisition, source-modeling, resolution, design, inference, and falsification arm rather than a separate consciousness theory.

For EEG, MEG, OPM-MEG, or other electromagnetic recordings, preregister:

- the physical observable and sensor units;
- sensor geometry, reference or montage, shielding, filters, and hardware transfer functions;
- frequency bands or frequencies of interest before confirmatory analysis;
- the spatial scale at which phase, covariance, rank, entropy, or perturbational features are computed;
- environmental reference channels and line-noise characterization;
- ECG, EOG, respiration, motion, and other plausible physiological contaminants;
- source-space analysis only when its forward and inverse assumptions are declared;
- explicit lead-field rank, singular spectrum, conditioning, null-space, inverse resolution matrix, and source-leakage diagnostics when a source-space claim is central;\n- point-spread and cross-talk functions when a linear inverse is used and spatial-resolution claims are central;
- covariance-aware pairwise source-topography distinguishability for source-separation claims;
- Fisher-information design criteria when comparing sensor, modality, or montage choices;
- the target information fraction removed by declared nuisance projection;
- a predeclared forward-model uncertainty set and robust information lower bound when source-space sensitivity is central;
- the estimator used for source-amplitude inference and its exact weighting convention;
- whether sensor covariance is known, externally estimated, cross-fitted, regularized, or estimated from the same data;
- the number of independent or effective samples used for covariance estimation;
- uncertainty intervals with explicit calibration assumptions and held-out or simulation-based coverage checks;
- the complete source, time, frequency, state, and pipeline search family used for multiplicity control;
- dependence-aware maximum-statistic, permutation, random-field, or other justified search-wide error control when independent-test assumptions are not valid;
- sandwich or otherwise robust uncertainty checks when covariance-model mismatch could affect source-space precision;\n- sensor-noise covariance, covariance-estimation partition, and whitening policy;\n- acquisition sampling rate, analog and digital anti-alias filters, and declared analysis bandwidth;
- sensitivity to reference choice, head geometry, conductivity, sensor registration, source orientation, regularization, and inverse prior;
- EEG-only, MEG-only, and combined operator comparisons when multimodal electromagnetic data are available;
- amplitude-matched and spectral-power-matched controls when testing organization beyond power;
- field-spread, volume-conduction, common-reference, and common-input sensitivity analyses;
- participant-held-out and state-held-out validation;
- sensor-noise covariance estimation and covariance-estimation stability;
- whitening diagnostics or an explicitly justified alternative noise metric;
- inverse resolution matrices, point-spread functions, cross-talk functions, or equivalent source-resolution diagnostics when source localization is central;
- singular-value and condition-spectrum diagnostics for the declared forward operator;
- acquisition sample rate, hardware anti-alias filtering, and the confirmatory analysis bandwidth relative to Nyquist;
- source-space sensitivity to regularization, sensor deletion, and plausible covariance perturbations;
- held-out sensor prediction or another sensor-space check when competing source models have similar in-sample residuals.

The initial preregistered electromagnetic feature vector is

\[
\Phi_{EM}
=
(H_f,C_\phi,r_{\mathrm{eff}},H_{SV},\rho_{CM}),
\]

containing normalized spectral entropy, frequency-specific sensor-phase concentration, covariance effective rank, normalized singular-value entropy, and common-mode fraction.

This vector is a measurement representation, not a consciousness score. Its scientific value must be established separately for each declared target.

A future empirical EM result should be compared with at least:

1. a spectral-power-only baseline;
2. a strong non-EM or conventional neural baseline where available;
3. nuisance-only models built from environmental and physiological reference channels;
4. a model evaluated after field-spread or common-source controls;
5. an out-of-sample model on held-out participants, states, sessions, sites, or hardware.

A consciousness-related EM claim should be demoted if its apparent advantage disappears after any predeclared amplitude, reference, environmental, field-spread, source-inverse, forward-model, or transport control. A source-space claim should also be demoted if reasonable regularization or head-model perturbations produce materially different source conclusions without a corresponding change in sensor-space fit. It should also be demoted if the effect depends on poorly estimated noise covariance, substantial unresolved source leakage, an alias-prone acquisition band, or a weak singular direction whose inverse amplification dominates the source-space effect.


## Phase 2. Confound dissection

Manipulate or measure independently:

- attention;
- working-memory load;
- motor response requirement;
- report delay;
- sensory strength;
- arousal;
- expectation;
- medication effects where relevant.

A candidate measure should be demoted if these variables reproduce its full effect without corresponding target evidence.

## Phase 3. Benchmark reanalysis and transport

Use open datasets to test reproducibility and transport before claiming universality.

Required analyses:

- participant-held-out evaluation;
- cross-dataset evaluation;
- state-held-out evaluation where possible;
- site and hardware sensitivity;
- calibration;
- comparison with strong single-channel baselines;
- analysis of failure-to-acquire and failure-to-interpret rates.

Retrospective results remain retrospective even when the pipeline is rigorous.

## Phase 4. Phenomenal structure

In communicative participants:

- collect repeated similarity, ordering, or discriminability judgments;
- estimate reliability of phenomenal relational structure;
- construct matched neural or causal relational structure;
- preregister alignment and distortion metrics;
- fit mappings only on training relations;
- test held-out experiences and participants;
- compare stimulus-only and other confound geometries;
- perturb neural geometry where ethically possible and predict structural changes.

M6 requires held-out structural prediction, not only a post hoc visualization.

## Phase 5. Multimodal latent inference

Build models that preserve channel differences rather than averaging them away.

Required components:

- explicit dependence model;
- strong single-channel baselines;
- latent-target model;
- missingness model;
- uncertainty and partial identification;
- abstention region;
- external-site evaluation;
- ablation of individual channels;
- machine-readable CEP output.

A multimodal model should be retained only if it adds prospective information and remains calibrated.

## Phase 6. Causal perturbation

Use perturbation to distinguish passive association from causal relevance.

Candidate tools include:

- TMS-EEG;
- sensory perturbation;
- state-dependent stimulation;
- clinically justified pharmacology;
- invasive stimulation only within independently justified clinical research.

Each intervention must specify:

- intended mechanism;
- manipulation check;
- alternative pathways;
- target outcome;
- temporal prediction;
- safety and ethical constraints.

## Phase 7. Disorders of consciousness

A multicenter clinical-research program should include:

- serial CRS-R by trained examiners;
- medication and confound review;
- routine EEG and sleep-wake characterization;
- passive paradigms where appropriate;
- task EEG/fMRI for covert command following when feasible;
- resting quantitative measures;
- TMS-EEG or related perturbational measures in equipped centers;
- PET or resting-state fMRI where clinically justified;
- repeat sessions to address fluctuation.

Primary output: a target-specific multimodal evidence profile, not a binary label from one test.

## Phase 8. Adversarial theory tournament

For each theory proposition:

- state the proposition exactly;
- specify the operationalization;
- define predicted location, direction, and timing;
- define the minimum effect or pass region;
- state the rival prediction;
- state controls;
- list auxiliary assumptions;
- define failure conditions before confirmatory data access.

Use independent analysts or blinded analysis where feasible.

Publish nulls and theory failures. Do not reinterpret every outcome post hoc as support.

## Phase 9. Edge-case transfer

Evaluate transfer to:

- infants;
- nonhuman animals;
- organoids and engineered neural tissue;
- artificial systems.

Do not copy adult human thresholds across substrates. Define domain-specific anchors and state which invariance assumptions are required.

## Cross-phase success criteria

A phase can succeed scientifically by producing:

- a generalizing calibrated marker;
- a reproducible dissociation;
- evidence that multimodal fusion adds value;
- a failed popular marker under strong controls;
- a structural correspondence with held-out prediction;
- a causal result;
- a theory-discriminating result;
- a non-identifiability result;
- a well-characterized failure domain.

A null result is informative when the design has adequate sensitivity and the target and assumptions were fixed in advance.

## Required publication package

Every mature confirmatory study should release, subject to governance and licensing:

- preregistration;
- data-access statement;
- acquisition specification;
- preprocessing code and configuration;
- analysis code;
- model definitions;
- split manifests;
- quality-control exclusions;
- calibration and uncertainty outputs;
- all confirmatory outcomes, including nulls;
- sensitivity analyses;
- machine-readable claim records;
- explicit protocol deviations;
- updated limitations.
