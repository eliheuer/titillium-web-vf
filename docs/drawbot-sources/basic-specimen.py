# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLES
W,H,M = 1000,1000,20  # WIDTH, HEIGHT, MARGIN
VAR_WGHT = 100        # VARIABLE FONT WEIGHT
U = 32                # ONE GRID UNIT

def set_font_roman():
    font("fonts/TitilliumWeb-Roman-VF.ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))

def set_font_italic():
    font("fonts/TitilliumWeb-Roman-VF.ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))

def grid(inc):
    stroke(0)
    stpX, stpY = 0, 0
    incX, incY = (W-(M*2))/inc, (H-(M*2))/inc
    for x in range(inc+1):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(inc+1):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

def set_box_style_a():
    fill(0)
    stroke(0)

def set_box_style_b():
    fill(1)
    stroke(0)

def draw_boxes():
    # HEADLINE
    set_box_style_b()
    rect(M, M+(U*26), (U*30), (U*4))
    # ROW 1
    rect(M+(U*1),  M+(U*15), (U*13), (U*10))
    rect(M+(U*16), M+(U*15), (U*13), (U*10))
    # ROW 2
    rect(M+(U*1),  M+(U*8), (U*13), (U*6))
    rect(M+(U*16), M+(U*8), (U*13), (U*6))
    # ROW 3
    rect(M+(U*1),  M+(U*1), (U*13), (U*6))
    rect(M+(U*16), M+(U*1), (U*13), (U*6))

# DRAW NEW PAGE
newPage(W, H)
fill(1)
rect(0, 0, W, H)
grid(30)
draw_boxes()
set_font_roman()
fill(0)

# HEADLINE
fontSize(100)
fontVariations(wght=800)
stroke(None)
text("Titillium Web VF", ( M+(U*1), M+(U*27) ))

# ART
fontSize(240)
wght_var = 200
stroke(1)
strokeWidth(1)
for i in range(4):
    fontVariations(wght=wght_var)
    text("a",      (M+(U*2)+(U*(i*2.3)), (M+5+(U*20))))
    wght_var += 200

stroke(0)
fontSize(57)
fontVariations(wght=200)
textBox("الخط العربي", 
        (M+(U*0), M+(U*12), M+10+(U*12), M+(U*8)), align="right")

fontVariations(wght=800)
textBox("الخط العربي", 
        (M+(U*0), M+(U*10.1), M+10+(U*12), M+(U*8)), align="right")

fontSize(30)
stroke(None)
for i in range(8):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
    text("Variable Font Weight: %s" %VAR_WGHT, ( M+(U*17), ((M+(U*23))-(U*i)) ))
tracking(0)

fill(0)
fontVariations(wght=400)
text("A B C D E F G H I J K L M N O ",        (M+(U*17), M+(U*12)))
text("P Q R S T U V W X Y Z  a b c ",         (M+(U*17), M+(U*11)))
text("d e f g h i j k l m n o p q r s t u",   (M+(U*17), M+(U*10)))
text("v w x y z  1 2 3 4 5 6 7 8 9 0",        (M+(U*17), M+(U*9 )))

stroke(None)
fontSize(29)
fontVariations(wght=400)
textBox(" ا ب ت ث ج ح خ د ذ ر ز س ش ",
        (M+12+(U*0),   M+17+(U*6), M+10+(U*12), M+(U*6)), align="right")
textBox(" ص ض ط ظ ع غ ف ق ك ل م ",
        (M+12+(U*0),   M+20+(U*4.5), M+10+(U*12), M+(U*6)), align="right")
textBox(" ه ن و ي ؤ ئ ",
        (M+12+(U*0),   M+20+(U*3), M+10+(U*12), M+(U*6)), align="right")
textBox(" ٩ ٨ ٧ ٦ ٥ ٤ ٣ ٢ ١ ",
        (M-155+(U*0), M+18+(U*3), M+10+(U*12), M+(U*6)), align="right")

fontSize(30)
font("fonts/TitilliumWeb-Italic-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
text("A B C D E F G H I J K L M N O ",        (M+(U*17), M+(U*5)))
text("P Q R S T U V W X Y Z  a b c ",         (M+(U*17), M+(U*4)))
text("d e f g h i j k l m n o p q r s t u",   (M+(U*17), M+(U*3)))
text("v w x y z  1 2 3 4 5 6 7 8 9 0",        (M+(U*17), M+(U*2)))

stroke(None)
fontSize(29)
fontVariations(wght=400)
textBox(" ا ب ت ث ج ح خ د ذ ر ز س ش ",
        (M+12+(U*0),   M+17+((U*-1)), M+10+(U*12), M+(U*6)), align="right")
textBox(" ص ض ط ظ ع غ ف ق ك ل م ",
        (M+12+(U*0),   M+20+(U*(-2.5)), M+10+(U*12), M+(U*6)), align="right")
textBox(" ه ن و ي ؤ ئ ",
        (M+12+(U*0),   M+20+(U*(-4)), M+10+(U*12), M+(U*6)), align="right")
textBox(" ٩ ٨ ٧ ٦ ٥ ٤ ٣ ٢ ١ ",
        (M-155+(U*0), M+18+(U*(-4)), M+10+(U*12), M+(U*6)), align="right")

# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("basic-specimen.gif")
# saveImage("basic-specimen.pdf")
os.chdir("..")
os.chdir("..")
