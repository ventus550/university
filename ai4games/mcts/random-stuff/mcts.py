from game.state import State
from math import log, inf
from game.RandomAgent import RandomAgent
from collections import deque
from random import randint
from heuristic import buildHeuristic

from math import isnan


def randomSimulation(state):
	while not state.terminal():
		state = RandomAgent(state)
	return state.winner()


class MCTS:

	class Node:

		def __init__(self, state : State, move = None, parent = None):
			self.state = state.copy()
			if move != None:
				self.state.move(move)
			self.parent = parent
			self.visits = 0
			self.value = 0
			self.ucb = inf
			self.children = []			
				
		def __str__(self):
			return str(self.state)
		
		def __gt__(self, other):
			return self.ucb > other.ucb


	def __init__(self, simulator = randomSimulation, exploration = 2, K = 100):
		self.root = self.Node(State())
		self.size = 0
		self.simulator = simulator
		self.exploration = exploration
		self.memory = {} #?
		self.K = K


	def __getitem__(self, state : State):
		self.replant(state)
		self.root.visits += 1
		self.grow()
		return self.minimax()

	def __repr__(self):
		string = ""; depth = 0
		def draw(node, offset):
			nonlocal string, depth
			if node.value or node.children:
				depth = max(depth, offset)
				string += offset * " |"  +  "-(" + str(node.value) + ", " + str(node.ucb) + ")\n"
			for c in node.children:
				draw(c, offset + 1)
		
		if self.root != None:
			draw(self.root, 0)
			string += "\nsize: " + str(self.size) + "  depth: " + str(depth) + "  spread: " + str(len(self.root.state.moves())) + "\n\n"
			return string
		return "*"


	def replant(self, state):
		key = hash(state)
		for m1 in self.root.children:
			for m2 in m1.children:
				if hash(m2.state) == key:
					self.root = m2
					self.root.parent = None
					return
		self.root = self.Node(state)


	def minimax(self):
		self.size = 1
		player_switch = 2*self.root.state.player()-1

		def evl(node, k = 1):
			self.size += 1
			try:
				# powinno być None zamiast 0, bo zera wciąż mogą być sprawdzonymi stanami :(
				return min( [evl(c, -k) for c in node.children if c.value != 0], key=lambda x: k*x ) 
			except:
				return node.value
		
		return max( [(c, evl(c, player_switch)) for c in self.root.children], key=lambda x: player_switch*x[1] )[0].state


	def grow(self):
		K = self.K

		def UCB(node, C = 2):
			if isnan(node.value):
				node.value = node.parent.value
			if node.value == inf or node.value == -inf:
				return -inf

			n = node.visits; N = node.parent.visits
			val = node.value; E = self.exploration
			avg = val/n
			return avg + E*(log(N)/n)**0.5

		def simulation(node):
			node.value += self.simulator(node.state.copy())
		
		def expansion(node):
			node.children = [self.Node(node.state, m, node) for m in node.state.moves()]

		def selection(node):
			while node.children:
				node = max(node.children)
			return node

		def back_propagation(node):
			val = node.value
			while node.parent != None:
				node.visits += 1
				node.value += (val - node.value) / node.visits  #poszerzanie średniej o czynnik

				node.ucb = UCB(node)
				node = node.parent

		root = self.root
		while K > 0:
			sel = selection(root)
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
			back_propagation(sel)