from pathlib import Path

from ocr_document.exporter import export_json_report
from ocr_document.ocr import extract_text_from_image


def process_directory(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)

    processed = []

    for image_file in input_path.iterdir():

        if image_file.suffix.lower() not in (
            ".png",
            ".jpg",
            ".jpeg",
        ):
            continue

        text = extract_text_from_image(str(image_file))

        report_path = output_path / f"{image_file.stem}.json"

        export_json_report(
            str(report_path),
            str(image_file),
            text,
        )

        processed.append(image_file.name)

    return processed
