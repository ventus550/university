from functools import cache

@cache
def sudan(n, x, y):

	if n == 0:
		return x + y

	if y == 0 and x >= 0:
		return x

	return sudan(n-1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)





# Ogólnie argument x zdaje się mieć najmniejszy wpływ na czas obliczeń
# Dla wersji bez spamiętywania można obliczać sudan(2, x, 1) dla relatywnie dużych x, np. x = 25
# Możliwe jest również obliczenie w sensownym czasie sudan(2, 1, 2), ale już nie sudan(2, 2, 2).
# Dla wersji ze spamiętywaniem sudan(2, 5, 2) daje dość spektakularne (co do wielkości wyniku) rezultaty.
# Spamiętując potrafimy również obliczyć np. sudan(2, 0, 3)