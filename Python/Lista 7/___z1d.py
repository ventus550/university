from turtle import forward, right, begin_fill, end_fill, fillcolor, pos, tracer, update, goto, pendown, penup, colormode
from random import choice, randint

directory = {}
with open('obraz.txt') as f:
    i = 0
    for x in f:
        x = x[:-1].split()
        for e in x:
            directory.update({i: e[1:-1]})
            i += 1
DL = len(directory)

def move(xy):
    penup()
    goto(xy)
    pendown()
    


def box(offsetX, offsetY):
    base = pos()
 
    #Offset 
    move((pos()[0] + 10 * offsetX, pos()[1]))
    move((pos()[0], pos()[1] - 10 * offsetY))
    

    #Draw
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

    
    move(base)

colormode(255)
while len(directory) != 0:
    R = choice(list(directory.keys()))
    C = directory[R].split(sep=',')
    for i in range(3):
        print(C[i])
        C[i] = int(float(C[i]))
    fillcolor(C[0], C[1], C[2])
    
    box(R // 3, R % 3)
    update()
    directory.pop(R)
















