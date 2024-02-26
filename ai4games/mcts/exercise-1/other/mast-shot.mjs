import {Board} from './mast-board.mjs'
import {SHOT} from './shot.mjs'

class MAST extends SHOT {

	constructor(decay, epsilon) {
		super()
		this.decay = decay
		this.epsilon = epsilon
	}

	action(state, K = 200) {
		let new_state = new Board(state.subboards)
		new_state.board = [...state.board]
		new_state.isterminal = state.isterminal
		new_state.winner = state.winner
		new_state.locked = state.locked
		new_state.mast.epsilon = this.epsilon
		const a = super.action(new_state, K)
		new_state.decay(this.decay)
		return a
	}

}

export function Agent(decay = 0.9, epsilon = 0.4) {
	return new MAST(decay, epsilon)
}