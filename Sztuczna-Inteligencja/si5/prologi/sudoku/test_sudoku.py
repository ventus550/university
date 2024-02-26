

solution = open("sud_solved.txt", "r")
solution = solution.readline()
solution = eval(solution)
solution = [ solution[row*9 : row*9 +9] for row in range(9) ]

def unique(L):
	return len(set(L)) == 9

def square(y, x):
	y *= 3; x *= 3

	L = []
	for row in range(y, y+3):
		L += solution[row][x:x+3]
	return unique(L)


isOK = (
	all([ square(row, col) for row in range(3) for col in range(3) ]) and
	all([ unique(row) for row in solution                          ]) and
	all([ unique([row[c] for row in solution]) for c in range(9)   ])
)

print(isOK)
