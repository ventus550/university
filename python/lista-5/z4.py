'''
Mozna zamienic liste na liste par zawierajacych wartosc w oryginalnej liscie i pozycje, nastepnie te liste
posortowac, usunac duplikaty wartosci i posortowac jeszcze raz ze wzgledu na pozycje.
'''

def usun_duplikaty(sq):
    L = [(sq[i], i) for i in range(len(sq))]
    L.sort()

    L2 = []
    p = (-1,-1)
    for e in L:
        if e[0] != p[0]:
            L2.append(e)
        p = e
    L2.sort(key = lambda x: x[1])

    for i in range(len(L2)):
        L2[i] = L2[i][0]

    return L2

print(usun_duplikaty([1,2,3,1,2,3,8,2,2,2,9,9,4]))
