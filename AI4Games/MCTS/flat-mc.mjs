import {randint} from './utils.mjs'



class FlatMC {
	action(state, K = 200) {
		let actions = state.actions()
		let states = [], len = actions.length
		for (let a of actions) states.push(state.apply(a))
	
		let W = []
		for (let s of states) W.push(s.eval())
	
		let N = new Array(len).fill(1)
		
		for (let i = 0; i < K; i++) {
			let idx = randint(0, len - 1)
			W[idx] += states[idx].eval()
			N[idx] += 1
		}
	
		let Q = []
		for (let i = 0; i < len; i++) Q.push( [W[i]/N[i], actions[i]] )
	
		let player = 2*state.player - 1
		return Q.reduce( (a, b) => (player*a[0] > player*b[0]) ? a : b )[1]
	}
	update(state) {}
}

export function Agent() {
	return new FlatMC()
}