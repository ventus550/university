import numpy as np

def 𝑁(mean, variance, shape=1):
	return np.random.normal(mean, variance, size=shape)

def random_population(µ, plane, chromosome_len):
	return np.hstack([
		np.random.uniform(-plane, plane, size=(µ, chromosome_len)),
		np.random.uniform(0, plane, size=(µ, chromosome_len))
	])

def split(P):
	d = P.shape[1] // 2
	return P[:, :d], P[:, d:]

class ES:
	def __init__(self, µ, λ, objective, joined_sampling = True):
		self.µ = µ
		self.λ = λ
		self.objective = objective
		self.joined_sampling = joined_sampling

	@staticmethod
	def mutation(P, τ, τ0):
		X, σ = split(P)
		σ *= np.exp(
			𝑁(0, τ**2, σ.shape) + 𝑁(0, τ0**2, σ.shape)
		)
		xr, xc = X.shape
		for i in range(xr):
			X[i] += np.random.multivariate_normal(
				np.zeros(xc), np.diag(σ[i]**2)
			)
		return np.hstack([X, σ])

	def evaluate_population(self, P):
		d = P.shape[1] // 2
		return self.objective(P[:, :d])

	def roulette_selection(self, P, size):
		fitness = self.evaluate_population(P)
		fitness = np.divide(1, fitness, where = fitness > 0)
		fitness = np.maximum(fitness, np.zeros_like(fitness))
		if sum(fitness) == 0:
			return P[:size]
		probs = fitness / sum(fitness)
		indices = np.random.choice(
			np.arange(len(P)), size, p=probs,
			replace=True
		)
		return P[indices]

	def best(self, P):
		vals = self.evaluate_population(P)
		i = np.argmin(vals)
		return P[i], vals[i]

	def kbest(self, P, k):
		vals = self.evaluate_population(P)
		i = np.argsort(vals)[:k]
		return P[i]
	
	def run(self, chromosome, steps = 100, plane = 10, lr = 1):
		τ, τ0 = lr/np.sqrt(2*chromosome), lr/np.sqrt(2*np.sqrt(chromosome))
		P = random_population(self.μ, plane, chromosome)
		while (steps := steps - 1):
			pc = self.roulette_selection(P, self.λ)
			pc = self.mutation(pc, τ, τ0)
			if self.joined_sampling:
				pc = np.vstack([P, pc])
			P = self.kbest(pc, self.μ)
			yield self.best(P)		