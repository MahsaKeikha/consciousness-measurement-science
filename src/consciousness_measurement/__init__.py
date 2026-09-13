"""Research utilities for theory-neutral consciousness measurement science."""

from .evidence import EvidenceChannel, fuse_independent_channels, posterior_from_lr
from .profile import (
    ChannelEvidence,
    ConsciousnessEvidenceProfile,
    InferenceState,
    Target,
)
from .structural_alignment import (
    distance_matrix,
    matrix_alignment,
    normalized_distortion,
    permutation_alignment_test,
)

__all__ = [
    "EvidenceChannel",
    "ChannelEvidence",
    "ConsciousnessEvidenceProfile",
    "InferenceState",
    "Target",
    "fuse_independent_channels",
    "posterior_from_lr",
    "distance_matrix",
    "matrix_alignment",
    "normalized_distortion",
    "permutation_alignment_test",
]
