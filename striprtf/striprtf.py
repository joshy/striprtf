import re
import codecs

"""
Taken from https://gist.github.com/gilsondev/7c1d2d753ddb522e7bc22511cfb08676
and modified for better output of tables.
"""

# fmt: off
# control words which specify a "destination".
destinations = frozenset((
    'aftncn','aftnsep','aftnsepc','annotation','atnauthor','atndate','atnicn','atnid',
    'atnparent','atnref','atntime','atrfend','atrfstart','author','background',
    'bkmkend','bkmkstart','blipuid','buptim','category','colorschememapping',
    'colortbl','comment','company','creatim','datafield','datastore','defchp','defpap',
    'do','doccomm','docvar','dptxbxtext','ebcend','ebcstart','factoidname','falt',
    'fchars','ffdeftext','ffentrymcr','ffexitmcr','ffformat','ffhelptext','ffl',
    'ffname','ffstattext','file','filetbl','fldinst','fldtype','fonttbl',
    'fname','fontemb','fontfile','footer','footerf','footerl','footerr',
    'footnote','formfield','ftncn','ftnsep','ftnsepc','g','generator','gridtbl',
    'header','headerf','headerl','headerr','hl','hlfr','hlinkbase','hlloc','hlsrc',
    'hsv','htmltag','info','keycode','keywords','latentstyles','lchars','levelnumbers',
    'leveltext','lfolevel','linkval','list','listlevel','listname','listoverride',
    'listoverridetable','listpicture','liststylename','listtable','listtext',
    'lsdlockedexcept','macc','maccPr','mailmerge','maln','malnScr','manager','margPr',
    'mbar','mbarPr','mbaseJc','mbegChr','mborderBox','mborderBoxPr','mbox','mboxPr',
    'mchr','mcount','mctrlPr','md','mdeg','mdegHide','mden','mdiff','mdPr','me',
    'mendChr','meqArr','meqArrPr','mf','mfName','mfPr','mfunc','mfuncPr','mgroupChr',
    'mgroupChrPr','mgrow','mhideBot','mhideLeft','mhideRight','mhideTop','mhtmltag',
    'mlim','mlimloc','mlimlow','mlimlowPr','mlimupp','mlimuppPr','mm','mmaddfieldname',
    'mmath','mmathPict','mmathPr','mmaxdist','mmc','mmcJc','mmconnectstr',
    'mmconnectstrdata','mmcPr','mmcs','mmdatasource','mmheadersource','mmmailsubject',
    'mmodso','mmodsofilter','mmodsofldmpdata','mmodsomappedname','mmodsoname',
    'mmodsorecipdata','mmodsosort','mmodsosrc','mmodsotable','mmodsoudl',
    'mmodsoudldata','mmodsouniquetag','mmPr','mmquery','mmr','mnary','mnaryPr',
    'mnoBreak','mnum','mobjDist','moMath','moMathPara','moMathParaPr','mopEmu',
    'mphant','mphantPr','mplcHide','mpos','mr','mrad','mradPr','mrPr','msepChr',
    'mshow','mshp','msPre','msPrePr','msSub','msSubPr','msSubSup','msSubSupPr','msSup',
    'msSupPr','mstrikeBLTR','mstrikeH','mstrikeTLBR','mstrikeV','msub','msubHide',
    'msup','msupHide','mtransp','mtype','mvertJc','mvfmf','mvfml','mvtof','mvtol',
    'mzeroAsc','mzeroDesc','mzeroWid','nesttableprops','nextfile','nonesttables',
    'objalias','objclass','objdata','object','objname','objsect','objtime','oldcprops',
    'oldpprops','oldsprops','oldtprops','oleclsid','operator','panose','password',
    'passwordhash','pgp','pgptbl','picprop','pict','pn','pnseclvl','pntext','pntxta',
    'pntxtb','printim','private','propname','protend','protstart','protusertbl','pxe',
    'result','revtbl','revtim','rsidtbl','rxe','shp','shpgrp','shpinst',
    'shppict','shprslt','shptxt','sn','sp','staticval','stylesheet','subject','sv',
    'svb','tc','template','themedata','title','txe','ud','upr','userprops',
    'wgrffmtfilter','windowcaption','writereservation','writereservhash','xe','xform',
    'xmlattrname','xmlattrvalue','xmlclose','xmlname','xmlnstbl',
    'xmlopen',
))
# fmt: on
charset_map = {
    0: "cp1252",  # Default
    42: "cp1252",  # Symbol
    77: "mac_roman",  # Mac Roman
    78: "mac_japanese",  # Mac Japanese
    79: "mac_chinesetrad",  # Mac Traditional Chinese
    80: "mac_korean",  # Mac Korean
    81: "mac_arabic",  # Mac Arabic
    82: "mac_hebrew",  # Mac Hebrew
    83: "mac_greek",  # Mac Greek
    84: "mac_cyrillic",  # Mac Cyrillic
    85: "mac_chinesesimp",  # Mac Simplified Chinese
    86: "mac_rumanian",  # Mac Romanian
    87: "mac_ukrainian",  # Mac Ukrainian
    88: "mac_thai",  # Mac Thai
    89: "mac_ce",  # Mac Central European
    128: "cp932",  # Japanese
    129: "cp949",  # Korean
    130: "cp1361",  # Johab (Korean)
    134: "cp936",  # Simplified Chinese (GBK)
    136: "cp950",  # Traditional Chinese (Big5)
    161: "cp1253",  # Greek
    162: "cp1254",  # Turkish
    163: "cp1258",  # Vietnamese
    177: "cp1255",  # Hebrew
    178: "cp1256",  # Arabic
    186: "cp1257",  # Baltic
    204: "cp1251",  # Cyrillic
    222: "cp874",  # Thai
    238: "cp1250",  # Eastern European
    254: "cp437",  # OEM United States
    255: "cp850",  # OEM Multilingual Latin 1
}

