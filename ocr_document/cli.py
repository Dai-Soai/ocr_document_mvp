import argparse

from ocr_document.exporter import export_json_report
from ocr_document.ocr import extract_text_from_image


def main():
    parser = argparse.ArgumentParser(
        prog="ocr-doc",
        description="OCR Document MVP",
    )

    parser.add_argument("image", help="Path to image file")
    parser.add_argument(
        "--json",
        help="Export OCR result to a JSON file",
    )

    args = parser.parse_args()

    text = extract_text_from_image(args.image)

    print("=" * 60)
    print("OCR DOCUMENT MVP")
    print("=" * 60)
    print(f"Image: {args.image}")
    print()
    print("Extracted text:")
    print(text)

    if args.json:
        output_path = export_json_report(
            args.json,
            args.image,
            text,
        )
        print()
        print(f"JSON report exported to: {output_path}")


if __name__ == "__main__":
    main()
