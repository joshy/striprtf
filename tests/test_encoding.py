import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestEncoding(unittest.TestCase):
    def test_default_font_charset(self):
        cases = (
            (1, 204, r"\'cf\'f0\'e8\'e2\'e5\'f2", "Привет"),
            (0, 161, r"\'e1\'e2", "αβ"),
            (2, 128, r"\'82\'a0", "あ"),
        )
        for font_id, charset, escaped, expected in cases:
            with self.subTest(font_id=font_id, charset=charset):
                source = (
                    rf"{{\rtf1\ansi\ansicpg1252\deff{font_id}"
                    rf"{{\fonttbl{{\f{font_id}\fcharset{charset} Font;}}}}"
                    + escaped
                    + "}"
                )
                self.assertEqual(expected, rtf_to_text(source))

    def test_default_font_after_scoped_override(self):
        source = (
            r"{\rtf1\ansi\ansicpg1252\deff1"
            r"{\fonttbl{\f0\fcharset0 Arial;}{\f1\fcharset204 Arial;}}"
            r"\'cf{\f0 \'e9}\'f0}"
        )
        self.assertEqual("Пéр", rtf_to_text(source))

    def test_explicit_font_selection_keeps_precedence(self):
        for font_id in (0, 99):
            with self.subTest(font_id=font_id):
                source = (
                    r"{\rtf1\ansi\ansicpg1252\deff1"
                    r"{\fonttbl{\f0\fcharset0 Arial;}{\f1\fcharset204 Arial;}}"
                    rf"\f{font_id} \'e9}}"
                )
                self.assertEqual("é", rtf_to_text(source))

    def test_unavailable_default_font_uses_document_codepage(self):
        fonttbl = r"{\fonttbl{\f1\fcharset204 Arial;}}"
        for header in (fonttbl, r"\deff99" + fonttbl, r"\deff1"):
            with self.subTest(header=header):
                source = r"{\rtf1\ansi\ansicpg1252" + header + r"\'e9}"
                self.assertEqual("é", rtf_to_text(source))

    def test_empty(self):
        example_rtf = RTF_DIR / "encoding.rtf"
        example_txt = TEXT_DIR / "encoding.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read(), errors="ignore")
        with example_txt.open(encoding="utf-8") as destination:
            self.assertEqual(destination.read(), result)

    def test_second_document(self):
        example_rtf = RTF_DIR / "encoding_2.rtf"
        example_txt = TEXT_DIR / "encoding_2.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read(), errors="ignore")
        with example_txt.open(encoding="utf-8") as destination:
            self.assertEqual(destination.read(), result)
