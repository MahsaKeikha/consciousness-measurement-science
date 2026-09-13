# Phenomenal Structure Program

## Why structure matters

If the qualitative character of experience cannot be directly exported from one mind to another, relational structure may still be empirically accessible.

Examples:

- red is judged more similar to orange than to blue;
- two tones can be ordered by pitch distance;
- pain qualities can be grouped by burning, stabbing, pressure, and affective dimensions;
- visual scenes have spatial and object-relational structure.

These relations can define measurable phenomenal spaces.

## Phenomenal geometry

For stimuli/experiences \(e_1,\dots,e_n\), collect repeated pairwise or triplet judgments to estimate a distance/dissimilarity matrix

\[
D_E=[d_E(e_i,e_j)].
\]

Use split-half reliability, hierarchical models, and cross-session replication to quantify measurement error.

## Neural/causal geometry

Construct matched physical matrices from:

- multivariate neural representation distances;
- effective connectivity;
- perturbational response profiles;
- dynamical trajectories;
- population coding manifolds.

Call this matrix \(D_N\).

## Structural correspondence

Normalize both spaces and test

\[
H_0: D_E\text{ and }D_N\text{ are no more aligned than expected under permutation.}
\]

Simple initial statistics include distance-matrix correlation and normalized absolute distortion. More advanced work can use:

- representational similarity analysis;
- multidimensional scaling;
- optimal transport / Gromov-Wasserstein comparison;
- persistent homology;
- category-theoretic structure-preserving maps;
- sheaf-based local-to-global consistency models.

## What success would mean

A robust, cross-validated low-distortion mapping would establish a nontrivial correspondence between **relations among experiences** and **relations among physical/neural states**.

It would not automatically establish identity, emergence, or metaphysical reduction.

## Critical falsification tests

A strong structural hypothesis must survive:

- same neural geometry, different phenomenal geometry;
- same phenomenal geometry, different neural geometry;
- remapping under learning/adaptation;
- cross-participant alignment;
- cross-modal structure;
- lesions/stimulation that selectively distort one part of phenomenal space;
- held-out experience classes.


## Local-to-global phenomenal structure

A 2026 frontier proposal by Lee-Youngzie, Tsuchiya, Robinson, Dietz, and Monti formalizes local and global phenomenal organization using category- and sheaf-theoretic language. This repository treats that work as a higher-order extension of the empirical geometry program, not as a premise.

The staged route is:

1. establish reliable inter-experience relations (for example similarity or discriminability);
2. establish within-experience part-whole relations where they can be operationalized;
3. test whether local relational measurements compose consistently into a global structure;
4. only then introduce richer category/sheaf models when they make predictions that simpler metric or topological models cannot make.

This ordering matters. A sophisticated formalism is scientifically useful only when its additional structure is empirically identifiable and yields discriminating predictions.

### Sheaf-style consistency as a future test

Let local experiential contexts be indexed by \(U_i\), each with measured local structure \(E(U_i)\). A future local-to-global test can ask whether compatible local sections agree on overlaps and admit a coherent global section. Empirical failure of the required compatibility conditions would count against that particular global-unity model.

The repository will not infer phenomenal unity merely because a mathematical global section can be constructed; the empirical interpretation of the local data and restriction maps must be independently justified.
