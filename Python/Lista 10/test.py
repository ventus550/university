

letters = list('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')

def ceasar(s, k):
    it = iter(letters)
    D = dict(zip(letters, letters[k%32:] + letters[:k%32]))
    return ''.join([D[e] for e in s])


def buildDict():
    D = {}
    for i in range(len(letters)):
        D[letters[i]] = i
    return D


DC = buildDict()

def checkC(w1, w2):
    if len(w1) != len(w2):
        return False

    diff = abs(DC[w1[0]] - DC[w2[0]])
    for i in range(1, len(w1)):
        if diff != abs(DC[w1[i]] - DC[w2[i]]):
            return False

    return True

print(ceasar('abc', 2))
print(checkC('abc', 'bćd'))