from turtle import forward, left, penup, pendown, speed, setpos
import random as r

speed('fastest')

WIDTH = 8
MAX_H = 100
MIN_H = 25

def rect(height):
    for i in range(4):
        if i % 2 == 0:
            forward(WIDTH)
        else:
            forward(height)
        left(90)

    penup()
    forward(WIDTH * 1.5)  
    pendown()

penup()
setpos(-500, -100)
pendown()


for i in range(80):
    rect(r.randint(MIN_H, MAX_H))
