from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.electromagnetic_simulations import (
    v16_field_identity,
    v17_scale_invariance,
    v18_power_nonidentifiability,
    v19_common_mode_confound,
    v20_frequency_specific_structure,
)
from consciousness_measurement.figure_svg import circle as svg_circle
from consciousness_measurement.figure_svg import line as svg_line
from consciousness_measurement.figure_svg import metric_card
from consciousness_measurement.figure_svg import polyline as svg_polyline
from consciousness_measurement.figure_svg import rect as svg_rect
from consciousness_measurement.figure_svg import text as svg_text

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def _write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: float) -> str:
    if abs(value) < 1e-12:
        return "0"
    if abs(value) >= 1000 or abs(value) < 1e-3:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _validation_svg(
    *,
    v16: dict[str, float],
    v17: list[dict[str, float]],
    v18: dict[str, float],
    v19: list[dict[str, float]],
    v20: list[dict[str, float]],
) -> str:
    width, height = 1400, 850
    v20_map = {row["frequency_hz"]: row["phase_concentration"] for row in v20}
    baseline = v17[1]
    invariant_keys = (
        "spectral_entropy",
        "phase_concentration",
        "effective_rank",
        "singular_entropy",
        "common_mode_fraction",
    )
    max_scale_drift = max(
        abs(row[key] - baseline[key])
        for row in v17
        for key in invariant_keys
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        svg_rect(0, 0, width, height, fill="#ffffff", stroke="none", stroke_width=0),
        svg_text(60, 56, "Research III V16-V20", size=13, weight=700, fill="#3156a3"),
        svg_text(
            60,
            92,
            "Electromagnetic observables and confound tests",
            size=31,
            weight=700,
            fill="#172236",
        ),
        svg_text(
            60,
            120,
            "Field quantities are treated as measurable evidence channels and stress-tested before interpretation.",
            size=15,
            fill="#657286",
        ),
        '<rect x="930" y="28" width="410" height="82" rx="12" fill="#f7f9fc" stroke="#d7dee8" stroke-width="1"/>',
        '<text x="950" y="50" text-anchor="start" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#3156a3">SCIENTIFIC QUESTION</text>',
        '<text x="950" y="72" text-anchor="start" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="#26374d">Can field organization survive gain changes,</text>',
        '<text x="950" y="92" text-anchor="start" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="#26374d">common-mode confounds, and frequency changes?</text>',
        svg_line(60, 145, 1340, 145, stroke="#d6dde7", width=1.2),
        metric_card(
            60,
            172,
            295,
            142,
            kicker="V16",
            title="Field identity",
            value=f'u = {v16["energy_density_j_m3"]:.2e} J/m^3',
            note=f'Poynting z = {_fmt(v16["poynting_z_w_m2"])} W/m^2',
            accent="#315b78",
        ),
        metric_card(
            375,
            172,
            295,
            142,
            kicker="V17",
            title="Scale invariance",
            value=f"max drift {max_scale_drift:.1e}",
            note="normalized features stable across 0.1x to 10x",
            accent="#506b3f",
        ),
        metric_card(
            690,
            172,
            295,
            142,
            kicker="V18",
            title="Matched-power test",
            value="power difference approx 0",
            note=(
                "phase concentration "
                f'{_fmt(v18["coherent_phase_concentration"])} vs '
                f'{_fmt(v18["balanced_phase_concentration"])}'
            ),
            accent="#7b435c",
        ),
        metric_card(
            1005,
            172,
            295,
            142,
            kicker="V20",
            title="Frequency specificity",
            value=(
                f'10 Hz: {_fmt(v20_map[10.0])} | '
                f'17 Hz: {_fmt(v20_map[17.0])}'
            ),
            note="organization depends on frequency",
            accent="#5b5791",
        ),
        '<rect x="319" y="186" width="24" height="20" rx="10" fill="#eef4f8" stroke="#c8d7e2"/>',
        '<text x="331" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#315b78">A</text>',
        '<rect x="634" y="186" width="24" height="20" rx="10" fill="#f1f5ee" stroke="#cfdbc7"/>',
        '<text x="646" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#506b3f">B</text>',
        '<rect x="949" y="186" width="24" height="20" rx="10" fill="#f8f0f4" stroke="#e1cfd8"/>',
        '<text x="961" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#7b435c">C</text>',
        '<rect x="1264" y="186" width="24" height="20" rx="10" fill="#f2f1f8" stroke="#d8d5e7"/>',
        '<text x="1276" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#5b5791">D</text>',
    ]

    # V19: common-mode confound stress test
    x0, y0, panel_width, panel_height = 60, 350, 1280, 410
    parts.extend(
        [
            svg_rect(
                x0,
                y0,
                panel_width,
                panel_height,
                fill="#fbfcfe",
                stroke="#d6dde7",
                stroke_width=1.2,
                radius=12,
            ),
            svg_text(
                x0 + 26,
                y0 + 38,
                "V19  Common-mode confound stress test",
                size=18,
                weight=700,
                fill="#244c64",
            ),
            svg_text(
                x0 + 26,
                y0 + 64,
                "A shared contaminant can create apparent phase organization at the sensor level",
                size=13,
                fill="#687588",
            ),
        ]
    )
    ax_left, ax_right = x0 + 86, x0 + panel_width - 52
    ax_top, ax_bottom = y0 + 100, y0 + 320
    parts.extend(
        [
            '<rect x="1292" y="366" width="28" height="22" rx="11" fill="#eef4f8" stroke="#c8d7e2"/>',
            '<text x="1306" y="381" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#244c64">E</text>',
            svg_text(ax_left, ax_top - 12, "phase concentration", size=11, weight=700, fill="#526276"),
            svg_text(ax_right, ax_top - 12, "0 = diffuse | 1 = concentrated", size=11, fill="#748195", anchor="end"),
            svg_text(ax_right, ax_bottom - 18, "post-removal concentration ~ 0", size=11, weight=700, fill="#1f6078", anchor="end"),
        ]
    )
    for value in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = ax_bottom - value * (ax_bottom - ax_top)
        label = f"{value:.2f}".rstrip("0").rstrip(".")
        parts.append(svg_line(ax_left, y, ax_right, y, stroke="#e3e8ef"))
        parts.append(
            svg_text(
                ax_left - 12,
                y + 5,
                label,
                size=11,
                fill="#657286",
                anchor="end",
            )
        )
    parts.extend(
        [
            svg_line(ax_left, ax_top, ax_left, ax_bottom, stroke="#8f9cad", width=1.4),
            svg_line(ax_left, ax_bottom, ax_right, ax_bottom, stroke="#8f9cad", width=1.4),
        ]
    )
    x_values = [
        ax_left
        + row["common_mode_amplitude"]
        / v19[-1]["common_mode_amplitude"]
        * (ax_right - ax_left)
        for row in v19
    ]
    raw_points = [
        (
            x,
            ax_bottom
            - row["phase_concentration_raw"] * (ax_bottom - ax_top),
        )
        for x, row in zip(x_values, v19, strict=True)
    ]
    clean_points = [(x, ax_bottom - 2) for x in x_values]
    parts.extend(
        [
            svg_polyline(raw_points, stroke="#7a425c", width=4),
            svg_polyline(clean_points, stroke="#1f6078", width=3),
        ]
    )
    for x, y in raw_points:
        parts.append(svg_circle(x, y, 5.2, fill="#7a425c"))
    for x, y in clean_points:
        parts.append(svg_circle(x, y, 4.0, fill="#1f6078"))
    for x, row in zip(x_values, v19, strict=True):
        parts.append(
            svg_text(
                x,
                ax_bottom + 24,
                _fmt(row["common_mode_amplitude"]),
                size=11,
                fill="#657286",
                anchor="middle",
            )
        )
    parts.extend(
        [
            svg_text(
                (ax_left + ax_right) / 2,
                ax_bottom + 44,
                "shared contaminant amplitude",
                size=12,
                weight=600,
                fill="#4f5e72",
                anchor="middle",
            ),
            svg_line(x0 + 845, y0 + 42, x0 + 871, y0 + 42, stroke="#7a425c", width=4),
            svg_text(
                x0 + 882,
                y0 + 47,
                "raw sensor phase concentration",
                size=11,
                weight=600,
                fill="#4f5e72",
            ),
            svg_line(x0 + 1080, y0 + 42, x0 + 1106, y0 + 42, stroke="#1f6078", width=3),
            svg_text(
                x0 + 1117,
                y0 + 47,
                "after removal",
                size=11,
                weight=600,
                fill="#4f5e72",
            ),
            svg_rect(
                x0 + 18,
                y0 + 374,
                panel_width - 36,
                24,
                fill="#eef4f7",
                stroke="#d7e3e9",
                stroke_width=1.0,
                radius=8,
            ),
            svg_text(
                x0 + 30,
                y0 + 392,
                "Finding: nuisance removal collapses the apparent organization to numerical zero.",
                size=12,
                weight=700,
                fill="#365064",
            ),
            svg_line(60, 805, 1340, 805, stroke="#d6dde7"),
            svg_text(
                60,
                833,
                "Synthetic validation only. Electromagnetic structure is a candidate evidence channel, not a direct measure of consciousness.",
                size=12,
                fill="#697587",
            ),
            "</svg>",
        ]
    )
    return "\n".join(parts)


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    v16 = v16_field_identity()
    v17 = v17_scale_invariance()
    v18 = v18_power_nonidentifiability()
    v19 = v19_common_mode_confound()
    v20 = v20_frequency_specific_structure()
    _write_csv(RESULTS / "v17_em_scale_invariance.csv", v17)
    _write_csv(RESULTS / "v19_common_mode_confound.csv", v19)
    _write_csv(RESULTS / "v20_frequency_specific_structure.csv", v20)
    summary = {
        "status": "analytic_and_synthetic_only",
        "claim_boundary": "electromagnetic observables are candidate evidence channels, not direct measures of consciousness",
        "v16_field_identity": v16,
        "v18_power_nonidentifiability": v18,
    }
    (RESULTS / "electromagnetic_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (FIGURES / "v16_v20_electromagnetic_validation.svg").write_text(
        _validation_svg(v16=v16, v17=v17, v18=v18, v19=v19, v20=v20),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
