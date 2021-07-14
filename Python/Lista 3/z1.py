import math

def isPrime(n):
    for i in range(2,math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2,100000):
    if '777' in str(i):
        if isPrime(i):
            print (i)

