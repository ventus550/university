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

		row = 0
		for line in m:
			line = list(line)
			self.MAP.append(line)
			for i in range(len(line)):
				pos = (row, i)

				if line[i] == '*':
					self.blocks.append(pos)
					self.destinations.append(pos)
					line[i] = 'G'
				elif line[i] == 'B':
					self.blocks.append(pos)
				elif line[i] == 'G':
					self.destinations.append(pos)
				elif line[i] == 'K':
					self.keeper = pos
					line[i] = '.'
			row += 1

	
	def dist(self, p1, p2):
		return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

	def isValid(self, pos):
		return self.MAP[pos[0]][pos[1]] != 'W'
	
	def isEndPoint(self, pos):
		return self.MAP[pos[0]][pos[1]] == 'G' or self.MAP[pos[0]][pos[1]] == '*'
	
	def pprint(self, keeper, blocks):
		MAP = self.MAP
		for r in range(len(MAP)):
			row = ""
			for c in range(len(MAP[0])):
				inblocks = (r, c) in blocks
				indests = (r, c) in self.destinations

				if inblocks and indests:
					row += '*'
				elif inblocks:
					row += 'B'
				elif indests:
					row += 'G'
				elif (r, c) == keeper:
					row += 'K'
				elif MAP[r][c] == 'W':
					row += 'W'
				else:
					row += '.'
			print(row)
		print("-----------------------------------------------")





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
		self.mvs = []

	def copy(self):
		product_state = MacroState(self.MAP)
		product_state.seq = self.seq
		product_state.blocks = self.blocks.copy()
		product_state.mvs = self.mvs.copy()
		product_state.keeper = self.keeper
		product_state.filled = self.filled
		product_state.stringified = self.stringified
		return product_state
	
	def __lt__(self, other):
		return False

	def __str__(self):
		return self.stringified
	
	def __len__(self):
		return len(self.mvs) #?
	
	def isWinPath(self):
		self.blocks = self.MAP.blocks
		for move in self.mvs:
			sub = SubState(self, move[0], move[1])
			res = BFS(sub)

			if res == None:
				return False

			print(self.keeper, "->", res.keeper, move[0], "->", move[1])
			print(res.seq)
			self.blocks = res.extraWalls + [res.destination]
			self.seq += res.seq
			self.keeper = res.keeper
		
		return True
			
		
	
	def step(self, pos, direction):
		mvector = self.moves[direction]
		return (pos[0] + mvector[0], pos[1] + mvector[1])

	def stepback(self, pos, direction):
		mvector = self.moves[direction]
		return (pos[0] - mvector[0], pos[1] - mvector[1])

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
		pblock = self.stepback(block, direction)

		if not self.MAP.isValid(nblock) or not self.MAP.isValid(pblock) or self.isDead(nblock) or nblock in self.blocks or pblock in self.blocks:
			return False

		if self.mvs and self.mvs[-1][1] == block:
			self.mvs[-1] = (self.mvs[-1][0], nblock)
		else:
			self.mvs.append( (block, nblock) )
				

		if self.MAP.isEndPoint(block):	
			self.filled -= 1
		if self.MAP.isEndPoint(nblock):
			self.filled += 1

		self.blocks.remove(block)
		self.blocks.append(nblock)
		

		#stringification
		self.stringified = "".join( [str(s[0]) + '|' + str(s[1]) + '|' for s in sorted(self.blocks)] )
		return self

class SubState(MacroState):

	def __init__(self, macro_state, block, destination):
		self.extraWalls = [b for b in macro_state.blocks if b != block]
		#print("EXXTRA",self.extraWalls, block)
		self.block = block
		self.destination = destination
		self.seq = ""
		self.keeper = macro_state.keeper
		self.MAP = macro_state.MAP
		self.stringified = ""
	
	def copy(self):
		product_state = SubState(MacroState(self.MAP), self.block, self.destination)
		product_state.extraWalls = self.extraWalls.copy()
		product_state.keeper = self.keeper
		product_state.seq = self.seq
		product_state.stringified = self.stringified
		return product_state		

	def isWinPath(self):
		return self.block == self.destination

	def move(self, direction):
		npos = self.step(self.keeper, direction)

		if not self.MAP.isValid(npos) or npos in self.extraWalls:
			return False
		
		if self.block == npos:
			nblock = self.step(self.block, direction)
			
			'''if nblock == (2, 4):
				print(self.keeper, "->", npos, self.block, "->", nblock)
				print(not self.MAP.isValid(nblock), nblock in self.extraWalls, self.isDead(nblock))'''

			if not self.MAP.isValid(nblock) or nblock in self.extraWalls or self.isDead(nblock):
				return False
			
			self.block = nblock
		
		#move is valid
		self.keeper = npos
		self.seq += direction


		#stringification
		self.stringified = str(self.block)  + str(self.keeper)
		return self


def BFS(origin):
	MEMORY = set()
	Q = Queue(); Q.put(origin)

	def lookup(state):
		k = str(state)
		if k in MEMORY:
			return True
		MEMORY.add(k)
		return False

	while not Q.empty():
		state = Q.get()
		
		if state.isWinPath():
			return state

		for move in ("R", "U", "L", "D"):
			newState = state.copy()
			newState = newState.move(move) #state if valid False if not
			'''if newState != False and newState.keeper == (2, 3) and state.keeper == (2, 2):
				print("==========>", newState.block)'''
			if newState != False and not lookup(newState):
				Q.put(newState)





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
		return h3(state) + h1(state)

	def cost(state):
		return H(state) + len(state)
	
	def push(Acost, state):
		hq.heappush(heap,  (Acost, state) )

	def lookup(state, Acost):
		if Acost == 0:
			return True
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
				
				if newState == False:
					continue
				
				Acost = cost(newState)
				if lookup(newState, Acost):
					push(Acost, newState)

	while heap:
		state = hq.heappop(heap)[1]
		#print(state.filled)
		

		if len(state.MAP.destinations) == state.filled:
			if state.isWinPath():
				return state.seq
		else:
			expand(state)


def solve(input):
	return AStar(MacroState(Map(input)))

#python3 validator.py zad2 python3 sokoban1.py
fio("zad_input.txt", "zad_output.txt", solve)