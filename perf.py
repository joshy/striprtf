import timeit
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / 'tests' / 'rtf'
simple_table_rtf = RTF_DIR / '25545032.rtf'

with simple_table_rtf.open() as f:
   source = f.read()

def wrap():
    return rtf_to_text(source)

globals()['g'] = wrap

print(timeit.timeit(wrap, setup='from striprtf.striprtf import rtf_to_text', number=1000))