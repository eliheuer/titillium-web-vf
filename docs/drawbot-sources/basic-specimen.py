# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLES
W,H,M = 1000,1000,20  # WIDTH, HEIGHT, MARGIN
VAR_WGHT = 100        # VARIABLE FONT WEIGHT
U = 32                # ONE GRID UNIT

def set_font_roman():
    print("Roman font set")
    font("fonts/TitilliumWeb-Roman-VF.ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))

def set_font_italic():
    print("italic font set")
    font("fonts/TitilliumWeb-Italic-VF.ttf")
    for i in listFontVariations().items():
        print(i)
        print(dir(font))

def grid(inc):
    stroke(0.2)
    stpX, stpY = 0, 0
    incX, incY = (W-(M*2))/inc, (H-(M*2))/inc
    for x in range(inc+1):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(inc+1):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

# DRAW NEW PAGE
newPage(W, H)
fill(0)
rect(0, 0, W, H)
#grid(30)
#draw_boxes()
set_font_roman()
fill(1)

# HEADLINE
fontSize(123)
fontVariations(wght=800)
stroke(None)
text("Titillium Web VF", ( M+(U*1), M+(U*24) ))

# ART
fontSize(290)
wght_var = 200
stroke(0)
strokeWidth(1)
for i in range(4):
    fontVariations(wght=wght_var)
    text("a",      (M+(U*0.6)+(U*(i*2.9)), (M+2+(U*20))))
    wght_var += 200

stroke(None)
fontSize(115)
fontVariations(wght=900)
textBox("الكتاب", 
        (M+(U*1.2), M+(U*13), M+10+(U*12), M+(U*8)), align="right")

fontSize(30)
stroke(None)
tracking(2)
for i in range(8):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
    text("Variable Font Weight: %s" %VAR_WGHT, ( M+(U*16), ((M+(U*23.5))-(U*i)) ))
tracking(0)

fill(1)
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
set_font_italic()
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
