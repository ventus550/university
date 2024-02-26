import sys
import math
from queue import PriorityQueue
from collections import defaultdict
SQRT2 = 2 ** 0.5

def err(*args):
    print(*args, file=sys.stderr, flush=True)


# [N NE E SE S SW W NW] -  directions
#  0 1  2 3  4 5  6 7
ValidDirLookUpTable = [
	[2, 1, 0, 7, 6], # North
	[0, 1, 2],       # Northeast			
	[4, 3, 2, 1, 0], # East
	[4, 3, 2],       # Southeast
	[6, 5, 4, 3, 2], # South
	[6, 5, 4],       # Southwest
	[0, 7, 6, 5, 4], # West
	[0, 7, 6],       # Northwest
    list(range(8))   # Omni
]


class Node:
    def __init__(self, position, direction_of_travel, parent = None):
        self.position = position
        self.direction = direction_of_travel
        self.parent = parent
        self.givenCost = 0
        self.finalCost = 0
    
    def __repr__(self): #${int(self.givenCost)} : ${int(self.finalCost)}
        return f"❨{self.parent.position} ⟶ {self.position} : {self.finalCost}❩"


    def __eq__(self, other):
        return self.position == other.position #and self.parent.position == other.parent.position


class ListQueue:
    def __init__(self):
        self.ls = []
    
    def put(self, item):
        self.ls.append(item)

    def pop(self):
        self.ls.sort(key=lambda x: x.finalCost, reverse=True)
        return self.ls.pop()
    
    def empty(self):
        return not len(self.ls)
    
    def update(self, item):
        for i in range(len(self.ls)):
            if self.ls[i] == item:
                self.ls[i] = item
    
    def cost(self, item):
        for x in self.ls:
            if x == item:
                return x.givenCost
        return 0

    def __contains__(self, item):
        return item in self.ls
    
    def __repr__(self):
        return "\n".join( str(x) for x in self.ls )
        





def heuristic(node, goal):
    x1, y1 = node.position
    x2, y2 = goal.position
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return dx + dy + (SQRT2 - 2) * min(dx,dy)


def JPS(start, goal, MAP):

    def is_cardinal(direction):
        return direction in (0, 2, 4, 6)

    def is_diagonal(direction):
        return direction in (1, 3, 5, 7)

    def distances(node, direction):
        x, y = node.position
        return MAP[x][y][direction]

    def is_direction_exact(node, direction): #BAD
        x1, y1 = node.position
        x2, y2 = goal.position

        outcomes = [
            x1 == x2 and y1 > y2,
            None,
            x1 < x2 and y1 == y2,
            None,
            x1 == x2 and y1 < y2,
            None,
            x1 > x2 and y1 == y2
        ]
        return outcomes[direction]


    def is_direction_general(node, direction): #BAD
        x1, y1 = node.position
        x2, y2 = goal.position
        
        outcomes = [
            y1 > y2,
            y1 > y2 and x1 < x2,
            x1 < x2,
            y1 < y2 and x1 < x2,
            y1 < y2,
            y1 < y2 and x1 > x2,
            x1 > x2,
            y1 > y2 and x1 > x2
        ]
        return outcomes[direction]


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


    def DiffNodes(node1, node2):
        return max(row_diff(node1, node2), col_diff(node1, node2))

    def GetNode(parent, direction, override_distance = False):
        move = distances(parent, direction)
        if override_distance != False: move = override_distance
        x, y = parent.position


        positions = [
            [x, y - move],
            [x + move, y - move],
            [x + move, y],
            [x + move, y + move],
            [x, y + move],
            [x - move, y + move],
            [x - move, y],
            [x - move, y - move]
        ]

        return Node(positions[direction], direction, parent = parent)

    OpenList = ListQueue()
    ClosedList = ListQueue()

    OpenList.put(start)

    while not OpenList.empty():

        txt = str(OpenList)
        curNode = OpenList.pop()


        ClosedList.put(curNode)
        traveling_direction = curNode.direction
        yield curNode

        if curNode == goal:
            print("PATH FOUND", file=sys.stderr, flush=True)
            break
        
        for direction in ValidDirLookUpTable[traveling_direction]:
            
            newSuccessor = None
            givenCost = None

            if (is_cardinal(direction)
            and is_direction_exact(curNode, direction)
            and DiffNodes(curNode, goal) <= abs(distances(curNode, direction))):

                # Goal is closer than wall distance or
                # closer than or equal to jump point distance
                newSuccessor = goal
                givenCost = curNode.givenCost + DiffNodes(curNode, goal)
                goal.parent = curNode
            

            elif (is_diagonal(direction)
            and   is_direction_general(curNode, direction)
            and   (DiffNodesRow(curNode, goal) <= abs(distances(curNode, direction))
                or DiffNodesCol(curNode, goal) <= abs(distances(curNode, direction)))):

                # Goal is closer or equal in either row or
                # column than wall or jump point distance

                # Create a target jump point
                minDiff = min(row_diff(curNode, goal), col_diff(curNode, goal))
                newSuccessor = GetNode(curNode, direction, override_distance=minDiff)
                givenCost = curNode.givenCost + SQRT2*minDiff
            

            elif distances(curNode, direction) > 0:

                # Jump point in this direction
                newSuccessor = GetNode(curNode, direction)
                givenCost = DiffNodes(curNode, newSuccessor)
                if is_diagonal(direction): givenCost *= SQRT2
                givenCost += curNode.givenCost


            # --------- A* ---------
            if isinstance(newSuccessor, Node):

                if newSuccessor not in OpenList and newSuccessor not in ClosedList:
                    newSuccessor.parent = curNode
                    newSuccessor.givenCost = givenCost

                    newSuccessor.finalCost = givenCost + heuristic(newSuccessor, goal)
                    OpenList.put( newSuccessor )

                elif givenCost < OpenList.cost(newSuccessor):
                    newSuccessor.parent = curNode
                    newSuccessor.givenCost = givenCost

                    newSuccessor.finalCost = givenCost + heuristic(newSuccessor, goal)
                    OpenList.update( newSuccessor )

    print("NO PATH")


    


