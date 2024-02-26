import {Engine, state, genotype, get, fuel, choice, pos, vector, speed, angle, addv} from "./engine.js";
import {CanvasScreen} from "./screen.js"
import * as genetics from "./genetics.js"
import {population, agent} from "./genetics.js"

const /* level specific stuff */
//surface1 = [0, 100, 1000, 500, 1500, 100, 3000, 100, 5000, 1500, 6999, 1000],
//spot1 = [1500, 3000],
// easy_right_surface = [0, 100, 1000, 500, 1500, 1500, 3000, 1000, 4000, 150, 5500, 150, 6999, 800],
// easy_right_spot = [4750, 150],
// easy_right_origin = [2500, 2700, 0, 0, 550, 0, 0] as state

wrong_side_surface = [0,  100, 1000,  500, 1500, 1500, 3000, 1000, 4000,  150, 5500,  150, 6999,  800],
wrong_side_spot = [4750, 150],
wrong_side_origin = [6500, 2800, -90, 0, 750, 90, 0] as state

// highground_surface = [
// 	0, 1000, 300, 1500, 350, 1400, 500, 2100, 1500, 2100,
// 	2000, 200, 2500, 500, 2900, 300, 3000, 200, 3200, 1000,
// 	3500, 500, 3800, 800, 4000, 200, 4200, 800, 4800, 600,
// 	5000, 1200, 5500, 900, 6000, 500, 6500, 300, 6999, 500
// ],
// highground_spot = [1000, 2100],
// highground_origin = [6500, 2700, -50, 0, 1000, 90, 0] as state


// cave_surface = [
// 	0, 1800,  300, 1200, 1000, 1550,
//  2000, 1200, 2500, 1650, 3700,  220,
//  4700,  220, 4750, 1000, 4700, 1650,
//  4000, 1700, 3700, 1600, 3750, 1900,
//  4000, 2100, 4900, 2050, 5100, 1000,
//  5500,  500, 6200,  800, 6999,  600
// ],
// cave_spot = [ 4200, 220 ] as [number, number],
// cave_origin = [6500, 2000, 0, 0, 1200, 0, 0] as state


function bounded_MSE(state : state, spot : [number, number], angle_coeff = 1, speed_coeff = 1) {
	const
	sq = (x : number) => Math.pow(x, 2),
	[x, y] = get(state, pos) as vector,
	[sx, sy] = spot,
	ang = Math.abs(get(state, angle) as number),
	[hs, vs] = get(state, speed) as vector,
	
	dist = sq(Math.max(Math.abs(x - sx) - 500, 0)) + sq(y - sy),
	bhs = Math.max(Math.abs(hs) - 20, 0),
	bvs = Math.max(Math.abs(vs) - 40, 0)
	
	return dist + angle_coeff * sq(ang) + speed_coeff * (sq(bhs) + sq(bvs))
}



class RHEA extends Engine {

	POPULATION : population

	constructor(surfaceN : Array<number>, spot : [number, number], origin : state) {
		super(surfaceN, spot, origin)	
		
		const
		POPULATION_SIZE = 500,
		HORIZON = 200

		this.POPULATION = []


		while (this.POPULATION.length < POPULATION_SIZE) {
			const genotype = []
			for (let j = 0; j < HORIZON / 2; j++)
				genotype.push( choice([-15, 0, 15]), 1 )
			this.POPULATION.push([genotype, Infinity])
		}
		this.evaluate(this.POPULATION)
	}

	evaluator(genotype : genotype) {
		let state : state
		for (let s of this.simulator(genotype))
			state = s

		if(this.succesful(state)) return -get(state, fuel)
		return bounded_MSE(state, SPOT)
	}

	evaluate(population : population) {
		for (let p of population) p[1] = this.evaluator(p[0])
	}

	step() {
		for(let a of this.POPULATION) { a[0].shift(); a[0].shift() }
	}

	best() {
		let b = [[], Infinity]
		for (let p of this.POPULATION)
			if (p[1] < b[1]) b = p
		return b as agent
	}

	crossover(a : agent, b : agent)  {
        const
		g = a[0], h = b[0],
		n = g.length, split = Math.random()

		const new_genotype = []
		for (let i = 0; i < n; i++) {
			new_genotype.push( Math.round(split*g[i] + (1 - split)*h[i]) )
		}
		return [new_genotype, Infinity]
	}

