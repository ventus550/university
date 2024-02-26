from numpy import array


def shadow(H, V):
	n = len(H)
	solution = []

	def choose(color):
		pos = len(solution)
		if pos == n**2:
			return sum(H) + sum(V) == 0

		solution.append(color)
		x, y = pos//n, pos%n
		V[x] -= color; H[y] -= color

		if (V[x] < 0 or H[y] < 0
		or (not choose(0) and not choose(1))):
			 solution.pop()
			 V[x] += color; H[y] += color
			 return False

		return True
	
	if choose(0) or choose(1):
		return array(solution).reshape((n,n))
	else:
		return False


print(shadow([2, 1, 3, 1], [1, 3, 1, 2]))

