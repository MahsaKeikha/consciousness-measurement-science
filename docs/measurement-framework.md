# Formal Measurement Framework

## 1. Variables

Let

- \(E_t\): latent experiential state at time \(t\);
- \(Y_t\): experiential content/structure when reportable;
- \(R_t\): first-person report;
- \(B_t\): overt intentional behavior;
- \(N_t\): passive neural measurements;
- \(P_t\): perturbational response;
- \(A_t\): autonomic/ocular physiology;
- \(I_t\): intervention;
- \(C_t\): context and confound variables.

A generic measurement model is

\[
p(R,B,N,P,A\mid E,Y,I,C,\theta).
\]

The central scientific problem is whether \(E\) and/or \(Y\) are identifiable from observed data under a defensible assumption set \(\mathcal A\).

## 2. Identification region

Instead of assuming point identification, define

\[
\mathcal I_E(D,\mathcal A)
=
\left\{e:\exists\theta\in\Theta(\mathcal A)
\text{ such that }p(D\mid E=e,\theta)>0\right\}.
\]

If \(\mathcal I_E\) contains multiple experiential states, the data are insufficient to uniquely identify the target.

## 3. Evidence channels

Each channel \(j\) has a context-dependent measurement model

\[
p(O_j\mid E,C,\theta_j).
\]

Reliability parameters must be externally estimated where possible. Combining channels requires a dependence model; naive multiplication of likelihood ratios is valid only under conditional independence.

## 4. Multidimensional global state

We avoid assuming a one-dimensional “level.” Let a measured global-state vector be

\[
G_t=(g_{\text{arousal}},g_{\text{connectedness}},g_{\text{complexity}},g_{\text{availability}},g_{\text{stability}},\ldots).
\]

These dimensions are measurements or model constructs, not definitions of consciousness.

## 5. Causal tests

For candidate mechanism \(M\), a causal claim requires interventions that change \(M\) while controlling alternative pathways.

Potential interventions include TMS, anesthetic manipulation, sensory masking, targeted stimulation, and clinically appropriate pharmacological or neuromodulatory changes.

A mechanism that tracks consciousness but does not respond as predicted under intervention is demoted from causal candidate to correlate/confound until explained.

## 6. Report model

Reports are noisy evidence:

\[
p(R\mid E,Y,C)\neq 1.
\]

Sources of report error include memory, criterion shifts, demand, language, deception, metacognitive noise, and motor failure.

This is not a reason to discard report. It is a reason to model it.

## 7. Claim outputs

The final system should output one of:

- **identified within model**;
- **bounded/partially identified**;
- **evidence favors preserved conscious processing**;
- **evidence favors absence under validated scope**;
- **inconclusive because assay sensitivity or assumptions are insufficient**;
- **model rejected**.

It should never output ontological certainty from an unvalidated classifier score.
