import os
import time
import glob
import subprocess
from fontTools.ttLib import TTFont


# Check to make sure script is run from the root directory
print("\n**** Checking to make sure the build script is working in the font repo root directory:")
REPO_ROOT = ['.gitignore', '.git']
repo_test = os.listdir(path='.')
repo_test_result =  all(elem in repo_test for elem in REPO_ROOT)
if repo_test_result:
    print("\n     [+] OK: Looks good")
else:
    print("\n     [!] ERROR: Please run this script from the root directory of a git repo.")

# Get a list of source files
print("\n**** Making a list of Glyphsapp source files:")
sources = []
os.chdir('sources')
for name in glob.glob('*.glyphs'):
    sources.append(os.path.splitext(name)[0])
os.chdir('..')
print("\n     [+] SOURCES: List of sources =", sources)

# Get Source info
print("\n**** Starting FAFR (Fully Automated Font Repository) build process:")
sources_styles = []
for source in sources:
    time.sleep(0.5)
    print("\n     [+] SOURCES: Preparing to build", source)
    print("     [+] SOURCES: Style =", source.rpartition('-')[2])
    sources_style = str(source.rpartition('-')[2])
    sources_styles.append(sources_style)
print("\n     [+] SOURCES: Styles =", sources_styles)


# FONTMAKE
for source in sources:
    try:
        print("\n**** Building %s font files with Fontmake:" %source)
        print("     [+] Run: fontmake -g sources/%s.glyphs -o variable" %source)
        subprocess.call("fontmake -g sources/%s.glyphs -o variable" %source, shell=True)
        #subprocess.call("fontmake -g sources/%s.glyphs -o variable > /dev/null 2>&1" %source, shell=True)
        print("     [!] Done")
    except:
        print("     [?] Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

quit()

# MOVE FONTS
for i in range( len(sources_styles) ):
    print("\n**** Moving %s font to the fonts directory" %SOURCES[i])
    #subprocess.call("cp variable_ttf/%s-VF.ttf fonts/%s-VF.ttf" % (OUTPUT, NEWFONT_ONE), shell=True)
print("     [+] Done")

quit()

# CLEANUP
print("\n**** Removing build directories")
print("     [+] Run: rm -rf variable_ttf master_ufo instance_ufo")
subprocess.call("rm -rf variable_ttf master_ufo instance_ufo", shell=True)
print("     [+] Done")

# AUTOHINT
print("\n**** Run: ttfautohint")
os.chdir('fonts')
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
for source in SOURCES:
    subprocess.call("ttfautohint -I %s-VF.ttf %s-VF-Fix.ttf" %(source, source), shell=True)
    subprocess.call("cp %s-VF-Fix.ttf %s-VF.ttf" %(source, source), shell=True)
    subprocess.call("rm -rf %s-VF-Fix.ttf" %source, shell=True)
print("     [+] Done")

# GFTOOLS
print("\n**** Run: gftools")
os.chdir("..")
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
for source in SOURCES:
    subprocess.call("gftools fix-dsig fonts/%s-VF.ttf --autofix" %source, shell=True)
print("     [+] Done")

# FONTTOOLS
print("\n**** Run: fonttools -- edit sAgCharWidth")
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
#font = TTFont('fonts/$font-VF.ttf')
#print("     [+] font =", FONT)
print("     [+] Done")

# DRAWBOT
print("\n**** Run: DrawBot")
subprocess.call("python3 docs/drawbot-sources/basic-specimen.py", shell=True)
print("     [+] Done")

