from turtle import tracer, forward, right, begin_fill, end_fill, fillcolor, pos, speed, goto, pendown, penup
from random import choice, randint

tracer(0, 1)
TAKEN_SPACE = set()
speed('fastest')

def move(xy):
    penup()
    goto(xy)
    pendown()

move((-200, 200)) 


def box(offsetX, offsetY):
    base = pos()
 
    #Offset 
    move((pos()[0] + offsetX * 10, pos()[1]))
    move((pos()[0], pos()[1] - offsetY * 10))
    

    #Draw
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

    
    move(base)

def draw(s):
    for e in s:
        box(e[0], e[1])

def N0(x, y):
    S = set()
    for i in range(1,4):
        S.add((i + x, y))
        S.add((i + x, 4 + y))
        S.add((4 + x, i + y))
        S.add((x, i + y))

    return S
    
def N1(x, y):
    S = set()
    for i in range(0,5):
        S.add((x + 2, y + i))

    S.add((x + 1, y + 1))
    S.add((x + 1, y + 4))
    S.add((x + 3, y + 4))

    return S

def N3(x, y):
    S = set()
    
    for i in range(0,4):
        S.add((x + i, y))
        S.add((x + i, y + 4))
    for i in range(1,4):
        S.add((x + i, y + 2))
    S.add((x + 4, y + 1))
    S.add((x + 4, y + 3))

    return S

def N5(x, y):

    S = set()
    for i in range(0,4):
        S.add((x + i, y))
        S.add((x + i, y + 2))
        S.add((x + i, y + 4))

    S.add((x + 4, y))
    S.add((x + 4, y + 3))
    S.add((x, y + 1))

    return S
    
colors = ['red', 'green', 'yellow', 'blue']
number_functions = [N0, N1, N3, N5]
for i in range(40):
    fillcolor(choice(colors))
    S = choice(number_functions)(randint(0, 30), randint(0, 30))
    if len(S & TAKEN_SPACE) == 0:
        TAKEN_SPACE |= S
        draw(S)
        







