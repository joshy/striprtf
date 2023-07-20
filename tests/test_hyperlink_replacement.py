import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TXT_DIR = Path.cwd() / "tests" / "text"


class TestSimple(unittest.TestCase):
    def test_extract_hyperlink(self):
        hyperlink_rtf = RTF_DIR / "hyperlink.rtf"
        hyperlink_txt = TXT_DIR / "hyperlink.txt"

        with hyperlink_rtf.open() as source:
            result = rtf_to_text(source.read())
        with hyperlink_txt.open() as destination:
            self.assertEqual(destination.read(), result)
