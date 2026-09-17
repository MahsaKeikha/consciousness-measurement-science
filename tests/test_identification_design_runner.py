from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_OUTPUTS = (
    ROOT / "results" / "v11_missingness_information_law.csv",
    ROOT / "results" / "v12_v13_multisite_identification.csv",
    ROOT / "results" / "v14_resolution_sample_size.csv",
    ROOT / "results" / "v15_independent_pilot_gate.csv",
    ROOT / "results" / "identification_design_summary.json",
    ROOT / "docs" / "figures" / "v11_missingness_information_law.svg",
    ROOT / "docs" / "figures" / "v12_v13_multisite_heterogeneity.svg",
    ROOT / "docs" / "figures" / "v14_resolution_sample_size.svg",
    ROOT / "docs" / "figures" / "v15_independent_pilot_gate.svg",
)


def test_v11_v15_runner_reproduces_committed_record_exactly() -> None:
    before = {path: path.read_bytes() for path in CANONICAL_OUTPUTS}

    subprocess.run(
        [sys.executable, "scripts/run_identification_design_validation.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    after = {path: path.read_bytes() for path in CANONICAL_OUTPUTS}
    assert after == before
