# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLE
W,H,M,F = 1000,1000,20,30     # WIDTH, HEIGHT, MARGIN, FRAMES
VAR_WGHT = 100                # VARIABLE FONT WEIGHT
LINE_H = H/10                 # LINE HEIGHT
U = 32
START_POS = (U*28)+M 

# SET FONT
font("fonts/Titillium-Web-Roman-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID DRAWING FUNCTION
def grid(inc):
    stroke(0.9,0.1,0)
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

def set_box_style_a():
    fill(0.9,0.1,0)
    stroke(0.9,0.1,0)

def set_box_style_b():
    fill(1)
    stroke(0.9,0.1,0)

def draw_boxes():
    # HEADLINE
    set_box_style_a()
    rect(M, M+(U*26), (U*30), (U*4))

    # ROW 1
    set_box_style_a()
    rect(M,        M+(U*24),  (U*14), (U))
    rect(M+(U*16), M+(U*24),  (U*14), (U))
    text("Titillium Web VF",      (M+(U*16), (START_POS)-(0*LINE_H)))
    set_box_style_b()
    rect(M,       M+(U*16),  (U*14), (U*8))
    rect(M+(U*16), M+(U*16),  (U*14), (U*8))

    # ROW 2
    set_box_style_a()
    rect(M,        M+(U*14),  (U*14), (U))
    rect(M+(U*16), M+(U*14),  (U*14), (U))
    set_box_style_b()
    rect(M,        M+(U*6),  (U*14), (U*8))
    rect(M+(U*16), M+(U*7),  (U*14), (U*7))

    # ROW 3
    set_box_style_a()
    rect(M,        M+(U*4),  (U*14), (U))
    rect(M+(U*16), M+(U*4),  (U*14), (U))
    set_box_style_b()
    rect(M,        M+(U*0),  (U*14), (U*4))
    rect(M+(U*16), M+(U*0),  (U*14), (U*4))

# DRAW NEW PAGE
newPage(W, H)
fill(1)
rect(0, 0, W, H)
grid(30)
draw_boxes()

fill(0)

# HEADLINE
fontSize(100)
fontVariations(wght=800)
fill(1)
stroke(None)
text("Titillium Web VF",      (M+U, (START_POS)-(0*LINE_H)))

fill(0)
fontSize(240)
wght_var = 200
stroke(1)
strokeWidth(1)
for i in range(4):
    fontVariations(wght=wght_var)
    text("a",      (M+20+(U*(i*2.8)), (START_POS-(U*7)-14)))
    wght_var += 200
    #fontSize(i*100)
# Draw large type
fontSize(30)
stroke(None)
for i in range(6):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
    text("Variable Font Weight: %s" %VAR_WGHT, ( M+(U*17), ((START_POS-(U*5)-M)-(U*i)) ))
tracking(0)


# Dot
fill(1,0,0)
oval(M, M, (W-(M*2))/20, (W-(M*2))/20)

# Draw small type
fill(0)
fontVariations(wght=400)
text("A B C D E F G H I J K L M N O P ",      (M+(U*17), (START_POS-M)-(U*15)))
text("Q R S T U V W X Y Z a b c d e f",       (M+(U*17), (START_POS-M)-(U*16)))
text("g h i j k l m n o p q r s t u v",       (M+(U*17), (START_POS-M)-(U*17)))
text("w x y z 1 2 3 4 5 6 7 8 9 0 ! ?",       (M+(U*17), (START_POS-M)-(U*18)))
text("@ # $ % ^ & * : ; ' < > , .",           (M+(U*17), (START_POS-M)-(U*19)))
tracking(-2)
#fontSize(40)
text(" ذ د خ ح ج ث ت ب ا "[::-1],   (M+(M/2+2)+(U*7),  (START_POS-M-9)-(U*15)))
text(" ﻅ ظ ط ض ص ش س  "[::-1],      (M+(M/2)+(U*6),  (START_POS-M-9)-(U*16)))
text(" ن م ل ك ق ف غ ع "[::-1],     (M+(M/2+2)+(U*7),  (START_POS-M-9)-(U*17)))


# SET FONT
font("fonts/Titillium-Web-Italic-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

# ITALIC
# text("A B C D E F G H I J K L M ",            (M+400, (START_POS-M)-( 16*40)))
# text("N O P Q R S T U V W X Y",               (M+400, (START_POS-M)-( 17*40)))


# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("basic-specimen.gif")
# saveImage("basic-specimen.pdf")
# saveImage("basic-specimen.png")
os.chdir("..")
os.chdir("..")
