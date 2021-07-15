from c import Cramer
from math import sin, cos, pi

print(Cramer(
    [lambda x: x, lambda x: 1],
    [0, 10, 20, 30, 40, 80, 90, 95],
    [68, 67.1, 66.4, 65.6, 64.6, 61.8, 61, 60]
))

for x in [0, 10, 20, 30, 40, 80, 90, 95]:
    print(-0.07993035770813506*x + 67.95932257043367)