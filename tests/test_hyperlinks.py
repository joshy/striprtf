import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestHyperlinks(unittest.TestCase):
    def test_hyperlinks(self):
        example_rtf = RTF_DIR / "hyperlinks.rtf"
        example_txt = TEXT_DIR / "hyperlinks.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())

        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

    def test_mac_textedit(self):
        example_rtf = RTF_DIR / "mac_textedit_hyperlink.rtf"
        example_txt = TEXT_DIR / "mac_textedit_hyperlink.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())

        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

    def test_user_sample(self):
        example_rtf = RTF_DIR / "Example_text.rtf"
        example_txt = TEXT_DIR / "Example_text.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())

        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)
