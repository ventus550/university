//import { Subboard, Board } from './board.mjs'

function shuffle(array) {
	let currentIndex = array.length,  randomIndex;
	// While there remain elements to shuffle...
	while (currentIndex != 0) {
		// Pick a remaining element...
		randomIndex = Math.floor(Math.random() * currentIndex);
		currentIndex--;
		// And swap it with the current element.
		[array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
	}
	return array;
}

class Node {

	constructor(state, parent, exploration = 1) {
		this.state = state
		this.results = 0
		this.visits = 0
		this.exploration = exploration

		this.parent = parent
		this.children = []
		this.actionlist = shuffle(state.actions())
	}

	ucb() {
		const c = this.exploration
		return this.results/this.visits + c * Math.sqrt( (2*Math.log(this.parent.visits)) / this.visits )
	}
}

export class MCTS {

	constructor(exploration = 1) {
		this.root = null
		this.exploration = exploration
	}

	action(state, K = 200) {

		this.root = new Node(state,null, this.exploration)
		this.player = state.player // 0 = x, 1 = o

		while (K--)
			this.search()

		return this.root.children.reduce( (a,b) => a.visits > b.visits ? a : b ).action		
	}

	search() {
		const selected = this.selection(this.root)
		const result = this.simulation(selected)
		this.backpropagation(selected, result)

	}

	selection(node) {
		while (!node.state.terminal()) {
			if (node.actionlist.length)
				return this.expansion(node)
			node = this.best_child(node.children)
		}
		return node
	}

	expansion(node) {
		let action = node.actionlist.pop(),
			child = new Node(node.state.apply(action), node, this.exploration)
		child.action = action
		node.children.push(child)
		return child
	}

	simulation(node) {
		const result = node.state.eval()
		return (2*this.player - 1) * result
	}

	backpropagation(node, result) {
		while (node != null) {
			node.visits += 1
			node.results += result
			node = node.parent
		}
	}

	best_child(children) {
		return children.reduce( (a,b) => a.ucb() > b.ucb() ? a : b )
	}
}

// export function Agent(exploration = 1) {
// 	return new MCTS()
// }


// let board = new Board()
// const mcts = new MCTS()

// board = board.apply(mcts.action(board))
//board = board.apply(mcts.action(board))


