import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestSimple(unittest.TestCase):
    def test_full_table(self):
        example_rtf = RTF_DIR / "nested_table.rtf"
        example_txt = TEXT_DIR / "nested_table.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
