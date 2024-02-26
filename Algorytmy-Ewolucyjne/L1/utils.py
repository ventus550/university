import matplotlib.pyplot as plt
from itertools import chain
from tqdm import tqdm
import contextlib
from seaborn import set_theme
set_theme(style = "darkgrid", palette="dark")

@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

def progress_bar(iterable, disabled = False, color="yellow", desc=None):
	return tqdm(iterable, disable=disabled, colour=color, desc=desc)

def loop(times, iterable):
	it = iter(iterable)
	while (times := times - 1) >= 0:
		yield next(it)

def pltcfg(legend = False, title = "", ylabel = "", path = "", tight = True):
	if legend:
		plt.legend()
	if tight:
		plt.tight_layout(pad=3)
	plt.ylabel(ylabel)
	plt.title(title)
	if path: plt.savefig(path)
	plt.show()
	plt.clf()

def quickplot(*values, legend = [], ylabel = "", title = "", path = ""):
	legendary = len(legend) == len(values)
	for i, v in enumerate(values):
		plt.plot(v, label = legend[i] if legendary else "")
	pltcfg(legendary, title, ylabel, path)

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
	plt.figure(figsize=(10,0.2), dpi=100)
	plt.imshow(v, cmap="coolwarm", aspect="auto")
	plt.yticks([])
	plt.xticks([])
	pltcfg(False, title, "", path, tight = False)