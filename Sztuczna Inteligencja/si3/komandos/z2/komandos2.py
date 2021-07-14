import heapq as hq
def fio(iput, oput, transform, encoding='utf-8'):
	res = []
	with open(iput, encoding=encoding) as f:
		for line in f:
			line = line.strip()
			res.append(line)

	resMap = Map(res)
	with open(oput, mode="w", encoding=encoding) as f:
		f.write(transform(resMap))


















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
				if line[i] == 'S' or line[i] == 'B':
					self.StartPoints.append( (row, i) )
				if line[i] == 'B' or line[i] == 'G':
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
		self.AStarCost = 0

	def __str__(self):
		return self.stringified
	
	def __len__(self):
		return len(self.seq)
	
	def __lt__(self, other):
		return self.AStarCost < other.AStarCost
	
	def copy(self):
		S = State(self.MAP, self.spots.copy())
		S.seq = self.seq
		S.EOP = self.EOP
		S.stringified = self.stringified
		S.AStarCost = self.AStarCost
		return S

	def isWinPath(self):
		return self.EOP
	
	def cost(self):
		return self.AStarCost

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
		self.AStarCost = H(self) + len(self)

		#stringification
		self.stringified = "".join( [str(s[0]) + '|' + str(s[1]) + '|' for s in sorted(list(self.spots))] )

		return self.spots





def dist(pos, MAP):
	return min( [abs(pos[0] - e[0]) + abs(pos[1] - e[1]) for e in MAP.EndPoints] )


#---- heurystyki -----

def H1(MS):
	return len(MS.spots)

def H2(MS):
	return len(MS.spots) / (H3(MS) + 1)

def H3(MS):
	return min([dist(p, MS.MAP) for p in MS.spots])

def H4(MS):
	return max([dist(p, MS.MAP) for p in MS.spots])

def H5(MS): #średnia odległości [*]
	return sum([dist(p, MS.MAP) for p in MS.spots])

def H6(MS):
	return H1(MS)   #min(H1(MS), H4(MS))

def paramH(MS, degree=1):
	return H1(MS)**degree

def H(MS):
	return H1(MS)**5

#---------------------


def AStar(MAP):
	MS = State(MAP, spots= set(MAP.StartPoints))

	heap = [MS]; hq.heapify(heap)
	MEMORY = {}

	def lookup(MS):
		k = str(MS)
		if k in MEMORY:
			return False
			#return MEMORY[k]
		MEMORY[k] = MS.AStarCost

		return MS.AStarCost+1 #chodzi o to, że jeśli jest nowy to zawsze idzie na heapa

	def stop(MS):
		if len(MS.spots) > len(MAP.EndPoints):
			return False
		return MS.isWinPath()

	def expand(MS):
		for move in ("R", "U", "L", "D"):
			NMS = MS.copy()
			NMS.move(move)


			if lookup(NMS): # > AStarCost:
				hq.heappush(heap, NMS)

	
	shortest = []
	while heap:
		node = hq.heappop(heap)

		if stop(node) and (not shortest or len(node) < len(shortest)):
			shortest = node
			break		
		
		#print(len(node.spots), node.cost())

		expand(node)
	
	print(shortest.seq, len(shortest.seq))
	return str(shortest)
	
	






mp = [
"######################",
"#SSSSSSSS#SSS##SSSSSS#",
"#SSSSSSSSSSSS##SSSSSS#",
"#SSSSSS###SSSSSSSSS#B#",
"#SSSSSS###SSSSSSSSSSS#",
"#SSSSSSSSSSSSSSSSSSSS#",
"#####SSSSSSSSSSSSSSSS#",
"#SSSSSSSSSSSSSSSSSSSS#",
"######################"
]

mp2 = [
"#####",
"#B  #",
"#   #",
"#  B#",
"#S# #",
"#   #",
"#SSS#",
"#####",
]

mp3 = [
"##################",
"#SSSSSSSSSSSSSSSS#",
"######SSSS###SSSS#",
"#SSSSSSSSS###SSSS#",
"#SSS###SSSSSSSSSS#",
"#SSS###SSSS#####S#",
"#SS####SSSS#SSSSS#",
"#SSSSSSSSSS#SSSSB#",
"#SSSSSSSSSS#SSSSB#",
"##################"
]

mp4 = [
"############",
"#SSSSSS#SSS#",
"#SS#####SSS#",
"#SSSS#SSSBS#",
"#BBSSSS#SSS#",
"#SS##SSSSSS#",
"#SS##SSSSSS#",
"############"
]
 
mp5 = [  #[(1,1), (3,3)]
"#####",
"#B#S#",
"#SSS#",
"#SSB#",
"#S#S#",
"#SSS#",
"#SSS#",
"#####"
]


M = Map(mp5)
AStar(M)
#fio("zad_input.txt", "zad_output.txt", AStar)










