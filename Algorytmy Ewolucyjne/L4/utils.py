import matplotlib.pyplot as plt
import numpy as np
import traceback
from itertools import product
from tqdm import tqdm
import contextlib
import pandas as pd
from tabulate import tabulate
from seaborn import reset_defaults, set_style, set_palette

@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

class Archives:
	def __init__(self, f, **kwargs):
		all(hasattr(v, '__iter__') for v in kwargs.values())
		prod = product(*tuple(kwargs.values())) if kwargs else {}
		data = [dict([*zip(kwargs.keys(), p), ("f", f(*p))]) for p in prod]
		self.__fill(pd.DataFrame.from_dict(data))

	def _repr_html_(self):
		return tabulate(self.data, headers='keys', tablefmt='html', showindex=False)

	def __repr__(self):
		return self.data.to_string(index=False)

	def __fill(self, df):
		self.data = df
		self.f = self.data.get("f", pd.DataFrame())
		self.keys = self.data.loc[:, self.data.columns != "f"]
	
	def where(self, key, value):
		arch = Archives(...)
		arch.__fill(self.data.loc[self.data[key] == value, self.data.columns != key])
		return arch

	def pick(self, key):
		return self.data[key].to_numpy()

def display(style = "darkgrid", palette = "dark", dpi=100, width=10, height=10):
	def inner(func):
		def wrapper(*args, title = "", tight = True, save = "", **kwargs):
			try:
				reset_defaults()
				if style: set_style(style)
				if palette: set_palette(palette)
				plt.figure(dpi=dpi, figsize=(width, height))
				func(*args, **kwargs)
				if tight: plt.tight_layout(pad=3)
				if save: plt.savefig(save)
				plt.title(title)
			except Exception as e:
				print(''.join(traceback.format_tb(e.__traceback__)))
				plt.clf()
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

@display(width=18, height=4)
def quickplot(*values, legend = [], ylabel = "", marker=""):
	legendary = len(legend) == len(values)
	for i, v in enumerate(values):
		plt.plot(v, marker, label = legend[i] if legendary else "")
	pltcfg(legendary, ylabel)
	return None

@display(width=10, height=5)
def histogram(*values, legend = [], overlap = False, ylabel = ""):
	legendary = len(legend) == len(values)
	if overlap:
		for i, v in enumerate(values):
			plt.hist(v, alpha = 0.5, label = legend[i] if legendary else "")
	else:
		plt.hist(values, label = legend)
	pltcfg(legendary, ylabel)

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

def plot3d(X, Y, Z, cmap="Blues", xaxis="", yaxis=""):
	ax = plt.axes(projection='3d')
	ax.set_xlabel(xaxis)
	ax.set_ylabel(yaxis)
	ax.plot_surface(X, Y, Z, cmap=cmap, linewidth=0, antialiased=True)

@display(style = None, palette = None, width=5, height=8)
def surfplot(X, Y, Z, **kwargs):
	plot3d(X, Y, Z, **kwargs)

@display(style = None, palette = None, width=5, height=8)
def surfplotf(f, start=0, end=1, n=100, **kwargs):
	plane = np.linspace(start, end, n)
	X, Y = np.meshgrid(plane, plane)
	xs = np.dstack((X, Y)).reshape(n*n, 2)
	Z = f(xs).reshape(n, n)
	plot3d(X, Y, Z, **kwargs)