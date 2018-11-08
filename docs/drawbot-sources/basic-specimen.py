# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLE
W,H,M,F = 1000,1000,100,30     # WIDTH, HEIGHT, MARGIN, FRAMES
VAR_WGHT = 100                 # VARIABLE FONT WEIGHT
LINE_H = H/10                  # LINE HEIGHT
START_POS = 854

# SET FONT
font("fonts/Titillium-Web-Roman-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID DRAWING FUNCTION
def grid(inc):
    stroke(0.2)
    stpX, stpY = 0, 0
    incX = (W-(M*2))/inc
    incY = (W-(M*2))/inc
    print("incX=", incX)
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
grid(20)
fill(1)

# HEADLINE
tracking(0)
stroke(None)
fontSize(100)
fontVariations(wght=900)
text("Titillium Web",      (M, (START_POS)-(0*LINE_H)))


fontSize(400)
fontVariations(wght=900)
text("a",      (M+390, (START_POS+225)-(4*LINE_H)))
fontVariations(wght=200)
text("a",      (M+610, (START_POS+225)-(4*LINE_H)))


# Draw large type
fontSize(40)
tracking(2)
for i in range(6):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
    text("Variable Font: %s" %VAR_WGHT, (M, (START_POS-M)-(i*40)))
tracking(0)


# Dot
fill(1,0,0)
oval(M, M, (W-(M*2))/20, (W-(M*2))/20)

# Draw small type
fontVariations(wght=400)
fill(1)
fontSize(40)
text("A B C D E F G H I J K L M ",            (M+400, (START_POS-M)-( 7*40)))
text("N O P Q R S T U V W X Y",               (M+400, (START_POS-M)-( 8*40)))
text("& Z 1 2 3 4 5 6 7 8 9 0",               (M+400, (START_POS-M)-( 9*40)))
text("a b c d e f g h i j k l m n o",         (M+400, (START_POS-M)-(10*40)))
text("p q r s t u v w x y z",                 (M+400, (START_POS-M)-(11*40)))
tracking(-2)
fontSize(50)
text(" ذ د خ ح ج ث ت ب ا "[::-1],         (M+26,  (START_POS+92)-( 6*80)))
text(" ﻅ ظ ط ض ص ش س  "[::-1],             (M+2, (START_POS+92)-( 7*80)))
text(" ن م ل ك ق ف غ ع "[::-1],           (M+60, (START_POS+92)-( 8*80)))

# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("basic-specimen.gif")
# saveImage("basic-specimen.pdf")
# saveImage("basic-specimen.png")
os.chdir("..")
os.chdir("..")
