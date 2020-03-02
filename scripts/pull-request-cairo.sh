#!/bin/bash
set -e

build_static_fonts=true

prDir="~/Google/fonts/ofl/cairo"
familyName="Cairo"

echo "[INFO] Preparing a new $familyName pull request at $prDir"

echo "[INFO] Moving variable fonts"
cp fonts/Cairo-Roman-VF.ttf ~/Google/fonts/ofl/cairo/Cairo[wght].ttf
cp fonts/Cairo-Italic-VF.ttf ~/Google/fonts/ofl/cairo/Cairo-Italic[wght].ttf

if [ "$build_static_fonts" = true ]; then
  for font in fonts/static-fonts/Cairo-*; do
    echo "[INFO] Moving $font ";
    cp $font ~/Google/fonts/ofl/cairo/static/
  done
fi

echo "[INFO] Done preparing $familyName pull request at $prDir"