	next_generation() {
		const
		mutation = genetics.mutation.directed_uniform_multiple,
		selection = genetics.selection.kbest,
		N = Math.sqrt(this.POPULATION.length)


		const POPULATION = selection(this.POPULATION, N)
		
		const generation = []
		for (let a of POPULATION)
 			for (let b of POPULATION)
			 	if (a[1] != b[1]) generation.push( this.crossover(a, b) )
		
		while (generation.length < N) {
			const genotype = []
			for (let j = 0; j < 200; j++)
				genotype.push( choice([-15, 0, 15]), 1 )
			generation.push([genotype, Infinity])
		}
		
		for (let i = 0; i < generation.length; i++) generation[i] = mutation(generation[i], 0.1)
		this.evaluate(generation)
		return POPULATION.concat(generation)
	}


	draw_population(population : population) {
		const
		worst = 300,
		states = []
	
		let
		mean = 0,
		min = Infinity
	
		for (let agent of population) {
			const
			[trj, state] = this.trajectory(agent[0]),
			density = genetics.fitness_function.speed(state)/worst
			states.push(state)			

			let color = `rgb(${255 * density}, ${255 * (1 - density)}, 0)`
			if (this.succesful(state)) {SCREEN.polyline(trj, 'teal', 3);}
			else SCREEN.polyline(trj, color)
	
			mean += agent[1]
			min = Math.min(min, agent[1])
		}
	}

	run() {
		const START = performance.now()
		while(performance.now() - START < 90) {

			// canvas stuff
			SCREEN.clear(1)
			this.draw_population(this.POPULATION)
			
			this.POPULATION = this.next_generation()
		}

		this.evaluate(this.POPULATION)
		const a = this.best()
		let action = [0, 0]

		SCREEN.clear(0.8)
		this.draw_population([a])
		
		if (a[0].length) {
			action = [a[0][0], a[0][1]]
			this.step()
		}

		this.update_state(this.origin, action[0], action[1])
		this.evaluate(this.POPULATION)
		return action
	}
}

const
SURFACE = wrong_side_surface,
SPOT = wrong_side_spot as [number, number],
ORIGIN = wrong_side_origin,
rhea = new RHEA(SURFACE, SPOT, ORIGIN),
SCREEN = new CanvasScreen(rhea)

const wind = window as any
wind.play = () => { setInterval( () => rhea.run() , 500) }


// function collision(a : number, b : number, A : number, B :number, x : number, y :number) {
// 	const bounded = (x1 : number, p :number , x2 : number) => (x1 <= p && p <= x2) || (x1 >= p && p >= x2)
// 	return Math.abs((x - a)*(B - b) - (y - b)*(A - a)) <= 5000 && bounded(a, x, A)
// }

// function wall(X : Array<number>, Y : Array<number>, x : number, y : number) {
// 	const n = X.length
// 	for (let i = 1; i < n; i++) {
// 		const
// 		a = X[i-1], b = Y[i-1], // first point
// 		A = X[i],   B = Y[i]	  // second point
// 		if (collision(a, b, A, B, x, y)) return true
// 	}
// 	return false
// }


function collision(a : number, b : number, A : number, B :number, x : number, y :number) {
	
	return Math.sign((x - a)*(B - b) - (y - b)*(A - a))
}

function wall(X : Array<number>, Y : Array<number>, x : number, y : number) {
	const n = X.length

	for (let i = 1; i < n; i++) {

		const
		a = X[i-1], b = Y[i-1], // first point
		A = X[i],   B = Y[i]	  // second point
		if (collision(a, b, A, B, x, y)) return true
	}
	return false
}



