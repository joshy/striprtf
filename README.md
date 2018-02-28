# striprtf
[![Build Status](https://api.travis-ci.org/joshy/striprtf.svg?branch=master)](https://travis-ci.org/joshy/striprtf)

## Purpose
This is a simple library to convert rtf files to python strings. A lot of
medical documents are written in rtf format which is not ideal for parsing
and further processing. This library converts it to plain old text. Reading
and Saving of files is not part of it.

## History
[Pyth](https://github.com/brendonh/pyth) was not working for the rtf files I
had. The next best thing was this gist:
https://gist.github.com/gilsondev/7c1d2d753ddb522e7bc22511cfb08676
Very few additions where made, e.g. better formatting tables.