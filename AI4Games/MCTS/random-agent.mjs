import { choice } from './utils.mjs'

class RandomAgent {
	action(state) {
		return choice(state.actions())
	}
	update(state) {}
}

export function Agent() {
	return new RandomAgent()
}