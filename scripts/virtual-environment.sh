#!/bin/bash
set -e

echo "[INFO] Making a Python3 venv"

python3 -m venv virtual-env
source "./virtual-env/bin/activate"
pip install --upgrade pip
pip list
pip install fontmake
pip install gftools
