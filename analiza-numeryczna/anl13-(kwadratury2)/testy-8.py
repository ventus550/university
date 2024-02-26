from scipy import integrate

'''def test(w):

	r = (0.6)**0.5
	T = [-r, 0, r]

	def g(t):
		return w((5*t - 1) * 0.5)

	def product(k):

		def p(t):
			res = 1
			for i in range(3):
				if i == k:
					continue
				res *= (t - T[i]) / (T[k] - T[i])
			return res

		return p
	
	res = 0
	for k in range(3):
		i = integrate.quad(product(k), -1, 1)[0] * (5/2)
		res += i * g(T[k])
	
	return res'''

def Q(w):
	r = 0.6**0.5
	A0 = A2 = 50/36
	A1 = 20/9
	x0 = (5*(-r) - 1) * 0.5
	x1 = -0.5
	x2 = (5*r - 1) * 0.5

	return A0*w(x0) + A1*w(x1) + A2*w(x2)


def w(x):
	return 2021*x**5 - 2020*x**4 + 2019*x**2 + 1010121*x + 550

print(integrate.quad(w, -3, 2)[0], Q(w))