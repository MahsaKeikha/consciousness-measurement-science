# Consciousness Measurement Science

## A theory-neutral, multimodal, causal, and structural research program

**Repository release:** v0.2.0 foundational measurement architecture.

**Scientific status:** research specification and computational scaffold. This repository is not a clinical device, does not claim to have solved the hard problem, and does not assume in advance that consciousness is physical, nonphysical, emergent, fundamental, dual-aspect, or reducible to one signal.

The central question is:

> **What observations, interventions, mathematical structures, assumptions, and validation standards would justify a scientific measurement claim about consciousness?**

![Consciousness measurement architecture](docs/figures/measurement_architecture.svg)

The project separates **experience itself** from the **evidence used to infer it**. Reports, behavior, neural activity, physiology, perturbational responses, complexity, connectivity, or any theory-specific quantity may become evidence for a declared target after validation. None is defined to be consciousness by fiat.

## Start here

For a first reading, use this path:

1. [Start Here](docs/start-here.md) - plain-language explanation.
2. [Research Questions](RESEARCH_QUESTIONS.md) - the questions and what would count as progress.
3. [Epistemic Boundaries](docs/epistemic-boundaries.md) - what can and cannot be inferred.
4. [Formal Measurement Framework](docs/measurement-framework.md) - latent targets, observables, identification, and causality.
5. [Consciousness Evidence Profile specification](docs/measurement-instrument-spec.md) - target-specific multimodal evidence architecture.
6. [Assumption Registry](docs/assumption-registry.md) and [Failure Modes](docs/failure-modes.md) - hidden dependencies and ways the inference can fail.
7. [Phase 1 Protocol](docs/protocol-phase1.md), [Experimental Program](docs/experimental-program.md), and [Statistical Validation](docs/statistical-validation.md) - the empirical path.
8. [Phenomenal Structure](docs/phenomenal-structure.md), [Theory Landscape](docs/theory-landscape.md), and [Falsification Matrix](docs/falsification-matrix.md) - structural and theory-comparison arms.
9. [Roadmap](ROADMAP.md) - staged deliverables and exit criteria.

The complete documentation map is in [docs/README.md](docs/README.md), and recurring terms are defined in the [Glossary](docs/glossary.md).

---

## The measurement problem

Let \(E\) denote the experiential target. Let \(R\) denote first-person report, \(B\) overt intentional behavior, \(N\) neural measurements, \(P\) perturbational responses, \(A\) autonomic or ocular physiology, \(I\) interventions, and \(C\) context and confounds.

Science observes

\[
D=(R,B,N,P,A,I,C),
\]

but does not directly observe another subject's \(E\) in the same way.

The program therefore asks

\[
\boxed{
\text{Given }D\text{ and explicit assumptions }\mathcal A,
\text{ what can be identified, bounded, predicted, or falsified about }E?
}
\]

This makes three things mandatory: a declared target, an explicit evidence model, and visible assumptions. When the evidence does not identify one conclusion, the allowed output is a bound, competing explanations, abstention, or an inconclusive result.

## Five targets that must remain distinct

| Target | Scientific question | Example anchors | Main warning |
|---|---|---|---|
| **Presence** | Is there evidence that any experience is occurring? | reliable report, covert command following, state and perturbational evidence | one failed channel is not proof of absence |
| **Global state** | What multidimensional condition is the system in? | arousal, connectedness, complexity, stability, availability | do not force every state onto one scalar ladder |
| **Content** | What is being experienced? | trial report, discrimination, decoding, structured behavior | stimulus decoding is not automatically experience decoding |
| **Phenomenal structure** | What relations hold among experiences? | similarity, ordering, discriminability, experiential geometry | structural correspondence is not ontological identity |
| **Capacity** | Does the system have organization associated with supporting experience? | causal organization, perturbational response, recurrent dynamics | capacity is not the same as a currently occurring content |

A measure validated for one target cannot automatically be promoted to another.

## Evidence channels

| Channel | What it can support | What it cannot establish alone |
|---|---|---|
| First-person report | experienced content when communication is reliable | third-person access to qualia as such |
| Intentional behavior | command following and discrimination | absence of experience when motor output fails |
| Task EEG/fMRI | covert task performance and content-related responses | universal absence of consciousness when negative |
| Resting EEG/MEG/fMRI | state-dependent spectra, complexity, connectivity, and networks | a direct reading of subjective feel |
| TMS-EEG / PCI family | perturbational capacity for differentiated and integrated response | a universal metaphysical cutoff |
| Autonomic and ocular signals | covert state or content clues | a unique consciousness-specific signature in every context |
| Lesion, stimulation, pharmacology | causal constraints on mechanisms | a complete explanation of why experience exists |

