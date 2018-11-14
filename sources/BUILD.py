import os
import time
import glob
import subprocess
from fontTools.ttLib import TTFont


# Globals
sources = []

def check_root_dir():
    """
    Checks to make sure script is run from a git repo root directory.
    """
    print("\n**** Checking to make sure the build script is working in the font repo root directory:")
    REPO_ROOT = ['.gitignore', '.git']
    repo_test = os.listdir(path='.')
    repo_test_result =  all(elem in repo_test for elem in REPO_ROOT)
    if repo_test_result:
        print("\n     [+] OK: Looks good")
    else:
        print("\n     [!] ERROR: Please run this script from the root directory of a git repo.")

def get_source_list():
    """
    Gets a list of source files.
    """
    print("\n**** Making a list of Glyphsapp source files:")
    os.chdir('sources')
    for name in glob.glob('*.glyphs'):
        sources.append(os.path.splitext(name)[0])
    os.chdir('..')
    print("\n     [+] SOURCES: List of sources =", sources)

def get_style_list():
    """
    Gets a list of styles from the source list.
    """
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
def run_fontmake():
    """
    Builds ttf fonts files with font make.
    """
    for source in sources:
        try:
            print("\n**** Building %s font files with Fontmake:" %source)
            print("     [+] Run: fontmake -g sources/%s.glyphs -o variable" %source)
            subprocess.call("fontmake -g sources/%s.glyphs -o variable" %source, shell=True)
            #subprocess.call("fontmake -g sources/%s.glyphs -o variable > /dev/null 2>&1" %source, shell=True)
            print("\n     [!] Done")
        except:
            print("     [?] Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

def move_fonts():
    """
    Moves fonts to the `fonts` dir.
    """
    for i in range( len(sources_styles) ):
        print("\n**** Moving %s font to the fonts directory" %SOURCES[i])
        #subprocess.call("cp variable_ttf/%s-VF.ttf fonts/%s-VF.ttf" % (OUTPUT, NEWFONT_ONE), shell=True)
    print("     [+] Done")

def rm_build_dirs():
    """
    Cleanup build dirs
    """
    print("\n**** Removing build directories")
    print("     [+] Run: rm -rf variable_ttf master_ufo instance_ufo")
    subprocess.call("rm -rf variable_ttf master_ufo instance_ufo", shell=True)
    print("     [+] Done")

def ttfautohint():
    """
    Runs ttfautohint
    """
    print("\n**** Run: ttfautohint")
    os.chdir('fonts')
    cwd = os.getcwd()
    print("     [+] In Directory:", cwd)
    for source in SOURCES:
        subprocess.call("ttfautohint -I %s-VF.ttf %s-VF-Fix.ttf" %(source, source), shell=True)
        subprocess.call("cp %s-VF-Fix.ttf %s-VF.ttf" %(source, source), shell=True)
        subprocess.call("rm -rf %s-VF-Fix.ttf" %source, shell=True)
    print("     [+] Done")

def fix_dsig():
    """
    Fixes DSIG table
    """
    print("\n**** Run: gftools")
    os.chdir("..")
    cwd = os.getcwd()
    print("     [+] In Directory:", cwd)
    for source in SOURCES:
        subprocess.call("gftools fix-dsig fonts/%s-VF.ttf --autofix" %source, shell=True)
    print("     [+] Done")

def render_specimens():
    """
    Render specimens
    """
    print("\n**** Run: DrawBot")
    subprocess.call("python3 docs/drawbot-sources/basic-specimen.py", shell=True)
    print("     [+] Done")

if __name__ == '__main__':
    check_root_dir()
    get_source_list()
    get_style_list()
    run_fontmake()
    # move_fonts()
    # rm_build_dirs()
