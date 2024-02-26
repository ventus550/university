import pandas
import numpy
import seaborn
import time
import networkx as nx
from sklearn.metrics.pairwise import haversine_distances
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from itertools import chain, combinations, count
from pathlib import Path

seaborn.set_palette("deep")
seaborn.set(rc={'figure.figsize':(10,5)}, font_scale=0.8)
seaborn.set_style({'axes.facecolor':'white', 'grid.color': '.8'})
seaborn.despine(fig=None, ax=None, top=False, right=False, left=False, bottom=False, offset=None, trim=False)

def timeit(f):
	start = time.time()
	f()
	end = time.time()
	return end - start

def preprocess(dataset):
	dataset = pandas.concat([dataset, dataset.coordinates.apply(pandas.Series)], axis=1)
	poland = dataset[dataset["country_code"] == "PL"][["name", "lon", "lat"]]
	coordinates = numpy.array(numpy.radians(poland[["lat", "lon"]]))
	return {
		"coordinates": coordinates,
		"distances": numpy.round(haversine_distances(coordinates) * 6371).astype(int),
		"cities": numpy.array(poland["name"])
	}

def load_dataset(dir = "", seed = None, frac = 1.0):
	dataset = pandas.read_json(dir / Path("dataset.json"))
	dataset = dataset.sample(frac=frac, random_state=seed)
	return preprocess(dataset)

def powerset(items):
	return chain.from_iterable(combinations(items, r) for r in range(len(items)+1))

def vars(model, dtype=float):
	return numpy.fromiter((v.x for v in model.getVars()), dtype=dtype)

def edges(solution):
	n = int(numpy.sqrt(len(solution)))
	return numpy.dstack(numpy.where(numpy.reshape(solution, (n,n)) > 0.5))[0]

def cycles(solution):
	return edges(solution)[:, 1]

def graphplot(edges, coordinates, distances, cities, title = None):
    ax = plt.subplots(figsize=(16,10))[1]
    plt.scatter(*coordinates.T, s=12)

    for coord, city in zip(coordinates + 3e-4, cities):
        plt.text(*coord, city, fontdict={'weight':'bold', 'size':7})

    for v, u, *_ in edges:
        ax.add_line(Line2D(*coordinates[[v, u]].T, linewidth=0.7, color='gray'))
        plt.text(*((coordinates[v] + coordinates[u]) / 2 + 3e-4), int(distances[v, u]), fontdict={'weight':'normal', 'size':6})

    plt.title(title)
    plt.show()

def polyplot(x, y, degree=3, color="black", extrapolate=1):
	coefficients = numpy.polyfit(x, y, degree)
	x_curve = numpy.linspace(min(x), extrapolate*max(x), 100)
	y_curve = numpy.polyval(coefficients, x_curve)

	plt.scatter(x, y, color=color)
	plt.plot(x_curve, y_curve, color=color)

def tour(graphx):
	visited = set()
	route = [visited.add(v) or v for v, u in nx.eulerian_circuit(nx.euler.eulerize(graphx)) if v not in visited]
	return [(route[i-1], route[i]) for i in range(len(route))]