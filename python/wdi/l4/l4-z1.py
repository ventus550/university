

#a:
def a(n):
    if n % 2 == 0:
        return n
    else:
        return -n

#b:
def b(n):
    s = 0
    for i in range(n):
        if i % 2 == 0:
            s += 1/i
        else:
            s += -1/i
    return s

#c:
def c(n, x):
    s = 0
    for i in range(1, n+1):
        X = 1
        for j in range(i):
            X = X * x
        s = s + X * i
    return s

            
