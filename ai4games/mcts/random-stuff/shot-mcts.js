
function PARSE_INPUT() {
	var inputs = readline().split(' ');
    const opponentRow = parseInt(inputs[0]);
    const opponentCol = parseInt(inputs[1]);
    const validActionCount = parseInt(readline());
    for (let i = 0; i < validActionCount; i++) {
        var inputs = readline().split(' ');
        const row = parseInt(inputs[0]);
        const col = parseInt(inputs[1]);
    }
	return [opponentRow, opponentCol]
}

function randint(a,b) {
	let n = b - a + 1
	return ~~(Math.random() * n) + a
}

function choice(arr) {
	 let n = arr.length
	 return arr[randint(0, n-1)]
}

function popcount(n) {
	n = n - ((n >> 1) & 0x55555555)
	n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
	return ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24
}

function err(msg) {
	console.error(msg)
}

let ROWS = [0b111000000, 0b000111000, 0b000000111],
COLS = [0b100100100, 0b010010010, 0b001001001],
DIGS = [0b100010001, 0b001010100],
ALL = ROWS.concat(COLS).concat(DIGS),
POPCOUNT = []
for (let i = 0; i <= 512; i++) POPCOUNT.push(popcount(i))

let VECT = []
for (let i = 8; i >= 0; i--) VECT.push(Math.pow(2,i))

class SubBoard {

	constructor() {
		this.board = [0b000000000, 0b000000000]
		this.isterminal = false
		this.winner = null
	}

	get(xyp) {
		let [x, y, p] = xyp; let v = VECT[3*x + y]
		return Number((v & this.board[p]) != 0)
	}

	set(x, y, p) {
		let v = VECT[3*x + y]
		this.board[p] |= v
	}

	str() {
		return (this.board[0] | this.board[1]).toString(2)
	}

	match(pattern, p) {
		return POPCOUNT[this.board[p] & pattern]
	}

	actions() {
		let board = this.board[0] | this.board[1]
		let res = []
		for (let i = 0; i < VECT.length; i++) {
			let v = VECT[i]
			if ((v & board) == 0) res.push( [~~(i / 3), i % 3] )
		}
		return res
	}

	perform_action(action, p) {
		let [i, j] = action
		let new_board = new SubBoard()
		new_board.board = [...this.board]
		new_board.set(i, j, p)
		
		if(new_board.match(ROWS[i], p) == 3
		|| new_board.match(COLS[j], p) == 3
		|| new_board.match(DIGS[0], p) == 3
		|| new_board.match(DIGS[1], p) == 3
		|| POPCOUNT[new_board.board[0] | new_board.board[1]] == 9) {
			new_board.isterminal = true
			new_board.winner = p
		}
		return new_board
	}

	terminal() {
		return this.isterminal
	}

	eval() {
		let state = this
		while (!state.terminal()) {
			state = state.perform_action(choice(state.actions()), Number(POPCOUNT[state.board[0]] != POPCOUNT[state.board[1]]))
		}
		return state.winner
	}
}

class Board extends SubBoard {

	constructor(subboards) {
		super()

		this.subboards = subboards
		if (!subboards) {this.subboards = new Array(9).fill(new SubBoard())}
		this.player = 0 // x = 0, o = 1
		this.locked = null
	}

	str() {
		let strr = ""
		let sbs = this.subboards
		for (let row = 0; row < 9; row++) {
			let r = row % 3

			if (r == 0)
				strr += "\n\n"
			else
				strr += "\n"

			for (let col = 0; col < 9; col++) {
				let idx = 3*~~(row / 3) + ~~(col / 3)
				let c = col % 3
				if (c == 0)
					strr += " "

				if (sbs[idx].get([r, c, 0]))
					strr += "X"
				else {
					if (sbs[idx].get([r, c, 1]))
						strr += "O"
					else { strr += "_" }
				}
			}
		}
		console.log(strr)
	}

	actions() {
		let board = this.board[0] | this.board[1]
		if (this.locked != null && !this.subboards[this.locked].terminal()) {
			let actions = this.subboards[this.locked].actions()
			if (actions.length != 0) {
				let res = []
				for ( let a of actions ) res.push( [this.locked, a] )
				return res
			}
		}

		let res = []
		for ( let i = 0; i < VECT.length; i++ ) {
			let v = VECT[i]
			if ((v & board) == 0)
				for ( let action of this.subboards[i].actions() ) {
					res.push([i, action])
				}
		}
		return res
	}

	copy_from(other) {
		this.board = [...other.board]
		this.isterminal = other.isterminal
		this.winner = other.winner
	}

	apply(action) {
		let [idx, subaction] = action
		let [i, j] = subaction

		let new_board = new Board([...this.subboards])
		new_board.player = Number(!this.player)
		new_board.locked = 3*i + j

		let new_subboard = this.subboards[idx].perform_action(subaction, this.player)
		new_board.subboards[idx] = new_subboard

		if (new_subboard.winner == null) {
			new_board.copy_from(this)
			return new_board
		}

		let binboard = this.perform_action( [~~(idx / 3), idx % 3], this.player)
		new_board.copy_from(binboard)
		return new_board
	}

	terminal() { return this.subboards.every( x => x.isterminal )}

	eval() {
		let state = this
		while (!state.terminal()) {
			let ch = choice(state.actions())
			state = state.apply(ch)
		}
		return 2*state.winner - 1
	}

}

class MCTS {

	constructor(state) {
		this.root = this.node(state, null)
		this.root.action = null
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

	expand(v) {
		let a = v.actionlist.pop()
		while (a) {
			let child = this.node(v.apply(a), v)
			child.action = a
			v.children.push(child)
			a = v.actionlist.pop()
		}
		return v
	}

	simulate(v, count=1) {
		let val = 0
		while(count--)
			val += v.eval()
		return val
	}

	magicformula(movecount, budget) {
		return budget / (movecount*Math.log2(movecount))
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
			this.expand(child)
		}
	}

	action(budget = 1000) {
		let player = 2*this.root.player - 1,
			states = this.expand(this.root).children,
			calc = v => player * v.value/v.visits

		while (states.length > 1) {
			let simulations = Math.floor(this.magicformula(states.length, budget))
			budget -= simulations * states.length

			for (let state of states) {
				state.value += this.simulate(state, simulations)
				state.visits += simulations
			}

			states.length = Math.floor(states.length / 2)
			states.sort( (a, b) => (calc(a) < calc(b)) ? 1 : -1 )
		}
		return states[0].action
	}
}


function abs2action(row, col) {
	let idx = 3*~~(row / 3) + ~~(col / 3)
	row %= 3; col %= 3
	return [idx, [row, col]]
}


function action2abs(action) {
	let [idx, [row, col]] = action
	return [ row + 3*~~(idx / 3), col + 3*(idx % 3) ]
}


// game loop
let mcts = new MCTS(new Board(), 10)
//mcts.action(1000)
while(true) {
	let [opponent_row, opponent_col] = PARSE_INPUT()

	if (opponent_row != -1 && opponent_col != -1) {
		let action = abs2action(opponent_row, opponent_col)
		mcts.update(action)
	}

	let action = mcts.action(2500)
	mcts.update(action)

	let [row, col] = action2abs(action)

	console.log(row + " " + col)
}