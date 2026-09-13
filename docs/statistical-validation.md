# Statistical Validation Plan

The statistical objective is not to maximize one performance metric. It is to determine whether a measurement claim is calibrated, transportable, identifiable, robust to confounding, and honest about uncertainty.

## 1. Discovery, confirmation, and external validation

Exploratory feature engineering belongs in discovery data. Confirmatory evaluation uses a locked pipeline and held-out participants. Strong claims require external confirmation at a held-out site or on independently collected data.

Recommended partitions:

1. discovery;
2. internal confirmation;
3. external confirmation.

Repeated observations from the same participant must remain grouped during splitting unless a different structure is explicitly modeled and preregistered.

## 2. Unit of inference

The unit of resampling and uncertainty must match the scientific claim.

Examples:

- trial-level content prediction with participant-level generalization requires participant-aware evaluation;
- site transport requires site-level holdout;
- repeated awakening reports require hierarchical treatment of within-person dependence;
- electrode or voxel samples are not independent participants.

Pseudoreplication can make uncertainty appear far smaller than it is.

## 3. Calibration over headline accuracy

For probabilistic outputs report, as appropriate:

- calibration curve;
- calibration intercept and slope;
- Brier score;
- log score;
- expected calibration error as a descriptive supplement, not a replacement for full calibration analysis;
- confidence or credible intervals;
- decision-curve analysis only for a defined decision context.

AUROC can be useful for ranking, but ranking alone is not enough for a probability-like consciousness claim.

## 4. Strong baselines

Every complex model should be compared with appropriate baselines, including:

- strongest single-channel model;
- demographic or site-only model where leakage is a concern;
- simple arousal or vigilance model;
- stimulus-only model for content analyses;
- shuffled or permutation null;
- theory-agnostic benchmark where a theory-derived feature is evaluated.

Multimodal complexity is justified only when it adds prospective value.

## 5. Hierarchical structure

Repeated measures are nested within participants and often within sites. Use multilevel models, clustered resampling, grouped cross-validation, or other methods that respect this dependence.

Confidence intervals that treat every trial as independent are not acceptable when the scientific claim is about people or sites.

## 6. Missingness and uninterpretable data

Report separately:

- missing channel;
- failed acquisition;
- failed preprocessing;
- low-quality recording;
- task noncompliance;
- model abstention.

Analyze whether missingness depends on severity, state, site, movement, medication, or other variables. Sensitivity analysis should include missing-not-at-random scenarios when plausible.

Missing or uninterpretable data must not be encoded as evidence of absence.

## 7. Identification and sensitivity analysis

When latent-state inference depends on assumptions, report how conclusions change under variation in:

- prior probability;
- channel dependence;
- sensitivity and specificity;
- report misclassification;
- reference-standard error;
- missingness mechanism;
- site effects;
- transport parameters;
- unmeasured-confounding bounds where relevant.

When point identification is not justified, report an identification interval or set.

## 8. Multimodal fusion

A multimodal model must demonstrate more than a larger AUROC.

Required evidence should include:

- improvement in proper scoring metrics;
- calibration maintained or improved;
- held-out participant performance;
- external-site performance;
- incremental value over the best single channel;
- sensitivity to channel dependence;
- interpretation of discordant channels;
- ablation analysis.

Naive multiplication of likelihood ratios is only valid under conditional independence and should be treated as an explicit benchmark assumption.

## 9. Cross-state transport

For a model developed in reference state \(s_0\) and evaluated in new state \(s_1\), define a preregistered transport loss, for example

\[
\Delta_{\mathrm{transport}}
=
\mathcal L_{s_1}-\mathcal L_{s_0},
\]

where \(\mathcal L\) is a proper scoring loss evaluated on held-out data.

Report both absolute performance in the new state and transport loss. A model can have small relative degradation while still performing poorly in absolute terms.

## 10. Measurement invariance

When a score is compared across groups or states, test whether the score retains the same interpretation.

Potential differences include:

- baseline distributions;
- feature loadings;
- calibration;
- thresholds;
- noise structure;
- hardware response;
- physiology induced by medication or pathology.

If invariance fails, either adapt the model explicitly or restrict the claim domain.

## 11. Negative and positive controls

The model must search for:

- false positives in conditions where the target is strongly disfavored by independent evidence;
- false negatives during clearly reportable experience;
- signatures reproduced by attention or motor preparation;
- signatures explained by arousal;
- site or scanner shortcuts;
- stimulus decoding without experiential decoding.

No single control establishes specificity, but a model without serious controls cannot support strong claims.

## 12. Multiple comparisons and researcher degrees of freedom

High-dimensional analyses require:

- preregistered primary families;
- multiplicity control or hierarchical inference;
- disclosure of exploratory analyses;
- immutable confirmatory windows, regions, or feature definitions where feasible;
- correction of selective model search.

If many pipelines are tried, the confirmatory result must come from an independent frozen pipeline.

## 13. Sample-size planning

Sample size should be determined by the primary endpoint and analysis unit.

Inputs may include:

- minimum scientifically important effect;
- repeated-measures correlation;
- between-person heterogeneity;
- site heterogeneity;
- desired calibration precision;
- expected uninterpretable rate;
- missingness;
- number of external-validation sites;
- permutation precision for structural analyses.

A universal sample-size rule is not scientifically defensible.

## 14. Structural correspondence statistics

Phenomenal-neural mapping should report:

- reliability of each relational space;
- held-out alignment;
- normalized distortion;
- null-model performance;
- permutation or randomization evidence;
- uncertainty across participants;
- sensitivity to distance metric;
- stimulus-geometry control;
- mapping complexity penalty where appropriate.

The mapping must be fit on training relations and evaluated on held-out relations if M6 is claimed.

## 15. Causal analyses

Causal claims require assumptions beyond association.

Report:

- intervention definition;
- manipulation check;
- treatment assignment mechanism;
- temporal order;
- mediators and side effects;
- missing outcome assumptions;
- causal estimand;
- sensitivity to unmeasured confounding where relevant.

A statistically significant intervention effect does not automatically establish sufficiency or identity.

## 16. Abstention

A scientifically responsible classifier should be allowed to abstain when:

- data quality is too low;
- the case is outside the validation domain;
- uncertainty exceeds a preregistered bound;
- channels are strongly discordant;
- required assumptions fail.

Report abstention rate and the characteristics of abstained cases. A model that makes fewer but better-supported claims may be more scientifically useful than one that always predicts.

## 17. Robustness and replication

At minimum distinguish:

- within-dataset robustness;
- held-out-participant replication;
- held-out-site replication;
- cross-state replication;
- independent-laboratory replication.

Do not use the word "replicated" when the same participants, site, or analysis-development loop remain involved.

## 18. Reporting standard

Every confirmatory result should state:

- target;
- population and context;
- primary endpoint;
- analysis unit;
- model freeze point;
- calibration;
- discrimination if relevant;
- uncertainty;
- external-validation status;
- assumptions;
- failure modes tested;
- M0-M7 claim level;
- explicit nonclaims.
