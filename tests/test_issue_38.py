import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


RTF_TABLE = r"""
{\rtf1\ansi\deff0
\trowd
\cellx1000
\cellx2000
\cellx3000
\intbl cell 1\cell
\intbl cell 2\cell
\intbl cell 3\cell
\row
}
"""

TEXT_TABLE = """cell 1|cell 2|cell 3|
"""


class Table(unittest.TestCase):
    def test_table_file(self):
        example_rtf = RTF_DIR / "issue_38.rtf"
        example_txt = TEXT_DIR / "issue_38.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open() as destination:
            print(result)
            self.assertEqual(destination.read(), result)

    def test_table_string(self):
        result = rtf_to_text(RTF_TABLE)
        self.assertEqual(TEXT_TABLE, result)
          
