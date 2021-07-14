from turtle import *
from math import sqrt

tracer(0)
def move(p):
    penup()
    goto(p)
    pendown()


def square(A):
    begin_fill()
    for _ in range(4):
        forward(A)
        left(90)
    left(90)
    forward(A)
    right(90)
    end_fill()
    
def triangle(A):
    begin_fill()
    forward(A)
    left(135)
    forward(A / sqrt(2))
    left(90)
    forward(A / sqrt(2))
    left(135)
    end_fill()
    
    left(45)

def tree(deph, MXD):
    s = 60 / sqrt(2)**(deph // 2)
    fillcolor((0, 0.5, deph / MXD))
    if deph == MXD:
        return 0

    if deph % 2 == 0:
        square(s)
        tree(deph + 1, MXD)
    else:
        triangle(s)
        
        base = pos()        #save status
        angle = heading()   #
        
        tree(deph + 1, MXD)

        move(base)          #load status
        setheading(angle)   #

        forward(s / sqrt(2))
        right(90)
        tree(deph + 1, MXD)


tree(0, 20)
update()














