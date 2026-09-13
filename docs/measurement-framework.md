# Formal Measurement Framework

This document defines the mathematical objects used throughout the repository. It is intentionally general enough to represent behavioral, neural, physiological, perturbational, structural, and clinical research without declaring any one observable to be consciousness.

## 1. Variables

For time \(t\), let:

- \(E_t\): latent experiential presence or state target;
- \(Y_t\): experiential content or phenomenal structure when defined;
- \(R_t\): first-person report;
- \(B_t\): overt intentional behavior;
- \(N_t\): passive neural measurements;
- \(P_t\): perturbational response;
- \(A_t\): autonomic or ocular physiology;
- \(I_t\): intervention;
- \(C_t\): context, acquisition conditions, and confounds.

A generic measurement model is

\[
p(R,B,N,P,A\mid E,Y,I,C,\theta).
\]

The central statistical question is whether \(E\) and/or \(Y\) are identifiable from the observed data under a defensible assumption set \(\mathcal A\).

## 2. Target-specific measurement

The symbol \(E\) should not be read as one universal binary consciousness variable in every analysis. The repository distinguishes:

- presence;
- global state;
- content;
- phenomenal structure;
- capacity.

A model must state which target it addresses and what other constructs are intentionally outside scope.

## 3. Identification region

Instead of assuming point identification, define

\[
\mathcal I_E(D,\mathcal A)
=
\left\{e:\exists\theta\in\Theta(\mathcal A)
\text{ such that }p(D\mid E=e,\theta)>0\right\}.
\]

If \(\mathcal I_E\) contains multiple experiential states, the observed evidence and assumptions do not uniquely identify the target.

A useful scientific result can therefore be:

- point identification;
- interval identification;
- partial identification;
- non-identification.

Non-identification is not analysis failure when it correctly reflects the limits of the evidence.

## 4. Evidence channels

Each evidence channel \(j\) has a context-dependent measurement model

\[
p(O_j\mid E,Y,C,\theta_j).
\]

where \(O_j\) may represent report, behavior, spontaneous neural data, task-evoked neural data, perturbational response, or physiology.

Every channel interpretation requires:

- a target;
- a validation domain;
- acquisition quality;
- an uncertainty model;
- a sensitivity model if negative evidence is interpreted;
- a confound model.

## 5. Multimodal fusion

For channels \(Y_1,\ldots,Y_K\), a generic fused model is

\[
p(E\mid Y_1,\ldots,Y_K,C)
\propto
p(E\mid C)
\,p(Y_1,\ldots,Y_K\mid E,C).
\]

The conditional-independence factorization

\[
p(Y_1,\ldots,Y_K\mid E,C)
=
\prod_{k=1}^{K}p(Y_k\mid E,C)
\]

is a special assumption, not a default truth. Shared dependence on arousal, medication, site, pathology, stimulus, or task can make naive fusion overconfident.

When dependence is uncertain, report sensitivity intervals, alternative dependence models, or partial-identification regions.

## 6. Multidimensional global state

The project does not assume that all states can be represented by one scalar level. Let

\[
G_t=
(g_{\mathrm{arousal}},
 g_{\mathrm{connectedness}},
 g_{\mathrm{complexity}},
 g_{\mathrm{availability}},
 g_{\mathrm{stability}},
 \ldots).
\]

These dimensions are measurements or model constructs, not definitions of consciousness.

A scalar summary may be useful within a validated domain, but it must not erase clinically or scientifically meaningful dissociations.

## 7. Report model

Reports are noisy evidence rather than perfect ground truth:

\[
p(R\mid E,Y,C)\neq 1.
\]

Potential report errors include:

- memory distortion;
- criterion shifts;
- demand characteristics;
- language limitations;
- deception;
- metacognitive noise;
- motor failure;
- report delay.

This does not make report disposable. It means report should be modeled, timed, and compared with no-report controls where appropriate.

## 8. Imperfect reference standards

Clinical and experimental validation often lacks a perfect gold standard.

If reference variable \(Z\) is itself noisy,

\[
p(Z\mid E,C)\neq 1,
\]

