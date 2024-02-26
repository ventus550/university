from queue import PriorityQueue


#load distances
MAP = [
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
	[1, 2, 3, 5, 8, 9, 0, 2],
]

class Node:
	def __init__(self, position, givenCost, direction_of_travel):
		self.position = position
		self.direction = direction_of_travel
		self.givenCost = givenCost

	def __eq__(self, other):
		return self.position == other.position




def JPS(start, goal, MAP):

	def is_cardinal(direction):
		return direction in (0, 2, 4, 6)

	def is_diagonal(direction):
		return direction in (1, 3, 5, 7)

	def distances(node, direction):
		x, y = node.position
		return MAP[x][y][direction]

	def is_direction_exact(node): #BAD
		x1, y1 = node.position
		x2, y2 = goal.position
		if node.direction in (2, 6):
			return y1 == y2
		if node.direction in (0, 4):
			return x1 == x2
		
	def is_direction_general(node): #BAD
		x1, y1 = node.position
		x2, y2 = goal.position
		if node.direction in (1, 3, 5, 7):
			return abs(x1-x2) == abs(y1-y2)
		return is_direction_exact(node)

	def row_diff(node1, node2):
		_, y1 = node1.position
		_, y2 = node2.position
		return abs(y1 - y2)

	def col_diff(node1, node2):
		x1, _ = node1.position
		x2, _ = node2.position
		return abs(x1 - x2)

	DiffNodesRow = row_diff
	DiffNodesCol = col_diff
	SQRT2 = 2 ** 0.5

	def DiffNodes(node1, node2):
		return max(row_diff(node1, node2), col_diff(node1, node2))



goalNode = Node((0,0), None, None)
goalNode = Node((0,0), None, None)

# [N NE E SE S SW W NW] -  directions
#  0 1  2 3  4 5  6 7
ValidDirLookUpTable = [
	[2, 1, 0, 7, 7], # North
	[0, 7, 6],       # Northeast			
	[4, 3, 2, 1, 0], # East
	[4, 3, 2],       # Southeast
	[6, 5, 4, 3, 2], # South
	[6, 5, 4],       # Southwest
	[0, 7, 6, 5, 4], # West
	[6, 5, 4],       # Northwest
]





OpenList = PriorityQueue()
ClosedList = set()
while not OpenList.empty():

	curNode = OpenList.pop()
	direction_of_travel = curNode.direction_of_travel

	if curNode == goalNode:
		print ("PathFound")

	for direction in ValidDirLookUpTable[direction_of_travel]:
		newSuccessor = None
		givenCost = None

		if (iscardinal(direction)
		and goalNode
		and DiffNodes(curNode, goalNode) <= abs(curNode.distances[direction])):
