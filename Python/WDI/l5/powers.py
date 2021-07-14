M = 0



def P(a, b):
    global M
    if b == 0:
        return 1
    if b % 2 != 0:
        M += 2
        return a * P(a*a, (b-1)/2)
    M += 1
    return P(a*a, b/2)

P(0, 2**10)
print(M)
