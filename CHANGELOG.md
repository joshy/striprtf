# Changelog


## v0.0.24 - 11.05.23
  * Clarified the meaning of the `encoding` parameter. It is used as the encoding if an explicit encoding is missing in the rtf file. As the majority of rtf files is encoded in ANSI, this is now the default. 
  Fixes [#41](https://github.com/joshy/striprtf/issues/41).
    Thanks to [plessbd](https://github.com/plessbd) and [stevengj](https://github.com/stevengj)

## v0.0.23 - 11.05.23
  * Parameter `encoding` is now always encoded to `utf-8` output. This release fixes some of the troubles with encodings. 
    Thanks to [plessbd](https://github.com/plessbd), [stevengj](https://github.com/stevengj) and [nikita-petrashen](https://github.com/nikita-petrashen)

## v0.0.22 - 18.11.22
  * Added parameter `encoding` to rtf_to_text which is set to `utf-8` as a default. Thanks to [jnth](https://github.com/jnth)

## v0.0.21 - 17.08.22
 * Fixes [#32](https://github.com/joshy/striprtf/issues/32)  
  Thanks to [akBeater](https://github.com/akBeater), [amirali1690](https://github.com/amirali1690)


## v0.0.20 - 23.02.22
 * Fixes [#31](https://github.com/joshy/striprtf/issues/31)

## v0.0.19 - 05.01.2022
 * Fixes [#29](https://github.com/joshy/striprtf/issues/29)

## v0.0.18 - 03.01.2022
 * Fixes [#20](https://github.com/joshy/striprtf/issues/20)

## v0.0.17 - 17.12.2021
 * Fixes [#28](https://github.com/joshy/striprtf/issues/28)

## v0.0.16 - 03.11.2021
 * Added a new parameter "errors" which accepts "strict" (default) and "ignore" as options
   on how to handle encoding errors. 

## v0.0.15 - 30.09.2021
 * Add support for ansicpg encoding (e.g. windows-1250) with #19 \
   Contributed by [Jan](https://github.com/jan-swiecki)

## v0.0.14 - 08.09.2021
 * Fixes #18. Small code improvements

## v0.0.13 - 19.05.2021
 * Fixes #17. Restore python2 compatibility. 
   This will be the last version to support that!

## v0.0.12 - 02.12.2020
 * migrate to github actions

## v0.0.11 - 27.08.2020
 * Fixed ldblquote (spotted by Ziyang(Claude) Hu)

## v0.0.10 - 16.03.2020
 * Wrong upload to pypi

## v0.0.9 - 12.3.2020
 * Fix for https://github.com/joshy/striprtf/issues/6
 * Added version to cli
 * Switched to pytest

## v0.0.8 - 21.02.2020
 * Removed f-string in setup.py (below python 3.6 fails to install)

## v0.0.7 - 27.01.2020
 * Added `__version__` attribute

## v0.0.6 - 17.12.2019
 * Add CR LR processing (contributed by [Simon](https://github.com/UnacceptableBehaviour))

## v0.0.5 - 27.05.2019
 * fix for #3

## v0.0.4 - 10.02.2019
 * added cli

## v0.0.3 - 27.03.2018
 * fixed wrong download url in setup.py

## v0.0.2 - 27.03.2018
 * nested cells are also separated with '|'

## v0.0.1 - 28.02.2018
 * Initial version