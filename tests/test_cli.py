from ocr_document.cli import print_full_output


def test_print_full_output(capsys):
    print_full_output("sample.png", "RADAR OCR")

    captured = capsys.readouterr()

    assert "OCR DOCUMENT MVP" in captured.out
    assert "sample.png" in captured.out
    assert "RADAR OCR" in captured.out
