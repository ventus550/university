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


def S(t):
    sum = 0
    for i in range(N):
        sum += wagi[i]*Bernstein(i, t)
    return sum

def Bernstein(k, t):
    return comb(N, k) * t**k * (1-t)**(N-k)

def alpha(i, t):
    calc = (1/S(t)) * wagi[i] * Bernstein(i, t)
    return calc

def point(t):
    v = kontrolne[0]
    for i in range(1, N):
        v = v + (kontrolne[i] - kontrolne[0])*alpha(i, t)
    return v

points = [point(k / 95) for k in range(0, 95)]
plt.plot([v.x for v in points], [v.y for v in points])
plt.scatter([v.x for v in kontrolne], [v.y for v in kontrolne])
plt.show()