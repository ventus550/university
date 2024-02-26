from itertools import count, accumulate
from operator import add

def pierwiastek(n):

	for k, val in enumerate(accumulate((2*i - 1 for i in count(1)), add)):
		if val > n:
			return k



	
