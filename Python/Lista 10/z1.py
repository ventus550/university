

letters = list('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')

def ceasar(s, k):
    it = iter(letters)
    D = dict(zip(letters, letters[k%32:] + letters[:k%32]))
    return ''.join([D[e] for e in s])

    

