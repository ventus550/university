def PPN(w):
    res = ''
    k = 0
    D = {}
    for x in w:
        if x not in D:
            k += 1
            D[x] = k
        res += str(D[x]) + '-'
    return res[:-1]

print(PPN('indianin'))
    

