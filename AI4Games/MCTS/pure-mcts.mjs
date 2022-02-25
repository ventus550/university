import {Board} from './board.mjs'
import {MCTS} from './mcts.mjs'

export function Agent(exploration = 1) {
	return new MCTS(exploration)
}