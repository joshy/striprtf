import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / 'tests' / 'rtf'
TEXT_DIR = Path.cwd() / 'tests' / 'text'

class TestSimple(unittest.TestCase):

    def test_empty(self):
        example_rtf = RTF_DIR / 'nutridoc.rtf'
        example_txt = TEXT_DIR / 'nutridoc.txt'
        out_txt = TEXT_DIR / 'nutridoc_out.txt'

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())

        with open(out_txt, 'w') as output_file:
            output_file.write(result)

        with example_txt.open() as destination:
            self.assertEqual(destination.read(), result)

