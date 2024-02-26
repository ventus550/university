from turtle import forward, right, begin_fill, end_fill, fillcolor, pos, speed, goto, pendown, penup
from random import choice, randint
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', '0.0')
speed('fastest')

def move(xy):
    penup()
    goto(xy)
    pendown()
    


def box(offsetX, offsetY):
    base = pos()
 
    #Offset 
    for i in range(offsetX):
        move((pos()[0] + 10, pos()[1]))
    for i in range(offsetY):
        move((pos()[0], pos()[1] - 10))
    

    #Draw
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

    
    move(base)
    

def N0(xy):
    
    move(xy)
    for i in range(1,4):
        box(i, 0)
        box(i, 4)
        box(4, i)        
        box(0, i)

def N1(xy):
    
    move(xy)
    for i in range(0,5):
        box(2, i)

    box(1, 1)
    box(1, 4)
    box(3, 4)

def N3(xy):
    
    move(xy)
    for i in range(0,4):
        box(i, 0)
        box(i, 4)
    for i in range(1,4):
        box(i, 2)
    box(4, 1)
    box(4, 3)

def N5(xy):
    
    move(xy)
    for i in range(0,4):
        box(i, 0)
        box(i, 2)
        box(i, 4)

    box(4, 0)
    box(4, 3)
    box(0, 1)
    
colors = ['red', 'green', 'yellow', 'blue']
number_functions = [N0, N1, N3, N5]
for i in range(20):
    fillcolor(choice(colors))
    choice(number_functions)((randint(-100 ,100), randint(-100, 100)))
    







