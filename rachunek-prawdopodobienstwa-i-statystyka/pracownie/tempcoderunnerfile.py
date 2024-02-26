def f(x):
	if x == 0:
		return 0
	denominator = 48
	numerator = x**2 * exp(-x/2)
	return numerator/denominator