from math import sin, pi
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt



def Trapeze(a, b, f, k):
	k = 2**k
	h = (b - a) / k
	return 0.5*h*(f(a) + f(a + k*h)) + h*sum( [f(a + i*h) for i in range(1, k)] )

def Romberg(a, b, f, k):
	
	# Do obliczeń wystarczą dwie kolumny tablicy Romberga
	cnow = [0 for _ in range(k+1)]
	cnxt = []

	
	# Wypełniam kolumnę cnow elementami T(0,0), T(0,1), T(0,2), ...
	def M(n):
		h = (b-a)/n
		return h * sum( [f(a + 0.5*h*(2*i - 1)) for i in range(1, n+1)] )

	cnow[0] = 0.5 * (b-a) * (f(a) + f(b))
	for n in range(1, k+1):
		cnow[n] = 0.5*( M(2**(n-1)) + cnow[n-1] )
	
	# Obliczam T(k,0)
	def T(c, r):
		return (4**c * cnow[r+1] - cnow[r]) / (4**c - 1)

	for c in range(1, k+1):

		for r in range(k+1 - c):
			cnxt.append(T(c,r))
		cnow = cnxt; cnxt = []

	return cnow[0]

def a(x):
	return 2021 * x**5 - 2020 * x**4 + 2019 * x**2
def b(x):
	return 1 / (1 + 25*x**2)
def c(x):
	return sin(7*x - 2) / x

def plot(a, b, f, n):
	r = range(1, n)
	val = integrate.romberg(f, a, b, show=False)
	real = [0 for _ in r]
	trapezy = [abs(val - Trapeze(a, b, f, k)) for k in r]
	romberg = [abs(val - Romberg(a, b, f, k)) for k in r]
	args = [k for k in r]

	for i in range(len(trapezy)):
		print(trapezy[i], romberg[i])

	plt.plot(args, real)
	plt.plot(args, trapezy)
	plt.plot(args, romberg)
	plt.legend(["0", "trapezy", "romberg"])
	plt.ylabel('błąd bezwględny')
	plt.xlabel('węzły (skala logarytmiczna)')
	plt.show()

plot(-2, 2, b, 10)


#print("a) ", Romberg(-1, 2, a, 16))
#print("b) ", Romberg(-2, 2, b, 16))
#print("c) ", Romberg(2, 3*pi, c, 16), Trapeze(2, 3*pi, c, 16), integrate.romberg(c, 2, 3*pi, show=False))