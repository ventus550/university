from RandomAgent import RandomAgentMove
from MCTS import MCTS
from reversi_show import Board

state = Board()
while not state.terminal():
	print("PLAYER", state.player)
	state = MCTS(state)
	print(state)
print("WINNER:", state.result())