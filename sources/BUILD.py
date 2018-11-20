import os
import time
import glob
import subprocess
from fontTools.ttLib import TTFont


sources = []
sources_styles = []
 

def check_root_dir():
    """
    Checks to make sure script is run from a git repo root directory.
    """
    print("\n**** Checking to make sure the build script is working in the font repo root directory:")
    REPO_ROOT = ['.gitignore', '.git']
    repo_test = os.listdir(path='.')
    repo_test_result =  all(elem in repo_test for elem in REPO_ROOT)
    if repo_test_result:
        print("     [+] OK: Looks good")
    else:
        print("     [!] ERROR: Please run this script from the root directory of a git repo.")

def get_source_list():
    """
    Gets a list of source files.
    """
    print("\n**** Making a list of Glyphsapp source files:")
    os.chdir('sources')
    for name in glob.glob('*.glyphs'):
        sources.append(os.path.splitext(name)[0])
    os.chdir('..')
    print("     [+] SOURCES: List of sources =", sources)

def get_style_list():
    """
    Gets a list of styles from the source list.
    """
    print("\n**** Starting FAFR (Fully Automated Font Repository) build process:")
    for source in sources:
        time.sleep(0.5)
        print("     [+] SOURCES: Preparing to build", source)
        print("     [+] SOURCES: Style =", source.rpartition('-')[2])
        sources_style = str(source.rpartition('-')[2])
        sources_styles.append(sources_style)
    print("     [+] SOURCES: Styles =", sources_styles)

def run_fontmake():
    """
    Builds ttf fonts files with font make.
    """
    for source in sources:
        print("\n**** Building %s font files with Fontmake:" %source)
        print("     [+] Run: fontmake -g sources/%s.glyphs -o variable --overlaps-backend booleanOperations --output-path fonts/%s-VF.ttf" %(source, source) )
        #subprocess.call("fontmake -g sources/%s.glyphs -o variable --output-path fonts/%s-VF.ttf" %(source, source), shell=True)
        subprocess.call("fontmake -g sources/%s.glyphs -o variable --overlaps-backend booleanOperations --output-path fonts/%s-VF.ttf > /dev/null 2>&1" %(source, source), shell=True)
        print("     [!] Done")

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
    for source in sources:
        subprocess.call("ttfautohint -c -I -W -x 0 -D latn -f arab -a qsq %s-VF.ttf %s-VF-Fix.ttf" %(source, source), shell=True)
        subprocess.call("cp %s-VF-Fix.ttf %s-VF.ttf" %(source, source), shell=True)
        subprocess.call("rm -rf %s-VF-Fix.ttf" %source, shell=True)
        print("     [+] Done:", source)
    print("     [+] Done")

def fix_dsig():
    """
    Fixes DSIG table
    """
    print("\n**** Run: gftools")
    os.chdir("..")
    cwd = os.getcwd()
    print("     [+] In Directory:", cwd)
    for source in sources:
        subprocess.call("gftools fix-dsig fonts/%s-VF.ttf --autofix > /dev/null 2>&1" %source, shell=True)
        print("     [+] Done:", source)
    print("     [+] Done")

def render_specimens():
    """
    Render specimens
    """
    print("\n**** Run: DrawBot")
    subprocess.call("python3 docs/drawbot-sources/basic-specimen.py > /dev/null 2>&1", shell=True)
    print("     [+] Done")

if __name__ == '__main__':
    check_root_dir()
    get_source_list()
    get_style_list()
    run_fontmake()
    rm_build_dirs()
    ttfautohint()
    fix_dsig()
    render_specimens()
    quit()
