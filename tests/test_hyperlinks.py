import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestHello(unittest.TestCase):
    def test_empty(self):
        example_rtf = RTF_DIR / "hyperlinks.rtf"
        example_txt = TEXT_DIR / "hyperlinks.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        print("------------------°°°°°°°°°°°°°°°°§")
        print(result)
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

