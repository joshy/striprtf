import unittest

from striprtf.striprtf import rtf_to_text


class TestSurrogatePairs(unittest.TestCase):
    def test_signed_surrogate_pairs(self):
        for source, expected in (
            (r"{\rtf1\u-10179?\u-8704?}", "\U0001f600"),
            (r"{\rtf1\u-10188?\u-8930?}", "\U0001d11e"),
            (r"{\rtf1\u-10176?\u-9216?}", "\U00020000"),
            (r"{\rtf1\u-10240?\u-9216?}", "\U00010000"),
            (r"{\rtf1\u-9217?\u-8193?}", "\U0010ffff"),
        ):
            with self.subTest(source=source):
                result = rtf_to_text(source)
                self.assertEqual(expected, result)
                self.assertEqual(expected.encode("utf-8"), result.encode("utf-8"))

    def test_unsigned_surrogate_pairs(self):
        self.assertEqual("\U0001f600", rtf_to_text(r"{\rtf1\u55357?\u56832?}"))

    def test_fallback_characters_are_skipped(self):
        for body in (
            r"\uc0\u-10179\u-8704",
            r"\uc1\u-10179?\u-8704?",
            r"\uc1\u-10179\'3f\u-8704\'3f",
            r"\uc2\u-10179??\u-8704??",
        ):
            with self.subTest(body=body):
                self.assertEqual("\U0001f600", rtf_to_text("{\\rtf1" + body + "}"))

    def test_formatting_between_surrogates(self):
        for body in (
            r"\u-10179?\b\u-8704?\b0",
            r"{\u-10179?}{\u-8704?}",
            r"\u-10179?{\*\comment ignored}\u-8704?",
        ):
            with self.subTest(body=body):
                self.assertEqual("\U0001f600", rtf_to_text("{\\rtf1" + body + "}"))

    def test_mixed_text_and_consecutive_pairs(self):
        source = (
            r"{\rtf1\ansicpg1252 Caf\'e9 \u20013? "
            r"\u-10179?\u-8704?\u-10188?\u-8930?\par}"
        )
        self.assertEqual("Caf\u00e9 \u4e2d \U0001f600\U0001d11e\n", rtf_to_text(source))

    def test_nonpaired_surrogates_keep_existing_behavior(self):
        for body, expected in (
            (r"\u-10179?", "\ud83d"),
            (r"\u-8704?", "\ude00"),
            (r"\u-8704?\u-10179?", "\ude00\ud83d"),
            (r"\u-10179?x\u-8704?", "\ud83dx\ude00"),
            (r"\u-10179?\par\u-8704?", "\ud83d\n\ude00"),
        ):
            with self.subTest(body=body):
                self.assertEqual(expected, rtf_to_text("{\\rtf1" + body + "}"))

    def test_existing_unicode_text_is_preserved(self):
        for text in ("", "ASCII", "\ufeff\u4e2d\u6587", "\U0001f600\U0010ffff"):
            with self.subTest(text=text):
                self.assertEqual(text, rtf_to_text("{\\rtf1 " + text + "}"))

    def test_bmp_unicode_escapes_are_preserved(self):
        self.assertEqual(
            "\u4e2d\u6587\uffff", rtf_to_text(r"{\rtf1\u20013?\u25991?\u-1?}")
        )
