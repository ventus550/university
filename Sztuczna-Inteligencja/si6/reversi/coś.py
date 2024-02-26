from RandomAgent import RandomAgentMove
from MCTS import MCTS
from reversi_show import Board

state = Board()
while not state.terminal():
	print("PLAYER", state.player)

	if state.player == 1:
		state = MCTS(state, K= 300)
	else:
		state = RandomAgentMove(state)

	print(state)
print("WINNER:", state.result())