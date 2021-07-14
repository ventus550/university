from RandomAgent import RandomAgentMove
from game.state import State
import os
from time import sleep

T = (None, State())

while T[0] != (-1, -1, -1, -1):
	T = RandomAgentMove(T[1])
	out = "PLAYER " + str(T[1].player) + "\n" + str(T[0]) + "\n\n" + str(T[1]) +  "\nFatigue: " + str(T[1].fatigue)
	os.system('clear')
	print(out)
	# sleep(0.5)
	
	



