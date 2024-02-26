from fio import fio
from draw import DRAW

class State:
	def __init__(self, dct):
		self.content = dct
	
	def __str__(self):
		return "<" + str(self.content["whiteK"]) + str(self.content["whiteT"]) + str(self.content["blackK"]) + ">"
	
	def __getitem__(self, key):
		return self.content[key]
	def __setitem__(self, key, item):
		self.content[key] = item
	def __eq__(self, value):
		return self.content == value
	def copy(self):
		return State(self.content.copy())

def sprint(seq):
	strr = ""
	for s in seq:
		strr += str(s) + "\n"
	return "__________"+ str(len(seq)) +"___________\n" + strr + "______________________"

def dist(p1, p2):
	return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def SEARCH(player, starting_state):
	states = []
	winnig_sequence = []

	#0 - white, 1 - black
	def move(player, seq = [], m_nr=1):

		if player == 0:
			moveTower(0, seq, m_nr)
			moveKing(0, seq, m_nr)
		else:
			moveKing(1, seq, m_nr)

	def moveTower(player, seq, m_nr):
		nonlocal states
		
		#its not worth it to move the tower while the kings are apart
		if dist(seq[-1]["whiteK"], seq[-1]["blackK"]) > 2:
			return False

		def tower(i, axis):
			nonlocal states
			nstate = seq[-1].copy()

			#tower cant be idle
			if i == nstate["whiteT"][axis]:
				return False


			nstate["whiteT"] = nstate["whiteT"].copy()

			def is_pathable(figure):
				figure = nstate[figure]

				if figure[not axis] != nstate["whiteT"][not axis]:
					return True

				b = nstate["whiteT"][axis]; e = i
				if b > e:
					b, e = e, b
				if b <= figure[axis] and figure[axis] <= e:
					return False
				return True


			if is_pathable("whiteK") and is_pathable("blackK"):
				nstate["whiteT"][axis] = i
				states += [seq + [nstate.copy()]]

		for i in range(0,8):
			tower(i, 0)
			tower(i, 1)
			

	def moveKing(player, seq, m_nr):
		nonlocal winnig_sequence
		nonlocal states

		
		
		king = "whiteK"
		if player == 1:
			king = "blackK"

		def towerCollisionBlack(state, axs):
			bK = state["blackK"]; wK = state["whiteK"]; wT = state["whiteT"]  
			return bK[axs] == wT[axs] and (wT[axs] != bK[axs] or not (min(bK[axs], wT[axs]) <= wK[axs] and wK[axs] <= max(bK[axs], wT[axs])))

		def is_pathable(state):
			p = state[king]

			

			#check if zone exists
			if p[0] < 0 or p[0] > 7 or p[1] < 0 or p[1] > 7:
				return False
			
			#check collision with the other king	
			if dist(state["whiteK"], state["blackK"]) < 2:
				return False

			#check collision with tower
			if king == "blackK":
				if towerCollisionBlack(state, 0) or towerCollisionBlack(state, 1):
					return False
			else:
				if state["whiteT"] == p:
					return False
			return True

		
		not_checkmate = False
		directions = [-1, 0, 1]
		for i in directions:
			for j in directions:
				if i == 0 and j == 0:
					continue

				nstate = seq[-1].copy()
				kpos = nstate[king]
				nstate[king] = [ kpos[0] + i, kpos[1] + j ]

				if is_pathable(nstate):
					not_checkmate = True
					states += [seq + [nstate]]

		lst = seq[-1]
		if not not_checkmate:
			if dist(lst["blackK"], lst["whiteT"]) < 2 and dist(lst["whiteK"], lst["whiteT"]) > 2:
				return False
			elif not towerCollisionBlack(lst, 0) and not towerCollisionBlack(lst, 1):
				#states += [seq + [lst.copy()]]
				return False
			else:
				winnig_sequence = seq
				#sprint(winnig_sequence)
			
	move(player, starting_state)
	return (winnig_sequence, states)

def CHESS(player, starting_state, debug=0):
	starting_state = [starting_state]

	winning_sequence = []
	MEMORY = {}
	MEMORY[str(starting_state[-1])] = starting_state

	moves_limit = 1
	while not winning_sequence and moves_limit < 30:
		
		moves_limit += 1
		states, MEMORY = MEMORY, {}

		for state in states.values():
			s = SEARCH((moves_limit+player) % 2, state)
			if s[0]:
				winning_sequence = s[0]
				break
			else:
				for seq in s[1]:
					MEMORY[str(seq[-1])] = seq

	if debug == 0:
		if not winning_sequence:
			print("pat")
		return len(winning_sequence) - 1
	else:
		DRAW(winning_sequence)
		return sprint(winning_sequence)

#--------------in/out-------------------------
def map_input(strr):

	MAP = {
		'a':0,	'1':0,
		'b':1,	'2':1,
		'c':2,	'3':2,
		'd':3,	'4':3,
		'e':4,	'5':4,
		'f':5,	'6':5,
		'g':6,	'7':6,
		'h':7,	'8':7,
		"white": 0, "black" : 1
	}

	if strr in MAP.keys():
		return MAP[strr]
	return [MAP[strr[0]], MAP[strr[1]]]

def prepare_line(line):
	line = line.split()
	s = State({
			"whiteK": map_input(line[1]),
			"whiteT": map_input(line[2]),
			"blackK": map_input(line[3])
	})
	return str(CHESS(map_input(line[0]), s, debug=1))

fio("zad1_input.txt", "zad1_output.txt", prepare_line)
