# Contributing

Contributions are welcome when they improve scientific clarity, reproducibility, falsifiability, or implementation quality without weakening the repository's claim discipline.

## Before opening a contribution

Please identify:

- the measurement target affected;
- whether the change is conceptual, computational, empirical, statistical, clinical, ethical, or editorial;
- which assumptions are added or changed;
- whether the M0-M7 claim level changes;
- which documentation and tests must be synchronized.

## Scientific contribution rules

A contribution should not:

- redefine consciousness as the proposed biomarker;
- treat a correlation as a mechanism;
- treat a mechanism as ontological identity;
- treat a negative detector output as evidence of absence without validated sensitivity;
- import a threshold from one context as a universal law;
- hide failed results or violated assumptions;
- use theory language that makes the tested proposition impossible to falsify.

## Code contribution rules

New code should:

- have a clear research purpose;
- expose assumptions in docstrings or accompanying documentation;
- preserve an inconclusive or abstention path where relevant;
- include tests;
- keep functions small enough to audit;
- use deterministic seeds in tests;
- pass `make check`.

## Documentation contribution rules

Documentation should:

- define technical terms before relying on them;
- distinguish specification from empirical validation;
- state what a result would and would not imply;
- link to the relevant formal, statistical, clinical, or software document;
- use ASCII hyphen-minus rather than Unicode en dash or em dash characters.

## Empirical contributions

Empirical analyses should include:

- data provenance;
- preregistration or a clear exploratory label;
- participant and site split logic;
- preprocessing specification;
- quality-control rules;
- calibration and uncertainty;
- negative and positive controls;
- claim record;
- reproducibility instructions;
- all confirmatory outcomes, including nulls.

## Review standard

A contribution is ready to merge when a technically competent reader can answer:

1. What target is being measured?
2. What data support the claim?
3. What assumptions are required?
4. What are the strongest alternative explanations?
5. What would falsify the claim?
6. What is the strongest allowed M0-M7 level?
7. What remains explicitly unproven?
