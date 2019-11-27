import argparse
from fontTools import ttLib

description = 'path to ttf file'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('ttf_font', help="Font in OpenType (TTF) format")

def main():
    args = parser.parse_args()
    font = ttLib.TTFont(args.ttf_font)

    print("[INFO] Looking for MVAR table...")
    has_MVAR = "MVAR" in font
    print(has_MVAR)

    if has_MVAR:
        print('[INFO] Removing MVAR table')
        del font['MVAR']
        font.save(args.ttf_font)
    else:
        print('[INFO] No MVAR, doing nothing')

if __name__ == '__main__':
    main()
