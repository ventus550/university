from turtle import *
import time
from math import sqrt
from random import randint, choice


def move(x, y):
    penup()
    goto(x, y)
    pendown()
    


def bombki(x, y, w, h):
    B = set()
    
    for _ in range(10):
        b_x = randint(x, x + w)
        b_y = randint(y, y + h)
        B.add((b_x, b_y))

    return B

def triangle(x, y, size, c):
    fillcolor(c)
    begin_fill()
    move(x - size/2, y - (size*sqrt(3)) / 2)
    for _ in range(3):
        forward(size)
        left(120)
    end_fill()

cls = [[0.2, 0.5, 0], [0.3, 0.75, 0], [0.45, 0.9, 0]]
bcls = ['red','blue','yellow','orange','purple','white']
Bs = bombki(-25, -150, 100, 200)

def tree():
    move(0, -200)
    fillcolor('brown')
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

    
    triangle(25, 10, 200, cls[0])
    triangle(25, 60, 150, cls[1])
    triangle(25, 100, 100, cls[2])

    for b in Bs:
        move(b[0], b[1])
        dot(10, choice(bcls))
    
screen = Screen()
screen.setup(500, 500)
screen.tracer(0)
while True:
    clear()
    tree()
    screen.update()
    time.sleep(0.05)







