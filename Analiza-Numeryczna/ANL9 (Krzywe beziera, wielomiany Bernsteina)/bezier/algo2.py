from math import comb
import matplotlib.pyplot as plt

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, v):
        return vector(self.x + v.x, self.y + v.y)
    def __mul__(self, other):
        return vector(self.x * other, self.y * other)
    def __sub__(self, v):
        return vector(self.x, self.y) + v * (-1)
    def tuple(self):
        return (self.x, self.y)
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"




wagi = [1, 2, 3, 2.5, 6, 1.5, 5, 1, 2, 1, 3, 5, 1]
kontrolne = [vector(x, y) for x,y in [(39.5, 10.5), (30, 20), (6, 6), (13, -12), (63, -12.5), (18.5, 17.5), (48, 63),
(7, 25.5), (48.5, 49.5), (9, 19.5), (48.5, 35.5), (59, 32.5), (56, 20.5)] ]
N = len(kontrolne)

def Bernstein(i,x):
    return comb(N,i) * x**i * (1-x)**(N-i)

def s(t):
    result = 0
    for i in range(N):
        result += wagi[i] * Bernstein(i,t)
    return result;

def alfa(i,t):
    return ( 1 / s(t) ) * wagi[i] * Bernstein(i,t)

def point(t):
    result = kontrolne[0]
    for i in range(1,N):
        result = result + (kontrolne[i] - kontrolne[0])*alfa(i,t)
    return result


points = [point(k / 95) for k in range(0, 95)]
plt.plot([v.x for v in points], [v.y for v in points])
plt.show()