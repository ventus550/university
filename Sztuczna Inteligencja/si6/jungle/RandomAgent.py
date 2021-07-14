from game.state import State
from game.board import Board
from random import choice, shuffle

# Agent dostaje na wejściu stan
# i zwraca nowy stan wraz z wykonanym ruchem
# jeśli gra się zakończyła lub ruchu nie da się wykonać zwraca stan otrzymany na wejściu

'''def random_move(state):
	moves = state.moves()
	if not moves or state.winner() != None:
		return state.player
	c = choice(moves)[1]
	return c'''

SURRENDER = (-1, -1, -1, -1)


def finish(state):
	winner = state.winner()
	if winner != None:
		return winner
	return state

def random_move(state):
	aniset = list(state.aniset())
	shuffle(aniset)
	while aniset:
		anm = aniset.pop()
		if state.owner(anm) == state.player:
			moves = ["right", "left", "up", "down"]
			shuffle(moves)
			while moves:
				move = moves.pop()
				if state.move(anm, move):
					return finish(state)
	return int(not state.player)

def play(state):
	count = 0
	while type(state) == State:
		state = random_move(state)
		count += 1
		# print()
		# print(state)
	return (count, state) # state is now the games winner

# 0 -> 1, 1 -> -1
def format(player):
	return player * -2 + 1

def RandomAgentMove(state, N = 20000):

	moves = state.moves()

	#check win condition
	if state.winner() != None or moves == []:
		return (SURRENDER, state)

	num = len(moves)
	count = 0

	ratios = [0 for _ in range(num)]
	while N > 0:
		cost, res = play(moves[count][1].copy())
		N -= cost
		ratios[count] += format(res)
		count += 1
		count %= num

	pick = None
	if state.player == 1:
		pick = ratios.index(min(ratios))
	else:
		pick = ratios.index(max(ratios))
	# print([x[0] for x in moves])
	# print(ratios)
	# print(pick)

	return moves[pick]





DEFAULT = Board(
"......."
"...W..."
"...e..."
"......."
"......."
"......."
"......."
"......."
"......."
)


# test = State(player = 1, brd = DEFAULT)
# RandomAgentMove(test)
# print(play(test))