# Translation of some special characters.
# and section characters reset formatting
sectionchars = {"par": "\n", "sect": "\n\n", "page": "\n\n"}
specialchars = {
    **{
        "line": "\n",
        "tab": "\t",
        "emdash": "\u2014",
        "endash": "\u2013",
        "emspace": "\u2003",
        "enspace": "\u2002",
        "qmspace": "\u2005",
        "bullet": "\u2022",
        "lquote": "\u2018",
        "rquote": "\u2019",
        "ldblquote": "\u201C",
        "rdblquote": "\u201D",
        "row": "\n",
        "cell": "|",
        "nestcell": "|",
        "~": "\xa0",
        "\n": "\n",
        "\r": "\r",
        "{": "{",
        "}": "}",
        "\\": "\\",
        "-": "\xad",
        "_": "\u2011",
    },
    **sectionchars,
}

PATTERN = re.compile(
    r"\\([a-z]{1,32})(-?\d{1,10})?[ ]?|\\'([0-9a-f]{2})|\\([^a-z])|([{}])|[\r\n]+|(.)",
    re.IGNORECASE,
)

HYPERLINKS = re.compile(
    r"(\{\\field\{\s*\\\*\\fldinst\{.*HYPERLINK\s(\".*\")\}{2}\s*\{.*?\s+(.*?)\}{2,3})",
    re.IGNORECASE,
)

FONTTABLE = re.compile(r"\\f(\d+).*?\\fcharset(\d+).*?([^;]+);")

def rtf_to_text(text, encoding="cp1252", errors="strict"):
    """Converts the rtf text to plain text.

    Parameters
    ----------
    text : str
        The rtf text
    encoding : str
        Input encoding which is ignored if the rtf file contains an explicit codepage directive,
        as it is typically the case. Defaults to `cp1252` encoding as it the most commonly used.
    errors : str
        How to handle encoding errors. Default is "strict", which throws an error. Another
        option is "ignore" which, as the name says, ignores encoding errors.

    Returns
    -------
    str
        the converted rtf text as a python unicode string
    """
    text = re.sub(
        HYPERLINKS, "\\1(\\2)", text
    )  # captures links like link_text(http://link_dest)
    stack = []
    fonttbl = {}
    default_font = None
    current_font = None
    ignorable = False  # Whether this group (and all inside it) are "ignorable".
    suppress_output = False  # Whether this group (and all inside it) are "ignorable".
    ucskip = 1  # Number of ASCII characters to skip after a unicode character.
    curskip = 0  # Number of ASCII characters left to skip
    hexes = None
    out = ""

    # Simplified font table regex

    fonttbl_matches = FONTTABLE.findall(text)
    for font_id, fcharset, font_name in fonttbl_matches:
        fonttbl[font_id] = {
            "name": font_name.strip(),
            "charset": fcharset,
            "encoding": charset_map.get(int(fcharset), encoding),
        }
    for match in PATTERN.finditer(text):
        word, arg, _hex, char, brace, tchar = match.groups()
        if hexes and not _hex:
            # Decode accumulated hexes
            out += bytes.fromhex(hexes).decode(
                encoding=fonttbl.get(current_font, {"encoding": encoding}).get(
                    "encoding", encoding
                ),
                errors=errors,
            )
            hexes = None
        if brace:
            curskip = 0
            if brace == "{":
                # Push state
                stack.append((ucskip, ignorable, suppress_output))
            elif brace == "}":
                # Pop state
                if stack:
                    ucskip, ignorable, suppress_output = stack.pop()
                # sample_3.rtf throws an IndexError because of stack being empty.
                # don't know right now how this could happen, so for now this is
                # a ugly hack to prevent it
                else:
                    ucskip = 0
                    ignorable = True
        elif char:  # \x (not a letter)
            curskip = 0
            if char in specialchars:
                if char in sectionchars:
                    current_font = default_font
                if not ignorable:
                    out += specialchars[char]
            elif char == "*":
                ignorable = True
        elif word:  # \foo
            curskip = 0
            if word in destinations:
                ignorable = True
            # http://www.biblioscape.com/rtf15_spec.htm#Heading8
            elif word == "ansicpg":
                encoding = f"cp{arg}"
                try:
                    codecs.lookup(encoding)
                except LookupError:
                    encoding = "utf8"
            if ignorable or suppress_output:
                pass
            elif word in specialchars:
                out += specialchars[word]
            elif word == "uc":
                ucskip = int(arg)
            elif word == "u":
                # because of https://github.com/joshy/striprtf/issues/6
                if arg is None:
                    curskip = ucskip
                else:
                    c = int(arg)
                    if c < 0:
                        c += 0x10000
                    out += chr(c)
                    curskip = ucskip
            elif word == "f":
                current_font = arg
            elif word == "deff":
                default_font = arg
            elif word == "fonttbl":
                suppress_output = True
            elif word == "colortbl":
                suppress_output = True

        elif _hex:  # \'xx
            if curskip > 0:
                curskip -= 1
            elif not ignorable:
                # Accumulate hex characters to decode later
                if not hexes:
                    hexes = _hex
                else:
                    hexes += _hex
        elif tchar:
            if curskip > 0:
                curskip -= 1
            elif not ignorable and not suppress_output:
                out += tchar

    return out
