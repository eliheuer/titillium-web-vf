# Titillium Web Variable Fonts
This repo contains the [fonts](fonts), [source files](sources), and [specimens](docs)
for a remastered Titillium Web font family available on
[Google Fonts](https://fonts.google.com/specimen/Titillium+Web).
It started as a fork of [Cario](https://github.com/Gue3bara/Cairo)
by [Mohamed Gaber](https://gaber.design/projects), which is a fork of
[Titillium Web](http://nta.accademiadiurbino.it/titillium.html)
that adds support for the Arabic Script.

An [interactive web specimen](https://elih.blog/titillium-web-vf)
hosted from this repository
( [docs/index.html](https://github.com/eliheuer/titillium-web-vf/blob/master/docs/index.html) )
is here: [https://elih.blog/titillium-web-vf](https://elih.blog/titillium-web-vf)

![basic specimen](https://github.com/eliheuer/titillium-web-vf/blob/master/docs/specimens/basic-specimen.gif)

## Building New Fonts from Source
A Bash build script is located in the sources directory.
To build new font files, open a Unix terminal and activate a
[Python3 virtual environment](https://docs.python.org/3/library/venv.html)
with the packages from [requirements.txt](requirements.txt) installed.
Then, navigate to the root of this repository, and run the following:
```
scripts/build.sh
```

## Installation Instructions
Font files are in the fonts directory, please follow the install inscructions for your operating system of choice:

- [Linux](https://wiki.archlinux.org/index.php/fonts#Manual_installation)
- [MacOS](https://support.apple.com/en-us/HT201749)
- [Windows](https://support.microsoft.com/en-us/help/314960/how-to-install-or-remove-a-font-in-windows)

## Getting Involved
Would you like to contribute to the development of this font? Here is how **you** can help:

- Tell us about any bugs you find, or enhancements you would like to see on the Google Fonts issue tracker: [https://github.com/googlefonts/issues](https://github.com/googlefonts/issues)

- Contribute directly to the fonts. This repository contains a complete set of source files. Make changes and submit a pull request.
