import math

def pdzielniki(n):
    S = set()
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        while n % i == 0:
            n /= i
            S.add(i)
    return S

print(pdzielniki(36))
