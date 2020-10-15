import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestSimple(unittest.TestCase):
    def test_full_table(self):
        example_rtf = RTF_DIR / "calcium_score.rtf"
        example_txt = TEXT_DIR / "calcium_score.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
            with (open("foo.text", "w")) as f:
                f.write(result)
        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
