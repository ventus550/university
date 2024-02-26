
class Board:
	width = 7
	height = 9

	def __init__(self, brd):
		self.brd = list(brd)
	
	def __str__(self):
		return "\n".join(["".join(self.brd[7*r:7*(r+1)]) for r in range(9)])
		
	def __getitem__(self, p):
		return self.brd[p[0]*7 + p[1]]
	
	def __setitem__(self, p, value):
		self.brd[p[0]*7 + p[1]] = value
	
	def copy(self):
		return Board(self.brd.copy())
		
	def out_of_boundaries(self, p):
		return (p[0]+1) * (p[1]+1) <= 0 or p[0] > 8 or p[1] > 6


brd = (
"..#*#.."
"...#..."
"......."
".~~.~~."
".~~.~~."
".~~.~~."
"......."
"...#..."
"..#*#.."
)

Terrain = Board(brd)

