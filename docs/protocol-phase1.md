# Phase 1 Preregisterable Protocol: Cross-State Consciousness Measurement Benchmark

## Purpose

This protocol is the first prospective benchmark for the repository. It is designed to answer a narrower question than the hard problem:

> Which candidate measurements preserve calibrated relationships with declared experiential targets when consciousness, responsiveness, arousal, attention, and report demands are deliberately dissociated?

This document is a research blueprint. Any human study requires institutional ethics approval, medical oversight where interventions are involved, and a site-specific statistical analysis plan.

## 1. Primary aims

### Aim 1 - Cross-state transport

Test whether candidate neural and physiological features learned in ordinary wakefulness retain predictive/calibration value across sleep and clinically supervised altered states.

### Aim 2 - Report confound separation

Test whether candidate signatures survive removal, delay, or alteration of overt report requirements.

### Aim 3 - Multimodal incremental value

Test whether a preregistered multimodal model improves held-out calibration relative to the strongest single channel.

### Aim 4 - Structural correspondence

In communicative conditions, test whether a preregistered neural relational geometry predicts held-out phenomenal similarity structure.

## 2. Primary measurement targets

The study must not use the word "consciousness" as an unlabeled binary endpoint. Primary targets are:

- **content availability:** trial-level report of a defined percept or experience;
- **connectedness:** evidence that experience is related to the external environment;
- **responsiveness:** ability to produce intentional task-linked output;
- **phenomenal structure:** similarity relations among reported experiences;
- **perturbational capacity:** complexity/propagation of the cortical response to a controlled perturbation where available.

Presence as a latent target is analyzed only through an explicit measurement model combining these anchors.

## 3. Cohorts and conditions

A staged design is recommended.

### Cohort A - Healthy waking participants

Within-subject conditions:

- clearly visible/perceptible stimuli;
- near-threshold stimuli;
- masking or rivalry paradigms;
- report versus matched no-report blocks;
- attention and working-memory control manipulations.

### Cohort B - Sleep

Repeated NREM/REM awakenings with immediate structured experience sampling. Analyses must distinguish "no recall" from "no experience".

### Cohort C - Medically supervised altered state

Where ethically and operationally appropriate, use more than one pharmacological mechanism because a marker that tracks one drug may track drug physiology rather than consciousness. Protocol-specific safety and clinical procedures remain outside this repository.

## 4. Measurements

Core synchronized measurements:

- high-density EEG where feasible;
- ECG and respiration;
- ocular/pupillary signals when eyes are available for measurement;
- electrodermal activity where feasible;
- stimulus/task event markers;
- trial-level report and confidence in communicative conditions.

Optional nested substudies:

- MEG or fMRI;
- TMS-EEG;
- source-localized EEG;
- intracranial recordings only in independently justified clinical research settings.

## 5. Candidate feature families

Feature families must be preregistered at the family level before confirmatory evaluation:

- spectral power and spectral slope;
- entropy/algorithmic-complexity proxies;
- functional/effective connectivity;
- metastability and dynamical repertoire;
- perturbational complexity/propagation;
- representational geometry;
- task-decoding features;
- autonomic and ocular features.

The study should compare families, not cherry-pick one favorable metric after seeing the test data.

## 6. Primary confirmatory endpoints

### Endpoint E1 - Held-out content calibration

For a predefined subset of communicative trials, evaluate whether predicted probability of reportable content is calibrated on held-out participants.

### Endpoint E2 - Report-operation invariance

Estimate the change in candidate signal when report requirements change while stimulus/perceptual conditions are matched. A marker proposed as consciousness-specific should not be explainable entirely by motor/report preparation.

### Endpoint E3 - Cross-state transport loss

For each feature/model, define

\[
\Delta_{\mathrm{transport}}
=
\mathcal L_{\mathrm{new\ state}}-\mathcal L_{\mathrm{reference}},
\]

where \(\mathcal L\) is a preregistered proper scoring loss. Smaller transport loss is better, but only within the target being tested.

### Endpoint E4 - Multimodal incremental value

Compare the locked multimodal model with the best locked single-channel model using held-out log score/Brier score and calibration. Improvement must be demonstrated prospectively.

### Endpoint E5 - Phenomenal-neural geometry prediction

Fit the mapping only on a training subset of experience labels and test preregistered relational predictions on held-out experience pairs. Report alignment, normalized distortion, and permutation-based evidence.

## 7. Key dissociation tests

The protocol is deliberately designed around cases that can falsify simplistic measurement rules:

- experience with minimal overt report;
- motor output failure despite preserved cognition;
- high arousal without rich experience;
- vivid dreaming despite environmental disconnection;
- dissociative states in which responsiveness and experience diverge;
- unconscious or preconscious processing that produces task-relevant neural signals.

A candidate measure that cannot survive these dissociations is not a general consciousness measure.

## 8. Analysis split

Use three non-overlapping partitions whenever sample size permits:

1. **discovery** - feature engineering and exploratory models;
2. **internal confirmation** - locked pipeline, held-out participants;
3. **external confirmation** - held-out site or independently collected dataset.

Repeated measures must remain grouped by participant during splitting.

## 9. Exclusion and quality control

Predefine:

- recording-quality thresholds;
- minimum usable duration/trial count;
- artifact rules;
- stimulation-quality rules for perturbational data;
- protocol deviations;
- missing-data handling;
- criteria for an uninterpretable channel.

Quality failure must produce `uninterpretable`, not a negative consciousness label.

## 10. Success criteria for Phase 1

Phase 1 succeeds scientifically if it yields any of the following with prospective support:

- a feature/model that generalizes across states and report manipulations;
- a documented dissociation showing a popular marker is not target-specific;
- evidence that multimodal fusion adds calibrated information;
- a reproducible phenomenal-neural structural correspondence;
- a clear non-identifiability result showing current measurements are insufficient.

A negative result is therefore informative if the protocol has enough power and the measurement assumptions are explicit.

## 11. Required publication package

Publish:

- preregistration;
- deidentified data or a justified controlled-access route;
- preprocessing and analysis code;
- complete model specifications;
- all confirmatory outcomes, including nulls;
- quality-control exclusions;
- calibration plots;
- sensitivity analyses;
- a machine-readable claim table linking each conclusion to its evidence and assumptions.
