import unittest

from striprtf.striprtf import rtf_to_text

FONTTBL = r"{\fonttbl{\f0\fcharset0 Arial;}{\f1\fcharset161 Arial Greek;}{\f2\fcharset128 MS Mincho;}}"


ISSUE_56 = r"""{\rtf1\ansi\ansicpg1252\uc1\deff0\stshfdbch0\stshfloch0\stshfhich0\stshfbi0\deflang1031\deflangfe1031{ \fonttbl {\f0\froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;} {\f395\fswiss\fcharset222\fprq2 Tahoma (Thai);} } {\fs28\cf1\insrsid9330230 \'fc } {\f395 \'E0} \'fc {\f0  \'fc} }"""


class FontGroupScope(unittest.TestCase):
    """A font selected inside a group must not leak past the closing brace."""

    def test_issue_56_mixed_document(self):
        self.assertEqual("  ü  เ ü  ü ", rtf_to_text(ISSUE_56))

    def test_greek_group_then_western(self):
        rtf = (
            r"{\rtf1\ansi\ansicpg1252\deff0"
            + FONTTBL
            + r"{\f1 \'e1\'e2}\par Caf\'e9\par}"
        )
        self.assertEqual("αβ\nCafé\n", rtf_to_text(rtf))

    def test_multibyte_group_then_western(self):
        rtf = (
            r"{\rtf1\ansi\ansicpg1252\deff0"
            + FONTTBL
            + r"{\f2 \'82\'a0}\par Caf\'e9\par}"
        )
        self.assertEqual("あ\nCafé\n", rtf_to_text(rtf))

    def test_nested_groups_restore_each_level(self):
        rtf = (
            r"{\rtf1\ansi\ansicpg1252\deff0"
            + FONTTBL
            + r"{\f1 \'e1{\f2 \'82\'a0}\'e2}\par Caf\'e9\par}"
        )
        self.assertEqual("αあβ\nCafé\n", rtf_to_text(rtf))


if __name__ == "__main__":
    unittest.main()
