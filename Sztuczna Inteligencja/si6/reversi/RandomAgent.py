from reversi_show import Board

def RandomAgentMove(state):
	state = state.copy()
	mv = state.random_move()
	state.do_move(mv)
	return state

'''
state = Board()
while not state.terminal():
	state = RandomAgentMove(state)
	print(state)
'''