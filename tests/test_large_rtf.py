import time
import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"

# Upper bound for parsing large_rtf.rtf (~2.4 MB). Takes ~0.4s, the headroom is
# for slow CI. Guards against the font table bottleneck of issue 71 coming back.
MAX_PARSE_SECONDS = 10


class TestLargeRtf(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        example_rtf = RTF_DIR / "large_rtf.rtf"

        with example_rtf.open() as source:
            raw = source.read()

        start = time.perf_counter()
        cls.result = rtf_to_text(raw)
        cls.duration = time.perf_counter() - start

    def test_large_rtf(self):
        example_txt = TEXT_DIR / "large_rtf.txt"

        with example_txt.open(encoding="utf-8") as destination:
            self.maxDiff = None
            self.assertEqual(destination.read(), self.result)

    def test_large_rtf_timing(self):
        print(f"\nparsed large_rtf.rtf in {self.duration:.2f}s")
        self.assertLess(self.duration, MAX_PARSE_SECONDS)
