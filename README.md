# Consciousness Measurement Science

## A theory-neutral, multimodal, causal, and structural research program

**Status:** foundational research program and computational scaffold. This repository is not a clinical device, does not claim to have solved the hard problem, and does not assume in advance that consciousness is physical, nonphysical, emergent, fundamental, dual-aspect, or reducible to any one measurable signal.

This project asks a concrete measurement-science question:

> **What observations, interventions, mathematical structures, assumptions, and validation standards would justify a scientific claim about consciousness?**

The project begins from an epistemic asymmetry. A subject has first-person access to their own experience. An external investigator observes reports, behavior, neural activity, physiological signals, perturbational responses, and the consequences of interventions. A scientifically responsible consciousness measure therefore has to make the bridge from observable evidence to an experiential target explicit rather than hiding that bridge inside a score.

![Consciousness measurement architecture](docs/figures/measurement_architecture.svg)

## Start here

If this is your first visit, read the repository in this order:

1. [Start Here](docs/start-here.md) for the plain-language logic of the project.
2. [Research Questions](RESEARCH_QUESTIONS.md) for the scientific questions the program is designed to answer.
3. [Epistemic Boundaries](docs/epistemic-boundaries.md) for what the project can and cannot infer.
4. [Formal Measurement Framework](docs/measurement-framework.md) for the mathematical object being measured.
5. [Consciousness Evidence Profile specification](docs/measurement-instrument-spec.md) for the proposed evidence architecture.
6. [Phase 1 protocol](docs/protocol-phase1.md) and [Experimental Program](docs/experimental-program.md) for the empirical path.
7. [Statistical Validation Plan](docs/statistical-validation.md) for calibration, generalization, partial identification, and uncertainty.
8. [Phenomenal Structure Program](docs/phenomenal-structure.md) for the structural arm of the project.
9. [Theory Landscape](docs/theory-landscape.md) and [Falsification Matrix](docs/falsification-matrix.md) for theory comparison.
10. [Roadmap](ROADMAP.md) for staged deliverables and completion criteria.

A complete documentation index is available in [docs/README.md](docs/README.md). Definitions are collected in the [Glossary](docs/glossary.md).

---

## The central measurement problem

Let

- \(E\) denote the experiential target;
- \(R\) denote first-person report;
- \(B\) denote overt intentional behavior;
- \(N\) denote neural measurements;
- \(P\) denote perturbational responses;
- \(A\) denote autonomic and ocular physiology;
- \(I\) denote interventions;
- \(C\) denote context, confounds, and acquisition conditions.

Science observes

\[
D=(R,B,N,P,A,I,C),
\]

but does not directly observe another subject's experience \(E\).

The core question is therefore

\[
\boxed{
\text{Given }D\text{ and explicit assumptions }\mathcal A,
\text{ what can be identified, bounded, predicted, or falsified about }E?
}
\]

This formulation forces the project to make three things visible:

1. **the target** - what exactly is being claimed about experience;
2. **the evidence model** - how observations are related to that target;
3. **the assumptions** - what must be true for the inference to be valid.

When those ingredients are insufficient for a unique answer, the correct scientific output is not a forced binary label. It is an identification region, competing explanations, an abstention, or an inconclusive result.

---

## What exactly is being measured?

The repository separates five targets that are often mixed together in the literature:

| Target | Core question | Typical anchors | Common category error |
|---|---|---|---|
| **Presence** | Is there evidence that any experience is occurring? | report when available, covert command following, state markers, perturbational capacity | treating one failed channel as proof of absence |
| **Global state** | What multidimensional condition is the system in? | arousal, connectedness, complexity, stability, cognitive availability | compressing all states into one universal level |
| **Content** | What is being experienced? | trial-level report, decoding, discrimination, structured behavior | confusing decoding of stimuli with decoding of experience |
| **Phenomenal structure** | What relations hold among experiences? | similarity, ordering, discriminability, report geometry | assuming matched neural geometry is ontological identity |
| **Capacity** | Does the system have organization capable of supporting experience? | causal organization, perturbational response, recurrent dynamics | equating capacity with a currently occurring content |

