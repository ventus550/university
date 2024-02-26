from turtle import forward, right, begin_fill, end_fill, fillcolor, pos, tracer, update, goto, pendown, penup, colormode
from random import choice, randint

PXS = []
with open('obraz.txt') as f:

    i = 0
    for x in f:
        x = x[:-1].split()
        j = 0
        for e in x:
            PXS.append(((i, j), eval(e)))
            j += 1
        i += 1
DL = len(PXS)

def move(xy):
    penup()
    goto(xy)
    pendown()
    


def box(offsetX, offsetY):
    base = pos()
 
    #Offset 
    move((pos()[0] + 5 * offsetX, pos()[1]))
    move((pos()[0], pos()[1] - 5 * offsetY))
    

    #Draw
    begin_fill()
    for i in range(4):
        forward(5)
        right(90)
    end_fill()

    
    move(base)
move((-200, 200))
tracer(0,1)
colormode(255)
while len(PXS) != 0:
    R = choice(PXS)
    R = (R[0], (int(R[1][0]), int(R[1][1]), int(R[1][2])))
    fillcolor(R[1])
    
    box(R[0][0], R[0][1])
    PXS.remove(R)
    
    if(len(PXS) % 20 == 0):
            update()
















