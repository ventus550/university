from c import Cramer
from math import sin, cos, pi

print(Cramer(
    [lambda x: 1, lambda x: sin((2*pi*x)/12), lambda x: cos((2*pi*x)/12)],
    [0, 2, 4, 6, 8, 10],
    [1, 1.6, 1.4, 0.6, 0.2, 0.8]
))

for x in [0, 2, 4, 6, 8, 10]:
    print(0.933333333333333 + 0.577350269189626*sin((2*pi*x)/12) + 0.2666666666666667*cos((2*pi*x)/12))