A measure validated for one target cannot automatically be promoted to another.

---

## The evidence architecture

Current consciousness science provides many useful measurements, but each one occupies a different evidential layer.

| Evidence channel | What it can support well | What it cannot establish by itself |
|---|---|---|
| First-person report | experienced content when communication is reliable | direct third-person access to qualia |
| Intentional behavior | command following, discrimination, communication | absence of experience when motor output fails |
| Task EEG/fMRI | covert command following and content-related activity | universal absence of consciousness when negative |
| Resting EEG/MEG/fMRI | state-dependent complexity, connectivity, spectra, network organization | a direct reading of subjective feel |
| TMS-EEG / PCI family | perturbational capacity for differentiated, integrated cortical responses | a universal metaphysical cutoff |
| Autonomic and ocular signals | covert evidence when overt report is unavailable | a unique consciousness-specific signature across all settings |
| Lesion, stimulation, pharmacology | causal constraints on candidate mechanisms | a complete explanation of why experience exists |

The project therefore requires **triangulation, causal intervention, cross-context validation, explicit uncertainty, and theory comparison**.

---

## Two research arms

### Arm A: state and content inference

The first arm asks how multiple evidence channels can support target-specific inferences without collapsing everything into a single score.

The initial evidence vector is

\[
\mathbf V=(V_R,V_B,V_N,V_P,V_A).
\]

Each component carries its own data-quality flag, uncertainty, validation domain, confounds, and negative-evidence rules. The repository's proposed instrument is the **Consciousness Evidence Profile (CEP)**:

\[
\operatorname{CEP}(s,t,\tau,c)
=
(\mathbf v,\mathbf q,\mathbf u,\mathcal A,\mathcal D,\Gamma),
\]

where \(s\) is the subject or system, \(t\) is the time window, \(\tau\) is the declared target, \(c\) is context, \(\mathbf v\) is the channel evidence vector, \(\mathbf q\) contains quality and interpretability, \(\mathbf u\) contains uncertainty, \(\mathcal A\) is the assumption set, \(\mathcal D\) is the validation domain, and \(\Gamma\) is the strongest allowed claim level.

The CEP is intentionally a structured profile before it is a scalar.

### Arm B: phenomenal-structure measurement

![Phenomenal structural measurement pipeline](docs/figures/structural_measurement_pipeline.svg)

The second arm asks whether the relational structure of experience can be measured and compared with physical or neural relational structure without assuming that the two are identical.

For communicative participants, define a phenomenal relational space

\[
(\mathcal E,d_E)
\]

from similarity judgments, discrimination, ordering, and structured report. Define a physical or neural relational space

\[
(\mathcal N,d_N)
\]

from neural population activity, effective connectivity, perturbational response, or representational geometry.

A candidate mapping \(f:\mathcal N\to\mathcal E\) can be tested using a preregistered distortion statistic such as

\[
D(f)=\frac{1}{|\mathcal P|}
\sum_{(i,j)\in\mathcal P}
\left|
\tilde d_E(e_i,e_j)-\tilde d_N(n_i,n_j)
\right|.
\]

Low distortion supports the declared mapping family. High distortion rejects that mapping family. Neither result alone establishes that the neural structure is experience.

---

## Scientific role taxonomy

Candidate mechanisms are classified by role rather than by enthusiasm:

- **necessary**: removing the condition eliminates the target within the declared scope;
- **sufficient**: producing the condition produces the target within the declared scope;
- **enabling**: the condition permits the target but is not enough by itself;
- **correlated**: the condition tracks the target but may be prerequisite, consequence, or confound.

This prevents the repository from treating a predictive marker as a mechanism or a mechanism as an ontological identity.

---

## Candidate theory and ontology families

