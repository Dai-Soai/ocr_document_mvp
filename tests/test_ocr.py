import pytest
from PIL import Image

from ocr_document.ocr import clean_ocr_text, extract_text_from_image, validate_image


def test_validate_image_accepts_supported_file(tmp_path):
    image = tmp_path / "sample.png"
    Image.new("RGB", (100, 50), "white").save(image)

    result = validate_image(str(image))

    assert result.name == "sample.png"


def test_validate_image_rejects_missing_file(tmp_path):
    missing = tmp_path / "missing.png"

    with pytest.raises(FileNotFoundError):
        validate_image(str(missing))


def test_validate_image_rejects_unsupported_file(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("not an image", encoding="utf-8")

    with pytest.raises(ValueError):
        validate_image(str(text_file))


def test_clean_ocr_text_removes_empty_lines():
    raw = "RADAR OCR\n\n   \nDocument MVP\n"

    result = clean_ocr_text(raw)

    assert result == "RADAR OCR\nDocument MVP"


def test_extract_text_from_image_uses_ocr(monkeypatch, tmp_path):
    image = tmp_path / "sample.png"
    Image.new("RGB", (100, 50), "white").save(image)

    def fake_image_to_string(*args, **kwargs):
        return "RADAR OCR\n\nDocument MVP\n"

    monkeypatch.setattr(
        "pytesseract.image_to_string",
        fake_image_to_string,
    )

    text = extract_text_from_image(str(image))

    assert "RADAR OCR" in text
    assert "Document MVP" in text
