import { Board } from './board.mjs'

export class MCTS {

	constructor(state, exploration = 1) {
		this.root = this.node(state, null)
		this.root.action = null
		this.exploration = exploration
	}

	node(state, parent) {
		Object.assign(state, {
			action: null,
			parent: parent,
			visits: 0,
			value: 0,
			actionlist: state.actions(),
			children: []
		})
		return state
	}

	uct(v, p) {
		// (2*this.root.player - 1) * 
		return v.value/v.visits + Math.sqrt( (2*Math.log(p.visits)) / v.visits )
	}

	bestChild(v) {
		let best = v.children[0], score = this.uct(best, v)
		for (let child of v.children) {
			let u = this.uct(child, v)
			if (u >= score) best = child
		}
		return best
	}

	select(v) {
		while (!v.terminal()) {
			if (v.actionlist.length)
				return this.expand(v)
			v = this.bestChild(v)
		}
		return v
	}

	expand(v) {
		let a = v.actionlist.pop(),
			child = this.node(v.apply(a), v)
		child.action = a
		v.children.push(child)
		return child
	}

	massexpand(v) {
		while (v.actionlist.length) {
			let child = this.expand(v)
			this.backpropagate(child, this.simulate(child))
		}
	}

	simulate(v) {
		return v.eval()
	}

	backpropagate(v, val) {
		while (v) {
			v.visits += 1
			v.value += val;
			v = v.parent
		}
	}

	iterate() {
		let v = this.select(this.root)
		let reward = this.simulate(v)
		this.backpropagate(v, reward)
	}

	update(action) {

		this.massexpand(this.root)
		let child = this.root.children.find( c => c.action.toString() == action.toString() )
		if (child == undefined) {
			console.error("failed to update " + action)
			console.error(this.root.children.map( c => c.action.toString() ))
			console.error(this.root.actionlist.map( c => c.toString() ))
		}
		else {
			this.root = child
			child.parent = null
		}
	}

	action(state, K = 1000) {
		let player = 2*this.root.player - 1
		while (K--)
			this.iterate()
		
		let calc = v => player * v.value/v.visits
		return this.root.children.reduce( (a,b) => calc(a) > calc(b) ? a : b ).action
	}
}

export function Agent(exploration = 1) {
	return new MCTS(new Board(), exploration)
}

// let game = new Board()
// let agent = Agent()
// console.log(agent.root.children)
// agent.massexpand(agent.root)
// console.log(agent.root.actionlist)