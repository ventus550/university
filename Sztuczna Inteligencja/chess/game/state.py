from uuid import uuid1
from numpy import array
import numpy as np
from random import choice
from chess import Board

def ID():
	return int(repr(uuid1().int))


# Gracz biały(1) jest w dolnej części planszy i wykonuje pierwszy ruch
class State(Board):
	pl = {True: ID(), False: ID()}

	#def __init__(self):
	#	Board.__init__(self)

	def __hash__(self):
		return (self.pl[self.turn]
			  ^ self.pawns
			  ^ self.knights
			  ^ self.bishops
			  ^ self.rooks
			  ^ self.queens
			  ^ self.kings)
	
	#1 if white, -1 if black
	def winner(self):
		if self.result()[0] != "*" and self.result() != "1/2-1/2":
			return 2*int(self.result()[0]) - 1
		return 0

	def player(self):
		return int(self.turn)

	def terminal(self, K = 100):
		return self.time() >= 100 or self.is_checkmate() or not self.legal_moves

	def softCopy(self):
		return self.copy(stack = False)
	
	def time(self):
		return len(self.move_stack)

	def move(self, mv):
		self.push(mv)
		return self

	def moves(self):
		return list(self.legal_moves)
	
	def random_move(self):
		return choice(self.moves())

