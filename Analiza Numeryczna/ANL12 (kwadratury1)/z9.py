from math import atan
from scipy.integrate import quad
import matplotlib.pyplot as plt

fig, axs = plt.subplots(6)
C = -1
plt.subplots_adjust(hspace=1)


def f(x):
	return 1/(1+x**2)





def L_plot(f, nodes):
	global C
	points = 500; h = ((nodes[-1] -  nodes[0])/points) * 2; C += 1
	xaxis = [2*nodes[0] + x*h for x in range(points)]
	
	axs[C].set_title("n =" + str(len(nodes) - 1))
	axs[C].plot(xaxis, [f(t) for t in xaxis])
	
	

	# b) Lagrange --------------------------
	def lmbd(k, x):
		res = 1
		for j in range(len(nodes)):
			if j == k:
				continue
			res *= (x-nodes[j])/(nodes[k]-nodes[j])
		return res

	def L(x):
		res = 0
		for k in range(len(nodes)):
			res += f(nodes[k])*lmbd(k, x)
		return res

	axs[C].plot(xaxis, [L(x) for x in xaxis])
	axs[C].set_ylim(-1, 1.5)
	axs[C].set_xlim(-4, 4)





def integrate(a, b, n, f):
	h = (b-a)/n; X = [a + k*h for k in range(n+1)]

	L_plot(f, X)



	def factorial(n):
		res = 1
		for i in range(1, n+1):
			res *= i
		return res

	def integrand(k):

		def func(t):
			res = 1
			for j in range(n+1):
				if j == k:
					continue
				res *= (t-j)
			return res
			
		return func


	def A(k):
		top = ((-1)**(n-k)) * h
		bot = factorial(k) * factorial(n-k)

		return (top/bot) * quad(integrand(k), 0, n)[0]

	res = 0
	for k in range(n+1):
		res += A(k) * f(X[k])
	return res



def test(val1, val2):
	print("error: ", abs(val1 - val2) / val1)

for d in range(2, 14, 2):
	test(2*atan(3), integrate(-3, 3, d, f))
plt.show()
