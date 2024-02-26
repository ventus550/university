import { Board } from './board.mjs'
import { Agent as RANDOM_AGENT } from './random-agent.mjs'
import { Agent as MAST_MCTS_AGENT } from './mast-mcts.mjs'
import { Agent as PURE_MCTS_AGENT } from './pure-mcts.mjs'
import { Agent as FLAT_MC_AGENT } from './flat-mc.mjs'
import { Agent as SHOT } from './shot.mjs'
import { Agent as MAST_SHOT } from './mast-shot.mjs'



function play(A1, A2, verbose = false) {
	let game = new Board()
	let turn = 0
	while ( !game.terminal() ) {
		let action = null
		if (turn == 0)
			action = A1.action(game)
		else
			action = A2.action(game)
		
		game = game.apply(action)
		
		if (verbose)
			game.str()
		turn = Number(!turn)
	}
	return game.winner
}

function test(A1, A2, k = 1000) {
	let count = 0
	while(k--)
		count += play(A1, A2)
	return countcle
}

// test exploration
for (let i = 0; i <= 0; i+=0.1) {
	let count = { '-1': 0, '0': 0, '1': 0 }
	for (let k = 0; k < 100; k++) {
		let res = play(MAST_SHOT(0.1, 0.8), FLAT_MC_AGENT(), false)
		console.log(res)
		count[res] += 1
	}
	//console.log( i + " {" + count[-1] + " " + count[0] + " " + count[1] + "}")
	console.log( i + " " + count[-1] / (count[-1] + count[1]) )
}

// test MAST MCTS
// console.log(play(MAST_MCTS_AGENT(1, 0.4, 0.5), RANDOM_AGENT()))