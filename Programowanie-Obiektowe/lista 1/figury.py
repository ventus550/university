import math

class Figura:
    typfig, x, y, leng = [None] * 4

def nowa_figura(typ, x, y, leng):
    if leng <= 0:
        raise Exception('{} nie jest dozwolona wartoscia'.format(leng))

    f = Figura()
    f.typfig = typ
    f.x = x
    f.y = y
    f.leng = leng

    return f

def pole(f):
    if type(f) != Figura:
        raise Exception('Argumentem nie jest figura')

    if f.typfig == 'kwadrat':
        return f.leng ** 2
    elif f.typfig == 'kolo':
        return math.pi * (f.leng) ** 2
    elif f.typfig == 'trojkat':
        return (((f.leng)**2) * 3**(1/2)) / 4

def przesun(f, x, y):
    if type(f) != Figura:
        raise Exception('Argumentem nie jest figura')

    f.x += x
    f.y += y

def sumapol(T):
    s = 0

    for e in T:
        s += pole(e)

    return s

