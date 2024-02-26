
import os
from game.state import State
from MCTS import MCTS
from heuristic import buildHeuristic, buildFinale
from game.RandomAgent import RandomAgent



class Opening:
	sqrs = dict( [(char, val) for val, char in enumerate("abcdefgh")] +
				 [(char, (int(char)-1)*8) for char in "12345678"] )

	def __init__(self, ls0, ls1):
		s = self.sqrs
		self.mvs = ([ (s[m[0]] + s[m[1]], s[m[2]] + s[m[3]]) for m in ls0],
					[ (s[m[0]] + s[m[1]], s[m[2]] + s[m[3]]) for m in ls1])	
	def __bool__(self):
		return bool(self.mvs[0]) and bool(self.mvs[1])
	def pop(self, player):
		return self.mvs[player].pop(0)
	

OP = Opening(["f7f5", "b8c6"], ["c2c4", "g1f3"])

class ChessMaster:

	def __init__(self, heuristic, exploration = 2, opening = Opening([], [])):
		self.tree = MCTS(simulator=heuristic, exploration=exploration, K=100)
		self.opening = opening
		self.finale = False
	
	def __repr__(self):
		return repr(self.tree)

	def __getitem__(self, state : State):

		def count(player):
			return sum( [len(state.pieces(piece, player)) for piece in range(1,7)] )

		if self.opening:
			return state.move(state.find_move(self.opening.pop()))

		if count(not state.turn) + count(state.turn) <= 7 and not self.finale and not state.castling_rights:
			#print("DEATH")
			self.tree = MCTS(simulator=buildFinale(not state.turn))

		return self.tree[state]


def makeAgent(h = {"r": 5, "n": 3, "b": 3, "q": 9}, coeffs = [1, 1, 1, 1, 1, 1]):
	return ChessMaster(buildHeuristic(h, coeffs=coeffs), exploration=coeffs[-1])