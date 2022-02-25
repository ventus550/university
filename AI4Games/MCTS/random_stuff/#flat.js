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
DIGS = [0b100010001, 0b001010100]

let POPCOUNT = []
for (let i = 0; i <= 512; i++) POPCOUNT.push(popcount(i))

let VECT = []
for (let i = 8; i >= 0; i--) { VECT.push(Math.pow(2,i)) }

class SubBoard {

	constructor() {
		this.board = [0b000000000, 0b000000000]
		this.isterminal = false
		this.winner = 0
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
		|| new_board.match(DIGS[1], p) == 3) {
			new_board.isterminal = true
			new_board.winner = 2*p - 1
		}

		if (POPCOUNT[new_board.board[0] | new_board.board[1]] == 9)
			new_board.isterminal = true

		return new_board
	}

	terminal() {
		return this.isterminal
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

		if (new_subboard.winner == 0) {
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
		if (state.winner)
			return state.winner
		else
			return 2*(POPCOUNT[state.board[0]] < POPCOUNT[state.board[1]]) - 1
	}
}

class FlatMC {
	action(state, K = 1000) {
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
let	 board = new Board()
let mcts = new FlatMC()
while(true) {
	let [opponent_row, opponent_col] = PARSE_INPUT()

	if (opponent_row != -1 && opponent_col != -1) {
		let action = abs2action(opponent_row, opponent_col)
		board = board.apply(action)
	}

	let action = mcts.action(board)
	board = board.apply(action)

	let [row, col] = action2abs(action)

	console.log(row + " " + col)
}