from RandomAgent import RandomAgentMove
from SmartAgent import SmartAgentMove
from game.state import State
import os
from time import sleep

T = (None, State())

while T[0] != (-1, -1, -1, -1):
	state = T[1]

	if state.player == 1:
		T = SmartAgentMove(state)
	else:
		T = RandomAgentMove(state)

	out = "PLAYER " + str(state.player) + "\n" + str(T[0]) + "\n\n" + str(state) +  "\nFatigue: " + str(T[1].fatigue)
	os.system('clear')
	print(out)
	sleep(0.5)
	
	



