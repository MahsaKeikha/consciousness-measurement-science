# Falsification Matrix for Competing Consciousness Hypotheses

## Purpose

A consciousness theory becomes scientifically useful when it risks being wrong. This matrix prevents the repository from treating every interesting brain signal as generic support for every theory.

The rows below are **hypothesis families**, not claims that the repository endorses any one theory. Exact predictions must be instantiated from primary theory papers before a confirmatory experiment.

| Hypothesis family | Distinctive empirical burden | Evidence that would count against the tested version | Common confound to exclude |
|---|---|---|---|
| Global neuronal workspace | conscious access should involve theory-specified widespread/global availability or ignition | robust conscious content without the predicted global-access signature under adequate measurement; predicted ignition present for demonstrably unconscious processing | report, working memory, motor preparation |
| Integrated causal structure | conscious capacity/content should track theory-specified irreducible causal organization | matched experiential states with large predicted integration changes but no experiential change, or high theory metric in validated unconscious systems/states | generic complexity, network size, estimator bias |
| Recurrent processing | recurrent/local feedback should be required for conscious perceptual content | reliable conscious content during selective disruption of the required recurrent process; recurrence preserved in matched unconscious processing | attention and late report processes |
| Higher-order/metacognitive | consciousness should require an appropriate higher-order representation or metacognitive relation | robust conscious experience with selective loss of the postulated higher-order representation while first-order processing remains matched | confidence, decision criterion, memory |
| Dynamical/critical regime | consciousness should occupy a specific rich/metastable dynamical regime | validated conscious states outside the proposed regime or validated unconscious states inside it | arousal, SNR, pharmacology-specific dynamics |
| Structural correspondence | relations among experiences should map systematically to relations in a physical/causal representation | preregistered held-out phenomenal relations repeatedly fail to match the proposed physical structure despite adequate reliability | shared stimulus geometry or semantics |
| Fundamental/dual-aspect bridge | a specific bridge law should make predictions not reducible to ordinary correlational neuroscience | bridge law adds no discriminating prediction, or unique predictions fail | unfalsifiable relabeling of physical variables |
| Quantum-specific necessity | uniquely quantum variables/processes should be necessary or improve prediction beyond classical accounts | classical models reproduce all declared effects, or disruption of the claimed quantum resource leaves conscious target unchanged | generic stochasticity, decoherence-free speculation |

## 1. Theory-neutral nulls first

Before comparing theories, test simpler explanations:

\[
\text{candidate signature}
\leftarrow
\{
\text{arousal, attention, report, memory, movement, sensory strength, pathology, medication}
\}.
\]

A theory comparison is uninterpretable if these alternatives have not been addressed.

## 2. Precommitment template

Every confirmatory theory test should preregister:

1. the exact theoretical proposition;
2. the operational variable representing it;
3. the predicted direction, location, and time window;
4. the minimum effect or equivalence region that matters;
5. a rival theory's divergent prediction;
6. positive and negative controls;
7. what result would be counted as failure;
8. what auxiliary assumptions could rescue the theory and whether those assumptions were independently tested.

## 3. Failure is not automatically theory death

A failed prediction can result from:

- the theory being wrong;
- a bad operationalization;
- low measurement reliability;
- an auxiliary assumption failing;
- insufficient perturbation strength;
- an underpowered test.

Therefore each outcome must state which layer was actually falsified. However, repeatedly modifying auxiliary assumptions only after unfavorable data is seen must not be counted as successful prediction.

## 4. Structural hypothesis-specific falsification

For a proposed physical representation \(Z\) and phenomenal geometry \(d_E\), preregister a mapping class \(\mathcal F\). Define held-out distortion

\[
D^* = \min_{f\in\mathcal F} D_{\mathrm{heldout}}(f).
\]

A strong structural claim requires:

- reliable phenomenal geometry across repeated judgments;
- held-out, not in-sample, alignment;
- controls for stimulus geometry and semantics;
- cross-subject or subject-specific predictions declared in advance;
- perturbational tests when causal structure is claimed.

If \(D^*\) remains above the preregistered tolerance despite adequate reliability and power, that mapping family is rejected.

## 5. Model-selection output

The preferred output is a table rather than a winner-takes-all slogan:

```text
prediction                     GNW    IIT    RPT    HOT    structural
---------------------------------------------------------------------
P1 preregistered outcome       pass   n/a    fail   n/a    n/a
P2 preregistered outcome       fail   pass   n/a    n/a    n/a
P3 held-out geometry           n/a    n/a    n/a    n/a    pass
...
```

The repository should preserve failed predictions permanently. A theory leaderboard is useful only if the evidential rules are stable before the results are known.
