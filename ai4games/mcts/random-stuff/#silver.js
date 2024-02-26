
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

class MAST {

	constructor(dec = 0.1, epsilon = 0.8, size = 9) {
		this.epsilon = epsilon
		this.dec = dec
		this.values = [[], []]
		this.count = [[], []]
		for(let i = 0; i < size; i++) {
			this.values[0].push( new Array(size).fill(0) )
			this.values[1].push( new Array(size).fill(0) )
			this.count[0].push( new Array(size).fill(0) )
			this.count[1].push( new Array(size).fill(0) )
		}
	}

	random() {
		return Math.random() < this.epsilon
	}

	read(action, p) {
		let [i, j] = action2abs(action)
		return this.values[p][i][j]/this.count[p][i][j]
	}
	
	update(action, p, value) {
		let [i, j] = action2abs(action)
		this.values[p][i][j] += value
		this.count[p][i][j] += 1
	}

	best(actionlist, p) {
		return actionlist.reduce( (a, A) => this.read(a, p) > this.read(A, p) ? a : A )
	}

	decay() {
		if (this.dec == 1) return
		let size = this.values[0].length
		for (let i = 0; i < size; i++)
			for (let j = 0; j < size; j++) {
				this.values[0][i][j] *= this.dec
				this.count[0][i][j] *= this.dec
				this.values[1][i][j] *= this.dec
				this.count[1][i][j] *= this.dec
			}
	}
}

const mast = new MAST()

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
		|| new_board.match(DIGS[1], p) == 3){
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
		let state = this, playedActions = []
		while (!state.terminal()) {

			let action = null
			if (mast.random()) {
				action = choice(state.actions())
			} else {
				action = mast.best(state.actions(), state.player)
			}
			playedActions.push(action)
			state = state.apply(action)
		}

		let enm = state.player
		for (let action of playedActions) {
			enm %= 2
			mast.update(action, enm, Number(2*enm-1 == state.winner))
			enm += 1
		}

		if (state.winner)
			return state.winner
		else
			return 2*(POPCOUNT[state.board[0]] < POPCOUNT[state.board[1]]) - 1
	}

	decay() {
		mast.decay()
	}

}

class SHOT {
	
	constructor() {
		this.TT = new Map()
	}
	
	update(action) {}
	
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

	action(state, K = 1200) {
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
let mcts = new SHOT()
while(true) {
	let [opponent_row, opponent_col] = PARSE_INPUT()

	if (opponent_row != -1 && opponent_col != -1) {
		let action = abs2action(opponent_row, opponent_col)
		mcts.update(action)
		board = board.apply(action)
	}

	let action = mcts.action(board)
	board = board.apply(action)
	mcts.update(action)
	mast.decay()

	let [row, col] = action2abs(action)

	console.log(row + " " + col)
}