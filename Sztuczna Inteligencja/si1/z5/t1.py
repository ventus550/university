from random import choice

inp1 =  [7, 7, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7]
inp2 =  [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

def solve(L):
	width = L[0]; height = L[1]
	ROWS = L[2:2+L[0]]; COLS = L[2+L[0]:]
	ILLEGAL_ROWS = set(); ILLEGAL_COLS = set()

	IMAGE = [ [0 for _ in range(width)] for _ in range(height) ]

	def reset():
		ILLEGAL_ROWS = set(); ILLEGAL_COLS = set()

		for x in range(width):
			for y in range(height):
				IMAGE[x][y] = choice([0,1])

	def evaluate(block, bits):
		operations = len(bits)

		for i in range(len(bits)-block+1):
			block_max = sum(bits[i:i+block])
			calc = sum(bits) + block - 2*block_max
			if operations > calc:
				operations = calc
		return operations
	
	def getRow(k):
		return IMAGE[k]

	def getCol(k):
		return [ IMAGE[i][k] for i in range(height) ]
	
	def validate():
		for row in range(height):
			if evaluate(ROWS[row], getRow(row)) != 0:
				ILLEGAL_ROWS.add(row)
		
		for col in range(width):
			if evaluate(COLS[col], getCol(col)) != 0:
				ILLEGAL_COLS.add(col)

		return not ILLEGAL_COLS and not ILLEGAL_ROWS
	
	def modSet(s, e):
		if e in s:
			s.remove(e)
		else:
			s.add(e)

	def modifyRow(i):
		mods = []

		for j in range(width):
			row = getRow(i).copy(); row[j] = not row[j]
			col = getCol(j).copy(); col[i] = not col[i] #raczej nie trzeba kopiować

			mods.append( (j, evaluate(ROWS[i], row), evaluate(COLS[j], col)) )
		
		mods.sort(key = lambda p: p[1] + p[2])
		best = mods[0]; j = best[0]
		IMAGE[i][j] = int(not IMAGE[i][j])
		#print("CHANGE:", i, j)
		if best[1] == 0:
			ILLEGAL_ROWS.remove(i)
		else:
			ILLEGAL_ROWS.add(i)
		if best[2] == 0:
			ILLEGAL_COLS.remove(j)
		else:
			ILLEGAL_COLS.add(j)

	def modifyCol(j):
		mods = []

		for i in range(height):
			row = getRow(i).copy(); row[j] = not row[j]
			col = getCol(j).copy(); col[i] = not col[i]

			mods.append( (i, evaluate(ROWS[i], row), evaluate(COLS[j], col)) )
		
		mods.sort(key = lambda p: p[1] + p[2])
		best = mods[0]
		IMAGE[best[0]][j] = int(not IMAGE[best[0]][j])
		#print("CHANGE:", i, j)
		if best[1] == 0:
			ILLEGAL_ROWS.remove(i)
		else:
			ILLEGAL_ROWS.add(i)
		if best[2] == 0:
			ILLEGAL_COLS.remove(j)
		else:
			ILLEGAL_COLS.add(j)

	def pick(): #bad
		L = []
		if ILLEGAL_ROWS:
			L.append( ("row", ILLEGAL_ROWS) )
		if ILLEGAL_COLS:
			L.append( ("col", ILLEGAL_COLS) )
		
		
		if L:
			c = choice(L)
			return ( c[0], choice(tuple(c[1])) )
		return False	

	def iprint():
		for row in IMAGE:
			print(row)
		print("--------------------------------")

	validate()
	while(ILLEGAL_ROWS or ILLEGAL_COLS):
		print("RESET", ILLEGAL_ROWS, ILLEGAL_COLS)
		reset()
		validate()
		k = 10000
		while(k):
			k -= 1

			p = pick()
			if not p:
				break
			modifyRow(p[1])
			
			#print(ILLEGAL_ROWS, ILLEGAL_COLS, '\n')
	iprint()
			



solve(inp1)
