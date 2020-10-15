import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TXT_DIR = Path.cwd() / "tests" / "text"


class TestSimple(unittest.TestCase):
    """
    Single backlash is not captured therefore the txt is without line breaks.
    """

    def test_extract_simple_table(self):
        simple_table_rtf = RTF_DIR / "line_break_textedit_mac.rtf"
        simple_table_txt = TXT_DIR / "line_break_textedit_mac.txt"

        with simple_table_rtf.open() as source:
            result = rtf_to_text(source.read())
        with simple_table_txt.open() as destination:
            self.assertEqual(destination.read(), result)

