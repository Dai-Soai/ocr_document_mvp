import pytest

from ocr_document.ocr import extract_text_from_image, validate_image


def test_validate_image_accepts_supported_file(tmp_path):
    image = tmp_path / "sample.png"
    image.write_bytes(b"fake image data")

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


def test_extract_text_from_image_returns_placeholder(tmp_path):
    image = tmp_path / "sample.jpg"
    image.write_bytes(b"fake image data")

    text = extract_text_from_image(str(image))

    assert "OCR placeholder" in text
    assert "sample.jpg" in text
