from turtle import pos, forward, right, penup, pendown, speed, setpos, fillcolor, goto,begin_fill, end_fill
from duze_cyfry import daj_cyfre
from random import choice

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

    
colors = ['red', 'green', 'yellow', 'blue']
def draw(num):
    N = daj_cyfre(num)
    fillcolor(choice(colors))
    for i in range(5):
        for j in range(5):
            if N[j][i] == '#':
                box(i, j)




move((-400, 0))

for i in range(10):
    draw(i)
    move((pos()[0] + 75, pos()[1]))
    







