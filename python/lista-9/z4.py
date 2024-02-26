from turtle import *
import random

tracer(0)
def kwadrat(x, y, kolor):
    penup()
    goto((x*10, y*10))
    pendown()

    begin_fill()
    fillcolor(kolor)
    for _ in range(4):
        forward(10)
        right(90)
    end_fill()

txt = '''
......................
...kkkkkkkkkkkk.......
......................
......................
......................
..nnnn................
..nnnn................
..n...................
......................
.........kkkkkkkkkkk..
......................
......................
......................
......................
.........ppppp........
......................
'''

def char(x):
    return ('empty', 0) if x == '.' else ('red', 5) if x == 'k' else ('green', 5) if x == 'p' else ('blue', 5)


tab = [[char(x) for x in list(wiersz)] for wiersz in txt.split()]      
tab.reverse()
MY = len(tab)
MX = len(tab[0])

def rysuj_plansze(tab):
    clear()
    for y in range(MY):
        for x in range(MX):
            if tab[y][x][0] == 'empty':
                kolor = 'black'
            elif tab[y][x][0] == 'red':
                kolor = ((tab[y][x][1] + 1) / 7, 0, 0)
            elif tab[y][x][0] == 'green':
                kolor = (0, (tab[y][x][1] + 1) / 7, 0)
            elif tab[y][x][0] == 'blue':
                kolor = (0, 0, (tab[y][x][1] + 1) / 7)
            kwadrat(x, y, kolor)
    update()        

def A_beats_B(a, b):
    if (a, b) in [('red', 'green'), ('green', 'blue'), ('blue', 'red')]:
        return 1
    return -1


def adjacent_interaction(x, y):
    base = tab[x][y]
    rand_adj = random.choice([(-1, 0), (0, -1), (0, 1), (1, 0)])
    try:
        if x + rand_adj[0] < 0:
            raise Exception
        if y + rand_adj[1] < 0:
            raise Exception
        adj = tab[x + rand_adj[0]][y + rand_adj[1]]
    except:
        return 0

    if base[1] == 0:
        return 0
    elif base[0] == adj[0]:
        return 0
    elif adj[0] == 'empty':
        tab[x + rand_adj[0]][y + rand_adj[1]] = (base[0], base[1] - 1)
    elif adj[0] != 'empty':
        AB = A_beats_B(base[0], adj[0])
        tab[x][y], tab[x + rand_adj[0]][y + rand_adj[1]] = (tab[x][y][0], tab[x][y][1] + AB), (adj[0], adj[1] - AB)

        if base[1] > 5:
            tab[x][y] = (tab[x][y][0], 5)
        if base[1] <= 0:
            tab[x][y] = ('empty', 0)
        if adj[1] > 5:
            tab[x + rand_adj[0]][y + rand_adj[1]] = (tab[x + rand_adj[0]][y + rand_adj[1]][0], 5)
        if adj[1] <= 0:
            tab[x + rand_adj[0]][y + rand_adj[1]] = ('empty', 0)
   
hideturtle()
while True:
    rysuj_plansze(tab)
    for x in range(MY):
        for y in range(MX):
            if tab[x][y][0] != 'empty':
                adjacent_interaction(x, y)
     

print ('Koniec')
done()
