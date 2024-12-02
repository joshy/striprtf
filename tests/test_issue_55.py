import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"




class Fonttbl(unittest.TestCase):
    def test_fonttbl_file(self):
        example_rtf = RTF_DIR / "issue_55.rtf"
        example_txt = TEXT_DIR / "issue_55.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

    def test_fonttbl_file1(self):
        example_rtf = RTF_DIR / "issue_55_1.rtf"
        example_txt = TEXT_DIR / "issue_55_1.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
            print("result:::", result)
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
  
