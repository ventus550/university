from timeit import timeit

def pierwsze_imperatywna(n):
	primes = []
	for i in range(2, n):
		test = True
		for p in primes:
			if i % p == 0:
				test = False
				break
		if test:		
			primes.append(i)
	return primes

def pierwsze_skladana(n):
	return [ p for p in range(2, n) if not [ i for i in range(2, p) if p % i == 0 ] ]

def pierwsze_funkcyjna(n):
	return list(filter(lambda p: not any( p % i == 0 for i in range(2, p) ), range(2, n)))

assert(pierwsze_imperatywna(100) == pierwsze_skladana(100) == pierwsze_funkcyjna(100))


# imperatywna < funkcjyna < składana
print(timeit(lambda: pierwsze_imperatywna(100), number=10000))
print(timeit(lambda: pierwsze_skladana(100), number=10000))
print(timeit(lambda: pierwsze_funkcyjna(100), number=10000))