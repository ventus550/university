def fibonacci(k, r):
    a = 1
    b = 0
    for i in range(1, k):
        t = a
        a = (a + b) % r
        b = t
    return a

print(fibonacci(5, 2))
