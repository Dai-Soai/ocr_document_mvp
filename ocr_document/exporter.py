import json
from pathlib import Path


def render_json_report(image_path: str, extracted_text: str) -> dict:
    return {
        "image_path": image_path,
        "characters": len(extracted_text),
        "lines": [line for line in extracted_text.splitlines() if line.strip()],
        "text": extracted_text,
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
