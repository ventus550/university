def PNF(w):
    res = ''
    k = 0
    D = {}
    for x in w:
        if x not in D:
            k += 1
            D[x] = k
        res += str(D[x]) + '-'
    return res[:-1]

def product(L):
    s = 1
    for x in L:
        s *= x
    return s
#----------------------------------------------------------------------------------------
szyfr1 = "fulfolfu ćtąśśótą tlźlźltą"
szyfr2 = "udhufńfd ąuąuęąę yrrożdśś śdśsdtsć"
szyfr3 = 'uwuąpwuw uw dwnuąźhąuąa'
szyfr4 = 'nlgwdg mgcumyćąlćiya l źuwbymyć iapąołwęlgźy ęoumaźy dgog iapoasmyćpęlć ąu uąęlgftumaiya'


D = {}
with open('slowa.txt', encoding='utf-8') as f:
    for x in f:
        x = x.strip()
        D[x] = PNF(x)

def comb(sets):
    L = []

    def rec(s, lis):
        for e in s:
            k = len(lis) + 1
            if k < len(sets):
                rec(sets[k], lis + [e])
            else:
                L.append(lis + [e])

    rec(sets[0], [])
    return L



def decipher(code):
    csPNF = PNF(code.replace(' ', '')).strip('-')
    code = code.split()


#------------ First Letter Exclusion -----
    exclude[len(code)] = set()
    excludedLetters = {'ą', 'ę', 'ó', 'y', 'ń'}
    s=0
    for i in range(len(code) - 1):
        exclude[i].add(csPNF[s])
        s += len(code[i])




    print('Searching for PNF of', code, '...')
    setFamily = [set() for x in code]



    
    for i in range(len(code)):
        pnf = PNF(code[i])
        for pair in D.items():

            if pair[1] == pnf:
                setFamily[i].add(pair[0])


    joined = ''.join(code)
    print('complexity:', product([len(e) for e in setFamily]))
    C = comb(setFamily)

    for x in C:
        joinedX = ''.join(x)
        if PNF(joinedX) == PNF(joined):
            print(x)




decipher(szyfr1)
decipher(szyfr2)
decipher(szyfr4)

