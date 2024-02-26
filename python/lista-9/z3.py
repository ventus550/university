D = []

def intoDict(x):
    d = dict()
    for y in list(x):
        if y in d.keys():
            d[y] += 1
        else:
            d[y] = 1
    return d


def zagadka(imie, nazwisko):
    IN = imie+nazwisko
    IND = intoDict(IN)

    with open('popularne_slowa.txt', encoding='utf-8') as f:
        for x in f:
            x = x.strip()
            for e in list(x):
                isOK = True
                if e not in list(IND.keys()):
                    isOK = False
                    break
            if isOK:
                D.append(x)
    print('exit')
    
    for i in range(len(D)):
        for j in range(i + 1, len(D) - 1):
            for y in range(j + 1, len(D) - 2):
                if len(IN) == len(D[i]) + len(D[j]) + len(D[y]):
                    if intoDict(D[i]+D[j]+D[y]) == IND:
                        print(D[i], D[j], D[y])



zagadka('jakub', 'skalski')
