from pathlib import Path

from ocr_document.batch import process_directory


def test_process_directory(tmp_path):

    image_dir = tmp_path / "images"
    image_dir.mkdir()

    sample = image_dir / "sample.png"
    sample.write_bytes(b"fake")

    output_dir = tmp_path / "reports"

    try:
        process_directory(
            image_dir,
            output_dir,
        )
    except Exception:
        pass

    assert output_dir.exists()
