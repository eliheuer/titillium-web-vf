#!/bin/bash
set -e

glyphs_source="Cairo-Roman Cairo-Italic"
output_dir="fonts"
family_name="Cairo"
build_static_fonts=true

echo "[INFO] Starting build script for $family_name font family"

if [ -d .git ]; then
  echo "[TEST] Running from a Git root directory, looks good"
else
  echo "[WARN] Font family Git root not found, please run from the root directory"
  echo "[WARN] Build process cancelled"
  exit 1
fi

for sources in $glyphs_source; do
  echo "[TEST] Queued source file: $sources.glyphs"
done

for sources in $glyphs_source; do
  echo "[INFO] Building $sources.glyphs with Fontmake..."
  fontmake -g sources/$sources.glyphs -o variable \
    --output-path $output_dir/$sources-VF.ttf \
    --verbose INFO
done

if [ "$build_static_fonts" = true ]; then
  echo "[INFO] Building static fonts"
  fontmake -g sources/Cairo-Roman.glyphs -i "Cairo ExtraLight" --verbose INFO
  fontmake -g sources/Cairo-Roman.glyphs -i "Cairo Light" --verbose INFO
  fontmake -g sources/Cairo-Roman.glyphs -i "Cairo Regular" --verbose INFO
  fontmake -g sources/Cairo-Roman.glyphs -i "Cairo SemiBold" --verbose INFO
  fontmake -g sources/Cairo-Roman.glyphs -i "Cairo Bold" --verbose INFO
  fontmake -g sources/Cairo-Roman.glyphs -i "Cairo Black" --verbose INFO
  fontmake -g sources/Cairo-Italic.glyphs -i "Cairo ExtraLight Italic" --verbose INFO
  fontmake -g sources/Cairo-Italic.glyphs -i "Cairo Light Italic" --verbose INFO
  fontmake -g sources/Cairo-Italic.glyphs -i "Cairo Italic" --verbose INFO
  fontmake -g sources/Cairo-Italic.glyphs -i "Cairo SemiBold Italic" --verbose INFO
  fontmake -g sources/Cairo-Italic.glyphs -i "Cairo Bold Italic" --verbose INFO
fi

if [ "$build_static_fonts" = true ]; then
  echo "[INFO] Moving static fonts"
  for font in instance_ttf/Cairo-*; do
    echo "[INFO] Moving $font ..."
    mv $font fonts/static-fonts/
  done
fi

echo "[INFO] Removing build directories"
rm -rf instance_ufo instance_otf instance_ttf master_ufo

echo "[INFO] Fixing VF DSIG tables"
for sources in $glyphs_source; do
  if gftools fix-dsig -f fonts/$sources-VF.ttf >/dev/null; then
    echo "[INFO] DSIG fixed for $sources-VF.ttf"
  else
    echo "[ERROR] GFtools is not working, please update or install: https://github.com/googlefonts/gftools"
  fi
done

if [ "$build_static_fonts" = true ]; then
  echo "[INFO] Fixing Static DSIG tables"
  for font in fonts/static-fonts/Cairo-*; do
    echo "[INFO] Fixing DSIG table for $font ..."
    gftools fix-dsig -f $font >/dev/null
  done
fi

echo "[INFO] Autohinting variable fonts with ttfautohint"
for font in fonts/Cairo-*; do
  echo "[INFO] Hinting $font ";
  ttfautohint $font temp.ttf
  mv temp.ttf $font
  gftools fix-hinting $font
  mv $font.fix $font
done

if [ "$build_static_fonts" = true ]; then
  echo "[INFO] Autohinting static fonts with ttfautohint"
  for font in fonts/static-fonts/Cairo-*; do
    echo "[INFO] Hinting $font ";
    ttfautohint $font temp.ttf
    mv temp.ttf $font
    gftools fix-hinting $font
    mv $font.fix $font
  done
fi

echo "[INFO] Removing MVAR table"
for font in fonts/Cairo-*; do
  echo "[INFO] Removing MVAR table for $font ";
  python3 scripts/helpers/remove-mvar-table.py $font
done

if [ "$build_static_fonts" = true ]; then
  for font in fonts/static-fonts/Cairo-*; do
    echo "[INFO] Removing MVAR table for $font ";
    python3 scripts/helpers/remove-mvar-table.py $font
  done
fi

echo "[INFO] Done building $family_name font family"
