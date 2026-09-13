import pytest

from consciousness_measurement.profile import (
    ChannelEvidence,
    ConsciousnessEvidenceProfile,
    InferenceState,
    Target,
)


def test_uninterpretable_channel_cannot_support_absence():
    with pytest.raises(ValueError):
        ChannelEvidence(
            name="task_eeg",
            value=None,
            interpretable=False,
            validation_domain="benchmark",
            negative_supports_absence=True,
        )


def test_profile_rejects_duplicate_channel_names():
    channel = ChannelEvidence(
        name="behavior",
        value=0.0,
        interpretable=True,
        validation_domain="benchmark",
    )
    with pytest.raises(ValueError):
        ConsciousnessEvidenceProfile(
            subject_id="example",
            target=Target.PRESENCE,
            context="test",
            state=InferenceState.INCONCLUSIVE,
            channels=(channel, channel),
        )


def test_profile_preserves_interpretable_and_uninterpretable_channels():
    positive = ChannelEvidence(
        name="task_eeg",
        value=1.0,
        interpretable=True,
        validation_domain="covert command following",
    )
    missing = ChannelEvidence(
        name="tms_eeg",
        value=None,
        interpretable=False,
        validation_domain="perturbational capacity",
    )
    profile = ConsciousnessEvidenceProfile(
        subject_id="example",
        target=Target.PRESENCE,
        context="research",
        state=InferenceState.MIXED,
        channels=(positive, missing),
    )
    assert profile.interpretable_channels == (positive,)
    assert profile.uninterpretable_channels == (missing,)


def test_profile_serialization_is_json_ready():
    channel = ChannelEvidence(
        name="behavior",
        value=0.4,
        interpretable=True,
        validation_domain="behavioral benchmark",
        uncertainty=(0.2, 0.6),
        quality_notes="synthetic example",
        negative_supports_absence=False,
    )
    profile = ConsciousnessEvidenceProfile(
        subject_id="example-001",
        target=Target.CONTENT,
        context="synthetic benchmark",
        state=InferenceState.SUPPORTING,
        channels=(channel,),
        assumptions=("A1", "A2"),
        allowed_claim="synthetic prediction example",
        forbidden_claims=("direct measurement of qualia",),
        metadata={"example_only": "true"},
    )
    record = profile.as_record()
    assert record["target"] == "content"
    assert record["state"] == "evidence_supporting"
    assert record["channels"][0]["uncertainty"] == [0.2, 0.6]
    assert record["metadata"]["example_only"] == "true"


def test_absence_claim_requires_all_interpretable_channels_to_be_validated():
    valid = ChannelEvidence(
        name="validated_negative",
        value=0.0,
        interpretable=True,
        validation_domain="bidirectional benchmark",
        negative_supports_absence=True,
    )
    invalid = ChannelEvidence(
        name="insensitive_negative",
        value=0.0,
        interpretable=True,
        validation_domain="one-sided benchmark",
        negative_supports_absence=False,
    )
    profile = ConsciousnessEvidenceProfile(
        subject_id="example",
        target=Target.PRESENCE,
        context="research",
        state=InferenceState.OPPOSING,
        channels=(valid, invalid),
    )
    assert profile.can_make_absence_claim() is False
