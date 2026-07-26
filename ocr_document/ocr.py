from typing import Any
from pathlib import Path

import pytesseract  # type: ignore[import-untyped]
from PIL import Image

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def validate_image(file_path: str) -> Path:
    path = Path(file_path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported image type: {path.suffix}")

    return path


def clean_ocr_text(text: str) -> str:
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def extract_text_from_image(path: Any) -> Any:
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    return text.strip()
