from queue import Queue
import heapq as hq

def fio(iput, oput, transform, encoding='utf-8'):
	res = []
	with open(iput, encoding=encoding) as f:
		for line in f:
			line = line.strip()
			res.append(line)

	with open(oput, mode="w", encoding=encoding) as f:
		f.write(transform(res))



class Map:
	def __init__(self, m = []):
		self.MAP = []
		self.blocks = []
		self.destinations = []
		self.keeper = None
		self.distances = {}

		row = 0
		for line in m:
			line = list(line)
			self.MAP.append(line)
			for i in range(len(line)):
				pos = (row, i)
				if line[i] == 'B' or line[i] == '*':
					self.blocks.append(pos)
				if line[i] == 'G' or line[i] == '*':
					self.destinations.append(pos)
				elif line[i] == 'K':
					self.keeper = pos
			row += 1

	
	def dist(self, p1, p2):
		return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

	def isValid(self, pos):
		return self.MAP[pos[0]][pos[1]] != 'W'
	
	def isEndPoint(self, pos):
		return self.MAP[pos[0]][pos[1]] == 'G' or self.MAP[pos[0]][pos[1]] == '*'






class MacroState:
	moves = {
		"R": (0, 1),
		"L": (0,-1),
		"U": (-1,0),
		"D": (1, 0)
	}

	def __init__(self, MAP):
		self.seq = ""
		self.blocks = MAP.blocks
		self.keeper = MAP.keeper
		self.MAP = MAP
		self.filled = 0
		self.stringified = ""

	def copy(self):
		product_state = MacroState(self.MAP)
		product_state.seq = self.seq
		product_state.blocks = self.blocks.copy()
		product_state.keeper = self.keeper
		product_state.filled = self.filled
		product_state.stringified = self.stringified
		return product_state
	
	def __lt__(self, other):
		return False

	def __str__(self):
		return self.stringified
	
	def __len__(self):
		return len(self.seq)

	def isWinPath(self):
		return len(self.MAP.destinations) == self.filled
	
	def step(self, pos, direction):
		mvector = self.moves[direction]
		return (pos[0] + mvector[0], pos[1] + mvector[1])

	def isDead(self, block):
		if self.MAP.isEndPoint(block):
			return False
		
		prev = self.step(block, "L")
		prev = self.MAP.isValid(prev)

		for m in [ "U", "R", "D", "L" ]:
			nblock = self.step(block, m)
			nblock = self.MAP.isValid(nblock)
			if not prev and not nblock:
				return True
			prev = nblock

		return False
			
	def move(self, block, direction):
		nblock = self.step(block, direction)

		if not self.MAP.isValid(nblock) or self.isDead(nblock) or nblock in self.blocks:
			return False
		
		self.blocks.remove(block)
		self.blocks.append(nblock)

		if self.MAP.isEndPoint(block):
			self.filled -= 1
		if self.MAP.isEndPoint(nblock):
			self.filled += 1

		#stringification
		self.stringified = "".join( [str(s[0]) + '|' + str(s[1]) + '|' for s in sorted(self.blocks)] )
		return self




def h1(state): #empty slots
	return len(state.MAP.destinations) - state.filled

def h2(state): #blocks optimistic distance
	return sum( [ min([state.MAP.dist(b, d) for d in state.MAP.destinations]) for b in state.blocks]  )

def h3(state):
	return max( [ min([state.MAP.dist(b, d) for d in state.MAP.destinations]) for b in state.blocks]  )

def h4(state): #keeper distance from blocks
	return min( [state.MAP.dist(state.keeper, b) for b in state.blocks] ) - 1
	
def AStar(origin):
	heap = [ (0, origin) ]; hq.heapify(heap)
	MEMORY = {}

	def H(state):
		return 0

	def cost(state):
		return H(state) + len(state)
	
	def push(Acost, state):
		hq.heappush(heap,  (Acost, state) )

	def lookup(state, Acost):
		k = str(state)
		if k in MEMORY and Acost >= MEMORY[k]:
			return False
		MEMORY[k] = Acost
		return True

	def expand(state):
		for block in state.blocks:
			for move in ("R", "U", "L", "D"):
				newState = state.copy()
				newState = newState.move(block, move)
				
				#print(newState, newState == False)
				if newState == False:
					continue
				
				Acost = cost(newState)
				if lookup(newState, Acost):
					push(Acost, newState)

	while heap:
		state = hq.heappop(heap)[1]
		#print(state.filled)

		if state.isWinPath():
			return res(state.seq)
		else:
			expand(state)


def solve(input):
	return AStar(MacroState(Map(input)))

#python3 validator.py zad2 python3 sokoban1.py
fio("zad_input.txt", "zad_output.txt", solve)