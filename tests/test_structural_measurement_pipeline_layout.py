from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs" / "figures" / "structural_measurement_pipeline.svg"
RECORD = ROOT / "docs" / "phenomenal-structure.md"
SVG_NS = "{http://www.w3.org/2000/svg}"
EXPECTED_NODES = {
    "phenomenal-observations",
    "phenomenal-structure",
    "physical-observations",
    "physical-structure",
    "mapping",
    "outcome",
}
HORIZONTAL_PADDING = 24.0
WIDTH_FACTOR = 0.52


def _number(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def test_pipeline_uses_distinct_scientific_block_colors() -> None:
    root = ET.parse(FIGURE).getroot()
    boxes = {
        rect.attrib["data-node"]: rect
        for rect in root.iter(f"{SVG_NS}rect")
        if "data-node" in rect.attrib
    }
    assert set(boxes) == EXPECTED_NODES

    fills = {node: box.attrib["fill"] for node, box in boxes.items()}
    assert len(set(fills.values())) == len(EXPECTED_NODES)


def test_pipeline_labels_stay_inside_parent_blocks() -> None:
    root = ET.parse(FIGURE).getroot()
    _, _, view_width, view_height = [
        float(value) for value in root.attrib["viewBox"].split()
    ]
    boxes = {
        rect.attrib["data-node"]: rect
        for rect in root.iter(f"{SVG_NS}rect")
        if "data-node" in rect.attrib
    }

    for box in boxes.values():
        x = _number(box, "x")
        y = _number(box, "y")
        width = _number(box, "width")
        height = _number(box, "height")
        assert 0 <= x < x + width <= view_width
        assert 0 <= y < y + height <= view_height

    checked = 0
    for text in root.iter(f"{SVG_NS}text"):
        parent = text.attrib.get("data-parent")
        if parent is None:
            continue
        checked += 1
        assert parent in boxes
        box = boxes[parent]
        box_x = _number(box, "x")
        box_y = _number(box, "y")
        box_width = _number(box, "width")
        box_height = _number(box, "height")

        assert text.attrib.get("text-anchor") == "middle"
        text_x = _number(text, "x")
        assert abs(text_x - (box_x + box_width / 2.0)) <= 0.5

        label = "".join(text.itertext()).strip()
        font_size = float(text.attrib["font-size"])
        estimated_width = len(label) * font_size * WIDTH_FACTOR
        available_width = box_width - 2.0 * HORIZONTAL_PADDING
        assert estimated_width <= available_width, (
            f"{parent!r} label {label!r} exceeds conservative width budget: "
            f"{estimated_width:.1f} > {available_width:.1f}"
        )

        baseline = _number(text, "y")
        assert box_y + 20.0 <= baseline <= box_y + box_height - 12.0

    assert checked == 22


def test_phenomenal_structure_record_keeps_pipeline_visible() -> None:
    text = RECORD.read_text(encoding="utf-8")
    assert "figures/structural_measurement_pipeline.svg?v=20260916c" in text
    assert "[Open the editable SVG source](figures/structural_measurement_pipeline.svg)" in text
