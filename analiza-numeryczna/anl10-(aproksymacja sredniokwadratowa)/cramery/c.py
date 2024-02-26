import numpy as np

def Cramer(g = [], X = [], Y = []):

    RANGE = len(g)
    def dotProduct(i, j):
        res = 0
        for x in X:
            res += g[i](x)*g[j](x)
        return res
    def dotProduct2(i):
        res = 0
        for k in range(len(X)):
            res += Y[k]*g[i](X[k])
        return res
    def det(arr):
        return np.linalg.det(np.array(arr))

    X_products = [[dotProduct(i, j) for i in range(RANGE)] for j in range(RANGE)]
    Y_products = [dotProduct2(i) for i in range(RANGE)]

    Parameters = []
    D = det(X_products)
    for i in range(RANGE):
        C_products = X_products[:i] + [Y_products] + X_products[i+1:]
        Di = det(C_products)
        Parameters += [Di/D]

    return Parameters

'''print(Cramer(
    [lambda x: x, lambda x: 1],
    [0, 10, 20, 30, 40, 80, 90, 95],
    [68, 67.1, 66.4, 65.6, 64.6, 61.8, 61, 60]
))
'''




















