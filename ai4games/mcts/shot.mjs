
export class SHOT {
	
	constructor() {
		this.TT = new Map()
	}
		
	sum(arr1, arr2) {
		return [arr1[0] + arr2[0], arr1[1] + arr2[1]]
	}
	
	node(parent, action) {
		const state = parent.apply(action),
		self = this
		
		Object.assign(state, {
			action: action,
			hash: self.hash(state)
		})
		return state
	}
	
	ksimulate(state, k = 1) {
		let count = 0
		while (k-- > 0)
		count += state.eval()
		return count
	}
	
	hash(board) {
		let tokens = []
		for (let sb of board.subboards)
		tokens.push( String(sb.board) )
		
		tokens.sort()
		tokens.push(board.locked)
		return String(tokens)
	}
	
	Q(state, sims) {
		let key = state.hash, entry = this.TT.get(key)
		if (entry == undefined) entry = [0, 0]
		
		const value = this.ksimulate(state, sims),
		new_entry = this.sum(entry, [value, sims])
		
		this.TT.set(key, new_entry)
		return new_entry[0] / new_entry[1]
	}
	
	magicformula(budget, move_count) {
		return Math.floor(budget / (move_count + Math.log2(move_count)))
	}

	assignQ(state, sims) {
		state.q = (2*state.player - 1) * this.Q(state, sims)
		return state
	}

	action(state, K = 200) {
		this.TT = new Map()
		let states = state.actions().map( a => this.node(state, a) )
		
		// SHOT loop
		while (states.length > 1) {
			const unit = this.magicformula(K, states.length),
			Q = s => (2*state.player - 1) * this.Q(s, unit)

			for (let s of states)
				s.q = Q(s, unit)
			
			
			// sequential halving
			K -= states.length * unit
			states.sort( (a, b) => a.q < b.q ? 1 : -1 )
			states.length = Math.ceil(states.length / 2)
		}
		return states.pop().action
	}
}

export function Agent() {
	return new SHOT()
}