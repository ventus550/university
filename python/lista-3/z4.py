from turtle import fd, bk, lt, rt,ht,  speed, setpos
from random import randint


speed('fastest')
ht()

distance = 100
for i in range(360):
    fd(distance + (i % 45)*3)
    rt(1)
    setpos(0, 0)
    
