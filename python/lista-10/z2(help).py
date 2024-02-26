

letters = list('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')
Alfa = {}
for i in range(len(letters)):
    Alfa[letters[i]] = i

def checkC(w1, w2):
    if len(w1) != len(w2):
        return False

    diff = abs(Alfa[w1[0]] - Alfa[w2[0]])
    for i in range(1, len(w1)):
        if diff != abs(Alfa[w1[i]] - Alfa[w2[i]]):
            return False

    return True

#----------------------------------------------------------------------------


words = set()
with open("slowa.txt", encoding='utf-8') as f:
    for x in f:
        words.add(x.strip())

        
def checkForFixedLength(lng):
    wfixed = []
    for x in words:
        if len(x) == lng:
            wfixed.append(x)
    print(len(wfixed))

    cwords = set()
    for i in range(1, len(wfixed) - 1):
        for j in range(i+1, len(wfixed)):
            if checkC(wfixed[i], wfixed[j]):
                cwords.add((wfixed[i], wfixed[j]))

    if(len(cwords) > 0):
        print(cwords)
        return 1
    return 0

def findCWords():
    maxLen = 0
    for x in words:
        if len(x) > maxLen:
            maxLen = len(x)

    for ln in range(maxLen, 0, -1):
        print(ln)
        if checkForFixedLength(ln):
            break
        

findCWords()

















    
