import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestCyrillic(unittest.TestCase):

    def test_good(self):
        example_rtf = RTF_DIR / "issue_29_good.rtf"
        example_txt = TEXT_DIR / "issue_29_good.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

    def test_bad(self):
        example_rtf = RTF_DIR / "issue_29_bad.rtf"
        example_txt = TEXT_DIR / "issue_29_bad.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