The program does not select one ontology in advance. It asks what unique empirical burden each account accepts.

| Family | Candidate commitment | Measurement strategy | Status in this project |
|---|---|---|---|
| Global workspace | widespread availability or broadcast | ignition, long-range coupling, access and report | testable, theory-dependent |
| Integrated causal structure | irreducible cause-effect organization | perturbation, integration, differentiation, causal structure | testable, theory-dependent |
| Recurrent processing | recurrent or feedback processing | timing, laminar and recurrent signatures, masking | testable, theory-dependent |
| Higher-order / metacognitive | representation of lower-order states | confidence, metacognition, prefrontal signatures | testable, theory-dependent |
| Dynamical / critical | rich metastable recurrent dynamics | complexity, entropy, criticality, effective connectivity | testable, non-unique |
| Structural correspondence | phenomenal relations mirrored by physical relations | geometry, topology, optimal transport, sheaf or category methods | central structural arm |
| Fundamental / dual-aspect | experiential properties are basic or dual-aspect | requires unique bridge laws and discriminating predictions | open, not assumed |
| Quantum-specific | uniquely quantum mechanism is necessary | must predict effects not captured by relevant classical models | open, high evidential burden |

The [Falsification Matrix](docs/falsification-matrix.md) records what would count against a tested version of each family.

---

## Measurement claim ladder

![Measurement claim ladder](docs/figures/claim_ladder.svg)

The repository uses a conservative M0-M7 claim ladder.

| Level | Allowed claim |
|---|---|
| **M0** | A signal, behavior, or feature differs between declared experimental conditions. |
| **M1** | A locked model predicts a validated report or behavioral target out of sample. |
| **M2** | The relation generalizes across participants or sites inside a declared domain. |
| **M3** | The relation generalizes across distinct consciousness manipulations or states. |
| **M4** | The relation survives confound controls and causal perturbation tests. |
| **M5** | A multimodal model identifies or bounds a latent experiential target under explicit assumptions. |
| **M6** | A preregistered physical structure predicts held-out phenomenal structure. |
| **M7** | A candidate theory makes a unique preregistered prediction that survives while relevant rivals fail. |

No level by itself licenses the statement that qualia have been directly measured.

The [Claim Registry](docs/claim-registry.md), [claim schema](schemas/claim.schema.json), and [worked claim example](examples/claim_example.json) make this discipline machine-readable.

---

## Negative evidence rule

A failed test is not automatically evidence of absent experience.

Negative evidence is scientifically meaningful only when all of the following are sufficiently characterized for the relevant context:

- the assay has demonstrated sensitivity to the declared target;
- acquisition quality is adequate;
- the participant or system could in principle produce the measured response;
- major confounds have been assessed;
- the model's false-negative behavior is known;
- the validation domain includes the present use case.

If these conditions fail, the result is **uninterpretable or inconclusive**, not negative evidence for absence.

This rule is especially important in severe brain injury, sleep, paralysis, sedation, sensory impairment, and any situation in which report or motor behavior can fail independently of experience.

---

## Minimum empirical program

The empirical program progresses from benchmark conditions to increasingly difficult tests:

1. healthy waking with trial-level report;
2. perceptual threshold, masking, rivalry, and matched no-report conditions;
3. NREM and REM sleep with awakening reports;
4. multiple anesthetic mechanisms rather than a single drug;
5. dissociative states in which responsiveness and experience can decouple;
6. explicit manipulation of attention, memory, report, movement, sensory strength, and arousal;
7. perturbational studies such as TMS-EEG where appropriate;
8. disorders of consciousness with serial standardized behavioral assessment and multimodal neurophysiology;
9. phenomenal geometry with held-out structural prediction;
10. adversarial theory tests with preregistered divergent predictions;
11. transfer analyses for infants, animals, organoids, and artificial systems.

The full staged plan is in [Experimental Program](docs/experimental-program.md), [Phase 1 Protocol](docs/protocol-phase1.md), and [Roadmap](ROADMAP.md).

