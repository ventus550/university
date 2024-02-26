import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from tqdm import tqdm
import contextlib	
import pandas as pd
from seaborn import reset_defaults, set_style, set_palette

@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

class Archives: #simulator?
	def __init__(self, f, **kwargs):
		if f is not None:
			prod = product(*list(kwargs.values()))
			data = [dict([*zip(kwargs.keys(), p), ("f", f(*p))]) for p in prod]
			self.data = pd.DataFrame.from_dict(data)
			self.build()

	def __repr__(self):
		return self.data.to_string(index=False)

	def build(self):
		self.f = self.data["f"]
		self.keys = self.data.loc[:, self.data.columns != "f"]
	
	def where(self, key, value):
		arch = Archives(None)
		arch.data = self.data.loc[self.data[key] == value, self.data.columns != key]
		arch.build()
		return arch

def display(style = "darkgrid", palette = "dark", dpi=100, width=10, height=10):
	def inner(func):
		def wrapper(*args, title = "", tight = True, save = "", **kwargs):
			reset_defaults()
			if style: set_style(style)
			if palette: set_palette(palette)
			plt.figure(dpi=dpi, figsize=(width, height))
			func(*args, **kwargs)
			if tight: plt.tight_layout(pad=3)
			if save: plt.savefig(save)
			plt.title(title)
			plt.show()
		return wrapper
	return inner

def progress_bar(iterable, disabled = False, color="yellow", desc=None):
	return tqdm(iterable, disable=disabled, colour=color, desc=desc)

def loop(times, iterable):
	it = iter(iterable)
	while (times := times - 1) >= 0:
		yield next(it)

def pltcfg(legend = False, ylabel = ""):
	if legend: plt.legend()
	plt.ylabel(ylabel)

@display(width=8, height=2.6, dpi=200)
def quickplot(*values, legend = [], ylabel = ""):
	legendary = len(legend) == len(values)
	for i, v in enumerate(values):
		plt.plot(v, label = legend[i] if legendary else "")
	pltcfg(legendary, ylabel)
	return None

def histogram(*values, legend = [], overlap = False, ylabel = "", title = "", path = ""):
	legendary = len(legend) == len(values)
	if overlap:
		for i, v in enumerate(values):
			plt.hist(v, alpha = 0.5, label = legend[i] if legendary else "")
	else:
		plt.hist(values, label = legend)
	pltcfg(legendary, title, ylabel, path)

def stemplot(values, mirror = 0.0, marker = True, ylabel = "", title = "", path = ""):
	markerline, _, _ = plt.stem(values, linefmt='grey', markerfmt='D', bottom=mirror)
	markerline.set_markerfacecolor('none')
	markerline.set_markeredgecolor('grey' if marker else 'none')
	pltcfg(False, title, ylabel, path)

def heatbar(v, title = "", path = ""):
	plt.figure(figsize=(10,0.2), dpi=80)
	plt.imshow(v, cmap="coolwarm", aspect="auto")
	plt.yticks([])
	plt.xticks([])
	pltcfg(False, title, "", path, tight = False)

def plot3d(X, Y, Z):
	ax = plt.axes(projection='3d')
	ax.plot_surface(X, Y, Z, cmap='Blues', linewidth=0, antialiased=True)

@display(style = None, palette = None)
def surfplot(X, Y, Z):
	plot3d(X, Y, Z)

@display(style = None, palette = None, width=5, height=5)
def surfplotf(f, start=0, end=1, n=100):
	plane = np.linspace(start, end, n)
	X, Y = np.meshgrid(plane, plane)
	xs = np.dstack((X, Y)).reshape(n*n, 2)
	Z = f(xs).reshape(n, n)
	plot3d(X, Y, Z)


# def apply(X, Y, f):
# 	x, y = X.shape
# 	F = np.zeros_like(X)
# 	for i, j in product(range(x), range(y)):
# 		F[i, j] = f(np.array((X[i, j], Y[i, j])))
# 	return F
# assert start < end
# plane = np.linspace(start, end, steps)
# X, Y = np.meshgrid(plane, plane)
# plot3d(X, Y, apply(X, Y, f))