function BFS(surface : Array<number>, spot : any) {

	spot = [spot[0], spot[1]]
	
	const 
	surfaceX = [], surfaceY = [],
	DIST = Array(7000),
	QUEUE = [[spot[0], spot[1]]]


	// function wall(x : number, y : number, X : number, Y : number) {
	// 	const bounded = (x1 : number, p :number , x2 : number) => (x1 <= p && p <= x2) || (x1 >= p && p >= x2)
	
	// 	for (let i = 1; i < surfaceX.length; i++) {
			
	// 		const
	// 		a = X[i-1], b = Y[i-1], // first point
	// 		A = X[i],   B = Y[i]	// second point

	// 		if( !(bounded(a, x, A) && bounded(a, X, A)) )
	// 			continue

	// 		if (collision(a, b, A, B, x, y) != collision(a, b, A, B, X, Y)) return true
	// 	}
	// 	return false 
	// }

	for (let i = 0; i < 7000; i++) DIST[i] = Array(3000)

	for (let i = 0; i < surface.length; i++)
		if (i % 2) surfaceY.push(surface[i])
		else surfaceX.push(surface[i])
	
	DIST[spot[0]][spot[1]] = 0
	
	function loop() {

		if(QUEUE.length == 0) return

		const
		q = QUEUE.shift() as vector,
		[x, y] = q,
		val = DIST[x][y]

		console.error(q)

		if (val == Infinity)
			SCREEN.box(q, 1, "red")
		else if (val == undefined)
			SCREEN.box(q, 1, "blue")
		else
			SCREEN.box(q, 1, "green")

		for (let i = -1; i <= 1; i++)
			for (let j = -1; j <= 1	; j++){
				const nx = x + i, ny = y + j
				console.log(nx, ny, DIST[nx][ny])
				if ((i == 0 || j == 0) && !(i == 0 && j == 0) && DIST[nx][ny] === undefined) {
					QUEUE.push([nx, ny]);
					DIST[nx][ny] = val + 1
				}

			}

				

		// const d = val + 1
		// for (let dir of directions) {
		// 	const
		// 	nq = addv(q, dir),
		// 	nval = DIST[nq[0]][nq[1]]
		// 	console.log(nq, nval)

		// 	if (nval == undefined) {
		// 		DIST[nq[0]][nq[1]] = d
		// 		if (0 <= nq[0] && nq[0] <= 7000 && 0 <= nq[1] && nq[1] <= 3000)
		// 			QUEUE.push(nq)
		// 	}
		// 	else if (nval != Infinity) DIST[nq[0]][nq[1]] = Math.min(nval, d)
		// }
		setTimeout(() => {loop()}, 100)
	}
	loop()
	return DIST
}


function intersect(Ax : number, Ay : number, Bx : number, By : number, Cx : number, Cy : number, Dx :number, Dy : number) {
	function ccw(Ax : number, Ay : number, Bx : number, By : number, Cx : number, Cy : number) {
		return (Cy - Ay) * (Bx - Ax) > (By - Ay) * (Cx - Ax)
	}
	return ccw(Ax, Ay, Cx, Cy, Dx, Dy) != ccw(Bx, By, Cx, Cy, Dx, Dy)
	&& ccw(Ax, Ay, Bx, By, Cx, Cy) != ccw(Ax, Ay, Bx, By, Dx, Dy);
}


function kamil(surface : Array<number>, spot : any) {
	const
	BOX_SIZE = 10,
	xL = 7000 / BOX_SIZE,
	yL = 3000 / BOX_SIZE,
	surfaceX = [], surfaceY = [],
	DIST = Array(xL).fill(Array(yL)),
	QUEUE = [ [spot[0] / BOX_SIZE, (spot[1] + 200)/ BOX_SIZE, 0] ]

	for (let i = 0; i < surface.length; i++)
		if (i % 2) surfaceY.push(surface[i])
		else surfaceX.push(surface[i])

	while (QUEUE.length) {
		const
		q = QUEUE.shift(),
		[x, y, val] = q
		console.log("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

		if (x < 0 || x >= xL || y < 0 || y >= yL || DIST[x][y] != undefined)
			continue
		
		let good = true
		for (let i = 1; i < surfaceX.length; i++) {
			const
			a = surfaceX[i-1], b = surfaceY[i-1], // first point
			A = surfaceX[i],   B = surfaceY[i],	  // second point
			realX = x * BOX_SIZE, realY = y * BOX_SIZE
			console.log(i)

			if(intersect(realX, realY, realX + BOX_SIZE, realY + BOX_SIZE, a, b, A, B)
			|| intersect(realX, realY  + BOX_SIZE, realX + BOX_SIZE, realY, a, b, A, B)
			|| intersect(realX, realY, realX, realY + BOX_SIZE, a, b, A, B)
			|| intersect(realX, realY, realX + BOX_SIZE, realY, a, b, A, B)
			|| intersect(realX + BOX_SIZE, realY + BOX_SIZE, realX, realY + BOX_SIZE, a, b, A, B)
			|| intersect(realX + BOX_SIZE, realY + BOX_SIZE, realX + BOX_SIZE, realY, a, b, A, B)) {
				DIST[x][y] = val + 1
				good = false
				break
			}
		}
		
		if (good) DIST[x][y] = val
		else continue
		console.log("bbbbbbbbbbbbbbbbbbbbbbbbb")

		for (let i = -1; i <= 1; i++)
			for (let z = -1; z <= 1; z++)
				if ((i == 0 || z == 0) && !(i == 0 && z == 0))
					QUEUE.push([x + i, y + z, val + BOX_SIZE]);
	}
	return DIST
}
