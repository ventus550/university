import re
import urllib.request as urllib

def parse(txt):
	splt = re.split(r' |\n', txt)
	return [int(float(x)) for i, x in enumerate(filter(''.__ne__, splt)) if i % 3]

def download_data(problem, begin, end):
	url =f"https://dev.heuristiclab.com/trac.fcgi/export/7465/branches/GeneralizedQAP/HeuristicLab.Problems.Instances.TSPLIB/3.3/Data/TSP/{problem}"
	data = urllib.urlopen(url)
	return parse("\n".join(line.decode('utf-8') for i, line in enumerate(data) if begin - 1 <= i <= end))
