# Source Notes

### Building fonts from source

The font files and specimens in this repo can be built all at once with the `BUILD.py` script in this directory.

`BUILD.py` requiers a few dependencies. These can be installed all at once with the included `requierments.txt` file.

Open a UNIX terminal and run `pip install -r requierments.txt`, or install each requierment individually:

 - [fontmake](https://github.com/googlei18n/fontmake)
 - [gftools](https://github.com/googlefonts/gftools)
 - [ttfautohint](https://www.freetype.org/ttfautohint/)

Once requierments are installed, run the following command from the root directory of this repo:

```
python3 sources/BUILD.py
```

### Building fonts and updating specimens

When building the fonts, the specimen can also be updated with any new changes to the fonts. Just install the above dependencies, plus `drawbot`:

 - [drawbot](http://drawbot.com)
