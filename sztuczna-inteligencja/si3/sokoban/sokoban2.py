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
		self.m = m.copy()
		self.height = len(m)
		if m:
			self.width = len(m[0])
		else:
			self.width = 0
	
	def __getitem__(self, pos):
		return self.m[pos[0]][pos[1]]
	
	def __setitem__(self, pos, char):
		r, c = pos
		row = self.m[r]
		self.m[pos[0]] = row[:c] + char +  row[c+1:]
	
	def dist(self, p1, p2):
		return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

	def isValid(self, pos):
		return self[pos] != 'W'
	
	def isEndPoint(self, pos):
		return self[pos] == 'G' or self[pos] == '*'
	
	def __str__(self):
		return "\n".join(self.m)




class State(Map):

	moves = {"R": (0, 1), "L": (0,-1), "U": (-1,0), "D": (1, 0)}

	def __init__(self, obj):
		self.steps = ""

		if type(obj) == Map:
			super().__init__(obj.m)
			self.blocks = []
			self.slots = []
			self.length = 0

			for pos in [(r, c) for r in range(obj.height) for c in range(obj.width)]:
				char = obj[pos]
				if char == '.' or char == 'W':
					continue
				elif char == '*':
					self.blocks.append(pos)
					self.slots.append(pos)
				elif char == 'B':
					self.blocks.append(pos)
				elif char == 'G':
					self.slots.append(pos)
				else:
					self.keeper = pos 
				
		elif type(obj) == State:
			self.blocks = obj.blocks.copy()
			self.slots = obj.slots
			self.keeper = obj.keeper
			self.steps = obj.steps
			self.height = obj.height
			self.width = obj.width
			self.length = obj.length
			self.m = obj.m
			
	
	def __lt__(self, other):
		return False
	
	def __len__(self):
		return self.length
	
	def __str__(self):
		strr = ""
		for r in range(self.height):
			row = ""
			for c in range(self.width):
				p = (r, c)
				if p in self.blocks:
					row += 'B'
				elif self[p] == 'W':
					row += 'W'
				elif p == self.keeper:
					row += 'K'
				else:
					row += '.'
			strr += row + '\n'
		return strr
			

	def key(self, keeper = True):
		strr = "".join( [str(s[0]) + '|' + str(s[1]) + '|' for s in sorted(self.blocks)] )
		if keeper:
			strr += str(self.keeper)
		return strr
	
	def step(self, pos, direction):
		mvector = self.moves[direction]
		return (pos[0] + mvector[0], pos[1] + mvector[1])
	
	def stepback(self, pos, direction):
		mvector = self.moves[direction]
		return (pos[0] - mvector[0], pos[1] - mvector[1])
	
	def isDead(self, block): #opt?
		if self.isEndPoint(block):
			return False

		prev = self.step(block, "L")
		prev = self.isValid(prev)

		for m in [ "U", "R", "D", "L" ]:
			nblock = self.step(block, m)
			nblock = self.isValid(nblock)
			if not prev and not nblock:
				return True
			prev = nblock

		return False
	
	def isSolved(self):
		return not len(set(self.blocks) - set(self.slots))

def QuickBFS(origin):
	MEMORY = {}
	Q = Queue(); Q.put( (origin.keeper, "") )

	def lookup(state):
		k = state[0]
		if k in MEMORY:
			return True
		MEMORY[k] = state[1]
		return False
	
	def move(state, direction):
		npos = origin.step(state[0], direction)

		if not origin.isValid(npos) or npos in origin.blocks:
			return False
		
		return (npos, state[1] + direction)
		
	while not Q.empty():
		state = Q.get()

		for mv in ("R", "U", "L", "D"):
			newState = move(state, mv) #state if valid False if not

			if newState != False and not lookup(newState):
				Q.put(newState)
	MEMORY[origin.keeper] = ""
	return MEMORY



def h1(state): #empty slots
	return len(set(state.blocks) - set(state.slots))

def h2(state): #blocks optimistic distance
	return sum( [ min([state.dist(b, d) for d in state.slots]) for b in state.blocks]  )

def h3(state):
	return max( [ min([state.dist(b, d) for d in state.slots]) for b in state.blocks]  )

def AStar(origin):
	heap = [ (0, origin) ]; hq.heapify(heap)
	MEMORY = {}

	def H(state):
		return h1(state) + h2(state)

	def cost(state):
		return H(state) + len(state)
	
	def push(Acost, state):
		hq.heappush(heap,  (Acost, state) )

	def lookup(state, Acost):
		k = state.key(True)
		if k in MEMORY and Acost >= MEMORY[k]:
			return False
		MEMORY[k] = Acost
		return True
	
	def move(state, block, direction, valid_areas):
		#print("V:", valid_areas)

		pblock = state.stepback(block, direction)
		if pblock not in valid_areas.keys():
			return False


		nblock = state.step(block, direction)
		if not state.isValid(nblock) or state.isDead(nblock) or nblock in state.blocks:
			return False


		state = State(state) #make copy of the validated state
		state.keeper = block
		state.steps += valid_areas[pblock] + direction
		state.length += 1

		state.blocks.remove(block)
		state.blocks.append(nblock)
		return state

	def expand(state):
		valid_areas = QuickBFS(state)
		for block in state.blocks:
			for mv in ("R", "U", "L", "D"):
				newState = move(state, block, mv, valid_areas)
				
				if newState == False:
					continue
				
				Acost = cost(newState)
				if lookup(newState, Acost):
					push(Acost, newState)
					
	while heap:
		state = hq.heappop(heap)[1]

		if state.isSolved():
			print(state.steps)
			return state.steps
		else:
			expand(state)
	return False

def solve(input):
	return AStar(State(Map(input)))

#python3 validator.py zad3 python3 sokoban2.py
fio("zad_input.txt", "zad_output.txt", solve)