import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestTXRTF32(unittest.TestCase):
    def test_empty(self):
        example_rtf = RTF_DIR / "TX_RTF32_18.0.541.501.rtf"
        example_txt = TEXT_DIR / "TX_RTF32_18.0.541.501.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read(), errors="strict")
        with example_txt.open(encoding="utf-8") as destination:
            self.assertEqual(destination.read(), result)
