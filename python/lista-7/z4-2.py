from turtle import ht, tracer, update, done
from murek import murek
#1 - yellow, 2 - orange, 3 - red
#f - forward, l - left, r - right



s = '1f'
for i in range(1,30):
    s += str((i % 3) + 1)

    s += 'r' + i*'f'




ht()
tracer(0,0) # szybkie rysowanie     
murek(s,10)
update() # uaktualnienie rysunku
done()