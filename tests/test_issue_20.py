import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class UnknownEncoding(unittest.TestCase):
    def test_empty(self):
        example_rtf = RTF_DIR / "issue_20.rtf"
        example_txt = TEXT_DIR / "issue_20.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
