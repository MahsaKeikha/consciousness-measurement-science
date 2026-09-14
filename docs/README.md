# Documentation Map

This directory is the reader-facing specification for the Consciousness Measurement Science program. The documents are intentionally modular so that a reader can distinguish epistemology, measurement theory, experimental design, statistics, theory testing, clinical translation, ethics, and software implementation.

## Recommended reading path

### 1. Orientation

- [Start Here](start-here.md): plain-language explanation of the measurement problem and how the repository is organized.
- [Glossary](glossary.md): definitions for targets, evidence channels, claim levels, and common methodological terms.
- [Epistemic Boundaries](epistemic-boundaries.md): direct and indirect access, correlation versus causation, report, and theory neutrality.

### 2. Measurement specification

- [Formal Measurement Framework](measurement-framework.md): latent targets, observed evidence, identification regions, causal tests, and allowed outputs.
- [Consciousness Evidence Profile](measurement-instrument-spec.md): structured multimodal evidence instrument.
- [Assumption Registry](assumption-registry.md): assumptions that must be named before an inference is trusted.
- [Failure Modes](failure-modes.md): ways a consciousness-measurement claim can fail even when the analysis is technically correct.
- [Claim Registry](claim-registry.md): M0-M7 claim language and machine-readable claim records.

### 3. Experimental program and statistical identification

- [Phase 1 Protocol](protocol-phase1.md): first preregisterable cross-state benchmark.
- [Preregistration Template](preregistration-template.md): required declarations before confirmatory analysis.
- [Experimental Program](experimental-program.md): staged empirical program from healthy benchmarks to theory tournaments.
- [Statistical Validation](statistical-validation.md): calibration, transport, partial identification, uncertainty, multiplicity, and abstention.
- [Dependence-Robust Partial Identification](partial-identification.md): sharp marginal-only bounds for multimodal evidence when conditional dependence is unknown.

### 4. Phenomenal structure and theory comparison

- [Phenomenal Structure](phenomenal-structure.md): relational measurement of experience and physical-neural structure.
- [Theory Landscape](theory-landscape.md): candidate theory families and their empirical commitments.
- [Falsification Matrix](falsification-matrix.md): what would count against tested theory propositions.
- [Literature Map](literature.md): curated primary and methodological sources.

### 5. Translation and boundaries

- [Clinical Translation](clinical-translation.md): disorders-of-consciousness evidence stack and clinical limits.
- [Ethics](ethics.md): false positives, false negatives, privacy, consent, governance, and communication of uncertainty.
- [Edge Cases](edge-cases.md): infants, animals, organoids, and artificial systems.

### 6. Reproducibility and implementation

- [Software Guide](software-guide.md): package structure, intended use, and worked code examples.
- [Reproducibility](reproducibility.md): environment, provenance, analysis freezing, seeds, data lineage, and release package.
- [Repository Policy](repository-policy.md): publication, style, link, schema, figure, and claim-discipline rules.

## What is specification versus evidence?

A major source of confusion in research repositories is mixing a proposed method with a validated result. This project marks that distinction explicitly.

**Specification** means the rule, model, protocol, schema, or test has been defined. It does not imply that human data have validated it.

**Empirical evidence** means the rule or model has been evaluated on data under a declared protocol.

**External validation** means the analysis has been evaluated on data not used to develop the model, ideally from an independent site.

**Clinical validation** requires additional prospective evidence, regulatory consideration, operational reliability, and specialist oversight. Nothing in this repository is currently a clinical diagnostic instrument.

## Machine-readable companion files

The prose documents are paired with machine-readable files where practical:

- `../schemas/cep.schema.json`: CEP record schema;
- `../examples/cep_example.json`: worked CEP example;
- `../schemas/claim.schema.json`: claim record schema;
- `../examples/claim_example.json`: worked claim example;
- `../scripts/verify_repository_policy.py`: repository-wide publication verifier.

The root [README](../README.md) remains the canonical public entry point.
