def T(n, m):
    if m == 0:
        return n
    if n == 0:
        return m
    return T(n-1,m) + 2*T(n,m-1)

print(T(3,4))
