from random import choice


POPCOUNT = bytes(bin(x).count("1") for x in range(512))
ROWS = [0b111000000, 0b000111000, 0b000000111]
COLS = [0b100100100, 0b010010010, 0b001001001]
DIGS = [0b100010001, 0b001010100]
ALL = ROWS + COLS + DIGS
VECT = list(2**p for p in range(8, -1, -1))


class SubBoard:

	def __init__(self):
		self.board = [0b000000000, 0b000000000]
		self.isterminal = False
		self.winner = None
	
	def __getitem__(self, xyp):
		x, y, p = xyp; v = VECT[3*x + y]
		return (v & self.board[p]) != 0

	def __setitem__(self, xyp, val):
		x, y, p = xyp; v = VECT[3*x + y]; val = val != 0
		self.board[p] |= (v * val)
	
	def __repr__(self):
		return bin(self.board[0] | self.board[1])
	
	def match(self, pattern, p):
		return POPCOUNT[self.board[p] & pattern]
			
	def actions(self):
		board = self.board[0] | self.board[1]
		return [ (e // 3, e % 3) for e,v in enumerate(VECT) if (v & board) == 0 ]

	def perform_action(self, action, p):
		i, j = action
		B = SubBoard()
		B.board = self.board.copy()
		B[i, j, p] = 1

		if(B.match(ROWS[i], p) == 3
		or B.match(COLS[j], p) == 3
		or B.match(DIGS[0], p) == 3
		or B.match(DIGS[1], p) == 3
		or POPCOUNT[B.board[0] | B.board[1]] == 9):
			B.isterminal = True
			B.winner = p
		return B
	
	def terminal(self):
		return self.isterminal
	
	def eval(self):
		state = self
		while not state.terminal():
			state = state.perform_action(choice(state.actions()), POPCOUNT[state.board[0]] != POPCOUNT[state.board[1]]) # x = 0, o = 1
		return state.winner 	#2*(not self.player) - 1 # 0 -> -1, 1 -> 1


class Board(SubBoard):

	def __init__(self, player=0, subboards = [SubBoard()] * 9):
		SubBoard.__init__(self)
		self.subboards = subboards
		self.player = player # x = 0, o = 1
	
	def __str__(self) -> str:
		string = []
		sbs = self.subboards
		for row in range(9):
			r = row % 3
			string.append((1+(r==0)) * "\n")

			for col in range(9):
				idx = 3*(row // 3) + col // 3
				c = col % 3
				string.append((c == 0) * " ")
				if sbs[idx][r, c, 0]:
					string.append("X")
				elif sbs[idx][r, c, 1]:
					string.append("O")
				else:
					string.append("_")
		return "".join(string)
		
	def actions(self):
		board = self.board[0] | self.board[1]
		return [ (e, action) for e,v in enumerate(VECT) for action in self.subboards[e].actions() if (v & board) == 0 ]
	
	def copy_from(self, other):
		self.board = other.board.copy()
		self.isterminal = other.isterminal
		self.winner = other.winner

	def apply(self, action):
		idx, subaction = action
		new_board = Board(subboards = self.subboards.copy())
		new_board.player = not self.player

		new_subboard = self.subboards[idx].perform_action(subaction, self.player)
		new_board.subboards[idx] = new_subboard

		if new_subboard.winner == None:
			new_board.copy_from(self)
			return new_board
		
		binboard = self.perform_action( (idx // 3, idx % 3), self.player )
		new_board.copy_from(binboard)
		return new_board
	
	def terminal(self):
		return all(b.isterminal for b in self.subboards)

	def eval(self, debug = False):
		state = self
		while not state.terminal():
			state = state.apply(choice(state.actions()))
		return state.winner




def log(state):
	print(state, repr(state), state.subboards, sep="\n")

for i in range(100):
	S = Board()
	print(S.eval())