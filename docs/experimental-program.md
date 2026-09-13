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
