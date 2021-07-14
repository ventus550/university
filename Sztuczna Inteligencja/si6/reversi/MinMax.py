from reversi_show import Board
from math import inf




# gracz zero (kółka) jest graczem minimalizującym
def MinMax(state, depth = inf, MEMORY = dict()):

	def lookup(state):
		key = str(state)
		if key in MEMORY:
			return MEMORY[key]
		MEMORY[key] = neval(state)
		return MEMORY[key]

	#heurystyka
	def neval(state, param = 200):

		b = state.board
		spots = [b[0][0], b[0][7], b[7][0], b[7][7]]
		return state.result() + sum([param*s for s in spots if s != None])

	def moved(state, move):
		return state.copy().do_move(move)

	def rec(state, dp = depth, alpha = -inf, beta = inf):
		moves = state.moves()

		if not moves or dp == 0:
			return lookup(state)

		if state.player == 1: # 1 to gracz maksymalizujący
			mx = -inf
			for m in moves:
				m = moved(state, m)
				ev = rec(m, dp - 1, alpha, beta)
				mx = max(mx, ev)
				alpha = max(alpha, ev)
				if beta <= alpha:
					break
			return mx
		
		else:
			mn = inf
			for m in moves:
				m = moved(state, m)
				ev = rec(m, dp - 1, alpha, beta)
				mn = min(mn, ev)
				beta = min(alpha, ev)
				if beta <= alpha:
					break
			return mn
	
	moves = [(rec(s), s) for s in [moved(state, m) for m in state.moves()]]
	# print([m[0] for m in moves])
	return max(moves, key= lambda x: x[0])[1]
	