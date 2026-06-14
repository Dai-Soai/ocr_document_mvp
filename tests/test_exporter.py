import json

from ocr_document.exporter import export_json_report, get_text_lines, render_json_report


def test_get_text_lines_removes_empty_lines():
    text = "RADAR OCR\n\n   \nDocument MVP\n"

    lines = get_text_lines(text)

    assert lines == ["RADAR OCR", "Document MVP"]


def test_render_json_report():
    report = render_json_report(
        "sample.png",
        "RADAR OCR\nDocument MVP",
    )

    assert report["image_path"] == "sample.png"
    assert report["metadata"]["characters"] == len("RADAR OCR\nDocument MVP")
    assert report["metadata"]["line_count"] == 2
    assert report["ocr"]["lines"] == ["RADAR OCR", "Document MVP"]
    assert "RADAR OCR" in report["ocr"]["text"]


def test_export_json_report(tmp_path):
    output = tmp_path / "ocr_report.json"

    result = export_json_report(
        str(output),
        "sample.png",
        "Extracted OCR text",
    )

    data = json.loads(result.read_text(encoding="utf-8"))

    assert result.exists()
    assert data["image_path"] == "sample.png"
    assert data["metadata"]["characters"] == len("Extracted OCR text")
    assert data["metadata"]["line_count"] == 1
    assert data["ocr"]["text"] == "Extracted OCR text"
