import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestUnicodeSimplifiedChinese(unittest.TestCase):
    def test_simplified_chinese(self):
        # this sample has some text within the fonttbl definition
        example_rtf = RTF_DIR / "issue_11.rtf"
        example_txt = TEXT_DIR / "issue_11.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
