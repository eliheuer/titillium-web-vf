#!/bin/bash
set -e

prDir="~/Google/fonts/ofl/titilliumweb"
familyName="TitilliumWeb"

echo "[INFO] Preparing a new $familyName pull request at $prDir"

cp fonts/TitilliumWeb-Roman-VF.ttf ~/Google/fonts/ofl/titilliumweb/TitilliumWeb[wght].ttf
cp fonts/TitilliumWeb-Italic-VF.ttf ~/Google/fonts/ofl/titilliumweb/TitilliumWeb-Italic[wght].ttf

for font in fonts/static-fonts/*.ttf; do
  echo "[INFO] Moving $font ";
  cp $font ~/Google/fonts/ofl/titilliumweb/static/
done

echo "[INFO] Done preparing $familyName pull request at $prDir"
