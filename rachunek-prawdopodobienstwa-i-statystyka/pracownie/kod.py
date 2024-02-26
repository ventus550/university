from math import exp, pi

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


def factorial(n):
	r = 1
	for i in range(2, n+1):
		r *= i
	return r

#dla k naturalnych dodatnich
def Gamma(k):
	if k == 1:
		return pi**0.5

	if k % 2:
		#k nie jest parzyste -> własność gammy
		n = (k - 1) // 2 #n=1
		return (2**(1-2*n) * pi**0.5 * factorial(2*n - 1)) / factorial(n - 1)
	else:
		#k jest parzyste czyli gamma jest zwyczajnie silnią
		return factorial(k//2 - 1)



# Funkcja wyliczająca całkę phi na przedziale [0, t] dla stopnia swobody k
def Phi(t, k):

	#mianownik wystarczy wyliczyć tylko raz
	denominator = 2**(k/2) * Gamma(k)
	
	def f(x):
		if x == 0:
			return 0
		numerator = x**((k/2)-1) * exp(-x/2)
		return numerator/denominator
	
	res = Romberg(0, t, f, 22)
	if res > 0.99999999:
		return 1.0
	return res

print(Phi(1000, 6))


