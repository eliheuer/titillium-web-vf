## Fontbakery report

Fontbakery version: 0.5.2.dev76+g2b6adfed

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>:fire: <b>FAIL:</b> DESCRIPTION.en_us.html must have less than 1000 bytes.</summary>

* [com.google.fonts/check/006](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/006)
* :fire: **FAIL** DESCRIPTION.en_us.html must have size smaller than 1000 bytes.

</details>
<br>
</details>
<details>
<summary><b>[13] TitilliumWeb-Italic-VF.ttf</b></summary>
<details>
<summary>:fire: <b>FAIL:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/020](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/020)
* :fire: **FAIL** OS/2 usWeightClass expected value for 'Regular' is 400 but this font has 200.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries. </summary>

* [com.google.fonts/check/157](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/157)
* :fire: **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the 'name' table: Expected 'Titillium Web' but got 'Titillium Web Light'.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: FULL_FONT_NAME entries. </summary>

* [com.google.fonts/check/159](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/159)
* :fire: **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the 'name' table: Expected 'Titillium Web Italic' but got 'Titillium Web Light Italic'.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: POSTSCRIPT_NAME entries. </summary>

* [com.google.fonts/check/160](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/160)
* :fire: **FAIL** Entry [POSTSCRIPT_NAME(6):WINDOWS(3)] on the 'name' table: Expected 'TitilliumWeb-Italic' but got 'TitilliumWeb-LightItalic'.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries. </summary>

* [com.google.fonts/check/161](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/161)
* :fire: **FAIL** Font style is 'Italic' and, for that reason, it is not expected to have a [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] entry! [code: ribbi]

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries. </summary>

* [com.google.fonts/check/162](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/162)
* :fire: **FAIL** Font style is 'Italic' and, for that reason, it is not expected to have a [TYPOGRAPHIC_SUBFAMILY_NAME(17):WINDOWS(3)] entry! [code: ribbi]

</details>
<details>
<summary>:fire: <b>FAIL:</b> Checking with Microsoft Font Validator.</summary>

* [com.google.fonts/check/037](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/037)
* :fire: **FAIL** MS-FonVal: The device table StartSize is greater than the end size DETAILS: 
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[43], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[44], BaseAnchor[1], YDeviceTable
* :fire: **FAIL** MS-FonVal: The AnchorFormat field is invalid DETAILS: 
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[188], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[189], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[190], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[191], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[192], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[193], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[194], BaseAnchor[1], AnchorFormat = 196
	- LookupList, Lookup[1], SubTable[0](MarkBasePos), BaseArray, BaseRecord[195], BaseAnchor[1], AnchorFormat = 196
* :fire: **FAIL** MS-FonVal: The LookupFlag reserved bits are not all set to zero DETAILS: 
	- LookupList, Lookup[3]
	- LookupList, Lookup[4]
* :warning: **WARN** MS-FonVal: The version number is valid, but less than 5 DETAILS: 4
* :warning: **WARN** MS-FonVal: PANOSE(tm) is undefined. Font mapping may not work properly
* :warning: **WARN** MS-FonVal: There are undefined bits set in fsSelection field DETAILS: Bit(s) 7
* :warning: **WARN** MS-FonVal: The value of sTypoAscender minus sTypoDescender is greater than unitsPerEm DETAILS: sTypoAscender = 1303, sTypoDescender = -571
* :warning: **WARN** MS-FonVal: A CodePage bit is set in ulCodePageRange, but the font is missing some of the printable characters from that codepage DETAILS: 
	- bit #0, Latin 1 (missing chars: U00AD)
	- bit #1, Latin 2 (missing chars: U00AD)
	- bit #4, Turkish (missing chars: U00AD)
	- bit #6, Arabic (missing chars: U200C U200D U00AD U200E U200F)
	- bit #7, Baltic (missing chars: U00AD)
	- bit #29, Mac character set (missing chars: UFB01 UFB02)
	- bit #51, Arabic (52 missing, first ten missing chars are: U2219 U2592 U2500 U2502 U253C U2524 U252C U251C U2534 U2510)
