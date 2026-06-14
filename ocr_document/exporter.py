import json
from pathlib import Path


def get_text_lines(extracted_text: str) -> list[str]:
    return [line.strip() for line in extracted_text.splitlines() if line.strip()]


def render_json_report(image_path: str, extracted_text: str) -> dict:
    lines = get_text_lines(extracted_text)

    return {
        "image_path": image_path,
        "metadata": {
            "characters": len(extracted_text),
            "line_count": len(lines),
        },
        "ocr": {
            "lines": lines,
            "text": extracted_text,
        },
    }


def export_json_report(
    output_path: str,
    image_path: str,
    extracted_text: str,
) -> Path:
    path = Path(output_path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    report = render_json_report(image_path, extracted_text)

    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return path
