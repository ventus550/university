
class Tablica:
    d = {}

def dodaj(t, idx, value):
    t.d[idx] = value

def indeks(t, idx):
    if idx in t.d.keys():
        return t.d[idx]
    else:
        return None

