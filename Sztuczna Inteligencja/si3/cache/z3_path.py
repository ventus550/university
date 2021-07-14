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




def dist(pos, MAP):
	return min( [abs(pos[0] - e[0]) + abs(pos[1] - e[1]) for e in MAP.EndPoints] )


def H3(pos_list, MAP):
	s = 0
	for p in pos_list:
		s = max(dist(p, MAP), s)
	return s


def H2(pos_list, MAP):
	s = 0
	for p in pos_list:
		s += dist(p, MAP)
	return s/len(pos_list)


def H(pos_list, MAP):
	return len(pos_list)


def AStar(MAP):
	p = MAP.StartPoints
	p = (H(p, MAP), p, [])
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


	def stop(node):
		if len(node) > len(MAP.EndPoints):
			return False
		return all([ MAP.isEndPoint(n) for n in node ])


	def reposition(node, move, path):		
		np = set()
		win = True
		for p in node:
			new_position = ( p[0] + move[0], p[1] + move[1] )

			if not MAP.isValid(new_position):
				new_position = p

			np.add(new_position)

		return np


	def expand(node, path):
		for move in [ (1,0), (-1,0), (0,1), (0,-1) ]:
			np = reposition(node, move, path)
			if lookup(np) and len(np) <= node_limit:
				hq.heappush(heap, (H(np, MAP), np, path + [move]) )

	
	while heap and not end:
		min_path, node, path = hq.heappop(heap)
		if stop(node):
			print(path, len(path))
			break

		#ceiling--
		if len(node) > node_limit:
			continue
		node_limit = min(node_limit, len(node))

		print(len(node))
		expand(node, path)
		#break
	
	#print(end, MAP.EndPoints)
	






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

M = Map(mp)
AStar(M)










