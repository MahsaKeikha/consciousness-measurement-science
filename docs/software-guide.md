# Software Guide

The Python package is deliberately small. Its purpose is to make the repository's core measurement logic executable and testable without pretending that the current code is a validated consciousness classifier.

## Installation

From the repository root:

```bash
python -m pip install -e ".[dev]"
make check
```

`make check` runs unit tests, repository-policy validation, and Ruff.

## Package layout

```text
src/consciousness_measurement/
  __init__.py
  evidence.py
  profile.py
  structural_alignment.py
```

## `evidence.py`

### Purpose

Demonstrates transparent Bayesian evidence updating for calibrated binary channels under an explicit conditional-independence assumption.

### Main object

`EvidenceChannel(name, sensitivity, specificity)` stores context-specific binary-test performance.

For a positive result,

\[
LR^+=\frac{\text{sensitivity}}{1-\text{specificity}}.
\]

For a negative result,

\[
LR^-=\frac{1-\text{sensitivity}}{\text{specificity}}.
\]

`posterior_from_lr(prior, likelihood_ratio)` converts prior odds to posterior odds.

`fuse_independent_channels(...)` multiplies channel likelihood ratios only under the declared conditional-independence assumption.

### Example

```python
from consciousness_measurement import EvidenceChannel, fuse_independent_channels

behavior = EvidenceChannel("behavior", sensitivity=0.70, specificity=0.95)
task_eeg = EvidenceChannel("task_eeg", sensitivity=0.65, specificity=0.97)

combined_lr, posterior = fuse_independent_channels(
    prior=0.50,
    observations=[(behavior, False), (task_eeg, True)],
)

print(combined_lr, posterior)
```

Interpretation boundary: the returned posterior is only meaningful for the latent event whose calibration model produced those sensitivities and specificities. It is not automatically a probability of consciousness.

## `profile.py`

### Purpose

Implements target-specific Consciousness Evidence Profile records.

### Main enums

- `Target.PRESENCE`
- `Target.GLOBAL_STATE`
- `Target.CONTENT`
- `Target.STRUCTURE`
- `Target.CAPACITY`

Inference states:

- `SUPPORTING`
- `OPPOSING`
- `MIXED`
- `INCONCLUSIVE`

### `ChannelEvidence`

Each channel records:

- a name;
- a numerical value or `None`;
- whether the measurement is interpretable;
- its validation domain;
- optional uncertainty;
- quality notes;
- whether a negative result has been validated to support an absence claim.

The class refuses an internally inconsistent state in which an uninterpretable channel is marked as valid negative evidence for absence.

### `ConsciousnessEvidenceProfile`

The profile stores:

- subject or system identifier;
- target;
- context;
- overall evidence state;
- channel records;
- assumptions;
- allowed claim;
- forbidden claims;
- metadata.

Example:

```python
from consciousness_measurement import (
    ChannelEvidence,
    ConsciousnessEvidenceProfile,
    InferenceState,
    Target,
)

profile = ConsciousnessEvidenceProfile(
    subject_id="example-001",
    target=Target.PRESENCE,
    context="research benchmark",
    state=InferenceState.MIXED,
    channels=(
        ChannelEvidence(
            name="behavior",
            value=0.0,
            interpretable=True,
            validation_domain="command-following benchmark",
            negative_supports_absence=False,
        ),
        ChannelEvidence(
            name="task_eeg",
            value=1.0,
            interpretable=True,
            validation_domain="motor-imagery benchmark",
        ),
    ),
    allowed_claim="evidence of covert task performance",
    forbidden_claims=("direct measurement of qualia",),
)

record = profile.as_record()
```

## `structural_alignment.py`

### Purpose

Provides minimal tools for comparing phenomenal and neural relational structures.

### `distance_matrix(features)`

Returns Euclidean pairwise distances among rows of a feature matrix.

### `matrix_alignment(a, b)`

Computes Pearson correlation between the upper triangles of two distance matrices.

### `normalized_distortion(a, b)`

Normalizes each distance matrix by its mean off-diagonal distance and computes mean absolute difference between corresponding upper-triangle entries.

### `permutation_alignment_test(...)`

Permutes neural labels while preserving internal neural geometry and returns an observed alignment plus a one-sided permutation p-value.

Example:

```python
import numpy as np

from consciousness_measurement import (
    distance_matrix,
    matrix_alignment,
    normalized_distortion,
    permutation_alignment_test,
)

phenomenal_features = np.array([[0.0], [1.0], [3.0], [4.0]])
neural_features = np.array([[0.0], [1.1], [3.1], [4.1]])

phenomenal = distance_matrix(phenomenal_features)
neural = distance_matrix(neural_features)

print(matrix_alignment(phenomenal, neural))
print(normalized_distortion(phenomenal, neural))
print(permutation_alignment_test(phenomenal, neural, permutations=500, seed=7))
```

## What the software does not do

The package does not currently:

- classify clinical patients;
- estimate a universal consciousness probability;
- implement PCI;
- decode dream content;
- infer AI consciousness;
- establish causal necessity or sufficiency from observational data;
- solve the hard problem;
- turn structural correspondence into ontological identity.

Those boundaries are deliberate.

## Extension rules

New software modules should satisfy the following:

1. name the measurement target;
2. state the assumption set;
3. expose uncertainty;
4. distinguish uninterpretable data from negative evidence;
5. include unit tests;
6. document the validation domain;
7. avoid stronger claim language than the implemented method supports;
8. add reader-facing documentation and update the repository policy if a new public research object is introduced.
