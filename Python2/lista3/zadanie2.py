from functools import reduce
from timeit import timeit


def doskonale_imperatywna(n):
	perfect = []
	for p in range(2, n):
		test = 0
		for d in range(1, p):
			if p % d == 0:
				test += d
		if test == p:
			perfect.append(p)
	return perfect

def doskonale_skladana(n):
	return [ p for p in range(2, n) if sum([ i for i in range(1, p) if p % i == 0 ]) == p ]

def doskonale_funkcyjna(n):
	return list(filter(lambda p: reduce(lambda acc, x: acc + x if not p % x else acc, range(1,p)) == p, range(2,n)))


assert(doskonale_imperatywna(1000) == doskonale_skladana(1000) == doskonale_funkcyjna(1000))


# imperatywna <= składana < funkcjyna
print(timeit(lambda: doskonale_imperatywna(100), number=10000))
print(timeit(lambda: doskonale_skladana(100), number=10000))
print(timeit(lambda: doskonale_funkcyjna(100), number=10000))