import argparse

from ocr_document.batch import process_directory
from ocr_document.exporter import export_json_report
from ocr_document.ocr import extract_text_from_image


def print_full_output(image_path: str, text: str):
    print("=" * 60)
    print("OCR DOCUMENT MVP")
    print("=" * 60)
    print(f"Image: {image_path}")
    print()
    print("Extracted text:")
    print(text)


def main():
    parser = argparse.ArgumentParser(
        prog="ocr-doc",
        description="OCR Document MVP",
    )

    parser.add_argument(
        "image",
        nargs="?",
        help="Path to image file",
    )

    parser.add_argument(
        "--json",
        help="Export OCR result to a JSON file",
    )

    parser.add_argument(
        "--text-only",
        action="store_true",
        help="Print extracted text only",
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress normal output except export messages",
    )
    parser.add_argument(
        "--batch",
        help="Process all images in directory",
    )

    args = parser.parse_args()

    if args.batch:
        processed = process_directory(
            args.batch,
            "outputs/batch_reports",
        )

        print(f"Processed {len(processed)} image(s)")
        return

    if not args.image:
        parser.error("image is required unless --batch is used")

    text = extract_text_from_image(args.image)

    if args.text_only:
        print(text)
    elif not args.quiet:
        print_full_output(args.image, text)

    if args.json:
        output_path = export_json_report(
            args.json,
            args.image,
            text,
        )

        if not args.quiet:
            print()
            print(f"JSON report exported to: {output_path}")
        else:
            print(output_path)


if __name__ == "__main__":
    main()
