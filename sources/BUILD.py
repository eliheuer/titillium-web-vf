import os
import time
import subprocess
from fontTools.ttLib import TTFont

# STATIC VARIABLES
# SOURCES is a list of the source names you want to build, without file extensions:
#SOURCES = ['Titillium-Web-Regular', 'Titillium-Web-Italic']
SOURCES = ['Titillium-Web-Regular']

# START SCRIPT
print("\n**** Starting FAFR (Fully Automated Font Repository) build process:")
for source in SOURCES:
    time.sleep(0.5)
    print("     [+] Sources: Preparing to build ", source)

# FONTMAKE
for source in SOURCES:
    try:
        print("\n**** Building %s font files with Fontmake:" %source)
        print("     [+] Run: fontmake -g sources/%s.glyphs -o variable" %source)
        subprocess.call("fontmake -g sources/%s.glyphs -o variable" %source, shell=True)
        subprocess.call("fontmake -g sources/%s.glyphs -o variable > /dev/null 2>&1" %source, shell=True)
        print("     [!] Done")
    except:
        print("     [?] Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

quit()

# MOVE FONTS
print("\n**** Moving %s font to the fonts directory" %source)
subprocess.call("cp variable_ttf/%s-VF.ttf fonts/%s-VF.ttf" % (FONT, FONT), shell=True)
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
subprocess.call("ttfautohint -I %s-VF.ttf %s-VF-Fix.ttf" %(FONT, FONT), shell=True)
subprocess.call("cp %s-VF-Fix.ttf %s-VF.ttf" %(FONT, FONT), shell=True)
subprocess.call("rm -rf %s-VF-Fix.ttf" %FONT, shell=True)
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

