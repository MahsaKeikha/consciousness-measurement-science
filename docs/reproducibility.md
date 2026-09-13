# Reproducibility

Reproducibility in this project means more than being able to rerun one script. A consciousness-measurement result is reproducible only when the data provenance, preprocessing, target definition, assumptions, analysis decisions, software environment, confirmatory split, and allowed claim can all be reconstructed.

## 1. Local environment

From the repository root:

```bash
python -m pip install -e ".[dev]"
make check
```

The `check` target runs:

- unit tests;
- repository-policy validation;
- Ruff static checks.

## 2. Minimum provenance record

Every empirical analysis should record:

- dataset name and authoritative source;
- dataset version or release date;
- file hashes where practical;
- participant inclusion and exclusion rules;
- acquisition hardware and relevant firmware/software;
- preprocessing software and version;
- preprocessing parameters;
- artifact rejection rules;
- feature-extraction version;
- target label provenance;
- preregistration identifier;
- random seeds;
- discovery, internal-confirmation, and external-confirmation split definitions;
- participant and site overlap audit;
- code commit SHA;
- operating-system and Python environment;
- package lock or environment export;
- all confirmatory outcomes and deviations.

## 3. Discovery versus confirmation

Exploratory work can be flexible, but confirmatory analysis must be frozen before access to the confirmatory outcomes.

The repository recommends three partitions when feasible:

1. **discovery** for feature engineering and model development;
2. **internal confirmation** for locked evaluation on held-out participants;
3. **external confirmation** for evaluation at a held-out site or independently collected dataset.

Repeated observations from one participant must remain in the same partition unless the analysis explicitly models leakage risk and has a different preregistered design.

## 4. Determinism and random seeds

Where algorithms are stochastic:

- record all seeds;
- distinguish algorithmic randomness from participant sampling uncertainty;
- rerun with multiple seeds when seed sensitivity could change conclusions;
- never report a single favorable seed as the confirmatory result.

Permutation and bootstrap procedures must record the random generator, seed, number of resamples, and resampling unit.

## 5. Data lineage

Participant data are not committed to this public repository.

For public datasets, prefer retrieval scripts that:

- download from the authoritative source;
- record source URL and release identifier;
- verify checksums;
- avoid silently replacing an older release;
- preserve licensing and citation metadata.

For controlled data, store only deidentified derivatives permitted by governance and provide a data-access statement rather than copying restricted data into the repository.

See [../data/README.md](../data/README.md).

## 6. Preprocessing freeze

Confirmatory preprocessing should be represented by a versioned configuration or code path. Any post-freeze change must be classified as one of:

- correction of an implementation bug;
- prespecified sensitivity analysis;
- exploratory analysis;
- protocol deviation.

The repository should not silently change preprocessing after viewing confirmatory outcomes.

## 7. Analysis inventory

For high-dimensional neural analyses, the publication package should list every confirmatory analysis family and enough information to reconstruct exploratory flexibility, including:

- channels or sensors;
- frequency bands;
- regions;
- time windows;
- feature families;
- models;
- regularization choices;
- hyperparameter search space;
- multiplicity correction;
- stopped or failed analyses.

This protects against selective reporting of favorable results.

## 8. Calibration and uncertainty artifacts

For probabilistic models, preserve:

- raw predictions on held-out data;
- calibration plots;
- Brier and log scores;
- calibration intercept and slope;
- bootstrap or model-based uncertainty;
- abstention thresholds and rates;
- subgroup and site results.

For partially identified models, preserve the full sensitivity surface or interval-generating inputs rather than only the preferred point estimate.

## 9. Structural analysis artifacts

Phenomenal-neural structure studies should preserve:

- raw or appropriately protected similarity judgments;
- construction of phenomenal distance matrices;
- neural feature definition;
- distance metric;
- normalization rule;
- mapping family;
- held-out pair definitions;
- null models;
- permutation seeds;
- distortion and alignment statistics.

## 10. Claim provenance

Every headline conclusion should have a machine-readable claim record that identifies:

- target;
- M0-M7 level;
- datasets;
- analyses;
- assumptions;
- identifiability status;
- external-validation status;
- falsification condition;
- explicit nonclaims;
- result status.

See [claim-registry.md](claim-registry.md) and [../schemas/claim.schema.json](../schemas/claim.schema.json).

## 11. Required release package

A mature empirical release should include, subject to privacy and licensing:

- preregistration;
- data-access statement;
- acquisition and preprocessing specification;
- executable analysis code;
- tests;
- environment definition;
- locked model or model-generation procedure;
- held-out predictions;
- calibration and uncertainty outputs;
- all confirmatory outcomes, including nulls;
- deviations and failures;
- machine-readable claims;
- updated literature and limitations.

## 12. Repository checks

The publication verifier checks that:

- required reader files exist and are linked from the README;
- local Markdown links resolve;
- JSON parses;
- SVG figures parse as XML;
- prohibited Unicode dash characters are absent from tracked text;
- the README exposes the major scientific artifacts.

These checks do not establish scientific truth. They establish that the public research record is internally navigable and mechanically consistent.
