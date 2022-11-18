# striprtf
![Build status](https://github.com/joshy/striprtf/workflows/striprtf%20build/badge.svg)

## Purpose
This is a simple library to convert rtf files to python strings. A lot of
medical documents are written in rtf format which is not ideal for parsing
and further processing. This library converts it to plain old text.

## How to use
```python
from striprtf.striprtf import rtf_to_text
rtf = "some rtf encoded string"
text = rtf_to_text(rtf)
print(text)
```

If you want to use a different encoding than `utf-8` to can pass the parameter `encoding`.
```python
from striprtf.striprtf import rtf_to_text
rtf = "some rtf encoded string in latin1"
text = rtf_to_text(rtf, encoding="latin-1")
print(text)
```

Sometimes UnicodeDecodingErrors can happen because of various reasons.
In this case you can try to relax the encoding process like this:
```python
from striprtf.striprtf import rtf_to_text
rtf = "some rtf encoded string"
text = rtf_to_text(rtf, errors="ignore")
print(text)
```

## How to use online
If you don't want to install, there is also an online version available at https://striprtf.dev which can be used for free. 


## History
[Pyth](https://github.com/brendonh/pyth) was not working for the rtf files I
had. The next best thing was this gist:
https://gist.github.com/gilsondev/7c1d2d753ddb522e7bc22511cfb08676

Very few additions where made, e.g. better formatting of tables.

## Pushing to PyPi
 * pip install twine


Run commands
```
python setup.py sdist bdist_wheel
twine upload -r testpypi dist/*
twine upload -r pypi dist/*
```
