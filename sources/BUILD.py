import os
import subprocess
from fontTools.ttLib import TTFont

# STATIC VARIABLES
FONT = "Titillium-Web"
ROOT = "titillium-web-vf"

# FONTMAKE
try:
    print("\n**** Running Fontmake")
    print("     [+] Run: fontmake -g sources/%s.glyphs -o variable" %FONT)
    subprocess.call("fontmake -g sources/%s.glyphs -o variable > /dev/null 2>&1" %FONT, shell=True)
    print("     [+] Done")
except:
    print("     [!] Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

# MOVE FONTS
print("\n**** Moving fonts to fonts directory")
subprocess.call("cp variable_ttf/%s-VF.ttf fonts/%s-Regular.ttf" % (FONT, FONT), shell=True)
print("     [+] Done")

# CLEANUP
print("\n**** Removing build directories")
print("     [+] Run: rm -rf variable_ttf master_ufo")
subprocess.call("rm -rf variable_ttf master_ufo", shell=True)
print("     [+] Done")

# AUTOHINT
print("\n**** Run: ttfautohint")
os.chdir('fonts')
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
subprocess.call("ttfautohint -I %s-Regular.ttf %s-Regular-Fix.ttf" %(FONT, FONT), shell=True)
subprocess.call("cp %s-Regular-Fix.ttf %s-Regular.ttf" %(FONT, FONT), shell=True)
subprocess.call("rm -rf %s-Regular-Fix.ttf" %FONT, shell=True)
print("     [+] Done")

# GFTOOLS
print("\n**** Run: gftools")
os.chdir("..")
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
#subprocess.call("gftools fix-dsgi fonts/Foo-VF.ttf --autofix", shell=True)

# FONTTOOLS
print("\n**** Run: edit xAvgCharWidth")
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
#font = TTFont('fonts/$font-VF.ttf')
print("     [+] font =", FONT)
print("     [+] Done")

# DRAWBOT
print("\n**** Run: DrawBot")
#subprocess.call("python3 docs/drawbot-sources/basic-specimen.py > /dev/null 2>&1", shell=True)
print("     [+] Done")

