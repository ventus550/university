from numpy import array
from numpy.linalg import inv
from numpy import transpose as tp
from numpy import dot
from random import random
import matplotlib.pyplot as plt

def regression(X, Y):
	X = [ [1, x] for x in X]
	Y = [ y for y in Y]

	b = dot(inv(dot(tp(X), X)), dot(tp(X), Y))

	return lambda x: b[0] + b[1]*x


def normalize(X):
	def avg(i):
		a = max(i - 6, 0)
		r = X[a:i+1]
		return sum(r)/len(r)

	return [ avg(i) for i in range(len(X)) ]


deaths = []
cases = []

with open("Mexico.csv", "r") as f:
	for line in f:
		line = line.split(',')
		deaths.append(int(line[-2]))
		cases.append(int(line[-4]))

deaths = normalize(deaths)
cases = normalize(cases)








X = [i for i in range(len(deaths))]
dr = regression(X, deaths)
cr = regression(X, cases)

#plt.plot(deaths)
#plt.plot([dr(x) for x in X])
#plt.plot(cases)
#plt.plot([cr(x) for x in X])
#plt.show()

