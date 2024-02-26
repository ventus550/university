from game.board import Board, Terrain

def u(s):
	return s.upper()

DEFAULT = Board(
"L.....T"
".D...C."
"R.J.W.E"
"......."
"......."
"......."
"e.w.j.r"
".c...d."
"t.....l"
)

class State:

	ranks = {
		"R":0, "C":1, "D":2, "W":3,
		"J":4, "T":5, "L":6, "E":7, ".": -1
	}

	directions = {
		"right": (0, 1), "left" : (0,-1),
		"up"   : (-1,0), "down" : (1, 0)
	}

	def __init__(self, player = 1, brd = DEFAULT):
		self.player = player
		self.fatigue = 0
		self.animals = {}
		self.brd = brd.copy()
		for row in range(brd.height):
			for col in range(brd.width):
				p = (row, col)
				self.animals[brd[p]] = p
		self.animals["."] = None

	def __str__(self):
		return str(self.brd)
	
	def aniset(self):
		s = set()
		for p in self.animals.items():
			if p[1] != None:
				s.add(p[0])
		return s
	
	def winner(self):
		if self.brd[(0,3)] != ".":
			return 1
		elif self.brd[(8,3)] != ".":
			return 0
		elif self.fatigue >= 30:
			L = [self.rank(x) if self.owner(x) == self.player else -self.rank(x) for x in self.aniset()]
			s = max(L) + min(L)
			if s >= 0:
				return self.player
			return int(not self.player)
		return None

	def owner(self, anm):
		return int(anm.islower())
	
	def enemy(self, anm1, anm2):
		return self.owner(anm1) != self.owner(anm2)
	
	def rank(self, anm):
		return self.ranks[u(anm)]

	def step(self, pos, direction):
		vect = self.directions[direction]
		return (pos[0] + vect[0], pos[1] + vect[1])

	def notValid(self, p, anm):
		owner = self.owner(anm)
		return (Terrain.out_of_boundaries(p)
				or (p == (0, 3) and owner == 0)
				or (p == (8, 3) and owner == 1))

	def capture(self, anm, target):
		apos, self.animals[anm] = self.animals[anm], target
		self.brd[apos] = "."

		victim = self.brd[target]
		self.brd[target] = anm
		self.animals[victim] = None
		if victim != ".":
			self.fatigue = 0
	
	def trapped(self, anm):
		return Terrain[self.animals[anm]] == "#"
	
	def wins(self, attacker, defender):
		if defender == ".":
			return True
		elif (u(attacker) == "R"
		   and Terrain[self.animals[attacker]] == "~"
		   and Terrain[self.animals[defender]] == "."):
			return False
		elif self.trapped(defender):
			return True
		elif u(attacker) == "R" and u(defender) == "E":
			return True
		elif u(attacker) == "E" and u(defender) == "R":
			return False
		elif self.rank(attacker) >= self.rank(defender):
			return True
		return False

	def move(self, anm, direction):

		def quickstep(s):
			return self.step(s, direction)

		pos = self.animals[anm]
		npos = quickstep(pos)

		if self.notValid(npos, anm):
			return False
		
		# Jump mechanic
		if (u(anm) == "T" or u(anm) == "L"):
			enemy_rat = "r"
			if self.owner(anm) == 1:
				enemy_rat = u(enemy_rat)

			while Terrain[npos] == "~":
				npos = quickstep(npos)
				if self.brd[npos] == enemy_rat:
					return False
		
		bnp = self.brd[npos]
		if ((Terrain[npos] == "~" and u(anm) != "R") or
			(bnp != "." and not self.enemy(anm, bnp))):
			return False
		
		if not self.wins(anm, bnp):
			return False

		self.fatigue += 1
		self.capture(anm, npos)
		self.player = int(not self.player)

		#Formatting
		pos = (pos[1], pos[0])
		npos = (npos[1], npos[0])
		return pos + npos
	
	def copy(self):
		s = State(brd = self.brd)
		s.player = self.player
		s.fatigue = self.fatigue
		return s

	def moves(self):
		animals = self.animals.keys()

		state_list = []
		for a in self.aniset():
			if self.owner(a) != self.player:
				continue
				
			state = self.copy()
			for mv in ("right", "left", "up", "down"):
				move = state.move(a, mv)
				if move:
					state_list += [(move, state)]
										
					state = self.copy() # one too many copies :(
		
		return state_list