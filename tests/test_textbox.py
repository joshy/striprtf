import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestTextBox(unittest.TestCase):
    """The text of text boxes is part of the document.

    Word writes a text box as a shape,
    ``{\\shp{\\*\\shpinst ...{\\shptxt text}}{\\shprslt ...}}``, where
    ``\\shprslt`` is a copy of the shape as an old style drawing object for readers
    that do not understand shapes. The text has to appear once: from ``\\shptxt``,
    not from the copy.
    """

    def test_textbox_file(self):
        example_rtf = RTF_DIR / "textbox.rtf"
        example_txt = TEXT_DIR / "textbox.txt"

        with example_rtf.open() as source:
            result = rtf_to_text(source.read())
        with example_txt.open(encoding="utf-8") as destination:
            self.assertEqual(destination.read(), result)

    def test_textbox_text_is_not_duplicated(self):
        rtf = (
            r"{\rtf1 before\par {\shp{\*\shpinst{\sp{\sn shapeType}{\sv 202}}"
            r"{\shptxt in the box\par}}"
            r"{\shprslt{\*\do\dptxbx{\dptxbxtext in the box\par}}}}after}"
        )
        self.assertEqual("before\nin the box\nafter", rtf_to_text(rtf))

    def test_shape_properties_are_ignored(self):
        rtf = (
            r"{\rtf1 {\shp{\*\shpinst{\sp{\sn fillColor}{\sv 16777215}}"
            r"{\shptxt box\par}}}}"
        )
        self.assertEqual("box\n", rtf_to_text(rtf))

    def test_group_shape(self):
        rtf = (
            r"{\rtf1 {\shpgrp{\*\shpinst{\sp{\sn groupLeft}{\sv 0}}"
            r"{\shp{\*\shpinst{\shptxt first\par}}}"
            r"{\shp{\*\shpinst{\shptxt second\par}}}}"
            r"{\shprslt{\*\do\dpgroup\dptxbx{\dptxbxtext first\par}"
            r"\dptxbx{\dptxbxtext second\par}\dpendgroup}}}}"
        )
        self.assertEqual("first\nsecond\n", rtf_to_text(rtf))

    def test_old_style_drawing_object(self):
        rtf = (
            r"{\rtf1 {\*\do\dobxcolumn\dptxbx{\dptxbxtext drawing object\par}"
            r"\dpx0\dpy0}after}"
        )
        self.assertEqual("drawing object\nafter", rtf_to_text(rtf))

    def test_picture_shape_has_no_text(self):
        rtf = (
            r"{\rtf1 {\shp{\*\shpinst{\sp{\sn pib}{\sv {\pict\pngblip 89504e47}}}}"
            r"{\shprslt{\*\shppict{\pict\pngblip 89504e47}}"
            r"{\nonshppict{\pict\wmetafile8 0100}}}}after}"
        )
        self.assertEqual("after", rtf_to_text(rtf))

    def test_textbox_in_ignored_destination_stays_ignored(self):
        # a text box in the header is ignored together with the header
        rtf = (
            r"{\rtf1 {\header {\shp{\*\shpinst{\shptxt header box\par}}}header\par}"
            r"body}"
        )
        self.assertEqual("body", rtf_to_text(rtf))

    def test_other_star_destinations_are_still_ignored(self):
        self.assertEqual("text", rtf_to_text(r"{\rtf1 {\*\unknownword hidden}text}"))
        self.assertEqual("text", rtf_to_text(r"{\rtf1 {\*\shpinstx hidden}text}"))


if __name__ == "__main__":
    unittest.main()
