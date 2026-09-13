import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def _load(relative_path: str):
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def test_cep_example_validates_against_schema():
    schema = _load("schemas/cep.schema.json")
    example = _load("examples/cep_example.json")
    Draft202012Validator(schema).validate(example)
    assert example["metadata"]["clinical_use"] == "prohibited"


def test_claim_example_validates_against_schema():
    schema = _load("schemas/claim.schema.json")
    example = _load("examples/claim_example.json")
    Draft202012Validator(schema).validate(example)
    assert example["claim_level"] == "M6"
    assert example["external_validation"] is False
    assert example["status"] == "proposed"


def test_claim_example_declares_assumptions_and_nonclaims():
    example = _load("examples/claim_example.json")
    assert example["assumptions"]
    assert example["nonclaims"]
    assert all(item.startswith("A") for item in example["assumptions"])
