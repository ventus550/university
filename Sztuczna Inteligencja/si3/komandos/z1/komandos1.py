from queue import Queue
from random import choice, randint
def fio(iput, oput, transform, encoding='utf-8'):
	res = []
	with open(iput, encoding=encoding) as f:
		for line in f:
			line = line.strip()
			res.append(line)

	with open(oput, mode="w", encoding=encoding) as f:
		f.write(transform(res))











class Map:
	MAP = []
	StartPoints = []
	EndPoints = []

	def __init__(self, m = []):

		row = 0
		for line in m:
			line = list(line)
			self.MAP.append(line)
			for i in range(len(line)):
				if line[i] == 'S':
					self.StartPoints.append( (row, i) )
				elif line[i] == 'B' or line[i] == 'G':
					self.EndPoints.append( (row, i) )
			row += 1

	def pprint(self, potentials):
		MAP = self.MAP
		for r in range(len(MAP)):
			row = ""
			for c in range(len(MAP[0])):
				if (r, c) in potentials:
					row += 'P'
				elif MAP[r][c] == 'B':
					row += 'B'
				elif MAP[r][c] == 'G':
					row += 'G'
				elif MAP[r][c] != '#':
					row += '.'
				else:
					row += '#'
			print(row)
		print("-----------------------------------------------")
	
	def isValid(self, pos):
		MAP = self.MAP
		return (MAP[pos[0]][pos[1]] != '#'
		and pos[0] >= 0
		and pos[1] >= 0
		and pos[0] < len(MAP)
		and pos[1] < len(MAP[0]))
	
	def isEndPoint(self,pos):
		return self.MAP[pos[0]][pos[1]] == 'B' or self.MAP[pos[0]][pos[1]] == 'G'



class State:
	moves = {
		"R": (0, 1),
		"L": (0,-1),
		"U": (-1,0),
		"D": (1, 0)
	}

	def __init__(self, MAP, spots = set()):
		self.seq = ""
		self.spots = spots
		self.MAP = MAP
		self.EOP = False
		self.stringified = ""

	def __str__(self):
		return self.stringified
	
	def __len__(self):
		return len(self.seq)
	
	def copy(self):
		S = State(self.MAP, self.spots.copy())
		S.seq = self.seq
		S.EOP = self.EOP
		S.stringified = self.stringified
		return S

	def isWinPath(self):
		return self.EOP

	def move(self, direction, times = 1):
		self.seq += times * direction
		direction = self.moves[direction]

		def step(pos):
			npos = (pos[0] + direction[0], pos[1] + direction[1])
			if not self.MAP.isValid(npos):
				return pos
			return npos

		def multistep(pos):
			npos = pos
			for _ in range(times):
				npos = step(npos)
			return npos

		EOP = True
		repositioned = set()
		for p in self.spots:
			p = multistep(p)
			repositioned.add(p)
			if not self.MAP.isEndPoint(p):
				EOP = False

		self.EOP = EOP
		self.spots = repositioned

		#stringification
		self.stringified = "".join( [str(s[0]) + '|' + str(s[1]) + '|' for s in sorted(list(self.spots))] )

		return self.spots



def stairs(MS, move1, move2, length):
	for i in range(length):
		moves = ( move1, move2 )
		MS.move(moves[i%2])
	return MS

def stairs_up(MS, length):
	return stairs(MS, "R", "U", length)

def stairs_down(MS, length):
	return stairs(MS, "L", "D", length)

def square(MS, length):
	length //= 4
	for move in ("R", "U", "L", "D"):
		MS.move(move, times=length)
	return MS

def spiral(MS, length):
	s = 0; i = 1
	while s < length:
		MS.move()


def constructReductionFunction(size = 100):
	component_functions = [stairs_down, stairs_up, square]

	F = lambda MS: MS
	s = 70

	while s >= 10:
		n = randint(4, min(s, 40));
		f = choice(component_functions)
		F = lambda MS, F=F, f=f: F( f(MS, n) )
		s -= n


	return F


def reduceUncertainty(MAP):

	def uncertainty(MS):
		return len(MS.spots)

	MS = State(MAP, set(MAP.StartPoints))

	test1 = stairs_down(stairs_up(MS.copy(), 40), 40)
	test2 = square(MS.copy(), 80)

	best = test1
	if uncertainty(test1) > uncertainty(test2):
		best = test2
	
	for _ in range(100):
		RF = constructReductionFunction()
		test = RF(MS.copy())
		if uncertainty(test) < uncertainty(best) or (uncertainty(test) == uncertainty(best) and len(test) < len(best)):
			best = test

	
	MAP.pprint(best.spots)


	
	return best





def BFS(MS):
	MEMORY = {}
	Q = Queue(); Q.put( MS )

	def lookup(spots):
		k = str(spots)
		if k in MEMORY:
			return True
		MEMORY[k] = True
		return False


	while not Q.empty():
		state = Q.get()
		if state.isWinPath():
			print(state.seq)
			return state.seq

		for move in ("R", "U", "L", "D"):
			newState = state.copy()
			newState.move(move)

			if not lookup(newState):
				Q.put( newState )

def solve(input):
	M = Map(input)
	MS = reduceUncertainty(M)
	return BFS(MS)

fio("zad_input.txt", "zad_output.txt", solve)








