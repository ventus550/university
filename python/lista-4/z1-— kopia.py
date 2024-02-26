from turtle import (forward, right, left, begin_fill, backward,
end_fill, color, speed, pendown, penup, setpos, tilt, heading, ht)
from random import randrange


speed('fastest')
#ht()

def roll():
    if 0 == randrange(2):
        return True
    else:
        return False

def square(n):
    begin_fill()
    
    for i in range(6):
        left(90)
        forward(n)

    color('red')
    end_fill()
    color('black')


def triangle(n):

    begin_fill()
    
    for i in range(3):
        right(120)
        forward(n)
        
    right(120)
    color('blue')
    end_fill()
    color('black')


for i in range(6):
    
    triangle(80)
    forward(80)
    if roll():
        right(210)
    square(80)
    
    
    
