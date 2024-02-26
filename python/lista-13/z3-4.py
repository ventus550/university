from turtle import *
from random import randint, random, choice

D = 10
tracer(0, 1)

GRID = set()





def neighbours(p1):
    res = []
    x, y = p1
    for x0, y0 in rooms:
        if abs(x - x0) <= 1 and abs(y - y0) <= 1:
            res.append((x0, y0))
    return res


def reachable(a):
    visited = {a}
    queue = [a]

    while queue != []:
        x = queue[0]  # pobranie z kolejki
        del queue[0]  # pobranie (cd)

        for n in neighbours(x):
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited


def corridors(K):
    res = []
    global GRID
    for _ in range(K):
        d = choice([(1,0), (-1,0), (0, 1), (0, -1)])
        p = choice(list(GRID))
        length = 5 #randint(1, 5)

        t = []
        while p in GRID:
            p = (p[0] + d[0], p[1] + d[1])
        t.append(p)

        while p[0] >= 1 and p[0] <= 63 and p[1] >= 1 and p[1] <= 63 and len(t) <= length:

            p = (p[0] + d[0], p[1] + d[1])
            t.append(p)

            if p in GRID:
                res += t
                break


    return res

def chambers(K):
    res = []
    global GRID
    for _ in range(K):
        size = randint(2,8)
        x = randint(1, 62 - size)
        y = randint(1, 62 - size)
        t = set()
        for i in range(x, x+size):
            for j in range(y, y+size):
                t.add((i, j))

        if len(t & GRID) == 0:
            res += list(t)
            GRID = GRID | t

    return res


def square(n):
    for _ in range(4):
        forward(10)
        right(90)

def draw_points(ps, kolor):
    fillcolor(kolor)
    for x, y in ps:
        pu()
        goto(x* 10 - 300, y * 10 - 300)
        pd()
        begin_fill()
        square(10)
        end_fill()
    update()


def kolor():
    return random(), 0, random()


ht()

rooms = chambers(200) + corridors(80)

vil2 = set(rooms)

t = set()
for x in range(64):
    for y in range(64):
        t.add((x,y))
draw_points(t, 'black')

while len(vil2) > 0:
    v = list(vil2)[0]
    r = reachable(v)
    draw_points(r, kolor())
    vil2 -= r

done()