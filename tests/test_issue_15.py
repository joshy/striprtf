from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


def test_empty():
    example_rtf = RTF_DIR / "issue_15.rtf"
    example_txt = TEXT_DIR / "issue_15.txt"

    with example_rtf.open() as source:
        result = rtf_to_text(source.read(), errors="ignore")
    with example_txt.open(encoding="utf-8") as destination:
        assert destination.read() == result
