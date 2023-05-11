import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestEncoding(unittest.TestCase):
    def test_empty(self):
        example_rtf = RTF_DIR / "encoding.rtf"
        example_txt = TEXT_DIR / "encoding.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read(), errors="ignore")
        with open(example_txt, 'w', encoding="utf-8") as fout:
            fout.write(result)
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
