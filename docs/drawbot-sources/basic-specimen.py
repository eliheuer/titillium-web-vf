# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os


# STATIC VARIABLE
W,H,M,F = 1000,1000,100,30     # WIDTH, HEIGHT, MARGIN, FRAMES
VAR_WGHT = 30                 # VARIABLE FONT WEIGHT
LINE_H = H/10                  # LINE HEIGHT
START_POS = 854


# SET FONT
font("fonts/Titillium-Web-VF.ttf")
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
#rect(0, 0, W, H)
grid(20)
fill(0.5)

# HEADLINE
tracking(0)
stroke(None)
fontSize(100)
fontVariations(wght=900)
text("Titillium Web",      (M+10, (START_POS)-(0*LINE_H)))

# Draw large type
fontSize(50)
for i in range(6):
    VAR_WGHT += 40
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
    text("Variable Font", (M+10, (START_POS-M+3)-(i*40)))

# Dot
fill(1,0,0)
oval(M, M, (W-(M*2))/20, (W-(M*2))/20)

# Draw small type
fontVariations(wght=400)
fill(0.5)
fontSize(50)
tracking(-4)
text("A B C D E F G H I J ",      (M+400, (START_POS)-( 8*LINE_H/2)))
text("K L M N O P Q R S T ",      (M+400, (START_POS)-( 9*LINE_H/2)))
text("U V W X Y Z ",              (M+400, (START_POS)-(10*LINE_H/2)))
text("a b c d e f g h i j k l",   (M+400, (START_POS)-(11*LINE_H/2)))
text("m n o p q r s t u v",       (M+400, (START_POS)-(12*LINE_H/2)))
text("w x y z",                   (M+400, (START_POS)-(13*LINE_H/2)))

text(" ز ر ذ د خ ح ج ث ت ب ا ",   (M, (START_POS)-( 8*LINE_H/2)))
text(" ق ف غ ع ظ ط ض ص ش س ",     (M, (START_POS)-( 9*LINE_H/2)))
text(" ي و ه ن م ل ك ",           (M, (START_POS)-(10*LINE_H/2)))
text(" ههه ",                     (M, (START_POS)-(11*LINE_H/2)))

# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("basic-specimen.gif")
saveImage("basic-specimen.pdf")
saveImage("basic-specimen.png")
os.chdir("..")
os.chdir("..")