---

## Statistical requirements

A candidate measurement model is not accepted because it has a high in-sample accuracy or an attractive visualization. Confirmatory evidence requires, as appropriate:

- participant-level and site-level holdout;
- calibration, not only discrimination;
- proper scoring rules;
- uncertainty intervals;
- measurement invariance checks;
- transport to new states and hardware;
- sensitivity to missing data and channel dependence;
- negative and positive controls;
- multiplicity control;
- abstention behavior;
- comparison with strong single-channel baselines;
- partial-identification analysis when the latent target is not point identified;
- prospective preregistration of confirmatory endpoints.

See [Statistical Validation Plan](docs/statistical-validation.md).

---

## Clinical boundary

The repository treats disorders of consciousness as a scientifically and ethically important validation domain, not as a shortcut to a binary consciousness classifier.

Large multicenter evidence has shown that some patients who show no observable command following at the bedside can nevertheless show task-based brain responses. The reverse problem also exists: a negative brain test can occur in people who can behaviorally follow commands. This means that behavioral and brain-based channels both have false-negative pathways and that discordance itself carries information.

The repository therefore requires serial behavioral assessment, confound control, repeated testing where appropriate, multimodal evidence, and explicit uncertainty. See [Clinical Translation](docs/clinical-translation.md) and [Ethics](docs/ethics.md).

Nothing in this repository is intended to guide withdrawal of life support, replace specialist clinical evaluation, or function as a diagnostic medical device.

---

## Reproducible computational scaffold

The package currently contains three intentionally small, auditable components:

- `evidence.py` implements likelihood-ratio updates under an explicit conditional-independence assumption;
- `profile.py` implements target-specific CEP records with an explicit inconclusive state and conservative negative-evidence rules;
- `structural_alignment.py` implements distance matrices, relational alignment, normalized distortion, and permutation testing.

These are research scaffolds, not clinical classifiers.

Install and run:

```bash
python -m pip install -e ".[dev]"
make check
```

`make check` runs the unit tests, repository policy verifier, and Ruff. The complete reproducibility contract is in [docs/reproducibility.md](docs/reproducibility.md), and the software API is explained in [docs/software-guide.md](docs/software-guide.md).

---

## Machine-readable research objects

The repository is designed so that important scientific commitments can be checked by software rather than living only in prose.

| Object | File | Purpose |
|---|---|---|
| CEP schema | [schemas/cep.schema.json](schemas/cep.schema.json) | machine-readable evidence-profile contract |
| CEP example | [examples/cep_example.json](examples/cep_example.json) | worked nonclinical profile example |
| Claim schema | [schemas/claim.schema.json](schemas/claim.schema.json) | machine-readable M0-M7 claim record |
| Claim example | [examples/claim_example.json](examples/claim_example.json) | worked claim with assumptions and nonclaims |
| Repository policy | [scripts/verify_repository_policy.py](scripts/verify_repository_policy.py) | checks links, schemas, figures, and publication rules |

The [Assumption Registry](docs/assumption-registry.md) and [Failure Modes](docs/failure-modes.md) make hidden inferential dependencies explicit.

---

## Documentation map

### Foundations

- [Start Here](docs/start-here.md)
- [Research Questions](RESEARCH_QUESTIONS.md)
- [Glossary](docs/glossary.md)
- [Epistemic Boundaries](docs/epistemic-boundaries.md)
- [Formal Measurement Framework](docs/measurement-framework.md)
- [Assumption Registry](docs/assumption-registry.md)
- [Failure Modes](docs/failure-modes.md)

### Measurement architecture

- [Consciousness Evidence Profile specification](docs/measurement-instrument-spec.md)
- [Claim Registry](docs/claim-registry.md)
- [Machine-readable CEP schema](schemas/cep.schema.json)
- [Worked CEP example](examples/cep_example.json)
- [Machine-readable claim schema](schemas/claim.schema.json)
- [Worked claim example](examples/claim_example.json)

