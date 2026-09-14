"""Synchronize README text with the partial-identification implementation."""

from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"

REPLACEMENTS = (
    (
        "7. [Statistical Validation Plan](docs/statistical-validation.md) for calibration, generalization, partial identification, and uncertainty.",
        "7. [Statistical Validation Plan](docs/statistical-validation.md) and [Dependence-Robust Partial Identification](docs/partial-identification.md) for calibration, dependence sensitivity, identification regions, and uncertainty.",
    ),
    (
        "See [Statistical Validation Plan](docs/statistical-validation.md).",
        "See [Statistical Validation Plan](docs/statistical-validation.md) and [Dependence-Robust Partial Identification](docs/partial-identification.md).",
    ),
    (
        "The package currently contains three intentionally small, auditable components:\n\n- `evidence.py` implements likelihood-ratio updates under an explicit conditional-independence assumption;\n- `profile.py` implements target-specific CEP records with an explicit inconclusive state and conservative negative-evidence rules;\n- `structural_alignment.py` implements distance matrices, relational alignment, normalized distortion, and permutation testing.",
        "The package currently contains four intentionally small, auditable components:\n\n- `evidence.py` implements likelihood-ratio updates under an explicit conditional-independence assumption;\n- `partial_identification.py` computes sharp marginal-only Frechet-Hoeffding bounds for joint evidence when conditional dependence is unknown;\n- `profile.py` implements target-specific CEP records with an explicit inconclusive state and conservative negative-evidence rules;\n- `structural_alignment.py` implements distance matrices, relational alignment, normalized distortion, and permutation testing.",
    ),
    (
        "- [Statistical Validation Plan](docs/statistical-validation.md)\n- [Clinical Translation](docs/clinical-translation.md)",
        "- [Statistical Validation Plan](docs/statistical-validation.md)\n- [Dependence-Robust Partial Identification](docs/partial-identification.md)\n- [Clinical Translation](docs/clinical-translation.md)",
    ),
    (
        "- statistical validation rules;\n- clinical translation and ethics boundaries;",
        "- statistical validation rules;\n- dependence-robust partial-identification bounds for unknown channel dependence;\n- clinical translation and ethics boundaries;",
    ),
    (
        "- computational scaffolds for evidence fusion, CEP records, and structural alignment;",
        "- computational scaffolds for independence-based fusion, dependence-robust fusion, CEP records, and structural alignment;",
    ),
)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count != 1:
            raise RuntimeError(f"expected one README match, observed {count}: {old[:80]!r}")
        text = text.replace(old, new, 1)
    README.write_text(text, encoding="utf-8")
    print("README synchronized with dependence-robust partial identification.")


if __name__ == "__main__":
    main()
