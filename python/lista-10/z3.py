
def to_int(w, dic):
    string = ''
    for x in w:
        string += str(dic[x])

    return int(string)

def zagadka(w1, w2, w3):
    chars = set()

    sentence = w1 + w2 + w3
    for x in sentence:
        chars.add(x)
    if len(chars) > 10:
        print('Too many unique characters')
        return 0
    chars = list(chars)


    def testResult(L):
        D = dict()
        for i in range(len(chars)):
            D[chars[i]] = L[i]

        if to_int(w1, D) + to_int(w2, D) == to_int(w3, D):
            print(D)

    def rec(P):
        if len(P) == len(chars):
            testResult(P)
            return
        else:
            for x in range(10):
                if x not in P:
                    rec(P + [x])


    rec([])


zagadka('send', 'more', 'money')