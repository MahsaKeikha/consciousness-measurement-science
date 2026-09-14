"""Research utilities for theory-neutral consciousness measurement science."""

from .evidence import EvidenceChannel, fuse_independent_channels, posterior_from_lr
from .partial_identification import (
    DependenceRobustFusion,
    LikelihoodRatioInterval,
    ProbabilityInterval,
    conditional_pattern_probability_bounds,
    frechet_intersection_bounds,
    fuse_unknown_dependence,
    likelihood_ratio_bounds,
    posterior_interval_from_lr_bounds,
)
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
    "ChannelEvidence",
    "ConsciousnessEvidenceProfile",
    "DependenceRobustFusion",
    "EvidenceChannel",
    "InferenceState",
    "LikelihoodRatioInterval",
    "ProbabilityInterval",
    "Target",
    "conditional_pattern_probability_bounds",
    "distance_matrix",
    "frechet_intersection_bounds",
    "fuse_independent_channels",
    "fuse_unknown_dependence",
    "likelihood_ratio_bounds",
    "matrix_alignment",
    "normalized_distortion",
    "permutation_alignment_test",
    "posterior_from_lr",
    "posterior_interval_from_lr_bounds",
]
