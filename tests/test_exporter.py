import json

from ocr_document.exporter import export_json_report, render_json_report


def test_render_json_report():
    report = render_json_report(
        "sample.png",
        "RADAR OCR\nDocument MVP",
    )

    assert report["image_path"] == "sample.png"
    assert report["characters"] == len("RADAR OCR\nDocument MVP")
    assert report["lines"] == ["RADAR OCR", "Document MVP"]
    assert "RADAR OCR" in report["text"]


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
    assert data["text"] == "Extracted OCR text"
