from wdi import Array
def nwd(a, b):
    if a < b:
        a = a + b
        b = a - b
        a = a - b

    while b > 0:
        a = a % b
        
        a = a + b
        b = a - b
        a = a - b
    
    return a
        
def f(n, L):
    n = len(L)

    p = L[0]
    for i in range(1, n):
        p = nwd(p, L[i])

    return p
        
