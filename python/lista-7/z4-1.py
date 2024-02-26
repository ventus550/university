from turtle import ht, tracer, update
from murek import murek
#1 - yellow, 2 - orange, 3 - red
#f - forward, l - left, r - right



s = ''
for i in range(0,20):
    s += str((i % 3) + 1)

    s += 4*((20-i)*'f' + 'r') 




ht()
tracer(0,0) # szybkie rysowanie     
murek(s,10)
update() # uaktualnienie rysunku
