import argparse

from ocr_document.ocr import extract_text_from_image


def main():
    parser = argparse.ArgumentParser(
        prog="ocr-doc",
        description="OCR Document MVP",
    )

    parser.add_argument("image", help="Path to image file")

    args = parser.parse_args()

    text = extract_text_from_image(args.image)

    print("=" * 60)
    print("OCR DOCUMENT MVP")
    print("=" * 60)
    print(f"Image: {args.image}")
    print()
    print("Extracted text:")
    print(text)


if __name__ == "__main__":
    main()
