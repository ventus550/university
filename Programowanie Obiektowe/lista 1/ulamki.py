
class Ulamek:
    licznik, mianownik = [None]*2

def normalizuj(u):
    l = u.licznik
    m = u.mianownik

    sign = (l * m) / abs(l * m)
    l = abs(l)
    m = abs(m)

    i = 2
    while i <= l and i <= m:
        if l % i == 0 and m % i == 0:
            l /= i
            m /= i
        else:
            i += 1
    l *= sign
    u.licznik = int(l)
    u.mianownik = int(m)

def formatuj(u1, u2):
    t = u1.mianownik
    l1 = u1.licznik; l2 = u2.licznik
    m1 = u1.mianownik; m2 = u2.mianownik

    l1 *= m2; m1 *= m2
    l2 *= t; m2 *= t

    return (l1, l2, m1)



def nowy_ulamek(l, m):
    u = Ulamek()
    u.licznik = l
    u.mianownik = m

    normalizuj(u)

    return u

def dodaj(u1, u2):
    f = formatuj(u1, u2)

    u3 = Ulamek
    u3.licznik = f[0] + f[1]
    u3.mianownik = f[2]

    normalizuj(u3)

    return u3

def dodaj2(u1, u2):
    f = formatuj(u1, u2)

    u2.licznik = f[0] + f[1]
    u2.mianownik = f[2]
    normalizuj(u2)

def odejmij(u1, u2):
    f = formatuj(u1, u2)

    u3 = Ulamek
    u3.licznik = f[0] - f[1]
    u3.mianownik = f[2]

    normalizuj(u3)
    return u3

def pomnoz(u1, u2):

    u3 = Ulamek()
    u3.licznik = u1.licznik * u2.licznik
    u3.mianownik = u1.mianownik * u2.mianownik

    normalizuj(u3)

    return u3

def podziel(u1, u2):

    u3 = Ulamek()
    u3.licznik = u1.licznik * u2.mianownik
    u3.mianownik = u1.mianownik * u2.licznik

    normalizuj(u3)

    return u3
