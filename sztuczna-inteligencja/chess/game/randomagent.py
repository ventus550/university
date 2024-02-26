from game.state import State

# Agent dostaje na wejściu stan i modyfikuje go o losowy ruch
def RandomAgent(state : State):
	return state.move(state.random_move())