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
<summary><b>[8] TitilliumWeb-Roman-VF.ttf</b></summary>
<details>
<summary>:fire: <b>FAIL:</b> Checking with Microsoft Font Validator.</summary>

* [com.google.fonts/check/037](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/037)
* :fire: **FAIL** MS-FonVal: The device table StartSize is greater than the end size DETAILS: 
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), MarkArray, MarkRecord[0], AnchorTable, YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), MarkArray, MarkRecord[3], AnchorTable, YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[23], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[24], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[25], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[26], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[47], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[48], BaseAnchor[1], YDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[89], BaseAnchor[0], XDeviceTable
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[90], BaseAnchor[0], XDeviceTable
	- NOTE: 20 other similar results were hidden!
* :fire: **FAIL** MS-FonVal: The AnchorFormat field is invalid DETAILS: 
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[192], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[193], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[194], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[195], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[196], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[197], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[198], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[199], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[200], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[201], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[202], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[203], BaseAnchor[1], AnchorFormat = 205
	- LookupList, Lookup[0], SubTable[0](MarkBasePos), BaseArray, BaseRecord[204], BaseAnchor[1], AnchorFormat = 205
* :fire: **FAIL** MS-FonVal: The LookupFlag reserved bits are not all set to zero DETAILS: 
	- LookupList, Lookup[2]
	- LookupList, Lookup[3]
* :warning: **WARN** MS-FonVal: The version number is valid, but less than 5 DETAILS: 4
* :warning: **WARN** MS-FonVal: PANOSE(tm) is undefined. Font mapping may not work properly
* :warning: **WARN** MS-FonVal: There are undefined bits set in fsSelection field DETAILS: Bit(s) 7
* :warning: **WARN** MS-FonVal: The value of sTypoAscender minus sTypoDescender is greater than unitsPerEm DETAILS: sTypoAscender = 1303, sTypoDescender = -571
* :warning: **WARN** MS-FonVal: A CodePage bit is set in ulCodePageRange, but the font is missing some of the printable characters from that codepage DETAILS: 
	- bit #6, Arabic (missing chars: U200C U200D U200E U200F)
	- bit #29, Mac character set (missing chars: UFB01 UFB02)
	- bit #51, Arabic (51 missing, first ten missing chars are: U2219 U2592 U2500 U2502 U253C U2524 U252C U251C U2534 U2510)
* :warning: **WARN** MS-FonVal: The table does not contain any Apple subtables
* :warning: **WARN** MS-FonVal: Apple logo mapping test not performed, cmap 1,0 not present
* :warning: **WARN** MS-FonVal: Characters are mapped in the Unicode Private Use area
* :warning: **WARN** MS-FonVal: Duplicated knots DETAILS: {'Glyph index': [163, 563, 566, 572, 579, 617]}
* :warning: **WARN** MS-FonVal: Misoriented contour DETAILS: Glyph index 580
* :warning: **WARN** MS-FonVal: Not all extremes are marked with the on-curve control points  DETAILS: {'Glyph index': [805, 806, 813, 816, 818, 821, 822, 823, 824, 825, 826, 827]}
* :warning: **WARN** MS-FonVal: The unitsPerEm value is not a power of two DETAILS: 1000
* :warning: **WARN** MS-FonVal: The lowestRecPPEM value may be unreasonably small DETAILS: lowestRecPPEM = 6
* :warning: **WARN** MS-FonVal: Ascender is different than OS/2.usWinAscent. Different line heights on Windows and Apple DETAILS: hhea.Ascender = 1303, OS/2.usWinAscent = 1312
* :warning: **WARN** MS-FonVal: The LineGap value is less than the recommended value DETAILS: LineGap = 0, recommended = 9
* :warning: **WARN** MS-FonVal: The leftSideBearing is greater than the advance width (unlikely value) DETAILS: {'Glyph index': [761, 786, 787, 788, 790, 791, 792, 793, 794, 795, 797, 798, 800, 801, 802, 803, 812, 813, 814, 815, 816, 817, 818, 819, 820, 828]}
* :warning: **WARN** MS-FonVal: Loca references a glyf entry which length is not a multiple of 4 DETAILS: Number of glyphs with the warning = 1
* :warning: **WARN** MS-FonVal: maxSizeOfInstructions computation not via either approved method DETAILS: glyf maxSizeOfInstructions=452, prep size=214, fpgm size=3605, whereas maxp maxSizeOfInstruction is 3605

</details>
<details>
<summary>:fire: <b>FAIL:</b> Glyph names are all valid?</summary>

* [com.google.fonts/check/058](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/058)
* :fire: **FAIL** The following glyph names do not comply with naming conventions: ['alefMaksura_alefMaksuraar.fina.alt', 'yehHamzaabove_yehHamzaabovear.fina'] A glyph name may be up to 31 characters in length, must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). and must not start with a digit or period. There are a few exceptions such as the special character ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not.

</details>
<details>
<summary>:fire: <b>FAIL:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance.</summary>

* [com.google.fonts/check/167](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/167)
* :fire: **FAIL** The 'wght' axis coordinate of the 'Regular' instance must be 400. Got a '361.61617' coordinate instead.

</details>
<details>
<summary>:fire: <b>FAIL:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance.</summary>

* [com.google.fonts/check/172](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/172)
* :fire: **FAIL** The 'wght' axis coordinate of the 'Bold' instance must be 700. Got a '600.0' coordinate instead.

</details>
<details>
<summary>:warning: <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/153](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/153)
* :warning: **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: currency	Contours detected: 6	Expected: 2
Glyph name: Euro	Contours detected: 3	Expected: 1 or 2
Glyph name: uni03BC	Contours detected: 2	Expected: 1
Glyph name: Eth	Contours detected: 3	Expected: 2
Glyph name: Oslash	Contours detected: 4	Expected: 3
Glyph name: eth	Contours detected: 3	Expected: 2
Glyph name: oslash	Contours detected: 4	Expected: 3
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
Glyph name: Oslashacute	Contours detected: 5	Expected: 4
Glyph name: oslashacute	Contours detected: 5	Expected: 4
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
<summary>:warning: <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/063](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/063)
* :warning: **WARN** GPOS table lacks kerning information.

</details>
<details>
<summary>:warning: <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/075](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/075)
* :warning: **WARN** The following glyphs have coordinates which are out of bounds:
[('uni066C', 44.0572, -122.4099), ('uni066C', 75.6118, 35.3631), ('uni066C', 105.6638, 35.3631), ('uni066C', 67.3475, -122.4099), ('quotesinglbase', 121.2, 114.85), ('quotedblbase', 247.2, 108.85), ('quotedblleft', 273.14588, 727.1452), ('quotedblleft', 243.65775, 727.1452), ('quotedblleft', 140.14588, 727.1452), ('quotedblleft', 110.65775, 727.1452), ('quotedblright', 62.85412, 526.8548), ('quotedblright', 92.34225, 526.8548), ('quotedblright', 206.85412, 526.8548), ('quotedblright', 236.34225, 526.8548), ('quoteleft', 140.2, 726.85), ('quoteright', 62.8, 527.15), ('approxequal', 492.465, 329.0), ('approxequal', 492.465, 167.0)]
This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message

</details>
<br>
</details>

### Summary

| :broken_heart: ERROR | :fire: FAIL | :warning: WARN | :zzz: SKIP | :information_source: INFO | :bread: PASS |
|:-----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 5 | 4 | 59 | 7 | 61 |
| 0% | 4% | 3% | 43% | 5% | 45% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
