import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestPartialConversion(unittest.TestCase):

    def test_partial(self):
        example_rtf = RTF_DIR / "BVWGT_20241227_W258_2227269_1_00_01.rtf"
        example_txt = TEXT_DIR / "BVWGT_20241227_W258_2227269_1_00_01.txt"

        with example_rtf.open(encoding="ISO-8859-1") as source:
            raw = source.read()
            result = rtf_to_text(raw, errors="ignore")

        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

   