board = require("./board")



class MCTS {

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
		return v.value/v.visits + this.exploration * Math.sqrt( (2*Math.log(p.visits)) / v.visits )
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
		let child = this.root.children.find( c => c.action.toString() == action.toString() )
		if (child == undefined) {
			console.error("failed to update " + action)
			console.error(this.root.children.map( c => c.action.toString() ))
		}
		else {
			this.root = child
			child.parent = null

			//console.error("new root of size " + child.visits)
			while (child.actionlist.length) {
				let v = this.expand(child)
				this.backpropagate(v, this.simulate(v))
			}
		}
	}

	action(K = 1000) {
		let player = 2*this.root.player - 1
		while (K--)
			this.iterate()
		
		let calc = v => player * v.value/v.visits
		return this.root.children.reduce( (a,b) => calc(a) > calc(b) ? a : b ).action
	}
}

let state = new board.Board()
let mcts = new MCTS(state)

// while (!state.terminal()) {
// 	state.str()
// 	let action = mcts.action()
// 	state = state.apply(action)
// }


function action2abs(action) {
	let [idx, [row, col]] = action
	return [ row + 3*~~(idx / 3), col + 3*(idx % 3) ]
}

console.log(action2abs([3, [1,1]]))