### Empirical program

- [Phase 1 Protocol](docs/protocol-phase1.md)
- [Preregistration Template](docs/preregistration-template.md)
- [Experimental Program](docs/experimental-program.md)
- [Statistical Validation Plan](docs/statistical-validation.md)
- [Clinical Translation](docs/clinical-translation.md)
- [Ethics](docs/ethics.md)
- [Edge Cases](docs/edge-cases.md)

### Theory and structure

- [Phenomenal Structure Program](docs/phenomenal-structure.md)
- [Theory Landscape](docs/theory-landscape.md)
- [Falsification Matrix](docs/falsification-matrix.md)
- [Literature Map](docs/literature.md)

### Implementation and governance

- [Software Guide](docs/software-guide.md)
- [Reproducibility](docs/reproducibility.md)
- [Data Policy](data/README.md)
- [Repository Policy](docs/repository-policy.md)
- [Schemas Guide](schemas/README.md)
- [Examples Guide](examples/README.md)
- [Claims Guide](claims/README.md)
- [Contributing](CONTRIBUTING.md)
- [Roadmap](ROADMAP.md)

---

## Current implementation status

### Implemented now

- target taxonomy: presence, global state, content, structure, capacity;
- explicit epistemic and ontological boundaries;
- formal latent-target measurement model;
- CEP specification and JSON schema;
- M0-M7 claim ladder;
- machine-readable claim schema and example;
- assumption registry and failure-mode registry;
- preregistration template;
- cross-state Phase 1 protocol;
- full experimental roadmap;
- theory falsification matrix;
- phenomenal-structure framework;
- statistical validation rules;
- clinical translation and ethics boundaries;
- edge-case standards for infants, animals, organoids, and AI;
- computational scaffolds for evidence fusion, CEP records, and structural alignment;
- unit tests and repository-wide publication checks.

### Not yet established

The repository does **not** yet contain prospective human data that validate a general consciousness measure, a clinically approved instrument, a universal threshold, a demonstrated substrate-independent scalar, or a completed adversarial theory tournament.

Those are empirical milestones, not documentation gaps. The [Roadmap](ROADMAP.md) states the evidence required before they can be claimed.

---

## What this project may eventually establish

A mature version of the program could support claims such as:

- a multimodal signature is a calibrated predictor of a declared experiential target across multiple altered states;
- a perturbational response is necessary for a defined class of conscious states within tested conditions;
- a candidate neural architecture is not sufficient because experience dissociates from it;
- a relational geometry of experience is predicted by a physical or causal representation with bounded distortion;
- one theory's unique prediction survives an adversarial test while relevant competitors fail;
- certain experiential claims remain non-identifiable from available third-person data.

Those would be strong scientific results even if the ultimate explanatory question of why experience exists remains open.

---

## What this project will not claim without new evidence

It will not claim that:

- consciousness has been proven nonphysical;
- consciousness has been reduced to a conventional state of matter;
- any current scalar metric equals consciousness;
- high complexity alone proves consciousness;
- a failed descriptor proves dualism, idealism, or panpsychism;
- a current AI system is conscious because it behaves intelligently;
- quantum mechanics is required merely because consciousness is mysterious;
- correlation closes the explanatory gap;
- a negative bedside, EEG, fMRI, or perturbational result proves absence of experience without validated sensitivity.

---

## Scientific north star

The goal is not to manufacture certainty where science does not yet have it.

The goal is to make consciousness measurement progressively harder to fool: harder to fool with behavior, harder to fool with one biomarker, harder to fool with theory-confirming analysis, harder to fool with hidden assumptions, harder to fool with data leakage, and harder to fool with elegant mathematics that lacks discriminating empirical predictions.

If a broadly valid consciousness measure is possible, this program aims to define the evidence required to earn that claim. If it is not possible under available observations and assumptions, the program should make that limitation scientifically visible.
