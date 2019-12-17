import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text, extract_tables

RTF_DIR = Path.cwd() / "tests" / "rtf"
CSV_DIR = Path.cwd() / "tests" / "csv"


class TestSimple(unittest.TestCase):
    def test_extract_simple_table(self):
        simple_table_rtf = RTF_DIR / "simple_table.rtf"
        simple_table_txt = CSV_DIR / "simple_table.csv"

        with simple_table_rtf.open() as source:
            result = extract_tables(source.read())
        with simple_table_txt.open() as destination:
            self.assertEqual(destination.read(), result)

