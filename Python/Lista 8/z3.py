from random import choice

def mkdict(s):
    D = {}

    for x in s:
        if x not in D:
            D.update({x: 1})
        else:
            D[x] += 1

    return D


def isOK(a, b):
    dA = mkdict(a)
    dB = mkdict(b)

    L = [x for x in dA if x in dB and dA[x] <= dB[x]]
    
    if len(L) == len(dA):
        return True
    return False


print(isOK('motyl', 'lokomotywa'))
