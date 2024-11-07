import unittest

from striprtf.striprtf import rtf_to_text


class TestFromString(unittest.TestCase):
    def test_from_simple_string(self):
        source = (
            "{\\rtf1\\ansi\n{\\fonttbl\\f0\\fnil Monospaced;\\f1\\fnil DejaVu Sans;}\n"
            "{\\colortbl\\red0\\green0\\blue0;\\red0\\green0\\blue0;}\n\n"
            "\\f1\\fs24\\i0\\b0\\cf1 Hello with simple text.\\par\n}\n"
        )
        result = rtf_to_text(source)
        self.assertEqual("Hello with simple text.\n", result)

    def test_with_special_chars_and_encoding_parameter(self):
        source = (
            "{\\rtf1\\ansi\\n{\\fonttbl\\f0\\fnil Monospaced;\\f1\\fnil DejaVu Sans;}\n"
            "{\\colortbl\\red0\\green0\\blue0;\\red0\\green0\\blue0;}\n"
            "\\f1\\fs24\\i0\\b0\\cf1 Visibilit\\'e9 r\\'e9duite sur les montagnes.\\par\\n}"
        )
        result = rtf_to_text(source, encoding="latin-1")
        self.assertEqual("Visibilité réduite sur les montagnes.\n", result)
