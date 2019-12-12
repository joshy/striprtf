import unittest
from pathlib import Path
from filecmp import cmp

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / 'tests' / 'rtf'
TEXT_DIR = Path.cwd() / 'tests' / 'text'

class TestSpeiseplan(unittest.TestCase):

    def test_speiseplan(self):
        example_rtf = RTF_DIR / 'Speiseplan_KW_32-33_Eybl.rtf'
        example_txt = TEXT_DIR / 'Speiseplan_KW_32-33_Eybl.txt'

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
            with(open('foo.text', 'w')) as f:
                f.write(result)
        with example_txt.open() as destination:
            self.maxDiff = None
            self.assertEqual(destination.read(), result)

