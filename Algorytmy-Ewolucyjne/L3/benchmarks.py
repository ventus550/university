import numpy as np

def _sphere(x):
	return np.sum(x**2)

def _schwefel(x):
	return 418.9829*len(x) + sum(x * np.sin(np.sqrt(np.abs(x))))

def _rastrigin(x):
	return 10*len(x) + sum(x**2 - 10*np.cos(2*np.pi*x))

def _griewank(x):
	indices = np.arange(len(x)) + 1
	return sum(x**2)/4000 - np.prod(np.cos(x)/np.sqrt(indices)) + 1

def _rosenbrock(x):
	y = 100*(x**2 - np.roll(x, -1))**2 + (x - 1)**2
	return sum(y[:-1])

def sphere(X):
	return np.sum(X**2, axis=1)

def schwefel(X):
	return 418.9829*len(X) + np.sum(X * np.sin(np.sqrt(np.abs(X))), axis=1)

def rastrigin(X):
	return 10*len(X) + np.sum(X**2 - 10*np.cos(2*np.pi*X), axis=1)

def griewank(X):
	r, c = X.shape
	indices = np.expand_dims(np.ones(r), 1) * np.arange(1, c+1)
	return np.sum(X**2, axis=1)/4000 - np.prod(np.cos(X)/np.sqrt(indices), axis=1) + 1

def rosenbrock(X):
	y = 100*(X**2 - np.roll(X, -1, axis=1))**2 + (X - 1)**2
	return np.sum(y[:, :-1], axis=1)