* :warning: **WARN** MS-FonVal: The table does not contain any Apple subtables
* :warning: **WARN** MS-FonVal: Apple logo mapping test not performed, cmap 1,0 not present
* :warning: **WARN** MS-FonVal: Characters are mapped in the Unicode Private Use area
* :warning: **WARN** MS-FonVal: Not all extremes are marked with the on-curve control points  DETAILS: {'Glyph index': [9, 83, 140, 141, 150, 212, 261, 375, 377, 401, 402, 405, 409, 562, 574, 576, 577, 580, 582, 583, 584, 586, 587, 590, 592, 593, 594, 596, 597, 600, 602, 603, 604, 606, 607, 610, 612, 613, 615, 703, 732, 733, 735, 748, 754, 756, 764, 768, 775]}
* :warning: **WARN** MS-FonVal: Duplicated knots DETAILS: {'Glyph index': [565, 566, 607]}
* :warning: **WARN** MS-FonVal: The unitsPerEm value is not a power of two DETAILS: 1000
* :warning: **WARN** MS-FonVal: The lowestRecPPEM value may be unreasonably small DETAILS: lowestRecPPEM = 6
* :warning: **WARN** MS-FonVal: Ascender is different than OS/2.usWinAscent. Different line heights on Windows and Apple DETAILS: hhea.Ascender = 1303, OS/2.usWinAscent = 1312
* :warning: **WARN** MS-FonVal: The LineGap value is less than the recommended value DETAILS: LineGap = 0, recommended = 9
* :warning: **WARN** MS-FonVal: The leftSideBearing is greater than the advance width (unlikely value) DETAILS: {'Glyph index': [575, 578, 579, 580, 581, 583, 584, 585, 588, 589, 590, 591, 593, 656, 690, 759, 771, 779, 782, 784, 786, 789, 794, 805, 808, 822]}
* :warning: **WARN** MS-FonVal: Loca references a glyf entry which length is not a multiple of 4 DETAILS: Number of glyphs with the warning = 1
* :warning: **WARN** MS-FonVal: maxSizeOfInstructions computation not via either approved method DETAILS: glyf maxSizeOfInstructions=448, prep size=214, fpgm size=3605, whereas maxp maxSizeOfInstruction is 3605

</details>
<details>
<summary>:fire: <b>FAIL:</b> Glyph names are all valid?</summary>

* [com.google.fonts/check/058](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/058)
* :fire: **FAIL** The following glyph names do not comply with naming conventions: ['yehHamzaabove_yehHamzaabovear.fina'] A glyph name may be up to 31 characters in length, must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). and must not start with a digit or period. There are a few exceptions such as the special character ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not.

</details>
<details>
<summary>:warning: <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/153](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/153)
* :warning: **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: dollar	Contours detected: 2	Expected: 1 or 3
Glyph name: Q	Contours detected: 3	Expected: 2
Glyph name: currency	Contours detected: 6	Expected: 2
Glyph name: Euro	Contours detected: 3	Expected: 1 or 2
Glyph name: uni03BC	Contours detected: 2	Expected: 1
Glyph name: Eth	Contours detected: 3	Expected: 2
Glyph name: eth	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: Dcroat	Contours detected: 3	Expected: 2
Glyph name: dcroat	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: hbar	Contours detected: 2	Expected: 1
Glyph name: Lslash	Contours detected: 2	Expected: 1
Glyph name: lslash	Contours detected: 2	Expected: 1
Glyph name: Eng	Contours detected: 2	Expected: 1
Glyph name: Tbar	Contours detected: 2	Expected: 1
Glyph name: tbar	Contours detected: 2	Expected: 1
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: radical	Contours detected: 2	Expected: 1
Glyph name: infinity	Contours detected: 4	Expected: 3
Glyph name: notequal	Contours detected: 3	Expected: 1
Glyph name: pi	Contours detected: 3	Expected: 1

</details>
<details>
<summary>:warning: <b>WARN:</b> Font contains .notdef as first glyph?</summary>

* [com.google.fonts/check/046](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/046)
* :warning: **WARN** Font should contain the .notdef glyph as the first glyph, it should not have a Unicode value assigned and should contain a drawing.

</details>
<details>
<summary>:warning: <b>WARN:</b> Combined length of family and style must not exceed 20 characters.</summary>

* [com.google.fonts/check/163](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/163)
* :warning: **WARN** The combined length of family and style exceeds 20 chars in the following 'WINDOWS' entries: FONT_FAMILY_NAME = 'Titillium Web Light' / SUBFAMILY_NAME = 'Italic'

</details>
<details>
<summary>:warning: <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/063](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/063)
* :warning: **WARN** GPOS table lacks kerning information.

</details>
<details>
<summary>:warning: <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/075](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/075)
* :warning: **WARN** The following glyphs have coordinates which are out of bounds:
[('uni066B', 98.5142, 83.0), ('uni066B', 187.34539999999998, -129.0), ('uni066C', 113.68809999999999, 32.3579), ('uni066C', 143.74009999999998, 32.3579), ('uni066C', 180.4375, -126.9177), ('uni060C', 173.48579999999998, 0.0), ('uni060C', 84.65460000000002, 212.0), ('approxequal', 124.65499999999997, 327.0), ('approxequal', 124.65499999999997, 165.0)]
This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message

</details>
<br>
</details>

### Summary

| :broken_heart: ERROR | :fire: FAIL | :warning: WARN | :zzz: SKIP | :information_source: INFO | :bread: PASS |
|:-----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 9 | 5 | 50 | 7 | 65 |
| 0% | 7% | 4% | 37% | 5% | 48% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