# Compute the nodes visited by the JPS+ algorithm when performing runtime phase search.

# width: Width of the map
# height: Height of the map
width, height = [int(i) for i in input().split()]

# start_column: coordinate of the starting tile
# start_row: coordinate of the starting tile
# goal_column: coordinate of the goal tile
# goal_row: coordinate of the goal tile
start_column, start_row, goal_column, goal_row = [int(i) for i in input().split()]
start_node = Node( (start_column, start_row), -1 )
start_node.parent = Node( (-1, -1), None)

goal_node = Node( (goal_column, goal_row), 0)

_open = int(input())  # number of open tiles on the map


MAP = [ [None for h in range(height)] for w in range(width) ]
for i in range(_open):
    # column: coordinate of the empty tile described
    # row: coordinate of the empty tile described
    # n: distance to the closest jump point (positive number) or wall (otherwise) going north
    # ne: distance to the closest jump point (positive number) or wall (otherwise) going northeast
    # e: distance to the closest jump point (positive number) or wall (otherwise) going east
    # se: distance to the closest jump point (positive number) or wall (otherwise) going southeast
    # s: distance to the closest jump point (positive number) or wall (otherwise) going south
    # sw: distance to the closest jump point (positive number) or wall (otherwise) going southwest
    # w: distance to the closest jump point (positive number) or wall (otherwise) going west
    # nw: distance to the closest jump point (positive number) or wall (otherwise) going northwest
    ### column, row, n, ne, e, se, s, sw, w, nw = [int(j) for j in input().split()]
    column, row, *directions = [int(j) for j in input().split()]
    MAP[column][row] = directions
    # print(column, file=sys.stderr, flush=True)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



# In order of nodes visited by the JPS+ algorithm, a line containing "nodeColumn nodeRow parentColumn parentRow givenCost".
#print("startColumn startRow -1 -1 0.00")


jps = JPS(start_node, goal_node, MAP)


# game loop
while True:

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    node = next(jps)
    x, y = node.position
    px, py = node.parent.position
    givenCost = node.givenCost


    # In order of nodes visited by the JPS+ algorithm, a line containing "nodeColumn nodeRow parentColumn parentRow givenCost".
    # First turn: print("1 4 -1 -1 0.00")
    
    print(f'{x} {y} {px} {py} {givenCost}')
