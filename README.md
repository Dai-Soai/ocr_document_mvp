
# OCR Document MVP

A lightweight OCR utility for extracting text from image files and exporting structured JSON reports.

---

## Current Status

M6 Batch OCR complete.

### Completed

* OCR text extraction from images
* Tesseract OCR integration
* JSON export layer
* Structured JSON report layer
* CLI interface
* Batch OCR processing
* Pytest coverage

### Test Status

```text
10 passed
```

---

## Features

* Extract text from PNG, JPG, JPEG, and WEBP images
* OCR powered by Tesseract
* Structured JSON report export
* Text-only CLI output
* Quiet mode for scripting
* Batch OCR processing
* Command-line interface (`ocr-doc`)
* Pytest test coverage

---

## Requirements

### System Package

```bash
sudo apt install tesseract-ocr tesseract-ocr-eng
```

### Python

```text
Python >= 3.11
```

---

## Installation

```bash
git clone git@github.com:Dai-Soai/ocr_document_mvp.git

cd ocr_document_mvp

python3 -m venv .venv

source .venv/bin/activate

pip install -e ".[dev]"
```

---

## Usage

### Single Image

```bash
ocr-doc data/sample.png
```

### Text Only

```bash
ocr-doc data/sample.png --text-only
```

### Export JSON

```bash
ocr-doc data/sample.png --json outputs/sample_ocr.json
```

### Quiet JSON Export

```bash
ocr-doc data/sample.png --json outputs/sample_ocr.json --quiet
```

### Batch OCR

```bash
ocr-doc --batch data/batch_images
```

---

## Example JSON Output

```json
{
  "image_path": "data/sample.png",
  "metadata": {
    "characters": 52,
    "line_count": 2
  },
  "ocr": {
    "lines": [
      "RADAR OCR Document MVP",
      "Extract text from image files"
    ],
    "text": "RADAR OCR Document MVP\n\nExtract text from image files"
  }
}
```

---

## Project Structure

```text
ocr_document_mvp/
├── data/
├── outputs/
├── tests/
├── ocr_document/
│   ├── cli.py
│   ├── ocr.py
│   ├── exporter.py
│   └── batch.py
├── pyproject.toml
└── README.md
```

---

## Roadmap

* [x] M1 Bootstrap
* [x] M2 Core OCR Engine
* [x] M3 Export Layer
* [x] M4 JSON Report Layer
* [x] M5 CLI Layer
* [x] M6 Batch OCR
* [ ] M7 Packaging & Release
* [ ] M8 GitHub Release

---

## License

MIT (optional)