then sensitivity and specificity estimated against \(Z\) are not automatically sensitivity and specificity for \(E\).

Possible approaches include:

- multimodal triangulation;
- latent-class or imperfect-reference models;
- sensitivity analysis over reference-standard error;
- explicit restriction of the claim to prediction of \(Z\) rather than experience.

## 9. Negative evidence

A negative observation \(O_j^-\) can lower support for \(E\) only if the channel has validated negative sensitivity in the relevant domain.

Formally, a useful negative channel requires the likelihood ratio

\[
LR_j^-=
\frac{p(O_j^-\mid E=1,C)}{p(O_j^-\mid E=0,C)}
\]

to be estimable or bounded well enough to interpret. If task failure, acquisition failure, or domain shift makes this quantity unknown, the correct output is inconclusive rather than evidence for absence.

## 10. Causal tests

For a candidate mechanism \(M\), observational association

\[
M\leftrightarrow E
\]

is weaker than an intervention claim.

A causal test ideally asks whether

\[
p(E\mid do(M=m_1),C)
\neq
p(E\mid do(M=m_0),C),
\]

while controlling plausible alternative pathways.

Potential interventions include TMS, anesthetic manipulation, sensory masking, targeted stimulation, and clinically appropriate pharmacological or neuromodulatory changes.

A mechanism that tracks consciousness but fails its preregistered intervention prediction should be demoted from causal candidate until the failure is explained.

## 11. Necessary, sufficient, enabling, and correlated roles

A mechanism should be classified by the strongest role actually tested.

- **Necessary:** the target does not occur without the mechanism in the declared scope.
- **Sufficient:** inducing the mechanism is enough to produce the target in the declared scope.
- **Enabling:** the mechanism permits the target but is not enough by itself.
- **Correlated:** the mechanism tracks the target without a stronger causal claim.

These are logically different and require different study designs.

## 12. Temporal measurement

Consciousness-related evidence can change on different timescales. A model should therefore declare the target interval \([t_0,t_1]\) and the observation windows used to infer it.

Temporal mismatch can create false disagreement when:

- report is delayed;
- state transitions occur during averaging;
- physiology integrates over a longer window than neural signals;
- an intervention has delayed effects.

Time alignment is an explicit assumption in the [Assumption Registry](assumption-registry.md).

## 13. Structural measurement

For phenomenal structure, define a relational space

\[
(\mathcal E,d_E)
\]

and a physical or neural relational space

\[
(\mathcal N,d_N).
\]

A mapping family \(f:\mathcal N\rightarrow\mathcal E\) is tested with preregistered metrics such as alignment or distortion.

The repository's simple normalized distortion is

\[
D(f)=\frac{1}{|\mathcal P|}
\sum_{(i,j)\in\mathcal P}
\left|
\tilde d_E(e_i,e_j)-\tilde d_N(n_i,n_j)
\right|.
\]

A successful mapping establishes predictive structural correspondence under the declared model. It does not establish ontological identity.

## 14. Decision states

The measurement system may output:

- **evidence-supporting**;
- **evidence-opposing**;
- **mixed/dissociated**;
- **inconclusive**.

These are evidence states, not metaphysical labels.

## 15. Allowed inferential outputs

Depending on evidence and assumptions, the final analysis may state:

- identified within model;
- bounded or partially identified;
- evidence favors preserved conscious processing;
- evidence opposes the target under a validated bidirectional model;
- channels are mixed or dissociated;
- inconclusive because sensitivity, quality, domain match, or assumptions are insufficient;
- measurement model rejected;
- tested theory proposition rejected;
- structural mapping supported or rejected.

It should never output ontological certainty from an unvalidated classifier score.

## 16. Relation to the CEP and claim ladder

The formal model feeds the [Consciousness Evidence Profile](measurement-instrument-spec.md), which records evidence and assumptions. The [Claim Registry](claim-registry.md) then limits public conclusions to the strongest M0-M7 level actually earned.

The [Assumption Registry](assumption-registry.md) and [Failure Modes](failure-modes.md) specify what must be challenged before stronger levels are accepted.
