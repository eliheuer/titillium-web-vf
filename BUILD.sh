#!/bin/sh
python3 sources/BUILD.py \
    --ttfautohint "-v --stem-width-mode=qsq" \
    --static \
    --googlefonts ~/Google/fonts/ofl/titilliumweb \
    --fontbakery \
#    --drawbot \
#    --addfont \
#    --fixnonhinting
