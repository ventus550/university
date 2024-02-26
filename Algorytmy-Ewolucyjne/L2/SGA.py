import numpy as np
import time

# https://mat.uab.cat/~alseda/MasterOpt/GeneticOperations.pdf
# https://arxiv.org/pdf/1203.3099.pdf

class Crossover:

	@staticmethod
	def ordered(parent1, parent2):
		plength = len(parent1)
		begin, end = np.sort(np.random.choice(np.arange(plength+1), 2, False))

		def make_offspring(p, q):
			offspring = np.zeros(plength, dtype=p.dtype)

			# Copy swath into offspring
			swath = offspring[begin:end] = p[begin:end]
			swath = set(swath)

			# Copy residuals from parent2
			j = 0
			for i in np.concatenate([np.arange(0, begin), np.arange(end, plength)]):
				while q[j] in swath:
					j += 1
				offspring[i] = q[j]
				j += 1
			return offspring

		offspring1 = make_offspring(parent1, parent2)
		offspring2 = make_offspring(parent2, parent1)
		return offspring1, offspring2

	@staticmethod
	def position_based(parent1, parent2, set_size = 0.5):
		plength = len(parent1)
		set_size = int(plength * set_size)
		enums = np.arange(plength)
		indices = np.random.choice(enums, set_size, False)

		def make_offspring(p, q):
			offspring = np.zeros(plength, dtype=p.dtype)

			# Copy swath into offspring
			swath = np.take(p, indices)
			np.put(offspring, indices, swath)
			swath = set(swath)

			# Copy residuals from parent2
			j = 0
			for i in np.setdiff1d(enums, indices):
				while q[j] in swath:
					j += 1
				offspring[i] = q[j]
				j += 1
			return offspring

		offspring1 = make_offspring(parent1, parent2)
		offspring2 = make_offspring(parent2, parent1)
		return offspring1, offspring2

	@staticmethod
	def PMX(parent1, parent2):
		plength = len(parent1)
		begin, end = np.sort(np.random.choice(np.arange(plength+1), size=2, replace=False))

		def make_offspring(p1, p2):
			offspring = np.zeros(plength, dtype=p1.dtype)

			# Copy swath into offspring
			swath = offspring[begin:end] = p1[begin:end]
			swath = set(swath)

			# Copy residuals from parent2
			for i in np.concatenate([np.arange(0, begin), np.arange(end, plength)]):
				candidate = p2[i]
				while candidate in swath:
					candidate = p2[np.where(p1 == candidate)[0][0]]
				offspring[i] = candidate
			return offspring

		offspring1 = make_offspring(parent1, parent2)
		offspring2 = make_offspring(parent2, parent1)
		return offspring1, offspring2

	@staticmethod
	def uniform(parent1, parent2):
		bits = np.random.randint(0, 2, len(parent1))

		def make_offspring(p1, p2):
			return bits*p1 + (1 - bits)*p2

		offspring1 = make_offspring(parent1, parent2)
		offspring2 = make_offspring(parent2, parent1)
		return offspring1, offspring2


class Mutation:

	@staticmethod
	def insertion(p):
		source, target = np.random.choice(np.arange(len(p)), 2, False)
		value = p[source]
		q = np.delete(p, source)
		return np.insert(q, target, value)

	@staticmethod
	def shift_sequence(p):
		q = p.copy()
		i, j = np.sort(np.random.choice(np.arange(len(q)), 2, False))
		q[i:j+1] = np.roll(q[i:j+1], 1)
		return q
	
	@staticmethod
	def reverse_sequence_mutation(p):
		a = np.random.choice(len(p), 2, False)
		i, j = a.min(), a.max()
		q = p.copy()
		q[i:j+1] = q[i:j+1][::-1]
		return q

	@staticmethod
	def bitflip(p):
		q = p.copy()
		pos = np.random.randint(len(q))
		q[pos] = int(not q[pos])
		return q


def identity(*args):
	return args

def zero(*_):
	return 0

def apply(arr, f):
	return np.apply_along_axis(f, 1, arr)

def random_permutation(length):
	return np.random.permutation(length)

def simple_genetic_algorithm(
	chromosome_length,
	crossover = identity,
	mutation = identity,
	objective_function = zero,
	individual_initialization = random_permutation,
	population = 500,
	crossover_probability = 0.95,
	mutation_probability = 0.25,
	steps = 250,
	verbose = False
):
	time0 = time.time()

	number_of_offspring = population
	best_objective_value = np.Inf
	best_chromosome = np.zeros((1, chromosome_length))

	# generating an initial population
	current_population = np.zeros((population, chromosome_length), dtype=np.int64)
	current_population = apply(current_population, lambda _: individual_initialization(chromosome_length))

	# evaluating the objective function on the current population
	objective_values = apply(current_population, objective_function)

	for t in range(steps):
		# selecting the parent indices by the roulette wheel method
		fitness_values = objective_values.max() - objective_values
		if fitness_values.sum() > 0:
			fitness_values = fitness_values / fitness_values.sum()
		else:
			fitness_values = np.ones(population) / population
		parent_indices = np.random.choice(population, number_of_offspring, True, fitness_values).astype(np.int64)

		# creating the children population
		children_population = np.zeros((number_of_offspring, chromosome_length), dtype=np.int64)
		for i in range(number_of_offspring // 2):
			if np.random.random() < crossover_probability:
				children_population[2*i, :], children_population[2*i+1, :] = crossover(current_population[parent_indices[2*i], :].copy(), current_population[parent_indices[2*i+1], :].copy())
			else:
				children_population[2*i, :], children_population[2*i+1, :] = current_population[parent_indices[2*i], :].copy(), current_population[parent_indices[2*i+1]].copy()
		if np.mod(number_of_offspring, 2) == 1:
			children_population[-1, :] = current_population[parent_indices[-1], :]

		# mutating the children population
		for i in range(number_of_offspring):
			if np.random.random() < mutation_probability:
				children_population[i, :] = mutation(children_population[i, :])

		# evaluating the objective function on the children population
		children_objective_values = apply(children_population[:number_of_offspring, :], objective_function)

		# replacing the current population by (Mu + Lambda) Replacement
		objective_values = np.hstack([objective_values, children_objective_values])
		current_population = np.vstack([current_population, children_population])

		I = np.argsort(objective_values)
		current_population = current_population[I[:population], :]
		objective_values = objective_values[I[:population]]

		# recording some statistics
		if best_objective_value > objective_values[0]:
			best_objective_value = objective_values[0]
			best_chromosome = current_population[0, :]

		if verbose:
			data = (
				t, time.time() - time0,
				objective_values.min(),
				objective_values.mean(),
				objective_values.max(),
				objective_values.std()
			)
			print('%3d %14.8f %12.8f %12.8f %12.8f %12.8f' % data)

		yield best_chromosome, objective_function(best_chromosome)