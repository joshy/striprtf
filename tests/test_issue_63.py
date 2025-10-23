import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestListtextNumbering(unittest.TestCase):
    """Test that \\listtext numbering is preserved in output.

    See https://github.com/joshy/striprtf/issues/63
    """

    def test_listtext_numbering_preserved(self):
        example_rtf = RTF_DIR / "issue_63.rtf"
        example_txt = TEXT_DIR / "issue_63.txt"

        with example_rtf.open() as source:
            raw = source.read()
            result = rtf_to_text(raw)

        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
