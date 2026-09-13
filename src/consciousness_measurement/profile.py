"""Target-specific Consciousness Evidence Profile (CEP) data structures.

The CEP is a research schema, not a clinical diagnostic instrument. It preserves
channel quality, uncertainty, validation domain, and an explicit inconclusive
state instead of forcing heterogeneous evidence into a universal scalar.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import Enum


class Target(str, Enum):
    PRESENCE = "presence"
    GLOBAL_STATE = "global_state"
    CONTENT = "content"
    STRUCTURE = "structure"
    CAPACITY = "capacity"


class InferenceState(str, Enum):
    SUPPORTING = "evidence_supporting"
    OPPOSING = "evidence_opposing"
    MIXED = "mixed_or_dissociated"
    INCONCLUSIVE = "inconclusive"


@dataclass(frozen=True)
class ChannelEvidence:
    """One interpretable evidence-channel result.

    `value` is deliberately unconstrained beyond numeric representation because
    different channels may use probabilities, standardized scores, likelihood
    ratios, or other preregistered quantities. Interpretation belongs to the
    declared channel model and validation domain.
    """

    name: str
    value: float | None
    interpretable: bool
    validation_domain: str
    uncertainty: tuple[float, float] | None = None
    quality_notes: str = ""
    negative_supports_absence: bool = False

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("channel name must be nonempty")
        if not self.validation_domain.strip():
            raise ValueError("validation_domain must be nonempty")
        if self.uncertainty is not None:
            low, high = self.uncertainty
            if low > high:
                raise ValueError("uncertainty interval must satisfy low <= high")
        if not self.interpretable and self.negative_supports_absence:
            raise ValueError(
                "an uninterpretable channel cannot support an absence claim"
            )


@dataclass(frozen=True)
class ConsciousnessEvidenceProfile:
    """A target-specific multimodal evidence record."""

    subject_id: str
    target: Target
    context: str
    state: InferenceState
    channels: tuple[ChannelEvidence, ...]
    assumptions: tuple[str, ...] = ()
    allowed_claim: str = ""
    forbidden_claims: tuple[str, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.subject_id.strip():
            raise ValueError("subject_id must be nonempty")
        if not self.context.strip():
            raise ValueError("context must be nonempty")
        names = [channel.name for channel in self.channels]
        if len(names) != len(set(names)):
            raise ValueError("channel names must be unique within one CEP")

    @property
    def interpretable_channels(self) -> tuple[ChannelEvidence, ...]:
        return tuple(channel for channel in self.channels if channel.interpretable)

    @property
    def uninterpretable_channels(self) -> tuple[ChannelEvidence, ...]:
        return tuple(channel for channel in self.channels if not channel.interpretable)

    def can_make_absence_claim(self) -> bool:
        """Return whether every interpretable negative channel is absence-valid.

        This is intentionally conservative and does not itself establish that the
        overall profile is an absence result. It only checks whether the supplied
        channel metadata permit negative evidence to be interpreted that way.
        """
        usable = self.interpretable_channels
        return bool(usable) and all(ch.negative_supports_absence for ch in usable)

    def as_record(self) -> dict[str, object]:
        """Return a JSON-serializable research record."""
        return {
            "subject_id": self.subject_id,
            "target": self.target.value,
            "context": self.context,
            "state": self.state.value,
            "channels": [
                {
                    "name": ch.name,
                    "value": ch.value,
                    "interpretable": ch.interpretable,
                    "validation_domain": ch.validation_domain,
                    "uncertainty": list(ch.uncertainty) if ch.uncertainty else None,
                    "quality_notes": ch.quality_notes,
                    "negative_supports_absence": ch.negative_supports_absence,
                }
                for ch in self.channels
            ],
            "assumptions": list(self.assumptions),
            "allowed_claim": self.allowed_claim,
            "forbidden_claims": list(self.forbidden_claims),
            "metadata": dict(self.metadata),
        }