A rigorous measurement program therefore needs triangulation, causal interventions, cross-context validation, explicit uncertainty, and theory comparison.

## Research Arm A: target-specific state and content inference

The initial evidence object is a vector rather than one universal number:

\[
\mathbf V=(V_R,V_B,V_N,V_P,V_A).
\]

The proposed **Consciousness Evidence Profile (CEP)** records channel values, quality, uncertainty, assumptions, validation domain, and the strongest claim supported by the evidence:

\[
\operatorname{CEP}(s,t,\tau,c)
=(\mathbf v,\mathbf q,\mathbf u,\mathcal A,\mathcal D,\Gamma).
\]

The CEP permits four top-level evidence states: supporting, opposing, mixed/dissociated, and inconclusive. It is intentionally a structured profile before it is a scalar.

### Negative evidence rule

A negative detector output is not automatically evidence of absence. It can count against a target only when negative sensitivity is validated for the relevant person, context, task, acquisition, and analysis domain. Otherwise the result remains missing, uninterpretable, or inconclusive.

### Multimodal fusion

A generic fusion model is

\[
p(E\mid Y_1,\ldots,Y_K,C)
\propto p(E\mid C)p(Y_1,\ldots,Y_K\mid E,C).
\]

Conditional independence is not assumed by default. Shared dependence on arousal, medication, injury severity, site, stimulus, or task can make naive multiplication of evidence strongly overconfident.

## Research Arm B: phenomenal-structure measurement

![Phenomenal structural measurement pipeline](docs/figures/structural_measurement_pipeline.svg)

The phrase "fabric of consciousness" is treated as a research question, not as a declaration about substance. For communicative participants, the program constructs a phenomenal relational space

\[
(\mathcal E,d_E)
\]

from similarity, discriminability, ordering, and structured report, and a physical or neural relational space

\[
(\mathcal N,d_N)
\]

from population activity, effective connectivity, perturbational responses, or representational geometry.

A preregistered mapping \(f:\mathcal N\to\mathcal E\) can be tested using alignment and distortion. One simple statistic is

\[
D(f)=\frac{1}{|\mathcal P|}
\sum_{(i,j)\in\mathcal P}
\left|\tilde d_E(e_i,e_j)-\tilde d_N(n_i,n_j)\right|.
\]

Low distortion supports the declared correspondence family; high distortion rejects it. Neither result by itself establishes that neural structure is identical to experience.

## Necessary, sufficient, enabling, and correlated

Candidate mechanisms are classified by the strongest role actually tested:

- **necessary:** removing the condition eliminates the target within the declared scope;
- **sufficient:** producing the condition produces the target within the declared scope;
- **enabling:** the condition permits the target but is not enough by itself;
- **correlated:** the condition tracks the target but may be a prerequisite, consequence, or confound.

Prediction, causation, and ontological identity are different claims.

## Candidate hypothesis families

The program keeps global-workspace, integrated-causal-structure, recurrent-processing, higher-order/metacognitive, dynamical/critical, structural-correspondence, fundamental/dual-aspect, and quantum-specific hypotheses distinct. Each must be translated into risky empirical predictions before confirmatory testing. A quantum-specific proposal has the additional burden of predicting results not adequately captured by relevant classical alternatives.

## Measurement claim ladder

![Measurement claim ladder](docs/figures/claim_ladder.svg)

| Level | Strongest allowed claim |
|---|---|
| M0 | signal or behavior differs across conditions |
| M1 | signal predicts a validated report or behavioral target out of sample |
| M2 | relation generalizes across participants or sites within a declared domain |
| M3 | relation transports across distinct consciousness manipulations |
| M4 | relation survives confound controls and causal perturbation tests |
| M5 | multimodal model identifies or bounds a latent experiential target under explicit assumptions |
| M6 | preregistered physical-to-phenomenal structural prediction succeeds on held-out relations |
| M7 | a unique theory prediction survives while relevant rivals fail |

A smaller p-value cannot move a result up this ladder. Claim level is determined by design and validation.

## Minimum empirical program

The staged program includes healthy waking benchmarks, threshold and no-report paradigms, NREM and REM sleep, multiple anesthesia mechanisms, dissociative states, explicit confound manipulations, perturbational studies, multicenter disorders-of-consciousness validation, phenomenal geometry, multimodal partial-identification models, adversarial theory tests, and separate transfer criteria for infants, animals, organoids, and artificial systems.

See [Experimental Program](docs/experimental-program.md), [Phase 1 Protocol](docs/protocol-phase1.md), [Preregistration Template](docs/preregistration-template.md), and [Roadmap](ROADMAP.md).

## Statistical validation requirements

