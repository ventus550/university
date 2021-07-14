def perm(L):    
    if L == []:
        return [[]]
    pierwszy = L[0]
    pozostale = perm(L[1:])

    newL = []
    for p in pozostale:
        for i in range(len(p) + 1):
            newL.append(p[:i] + [pierwszy] + p[i:])
    return newL

print(perm([1,2,3,4]))
print(perm([1]))
