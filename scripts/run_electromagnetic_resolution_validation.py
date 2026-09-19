from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.electromagnetic_resolution_simulations import (
    v26_correlated_noise_whitening,
    v27_resolution_leakage_path,
    v28_correlated_noise_fisher_information,
    v29_temporal_aliasing,
    v30_inverse_noise_amplification,
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
    if value == 0.0:
        return "0"
    if abs(value) >= 1000 or abs(value) < 1e-3:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _svg(
    *,
    v26: dict[str, float],
    v27: list[dict[str, float]],
    v28: list[dict[str, float]],
    v29: dict[str, float],
    v30: list[dict[str, float]],
) -> str:
    width, height = 1400, 900
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        svg_rect(0, 0, width, height, fill="#ffffff", stroke="none", stroke_width=0),
        svg_text(60, 56, "Research III V26-V30", size=13, weight=700, fill="#3156a3"),
        svg_text(
            60,
            92,
            "Electromagnetic resolution and information limits",
            size=31,
            weight=700,
            fill="#172236",
        ),
        svg_text(
            60,
            120,
            "Noise geometry, inverse leakage, information loss, aliasing, and unstable inverse directions.",
            size=15,
            fill="#657286",
        ),
        '<rect x="930" y="28" width="410" height="82" rx="12" fill="#f7f9fc" stroke="#d7dee8" stroke-width="1"/>',
        '<text x="950" y="50" text-anchor="start" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#3156a3">SCIENTIFIC QUESTION</text>',
        '<text x="950" y="72" text-anchor="start" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="#26374d">Where do acquisition and inverse geometry destroy</text>',
        '<text x="950" y="92" text-anchor="start" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="#26374d">resolution, information, or numerical stability?</text>',
        svg_line(60, 145, 1340, 145, stroke="#d6dde7", width=1.2),
        metric_card(
            60,
            172,
            400,
            150,
            kicker="V26",
            title="Whitening identity",
            value=f'{v26["absolute_identity_error"]:.2e}',
            note="weighted energy equals whitened energy",
            accent="#315b78",
        ),
        metric_card(
            500,
            172,
            400,
            150,
            kicker="V29",
            title="Temporal aliasing",
            value=f'{_fmt(v29["frequency_hz"])} Hz = {_fmt(v29["alias_frequency_hz"])} Hz @ {_fmt(v29["sample_rate_hz"])} Hz',
            note=f'max sampled difference {v29["max_sample_difference"]:.2e}',
            accent="#51683f",
        ),
        metric_card(
            940,
            172,
            400,
            150,
            kicker="V30",
            title="Inverse amplification",
            value=f'{_fmt(v30[-1]["realized_noise_amplification"])}x',
            note=f'at smallest singular value {_fmt(v30[-1]["smallest_singular_value"])}',
            accent="#7a425c",
        ),
        '<rect x="424" y="186" width="24" height="20" rx="10" fill="#eef4f8" stroke="#c8d7e2"/>',
        '<text x="436" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#315b78">A</text>',
        '<rect x="864" y="186" width="24" height="20" rx="10" fill="#f1f5ee" stroke="#cfdbc7"/>',
        '<text x="876" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#51683f">B</text>',
        '<rect x="1304" y="186" width="24" height="20" rx="10" fill="#f8f0f4" stroke="#e1cfd8"/>',
        '<text x="1316" y="200" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#7a425c">C</text>',
    ]

    plot_y = 365
    panel_height = 430

    # V27: resolution leakage
    x0, panel_width = 60, 610
    parts.extend(
        [
            svg_rect(
                x0,
                plot_y,
                panel_width,
                panel_height,
                fill="#fbfcfe",
                stroke="#d6dde7",
                stroke_width=1.2,
                radius=12,
            ),
            svg_text(
                x0 + 26,
                plot_y + 36,
                "V27  Resolution leakage",
                size=18,
                weight=700,
                fill="#244c64",
            ),
            svg_text(
                x0 + 26,
                plot_y + 61,
                "Identity error as regularization increases",
                size=13,
                fill="#687588",
            ),
        ]
    )
    ax_left, ax_right = x0 + 78, x0 + panel_width - 28
    ax_top, ax_bottom = plot_y + 96, plot_y + 335
    parts.extend(
        [
            '<rect x="628" y="381" width="28" height="22" rx="11" fill="#eef4f8" stroke="#c8d7e2"/>',
            '<text x="642" y="396" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#244c64">D</text>',
            svg_text(ax_left, ax_top - 12, "inverse identity error", size=11, weight=700, fill="#526276"),
            svg_text(ax_right, ax_top - 12, "dashed line = irreducible rank floor", size=11, fill="#748195", anchor="end"),
        ]
    )
    y_min, y_max = 0.70, 0.82
    for value in (0.70, 0.74, 0.78, 0.82):
        y = ax_bottom - (value - y_min) / (y_max - y_min) * (ax_bottom - ax_top)
        parts.append(svg_line(ax_left, y, ax_right, y, stroke="#e3e8ef"))
        parts.append(
            svg_text(
                ax_left - 12,
                y + 5,
                f"{value:.2f}",
                size=12,
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
        ax_left + i * (ax_right - ax_left) / (len(v27) - 1)
        for i in range(len(v27))
    ]
    points = [
        (
            x,
            ax_bottom
            - (row["identity_error"] - y_min)
            / (y_max - y_min)
            * (ax_bottom - ax_top),
        )
        for x, row in zip(x_values, v27, strict=True)
    ]
    lower_bound = v27[0]["rank_lower_bound"]
    bound_y = (
        ax_bottom
        - (lower_bound - y_min) / (y_max - y_min) * (ax_bottom - ax_top)
    )
    parts.extend(
        [
            svg_line(
                ax_left,
                bound_y,
                ax_right,
                bound_y,
                stroke="#aeb8c5",
                width=1.6,
                dash="6 5",
            ),
            svg_text(
                ax_right - 2,
                bound_y - 8,
                f"rank floor {lower_bound:.4f}",
                size=11,
                weight=600,
                fill="#778394",
                anchor="end",
            ),
            svg_polyline(points, stroke="#1f6078", width=4),
        ]
    )
    for x, y in points:
        parts.append(svg_circle(x, y, 5.5, fill="#1f6078"))
    labels = ("1e-4", "1e-2", "0.1", "1")
    for x, label in zip(x_values, labels, strict=True):
        parts.append(
            svg_text(x, ax_bottom + 24, label, size=11, fill="#657286", anchor="middle")
        )
    parts.extend(
        [
            svg_text(
                (ax_left + ax_right) / 2,
                ax_bottom + 44,
                "regularization",
                size=12,
                weight=600,
                fill="#4f5e72",
                anchor="middle",
            ),
            svg_rect(
                x0 + 18,
                plot_y + 395,
                panel_width - 36,
                24,
                fill="#eef4f7",
                stroke="#d7e3e9",
                stroke_width=1.0,
                radius=8,
            ),
            svg_text(
                x0 + 26,
                plot_y + 414,
                "Finding: leakage persists and worsens under stronger regularization.",
                size=12,
                weight=700,
                fill="#365064",
            ),
        ]
    )

    # V28: Fisher information under correlated noise
    x0, panel_width = 730, 610
    parts.extend(
        [
            svg_rect(
                x0,
                plot_y,
                panel_width,
                panel_height,
                fill="#fbfcfe",
                stroke="#d6dde7",
                stroke_width=1.2,
                radius=12,
            ),
            svg_text(
                x0 + 26,
                plot_y + 36,
                "V28  Fisher information under common sensor noise",
                size=18,
                weight=700,
                fill="#415f46",
            ),
            svg_text(
                x0 + 26,
                plot_y + 61,
                "Information decreases as common-noise correlation increases",
                size=13,
                fill="#687588",
            ),
        ]
    )
    ax_left, ax_right = x0 + 78, x0 + panel_width - 28
    ax_top, ax_bottom = plot_y + 96, plot_y + 335
    parts.extend(
        [
            '<rect x="1298" y="381" width="28" height="22" rx="11" fill="#f1f5ee" stroke="#cfdbc7"/>',
            '<text x="1312" y="396" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#415f46">E</text>',
            svg_text(ax_left, ax_top - 12, "Fisher information", size=11, weight=700, fill="#526276"),
            svg_text(ax_right, ax_top - 12, "higher common noise -> less target information", size=11, fill="#748195", anchor="end"),
        ]
    )
    y_min, y_max = 0.8, 4.2
    for value in (1.0, 2.0, 3.0, 4.0):
        y = ax_bottom - (value - y_min) / (y_max - y_min) * (ax_bottom - ax_top)
        parts.append(svg_line(ax_left, y, ax_right, y, stroke="#e3e8ef"))
        parts.append(
            svg_text(
                ax_left - 12,
                y + 5,
                _fmt(value),
                size=12,
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
        + row["common_noise_correlation"]
        / v28[-1]["common_noise_correlation"]
        * (ax_right - ax_left)
        for row in v28
    ]
    points = [
        (
            x,
            ax_bottom
            - (row["fisher_information"] - y_min)
            / (y_max - y_min)
            * (ax_bottom - ax_top),
        )
        for x, row in zip(x_values, v28, strict=True)
    ]
    parts.append(svg_polyline(points, stroke="#456848", width=4))
    for x, y in points:
        parts.append(svg_circle(x, y, 5.5, fill="#456848"))
    for x, row in zip(x_values, v28, strict=True):
        parts.append(
            svg_text(
                x,
                ax_bottom + 24,
                _fmt(row["common_noise_correlation"]),
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
                "common-noise correlation",
                size=12,
                weight=600,
                fill="#4f5e72",
                anchor="middle",
            ),
            svg_rect(
                x0 + 18,
                plot_y + 395,
                panel_width - 36,
                24,
                fill="#f0f5ef",
                stroke="#d7e3d5",
                stroke_width=1.0,
                radius=8,
            ),
            svg_text(
                x0 + 26,
                plot_y + 414,
                f'Finding: CRLB variance rises from {_fmt(v28[0]["crlb_variance"])} to {_fmt(v28[-1]["crlb_variance"])}',
                size=12,
                weight=700,
                fill="#3f5d45",
            ),
            svg_line(60, 840, 1340, 840, stroke="#d6dde7"),
            svg_text(
                60,
                868,
                "Deterministic synthetic validation. These results quantify measurement limits; they do not identify consciousness or qualia.",
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

    v26 = v26_correlated_noise_whitening()
    v27 = v27_resolution_leakage_path()
    v28 = v28_correlated_noise_fisher_information()
    v29 = v29_temporal_aliasing()
    v30 = v30_inverse_noise_amplification()

    _write_csv(RESULTS / "v26_correlated_noise_whitening.csv", [v26])
    _write_csv(RESULTS / "v27_resolution_leakage.csv", v27)
    _write_csv(RESULTS / "v28_fisher_information.csv", v28)
    _write_csv(RESULTS / "v29_temporal_aliasing.csv", [v29])
    _write_csv(RESULTS / "v30_inverse_noise_amplification.csv", v30)
    (RESULTS / "electromagnetic_resolution_validation_summary.json").write_text(
        json.dumps(
            {
                "status": "analytic_and_synthetic_only",
                "claim_boundary": (
                    "resolution and information limits do not identify "
                    "consciousness or remove electromagnetic inverse ambiguity"
                ),
                "v26_correlated_noise_whitening": v26,
                "v27_resolution_leakage": v27,
                "v28_fisher_information": v28,
                "v29_temporal_aliasing": v29,
                "v30_inverse_noise_amplification": v30,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (FIGURES / "v26_v30_electromagnetic_resolution_validation.svg").write_text(
        _svg(v26=v26, v27=v27, v28=v28, v29=v29, v30=v30),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
