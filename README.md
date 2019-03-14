# Titillium Web Variable Fonts
This repo contains the fonts and source files for a remastered variable font containing the full Titillium Web font family. It started as a fork of [Cario](https://github.com/Gue3bara/Cairo) by [Mohamed Gaber](https://gaber.design/), which is a fork of Titillium Web that adds support the Arabic script.

Titillium Web is a contemporary Arabic and Latin typeface family. Mohamed Gaber extended the famous Latin typeface family [Titillum Web](https://www.google.com/fonts/specimen/Titillium+Web) to support the Arabic script, with a design that is based on the Kufi calligraphic style. It balances classic and contemporary tastes with wide open counters and short ascenders and descenders that minimize length while maintaining easy readability. The lighter weights can be used for body text while the heavier weights are perfect for headlines and display typography. Each font includes stylistic ligatures and the Arabic component has a wide glyph set that supports the Arabic, Farsi and Urdu languages. 

![basic specimen](https://github.com/eliheuer/titillium-web-vf/blob/master/docs/specimens/basic-specimen.gif)

## Building From Source
To build new fonts from the source files, run `./BUILD.sh` from the root directory of this repo. This will start the automated build process with a few default flags enabled. To run just the build script or to set flags manually from the command line run the script directly: `python3 sources/BUILD.py`.

A few dependancies are requiered for the build script to work, from the root directory of this repo run: `pip install -r requirements.txt`.

For more information on the requirements, please see the source documentation [here](https://github.com/eliheuer/titillium-web-vf/tree/master/sources).

## License

Titillium Web is licensed under the SIL Open Font License v1.1 (<http://scripts.sil.org/OFL>).
To view the copyright and specific terms and conditions please refer to [OFL.txt](OFL.txt)

## Downloading Font Files (TTF)

Font files are located in the `fonts` directory: <https://github.com/eliheuer/titillium-web-vf/tree/master/fonts>

## Installation Instructions

- [GNU+Linux](https://wiki.archlinux.org/index.php/fonts#Manual_installation)
- [MacOS](https://support.apple.com/en-us/HT201749)
- [Windows](https://support.microsoft.com/en-us/help/314960/how-to-install-or-remove-a-font-in-windows)

## Getting Involved

Would you like to contribute to the development of this font? Here is how **you** can help:

1. Tell us about any bugs you find, or enhancements you would like to see on the issue tracker: [https://github.com/googlefonts/issues](https://github.com/googlefonts/issues)

2. Contribute directly to the fonts. This repository contains a complete set of source files. Make changes and submit a pull request.