Strong claims require more than in-sample discrimination. The program requires, as appropriate, participant-level and site-level holdout, calibration, proper scoring rules, hierarchical uncertainty, transport tests, measurement invariance, negative and positive controls, missingness analysis, channel-dependence sensitivity, multiplicity control, abstention, strong baselines, and partial-identification analysis.

See [Statistical Validation](docs/statistical-validation.md).

## Clinical and ethical boundary

Disorders of consciousness are treated as a critical validation domain, not a shortcut to a binary classifier. Behavioral and task-based neural measures both have false-negative pathways, so discordance itself can be informative. The project requires serial standardized assessment, confound review, multimodal evidence, repeat testing when appropriate, and explicit uncertainty.

See [Clinical Translation](docs/clinical-translation.md) and [Ethics](docs/ethics.md).

Nothing in this repository is intended to guide withdrawal of life support, replace specialist clinical evaluation, establish legal capacity, or function as a diagnostic medical device.

## Machine-readable research objects

The repository pairs prose commitments with machine-readable objects:

- [CEP schema](schemas/cep.schema.json) and [CEP example](examples/cep_example.json);
- [Claim schema](schemas/claim.schema.json) and [Claim example](examples/claim_example.json);
- [Claim Registry](docs/claim-registry.md);
- [Assumption Registry](docs/assumption-registry.md);
- [Failure Modes](docs/failure-modes.md).

Future stable claim records belong under [claims/](claims/README.md).

## Reproducible software scaffold

The Python package contains auditable research utilities for calibrated binary evidence, CEP records, and structural alignment. It is not a clinical classifier.

```bash
python -m pip install -e ".[dev]"
make check
```

Read the [Software Guide](docs/software-guide.md), [Reproducibility](docs/reproducibility.md), [Data Policy](data/README.md), and [Repository Policy](docs/repository-policy.md). Contributions should follow [CONTRIBUTING.md](CONTRIBUTING.md).

## Current implementation status

### Implemented now

- five-target taxonomy;
- formal latent-target measurement model;
- explicit epistemic and ontological boundaries;
- CEP specification and JSON schema;
- M0-M7 claim ladder and machine-readable claim schema;
- Assumption Registry and Failure Modes;
- preregistration template and Phase 1 protocol;
- cross-state experimental program;
- statistical validation and partial-identification rules;
- phenomenal-structure framework;
- theory landscape and falsification matrix;
- clinical, ethical, data, and edge-case boundaries;
- software utilities, unit tests, and repository publication checks.

### Not yet established

The repository does **not** yet contain prospective human evidence validating a general consciousness measure, a clinically approved instrument, a universal threshold, a substrate-independent scalar, or a completed adversarial theory tournament. These are empirical milestones, not documentation gaps.

## Complete documentation

- [Documentation Map](docs/README.md)
- [Start Here](docs/start-here.md)
- [Research Questions](RESEARCH_QUESTIONS.md)
- [Glossary](docs/glossary.md)
- [Epistemic Boundaries](docs/epistemic-boundaries.md)
- [Formal Measurement Framework](docs/measurement-framework.md)
- [Consciousness Evidence Profile](docs/measurement-instrument-spec.md)
- [Assumption Registry](docs/assumption-registry.md)
- [Failure Modes](docs/failure-modes.md)
- [Claim Registry](docs/claim-registry.md)
- [Phase 1 Protocol](docs/protocol-phase1.md)
- [Preregistration Template](docs/preregistration-template.md)
- [Experimental Program](docs/experimental-program.md)
- [Statistical Validation](docs/statistical-validation.md)
- [Phenomenal Structure](docs/phenomenal-structure.md)
- [Theory Landscape](docs/theory-landscape.md)
- [Falsification Matrix](docs/falsification-matrix.md)
- [Clinical Translation](docs/clinical-translation.md)
- [Ethics](docs/ethics.md)
- [Edge Cases](docs/edge-cases.md)
- [Literature Map](docs/literature.md)
- [Software Guide](docs/software-guide.md)
- [Reproducibility](docs/reproducibility.md)
- [Data Policy](data/README.md)
- [Repository Policy](docs/repository-policy.md)
- [Schemas Guide](schemas/README.md)
- [Examples Guide](examples/README.md)
- [Claims Guide](claims/README.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

## Scientific north star

The aim is to make consciousness measurement progressively harder to fool: harder to fool with behavior, harder to fool with one biomarker, harder to fool with theory-confirming analysis, harder to fool with hidden assumptions, harder to fool with data leakage, and harder to fool with elegant mathematics that lacks discriminating empirical predictions.

If a broadly valid consciousness measure is possible, this program aims to define the evidence required to earn that claim. If available observations and assumptions cannot identify the target, the program should make that limitation scientifically visible rather than manufacture certainty.
