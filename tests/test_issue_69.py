import unittest

from striprtf.striprtf import rtf_to_text


class TestTrailingBytes(unittest.TestCase):
    """An RTF file is a single ``{ <header> <document> }`` group, everything
    after the closing brace is out of band and gets discarded.

    See https://github.com/joshy/striprtf/issues/69
    """

    def test_trailing_text_is_discarded(self):
        self.assertEqual("hello", rtf_to_text(r"{\rtf1 hello}TRAILING"))

    def test_trailing_group_is_discarded(self):
        self.assertEqual("hello", rtf_to_text(r"{\rtf1 hello}{\rtf1 second}"))

    def test_balanced_document_is_untouched(self):
        self.assertEqual("a b c", rtf_to_text(r"{\rtf1 a {\b b} c}"))

    def test_text_before_the_document_is_kept(self):
        # nothing to discard yet, the outer group has not been opened
        self.assertEqual("LEADINGhello", rtf_to_text(r"LEADING{\rtf1 hello}"))
