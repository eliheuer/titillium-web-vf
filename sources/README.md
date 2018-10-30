# Source Notes

### Building fonts from source

The font files and specimens in this repo can be built all at once with the `BUILD.py` script in this directory.

Open a UNIX terminal and run the following command from the root directory of this repo:

```
python3 sources/BUILD.py
```

Dependencies installed should include:

 - [fontmake](https://github.com/googlei18n/fontmake)
 - [gftools](https://github.com/googlefonts/gftools)
 - [ttfautohint](https://www.freetype.org/ttfautohint/)

### Building fonts and updating the specimen

When building the font, the specimen can also be updated and regenerated. Just install the above dependencies, plus `drawbot`:

 - [drawbot](http://drawbot.com)
