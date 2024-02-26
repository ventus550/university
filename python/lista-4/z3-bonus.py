from random import randint, choice
import time


def randperm(n):
    L = [x for x in range(n)]
    permutacja = [0 for i in range(n)]


    for i in range(n-1, -1, -1):
        rand = randint(0, i)

        permutacja[n - 1 - i] = L[rand]

        t = L[rand]
        L[rand] = L[i]
        L[i] = t
        
    return permutacja



print('Przykladowe wywolania:')
for i in range(5):
    print (randperm(10))

t0 = time.time()
x = randperm(10**6)
t1 = time.time()

print('czas wykonania dla 10**6:', t1 - t0)
