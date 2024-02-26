from math import sin, pi
from scipy import integrate


def Romberg(a, b, f, k):
	
	def T(n):
		h = (b-a) / n
		points = [a + i*h for i in range(n+1)]

		s = 0
		for i in range(n+1):
			res = f(points[i])
			if i != 0 and i != n:
				s += res
			else:
				s += 0.5 * res
		return s*h

	T0s = [T(2**i) for i in range(k+1)]
	
	def T(M, K):
		if M == 0:
			return T0s[K]
		return (4**M * T(M-1, K+1) - T(M-1, K)) / (4**M - 1)

	return T(k, 0)

def a(x):
	return 2021 * x**5 - 2020 * x**4 + 2019 * x**2
def b(x):
	return 1 / (1 + 25*x**2)
def c(x):
	return sin(7*x - 2) / x

print("a) ", Romberg(-1, 2, a, 16))
print("b) ", Romberg(-2, 2, b, 16))
print("c) ", Romberg(2, 3*pi, c, 16))