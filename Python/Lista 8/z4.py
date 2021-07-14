from turtle import forward, right, begin_fill, end_fill, fillcolor, pos, tracer, update, goto, pendown, penup, colormode
from random import choice, randint
from math import ceil, floor


SIZE = 100
SIDE = 5



def move(xy):
    goto(xy)
    
def box(offsetX, offsetY):
    base = pos()
 
    #Offset 
    move((pos()[0] + SIDE * offsetX, pos()[1]))
    move((pos()[0], pos()[1] - SIDE * offsetY))
    

    #Draw
    begin_fill()
    for i in range(4):
        forward(SIDE)
        right(90)
    end_fill()

    
    move(base)
penup()
move(((-SIZE//2) * SIDE, (SIZE//2) * SIDE))


MAP = []
for x in range(SIZE):
    L = []
    for y in range(SIZE):
        L.append(0)
    MAP.append(L)

#wzgórza
for i in range(SIZE):
    MAP[randint(0, SIZE-1)][randint(0, SIZE-1)] = 100





#średnie
for i in range(SIZE**2 * 100):
    x = randint(0, SIZE-1)
    y = randint(0, SIZE-1)


    L = []
    for i in range(-1, 1):
        for j in range(-1, 1):
            try:
                L.append(MAP[x + i][y + j])
            except:
                {}
    try:   
        MAP[x][y] = (sum(L) / len(L))
    except:
        print(L)


kolory = ['green', (0.5, 1, 0) , 'yellow', 'orange', 'red', (0.5, 0,0) ]

#skalowanie
MAX = max([max(x) for x in MAP]) / 5
for x in range(SIZE):
    for y in range(SIZE):
        MAP[x][y] = ceil(MAP[x][y] / MAX)



#draw
tracer(0,1)
for x in range(SIZE):
    for y in range(SIZE):
        fillcolor(kolory[MAP[x][y]])
        box(x, y)









