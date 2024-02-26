import {choice, abs2action, action2abs, popcount} from './utils.mjs'


let ROWS = [0b111000000, 0b000111000, 0b000000111],
COLS = [0b100100100, 0b010010010, 0b001001001],
DIGS = [0b100010001, 0b001010100]

let POPCOUNT = []
for (let i = 0; i <= 512; i++) POPCOUNT.push(popcount(i))

let VECT = []
for (let i = 8; i >= 0; i--) VECT.push(Math.pow(2,i))

class MAST {

	constructor(epsilon = 0.4, size = 9) {
		this.epsilon = epsilon
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

	decay(dec = 0.1) {
		if (dec == 1) return
		let size = this.values[0].length
		for (let i = 0; i < size; i++)
			for (let j = 0; j < size; j++) {
				this.values[0][i][j] *= dec
				this.count[0][i][j] *= dec
				this.values[1][i][j] *= dec
				this.count[1][i][j] *= dec
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

export class Board extends SubBoard {

	static epsilon = 0.8
		
	constructor(subboards, mast = new MAST()) {
		super()
		this.subboards = subboards
		if (subboards == undefined) {this.subboards = new Array(9).fill(new SubBoard())}
		this.player = 0 // x = 0, o = 1
		this.locked = null
		this.mast = mast
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
		this.mast = mast
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
			if (this.mast.random()) {
				action = choice(state.actions())
			} else {
				action = this.mast.best(state.actions(), state.player)
			}
			playedActions.push(action)
			state = state.apply(action)
		}

		let enm = state.player
		for (let action of playedActions) {
			enm %= 2
			this.mast.update(action, enm, Number(2*enm-1 == state.winner))
			enm += 1
		}

		if (state.winner)
			return state.winner
		else
			return 2*(POPCOUNT[state.board[0]] < POPCOUNT[state.board[1]]) - 1
	}

	decay(dec) {
		this.mast.decay(dec)
	}
}
