import time
import math

def isPrime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_happy(n, c7): #100, 101, 102 ...
    t = str(n)
    count = 0
    for i in range(len(t) + 1):
        new = t[:i] + c7 * '7' + t[i:]
        if isPrime(int(new)):
            count += 1
    return count


def hyperhappy(digits, c7):
    result = 0
    for i in range(10**(digits - 1 - c7), 10**(digits - c7) - 1):
        result += generate_happy(i, c7)
    print(result)

hyperhappy(11, 7)
