import heapq as hq

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
				elif line[i] == 'B':
					self.EndPoints.append( (row, i) )
			row += 1

	def pprint(self, potentials):
		MAP = self.MAP
		for r in range(len(MAP)):
			row = ""
			for c in range(len(MAP[0])):
				if (r, c) in potentials:
					row += 'P'
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
		return self.MAP[pos[0]][pos[1]] == 'B'




def dist(pos, map):
	return min( [abs(pos[0] - e[0]) + abs(pos[1] - e[1]) for e in map.EndPoints] )


def macroDist(pos_list, map):
	s = 0
	for p in pos_list:
		s += dist(p, map)
	return s/len(pos_list)


def AStar(MAP):
	p = MAP.StartPoints
	p = (macroDist(p, MAP), p)
	heap = [p]; hq.heapify(heap)
	MEMORY = {}
	end = False
	node_limit = len(MAP.MAP) * len(MAP.MAP[0])


	def lookup(node):
		k = str(sorted(list(node)))
		if k in MEMORY:
			return False
		MEMORY[k] = False
		return True
	

	def reposition(node, move):		
		np = set()
		win = True
		for p in node:
			new_position = ( p[0] + move[0], p[1] + move[1] )

			if not MAP.isValid(new_position):
				new_position = p
			
			if not MAP.isEndPoint(new_position):
				win = False

			np.add(new_position)

		if win:
			end = np
		return np


	def expand(node):
		for move in [ (1,0), (-1,0), (0,1), (0,-1) ]:
			np = reposition(node, move)
			if lookup(np) and len(np) <= node_limit:
				hq.heappush(heap, (macroDist(np, MAP), np))

	
	while heap and not end:
		min_path, node = hq.heappop(heap)

		#ceiling--
		if len(node) > node_limit:
			continue
		node_limit = min(node_limit, len(node))

		print(len(node))
		expand(node)
	






mp = ["######################",
"#SSSSSSSS#SSS##SSSSSS#",
"#SSSSSSSSSSSS##SSSSSS#",
"#SSSSSS###SSSSSSSSS#B#",
"#SSSSSS###SSSSSSSSSSS#",
"#SSSSSSSSSSSSSSSSSSSS#",
"#####SSSSSSSSSSSSSSSS#",
"#SSSSSSSSSSSSSSSSSSSS#",
"######################"]

M = Map(mp)
AStar(M)










