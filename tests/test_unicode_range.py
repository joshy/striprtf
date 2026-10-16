import unittest

from striprtf.striprtf import rtf_to_text

B = "\\"  # backslash


def rtf(control_word):
    return "{" + B + "rtf1 a" + B + control_word + " ?b}"


class TestUnicodeRange(unittest.TestCase):
    """The parameter of the u control word is a signed 16-bit number. A value out of
    the Unicode range raised OverflowError or ValueError from chr(), so a few bytes of
    RTF stopped the conversion. It becomes U+FFFD now.
    """

    def test_out_of_range_values_do_not_raise(self):
        for value in ("9999999999", "-9999999999", "1114112"):
            with self.subTest(value=value):
                self.assertEqual("a" + chr(0xFFFD) + "b", rtf_to_text(rtf("u" + value)))

    def test_values_in_range_are_unchanged(self):
        for value, char in (("337", 0x151), ("-1", 0xFFFF), ("-32768", 0x8000),
                            ("1114111", 0x10FFFF)):
            with self.subTest(value=value):
                self.assertEqual("a" + chr(char) + "b", rtf_to_text(rtf("u" + value)))


if __name__ == "__main__":
    unittest.main()
