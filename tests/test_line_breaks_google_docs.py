import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TXT_DIR = Path.cwd() / "tests" / "text"


class TestSimple(unittest.TestCase):
    def test_extract_simple_table(self):
        simple_table_rtf = RTF_DIR / "test_line_breaks_google_docs.rtf"
        simple_table_txt = TXT_DIR / "test_line_breaks_google_docs.txt"

        with simple_table_rtf.open() as source:
            result = rtf_to_text(source.read())
            with open("o.txt", "w") as f:
                f.write(result)
        with simple_table_txt.open() as destination:
            self.assertEqual(destination.read(), result)

