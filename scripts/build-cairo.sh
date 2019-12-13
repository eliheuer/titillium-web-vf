#!/bin/bash
set -e

glyphsSource="Cairo-Roman Cairo-Italic"
outputDir="fonts"
familyName="Cairo"

echo "[INFO] Starting build script for $familyName font family"

if [ -d .git ]; then
  echo "[TEST] Running from a Git root directory, looks good"
else
  echo "[WARN] Font family Git root not found, please run from the root directory"
  echo "[WARN] Build process cancelled"
  exit 1
fi

for sources in $glyphsSource; do
  echo "[TEST] Queued source file: $sources.glyphs"
done

for sources in $glyphsSource; do
  echo "[INFO] Building $sources.glyphs with Fontmake, this might take some time..."
  fontmake -g sources/$sources.glyphs -o variable \
    --output-path $outputDir/$sources-VF.ttf \
    --verbose ERROR
done

#echo "[INFO] Building static fonts"
#fontmake -g sources/TitilliumWeb-Roman.glyphs -i "Titillium Web ExtraLight" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Roman.glyphs -i "Titillium Web Light" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Roman.glyphs -i "Titillium Web Regular" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Roman.glyphs -i "Titillium Web SemiBold" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Roman.glyphs -i "Titillium Web Bold" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Roman.glyphs -i "Titillium Web Black" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Italic.glyphs -i "Titillium Web ExtraLight Italic" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Italic.glyphs -i "Titillium Web Light Italic" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Italic.glyphs -i "Titillium Web Italic" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Italic.glyphs -i "Titillium Web SemiBold Italic" --verbose ERROR
#fontmake -g sources/TitilliumWeb-Italic.glyphs -i "Titillium Web Bold Italic" --verbose ERROR

#echo "[INFO] Moving static fonts"
#for font in instance_ttf/*.ttf; do
#  echo "[INFO] Moving $font ..."
#  mv $font fonts/static-fonts/
#done

echo "[INFO] Removing build directories"
rm -rf instance_ufo instance_otf instance_ttf master_ufo

echo "[INFO] Fixing VF DSIG tables"
for sources in $glyphsSource; do
  if gftools fix-dsig -f fonts/$sources-VF.ttf >/dev/null; then
    echo "[INFO] DSIG fixed for $sources-VF.ttf"
  else
    echo "[ERROR] GFtools is not working, please update or install: https://github.com/googlefonts/gftools"
  fi
done

#echo "[INFO] Fixing Static DSIG tables"
#for font in fonts/static-fonts/*.ttf; do
#  echo "[INFO] Fixing DSIG table for $font ..."
#  gftools fix-dsig -f $font >/dev/null
#done

echo "[INFO] Autohinting with ttfautohint"
for font in fonts/*.ttf; do
  echo "[INFO] Hinting $font ";
  ttfautohint $font temp.ttf
  mv temp.ttf $font
  gftools fix-hinting $font
  mv $font.fix $font
done
#for font in fonts/static-fonts/*.ttf; do
#  echo "[INFO] Hinting $font ";
#  ttfautohint $font temp.ttf
#  mv temp.ttf $font
#  gftools fix-hinting $font
#  mv $font.fix $font
#done

echo "[INFO] Removing MVAR table"
for font in fonts/*.ttf; do
  echo "[INFO] Removing MVAR table for $font ";
  python3 scripts/helpers/remove-mvar-table.py $font
done
#for font in fonts/static-fonts/*.ttf; do
#  echo "[INFO] Removing MVAR table for $font ";
#  python3 scripts/helpers/remove-mvar-table.py $font
#done

#echo "[INFO] Running fix-name-table.py"
#python3 sources/scripts/helpers/fix-name-table.py fonts/vf/$familyName-VF.ttf

echo "[INFO] Done building $familyName font family"
