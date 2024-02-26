from game.state import State
from game.board import Board
from random import choice, shuffle

# Agent dostaje na wejściu stan
# i zwraca nowy stan wraz z wykonanym ruchem
# jeśli gra się zakończyła lub ruchu nie da się wykonać zwraca stan otrzymany na wejściu

SURRENDER = (-1, -1, -1, -1)

def sqrt(x):
	return x**0.5

def parth(p1, p2):
	return (p1[0] + p2[0], p1[1] + p2[1])

def dist(p1, p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def edist(p1, p2):
	return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

def evals(state, player=1):
	aniset = state.aniset()
	friendly = set([x for x in aniset if state.owner(x) == player])
	hostile = aniset - friendly

	def POS(anm):
		return state.animals[anm]

	def ANM(pos):
		return state.brd[pos]

	def endangered(anm):
		for mv in ( (0,1), (1,0), (-1,0), (0,-1) ):
			npos = parth( POS(anm), mv )
			if state.notValid(npos, anm):
				continue

			nanm = ANM(npos)
			if nanm in hostile and state.rank(nanm) >= state.rank(anm):
				return True

		return False
	
	def weight(anm):
		return (POS(anm)[0]**3) #*state.fatigue
	
	def mdist(anm):
		p = POS(anm)
		return min(dist(p, (0,0)), dist(p, (0,6)), dist(p, (0,3)))
	
	def distance():
		distances = [mdist(f)**2 for f in friendly]
		if state.fatigue > 20 or min(distances) <= 4:
			return min([edist(POS(f), (0,3)) for f in friendly])
		return sum(distances)
	
	def hostility():
		return sum([weight(h) for h in hostile]) * state.fatigue

	return -hostility() - distance()


	






def SmartAgentMove(state):

	moves = state.moves()

	#check win condition
	if state.winner() != None or moves == []:
		return (SURRENDER, state)

	#eval all states and pick the best one
	shuffle(moves)
	values = [evals(s[1]) for s in moves]
	pick = values.index(max(values))
	return moves[pick]
	

	




