from wdi import *

def f(n, k, L):
    A = Array(k)
    p = 0

    for i in range(k):
        print('k:',i)
        
        tmp = n
        while tmp % L[i] == 0:
            print('   ',L[i])
            A[i] += 1
            tmp /= L[i]
        
        if A[i] > p:
            p = A[i]

    print('--------------------------')
    print(p)
    for i in range(k):
       if A[i] == p:
           print(L[i])

f(63000, 3, [2, 3, 5])
