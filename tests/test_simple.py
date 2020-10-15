import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestSimple(unittest.TestCase):
    def test_empty(self):
        example_rtf = RTF_DIR / "hello.rtf"
        example_txt = TEXT_DIR / "hello.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

    def test_table(self):
        simple_table_rtf = RTF_DIR / "simple_table.rtf"
        simple_table_txt = TEXT_DIR / "simple_table.txt"

        with simple_table_rtf.open() as source:
            result = rtf_to_text(source.read())
        with simple_table_txt.open() as destination:
            self.assertEqual(destination.read(), result)

