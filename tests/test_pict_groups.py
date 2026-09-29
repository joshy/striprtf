import unittest
from pathlib import Path

from striprtf.striprtf import remove_pict_groups, rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestPictGroups(unittest.TestCase):
    """Removing binary encoded pictures must not change the group structure.

    A \\pict group ends at its own closing brace, not at the first closing brace in
    it: it usually contains nested groups ({\\*\\picprop ...}, {\\*\\blipuid ...}), and
    the N bytes of \\binN binary data can contain braces too. Otherwise the rest of
    the picture ends up in the output, the braces get unbalanced and the text after
    the picture is lost (the document group is closed too early, see issue 69).
    """

    def test_pict_bin_file(self):
        example_rtf = RTF_DIR / "pict_bin.rtf"
        example_txt = TEXT_DIR / "pict_bin.txt"

        # newline="": the binary data must be read unchanged, \binN counts bytes
        with example_rtf.open(encoding="ISO-8859-1", newline="") as source:
            result = rtf_to_text(source.read())
        with example_txt.open(encoding="utf-8") as destination:
            self.assertEqual(destination.read(), result)

    def test_binary_data_is_not_in_the_output(self):
        # a picture in the document body, with a nested group before the binary PNG
        # data: the picture was ended at the brace of {\*\blipuid ...} and the PNG
        # data was output as text
        example_rtf = RTF_DIR / "pict_bin_leak.rtf"
        example_txt = TEXT_DIR / "pict_bin_leak.txt"

        with example_rtf.open(encoding="ISO-8859-1", newline="") as source:
            result = rtf_to_text(source.read())
        for marker in ("PNG", "IHDR", "IDAT", "IEND"):
            self.assertNotIn(marker, result)
        self.assertFalse([c for c in result if ord(c) < 32 and c not in "\n\t"])
        with example_txt.open(encoding="utf-8") as destination:
            self.assertEqual(destination.read(), result)

    def test_nested_groups_in_pict(self):
        rtf = (
            r"{\rtf1 before{\pict{\*\picprop{\sp{\sn shapeType}{\sv 75}}}\pngblip"
            r"{\*\blipuid 0123}\bin4 ABCD}after}"
        )
        self.assertEqual("beforeafter", rtf_to_text(rtf))

    def test_braces_in_binary_data(self):
        rtf = "{\\rtf1 before{\\pict\\pngblip\\bin6 {{}}\\x}after}"
        self.assertEqual("beforeafter", rtf_to_text(rtf))

    def test_space_after_bin_is_not_data(self):
        # the space delimits the control word, the 3 bytes of data are "}}}"
        rtf = "{\\rtf1 a{\\pict\\bin3 }}}}b}"
        self.assertEqual("ab", rtf_to_text(rtf))

    def test_pict_in_binary_data(self):
        rtf = "{\\rtf1 a{\\pict\\bin11 {\\pict\\bin9}b}"
        self.assertEqual("ab", rtf_to_text(rtf))

    def test_escaped_braces_in_pict(self):
        rtf = r"{\rtf1 a{\pict{\*\picprop{\sv \}\{\\}}\bin1 x}b}"
        self.assertEqual("ab", rtf_to_text(rtf))

    def test_several_pictures(self):
        rtf = (
            r"{\rtf1 one{\pict\bin2 xy}two{\*\shppict{\pict{\*\blipuid 1234}\bin1 z}}"
            r"three{\pict\pngblip 89504e47}four}"
        )
        self.assertEqual("onetwothreefour", rtf_to_text(rtf))

    def test_braces_of_pict_groups_are_kept(self):
        rtf = r"{\rtf1 a{\pict{\*\blipuid 12}\bin2 {{}b{\*\shppict{\pict\bin1 }}}c}"
        self.assertEqual(r"{\rtf1 a{}b{\*\shppict{}}c}", remove_pict_groups(rtf))

    def test_unterminated_pict(self):
        self.assertEqual("text", rtf_to_text(r"{\rtf1 text{\pict\bin2 ab"))

    def test_text_without_binary_data_is_untouched(self):
        rtf = r"{\rtf1 a{\pict\pngblip 89504e47}b}"
        self.assertIs(rtf, remove_pict_groups(rtf))


if __name__ == "__main__":
    unittest.main()
