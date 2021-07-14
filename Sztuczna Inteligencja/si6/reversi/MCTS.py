from RandomAgent import RandomAgentMove
from reversi_show import Board
from math import log, inf





def UCB1(val, N, n, C= 2):
	if n == 0:
		return inf
	avg = val/n
	return avg + C*(log(N)/n)**0.5

def nodify(state, move, parent):
	return Node(state.do_move(move), move, parent)

class Node:
	def __init__(self, state, move = None, parent = None):
		self.state = state.copy()
		if move != None:
			self.state.do_move(move)
		self.move = move
		self.parent = parent
		self.visits = 0
		self.value = 0
		self.children = []
	
	def __str__(self):
		return str(self.state)
	
	def __float__(self):
		return UCB1(self.value, self.parent.visits, self.visits)
	
	def __gt__(self, other):
		return float(self) > float(other)

	def expand(self):
		self.children = [nodify(self.state, m) for m in self.state.moves()]
	
	



def MCTS(state, K = 50):

	def simulation(node):
		state = node.state.copy()
		while not state.terminal():
			state = RandomAgentMove(state)
		res = state.result()
		node.value += res
		node.visits += 1
		return res
	
	def expansion(node):
		node.children = [nodify(node.state, m, node) for m in node.state.moves()]

	def selection(node):
		while node.children:
			node = max(node.children)
		return node

	def back_propagation(node):
		while node.parent != None:
			node = node.parent
			node.value = sum( [n.value for n in node.children] )  # da się znacznie lepiej ;)
			node.visits += 1


	



	origin = Node(state)

	while K > 0:
		sel = selection(origin)
		K -= 1
		if sel.visits == 0:
			simulation(sel)
		else:
			expansion(sel)
			try:
				sel = sel.children[0]
				simulation(sel)
			except:
				pass

		# print(sel, sel.value)
		back_propagation(sel)
	best = max(origin.children).move
	return state.do_move(best)
	#[(x.value, x.move) for x in origin.children] #max(origin.children).move
		