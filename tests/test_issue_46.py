import unittest

from striprtf.striprtf import rtf_to_text

RTF = r"{\rtf1\ansi\ansicpg0 T\'e4st}"


class Table(unittest.TestCase):
    def test_error_handling_ignore(self):
        result = rtf_to_text(RTF, errors="ignore")
        self.assertEqual("Tst", result)

    def test_error_handling_replace(self):
        result = rtf_to_text(RTF, errors="replace")
        self.assertEqual("T�st", result)
