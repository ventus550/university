from turtle import (forward, right, left, begin_fill,
end_fill, color, speed, pendown, penup, setpos, tilt, heading, ht)
from random import randint


size = 20
speed(0)
ht()


def rcolor():
    return [randint(0,100)/100 for i in range(3)]

def roll():
    if randint(0, 1) == 0:
        return True
    return False


def square(n, direction):
    begin_fill()
    for _ in range(7):
        forward(n)
        right(direction * 90)
    color(rcolor())
    end_fill()
    color('black')




def triangle(n, direction):
    begin_fill()
    right(direction * 90)
    for _ in range(5):
        forward(n)
        right(direction * 120)
    color(rcolor())
    end_fill()
    color('black')



drc = -1
for i in range(1000):
    drc *= -1
    square(size, drc)
    triangle(size, drc)

    if(roll()):
        right(60 * drc)
        drc *= -1
