import unittest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF = r"""{\rtf1\fbidis\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Microsoft Sans Serif;}{\f1\fswiss\fcharset134 Microsoft YaHei;}{\f2\fnil Microsoft Sans Serif;}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\ltrpar\f0\fs17 
00:00:44:22\par
00:00:48:05\par
\f1\'b8\'f9\'be\'dd\'d5\'e6\'ca\'b5\'b9\'ca\'ca\'c2\'b4\'b4\'d7\'f7\f0\par"""


class Table(unittest.TestCase):
    def test_parse_w_fontbl(self):
        result = rtf_to_text(RTF)
        self.assertEqual("00:00:44:22\n00:00:48:05\n根据真实故事创作\n", result)
