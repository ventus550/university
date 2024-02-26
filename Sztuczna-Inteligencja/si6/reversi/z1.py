from RandomAgent import RandomAgentMove
from MinMax import MinMax
from reversi_show import Board

wins = 0

def winner(x):
	return int(x >= 0)

'''MEMORY = dict()
def MemMinMax(state, depth):
	key = str(state)
	if key in MEMORY:
		return MEMORY[key]
	MEMORY[key] = MinMax(state, depth=depth)
	return MEMORY[key]'''


def play(debug = False):
	state = Board()
	time = 0
	while not state.terminal():
		time += 1
		

		if state.player == 1:
			state = MinMax(state, depth = 1)
		else:
			state = RandomAgentMove(state)
		
		if debug:
			print("PLAYER", 1 - state.player)
			print(state)

	win = winner(state.result())
	# print("WINNER:", win)
	return win


for i in range(1000):
	wins += play(0)
	print(i, wins)
print("wins", wins)
