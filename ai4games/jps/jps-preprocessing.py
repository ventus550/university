import sys
import math
import numpy as np

def addv(v, u):
	return (v[0] + u[0], v[1] + u[1])

class Grid:

	class Cell:
		def __init__(self):
			self.ls = np.full((3,3), np.nan)
		def __getitem__(self, direction):
			dv = addv(direction, (1,1))
			ret = self.ls[dv[1]][dv[0]]
			return ret if math.isnan(ret) else int(ret)
		def __setitem__(self, direction, val):
			dv = addv(direction, (1,1))
			self.ls[dv[1]][dv[0]] = val
		def __repr__(self):
			return str(self.ls)


	def __init__(self, rows):
		self.width = len(rows[0])
		self.height = len(rows)
		self.types = rows

		self.flags = [ [self.set_flags((x, y)) for y in range(self.height)] for x in range(self.width) ]
		self.jumps = [ [self.Cell() for y in range(self.height)] for x in range(self.width) ]

		self.sweep_straight((-1, 0))
		self.sweep_straight((1, 0))
		self.sweep_straight((0, -1))
		self.sweep_straight((0, 1))

		self.sweep_diagonal((-1, -1))
		self.sweep_diagonal((1, -1))
		self.sweep_diagonal((1, 1))
		self.sweep_diagonal((-1, 1))


	def is_wall(self, pos):
		x, y = pos
		if 0 <= x < self.width and 0 <= y < self.height:
			return self.types[y][x] == '#'
		return True


	def set_flags(self, pos):
		FLAGS = self.Cell()

		if self.is_wall(pos):
			return FLAGS

		for d in [ (1,1), (-1,1), (1,-1), (-1,-1) ]:
			corner = addv(d, pos)
			d1, d2 = (d[0], 0), (0, d[1])
			D1, D2 = addv(pos, d1), addv(pos, d2)
			
			if(self.is_wall(corner) and not self.is_wall(D1) and not self.is_wall(D2)):
				FLAGS[d1] = FLAGS[d2] = 1
		return FLAGS


	def sweep_straight(self, direction = (-1,0)):	
		rx = range(self.width)
		if direction[0] == 1: rx = reversed(rx)
		
		for col in rx:

			ry = range(self.height)
			if direction[1] == 1: ry = reversed(ry)

			for row in ry:
				predecessor = addv((col, row), direction)
				this = self.jumps[col][row]

				if self.is_wall(predecessor):
					this[direction] = 0
				elif self.flags[predecessor[0]][predecessor[1]][-direction[0], -direction[1]] == 1:
					this[direction] = 1
				else:
					jval = self.jumps[predecessor[0]][predecessor[1]][direction]
					if jval <= 0: this[direction] = jval - 1
					else: this[direction] = jval + 1

	
	def sweep_diagonal(self, direction = (1, 1)):
		ry = range(self.height)
		if direction[1] == 1: ry = reversed(ry)

		for row in ry:
			for col in range(self.width):
				predecessor = addv((col, row), direction)
				this = self.jumps[col][row]

				if(self.is_wall(predecessor)
				or self.is_wall((col + direction[0], row))
				or self.is_wall((col, row + direction[1]))):
					this[direction] = 0

				elif(self.jumps[predecessor[0]][predecessor[1]][direction[0], 0] > 0
				or   self.jumps[predecessor[0]][predecessor[1]][0, direction[1]] > 0):
					this[direction] = 1

				else:
					jval = self.jumps[predecessor[0]][predecessor[1]][direction]
					if jval <= 0: this[direction] = jval - 1
					else: this[direction] = jval + 1


# Compute the proper wall / jump point distances, according to the preprocessing phase of the JPS+ algorithm.

# width: Width of the map
# height: Height of the map
width, height = [int(i) for i in input().split()]
rows = [input() for _ in range(height)] # A single row of the map consisting of passable terrain ('.') and walls ('#')
grid = Grid(rows)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each empty tile of the map, a line containing "column row N NE E SE S SW W NW".
for x in range(grid.width):
    for y in range(grid.height):
        c = grid.jumps[x][y]
        if not grid.is_wall((x,y)):
            print( f"{x} {y} {c[0,-1]} {c[1,-1]} {c[1,0]} {c[1,1]} {c[0,1]} {c[-1,1]} {c[-1,0]} {c[-1,-1]}" )



