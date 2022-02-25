from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, List

class State(ABC):

	@abstractmethod
	def actions(self) -> list:
		''' Return a collection of actions available to the current state '''

	@abstractmethod
	def perform_action(self, action) -> State:
		''' Return a new state resulting form a given action '''
	
	# @abstractmethod
	# def player(self) -> int:
	# 	''' Return the current player '''
	
	@abstractmethod
	def eval(self) -> int:
		''' Return value of the current state '''

	# @abstractmethod
	# def __hash__(self) -> int or str:
	# 	''' Return state's hash '''

	@abstractmethod
	def terminal(self) -> int:
		''' Test if the state is terminal meaning the game has ended. '''