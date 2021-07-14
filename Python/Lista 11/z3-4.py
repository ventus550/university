

def DHondt(M, N):
    M = int(M)
    divs = []
    res = [0 for x in N]
    for i in range(len(N)):
        for j in range(1, M+1):
            if N[i] == '–':
                break
            divs.append( (float(N[i]) / j, i) )
    divs.sort(key=lambda x: x[0], reverse=True)
    #print(divs)
    for i in range(M):
        res[divs[i][1]] += 1

    return res

def Sainte_Laguë(M, N):
    M = int(M)
    divs = []
    res = [0 for x in N]
    for i in range(len(N)):
        for j in range(1, M+1):
            if N[i] == '–':
                break
            divs.append( (float(N[i]) / (2*j - 1), i) )
    divs.sort(key=lambda x: x[0], reverse=True)
    #print(divs)
    for i in range(M):
        res[divs[i][1]] += 1

    return res

def ordynacja_wiekszosciowa(M, N):
    M = int(M)
    N = [float(x) for x in N if x != '–']
    res = [0 for x in N]
    mx = max(N)
    for i in range(len(N)):
        if N[i] == mx:
            res[i] = M
            break

    return res

def wybory(metoda):
    with open('wyniki_wyborow.tsv', encoding='utf-8') as f:
        et = f.readline().split()
        komitety = et[3:-1]

        SUM = [0 for x in komitety]
        for x in f:
            Ms = x.split()[2]
            stats = x.split()[3:-1]

            SUM = [x + y for x, y in zip(SUM, metoda(Ms, stats))]
        print(metoda.__name__, SUM)


wybory(DHondt)
wybory(Sainte_Laguë)
wybory(ordynacja_wiekszosciowa)


