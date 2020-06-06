import unittest
from filecmp import cmp
from pathlib import Path

from tabulate import tabulate

from striprtf.striprtf import extract_tables

RTF_DIR = Path.cwd() / "tests" / "rtf"
CSV_DIR = Path.cwd() / "tests" / "csv"


class TestHello(unittest.TestCase):
    def test_empty(self):
        example_rtf = RTF_DIR / "Speiseplan_KW_32-33_Eybl.rtf"
        example_txt = CSV_DIR / "simple_table.csv"

        with example_rtf.open() as source:
            tables = extract_tables(source.read())
            for t in tables:
                print(tabulate(t))
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
