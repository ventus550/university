

/*-------- utils --------*/
type vector = [number, number]
type genotype = Array<number>

function addv(v : vector, u : vector) : vector {
	return [ v[0] + u[0], v[1] + u[1] ]
}

function randint(a : number, b : number) {
	const n = b - a + 1
	return ~~(Math.random() * n) + a
}

function bounds(val : number, low : number, high : number) {
	const
	ltest = Number(val < low),
	htest = Number(val > high),
	vtest = Number(ltest + htest == 0)

	return ltest * low + htest * high + vtest * val
}


/*-------- engine --------*/
type state = [
	// X, Y
	number, number,
	// HS, VS
	number, number,
	// fuel, angle, thrust
	number, number, number
]

// constants and access codes
const DEFAULT_STATE : state = [0,0,0,0,0,0,0],
	  gravity_acceleration = -3.711,
	  pos = 0, speed = 2,
	  fuel = 4, angle = 5, thrust = 6

function set(state : state, field : number, val : vector | number) {
	if (typeof val == "number") {state[field] = val}
	else if (field < 2) { state[0] = val[0]; state[1] = val[1] }
	else { state[2] = val[0]; state[3] = val[1] }
}

function get(state : state, field : number) : vector | number {
	if (field < 2) { return [state[0], state[1]] }
	else if (field < 4) { return [state[2], state[3]] }
	else { return state[field] }
}

function update(state : state, set_angle : number, set_thrust : number) {

	const
	ang = get(state, angle) as number,
	thrst = get(state, thrust) as number,
	fl = get(state, fuel) as number,
	spd = get(state, speed) as vector,
	position = get(state, pos) as vector

	if (fl <= 0) set_thrust = -4

	const
	new_ang = bounds(ang + set_angle, -90.0, 90.0),
	new_thrst = bounds(thrst + set_thrust, 0, 4),
	arcAngle = -new_ang * Math.PI / 180.0,
	acc = [Math.sin(arcAngle) * new_thrst, Math.cos(arcAngle) * new_thrst + gravity_acceleration] as vector,
	new_spd = addv(spd, acc),
	new_pos = addv(position, addv(new_spd, [-acc[0] * 0.5, -acc[1] * 0.5]))

	set(state, pos, new_pos)
	set(state, fuel, fl - new_thrst)
	set(state, angle, new_ang)
	set(state, thrust, new_thrst)
	set(state, speed, new_spd)
}


function collision(a : number, b : number, A : number, B :number, x : number, y :number) {
	const bounded = (x1 : number, p :number , x2 : number) => (x1 <= p && p <= x2) || (x1 >= p && p >= x2)
	return (x - a)*(B - b) - (y - b)*(A - a) >= 0 && bounded(a, x, A)
}



class Engine {

	surfaceX : Array<number>
	surfaceY : Array<number>
	surface  : Array<number>
	spot  	 : Array<number>
	origin   : state	 

	constructor(surfaceN : Array<number>, spot : [number, number], origin : state = DEFAULT_STATE) {
		this.surface = surfaceN
		this.origin = origin
		this.spot = spot
		this.surfaceX = []; this.surfaceY = []
		for (let i = 0; i < surfaceN.length; i++)
			if (i % 2)
				this.surfaceY.push(surfaceN[i])
			else
				this.surfaceX.push(surfaceN[i])
	}

	make_state() : state { return [...this.origin] }

	succesful(state : state) {
		const x = (get(state, pos) as vector)[0]

		return Math.abs(get(state, speed)[0]) <= 20
		&& Math.abs(get(state, speed)[1]) <= 40
		&& Math.abs(get(state, angle) as number) == 0
		&& this.spot[0] - 500 <= x
		&& this.spot[0] + 500 >= x
	}

	terminal(state : state) {
		const X = this.surfaceX, Y = this.surfaceY, n = X.length,
			  [x, y] = get(state, pos) as vector

		for (let i = 1; i < n; i++) {
			const a = X[i-1], b = Y[i-1], // first point
				  A = X[i],   B = Y[i]	  // second point
			// run geometry test (który nie działa dla pionwych prostych btw)
			if (collision(a, b, A, B, x, y)) return true
		}
		return false
	}

	update_state(state : state, angle : number, thrust : number) {
		if (this.terminal(state)) return false
		update(state, angle, thrust)
		return true
	}


	*simulator(genotype : genotype) {
		console.assert(genotype.length % 2 == 0, "corrupted genotype " + genotype.length)
		const state = this.make_state()

		for (let i = 0; i < genotype.length; i+=2)
			if (this.update_state(state, genotype[i], genotype[i+1])) yield state
			else break
		yield state
	}

	trajectory(genotype : genotype) : [Array<number>, state] {
		const res = [ ...get(this.origin, pos) as vector ]; 
		let state : state
		for (let s of this.simulator(genotype)) {
			state = s
			res.push( ...get(s, pos) as vector )
		}

		return [res, state]
	}
}


// Canvas
export class CanvasScreen {

	engine   : Engine
	surface  : Array<number>
	canvas   : HTMLCanvasElement
	ctx		 : CanvasRenderingContext2D

	constructor(engine : Engine) {
		this.surface = engine.surface
		this.engine = engine
		this.canvas = document.createElement("canvas")
		document.body.appendChild(this.canvas)
		this.canvas.width = window.innerWidth
		this.canvas.height = window.innerHeight
		this.canvas.style.backgroundColor = 'black'
		this.canvas.style.position = 'absolute'
		this.ctx = this.canvas.getContext("2d")
		this.ctx.transform(1, 0, 0, -1, 0, this.canvas.height)
		this.clear()
	}
	
	polyline(coords : Array<number>, color = 'red', width = 0.5) {
		this.ctx.lineWidth = width;
		const X = [], Y = [], ctx = this.ctx,
			  scaleX = this.canvas.width / 7000,
			  scaleY = this.canvas.height / 3000 

		for (let i = 0; i < coords.length; i++)
			if (i % 2) Y.push(coords[i] * scaleY)
			else X.push(coords[i] * scaleX)
		
		ctx.strokeStyle = color;
		
		ctx.beginPath();
		for (let i = 0; i < X.length; i++) ctx.lineTo(X[i], Y[i]);
		ctx.stroke();
	}

	clear(opacity = 0.5) {
		this.ctx.fillStyle = 'rgba(0,0,0,' + opacity + ')'
		this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
		this.polyline(this.surface)
	}
}


// Genetics
type agent = [genotype, number]
type population = Array<agent>

function make_agent(genotype : genotype, evalf : Function) : agent { return [genotype, evalf(genotype)] }


function kamilfit(state : state, spot : [number,number]) {
	let speedVertical = Math.abs(state[3])
	speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
	let speedHorizontal = Math.abs(state[2]);
	speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
	//angle
	let angle = state[5];
	angle *= angle;
	//dist
	let dist = Math.pow(spot[0] - state[0], 2) + Math.pow(spot[1] - state[1], 2);

	return (dist + 3000 * angle + 3000 * Math.pow(speedHorizontal + speedVertical, 2))
}

function full_random(population : population, genotype_eval_function : Function, size : number, horizon : number) {
	while (population.length < size) {
		const genotype = []
		for (let j = 0; j < horizon / 2; j++)
			genotype.push( randint(-15, 15), randint(-1,1) )
		population.push(make_agent(genotype, genotype_eval_function))
	}
	return population
}

function kbest(population : population, k : number) {
	population.sort( (a, b) => a[1] - b[1] )
	population.length = Math.round(k)
	return population
}

function continuous2(a : agent, b : agent, genotype_eval_function : Function) {
	const
	g = a[0], h = b[0],
	n = g.length, split = Math.random()

	const new_genotype = [], new_genotype2 = []
	for (let i = 0; i < n; i++) {
		new_genotype.push( Math.round(split*g[i] + (1 - split)*h[i]) )
		new_genotype2.push( Math.round(split*h[i] + (1 - split)*g[i]) )
	}
	return [make_agent(new_genotype, genotype_eval_function), make_agent(new_genotype2, genotype_eval_function)]
}

function uniform_multiple(agent : agent, chance : number = 0.01) {
	const genotype = agent[0]
	for (let i = 0; i < genotype.length; i++)
		if (Math.random() <= chance)
			if (i % 2) genotype[i] = randint(-1, 1)
			else genotype[i] = randint(-15,15)
	return agent
}

function fspeed(state : state) {
	const [hs, vs] = get(state, speed) as vector

	return Math.abs(hs) + Math.abs(vs)
}

// Main

const
SURFACE = [0, 100, 1000, 500, 1500, 1500, 3000, 1000, 4000, 150, 5500, 150, 6999, 800],
SPOT = [4750, 150] as [number, number],
ORIGIN = [2500, 2700, 0, 0, 550, 0, 0] as state,
ENGINE = new Engine(SURFACE, SPOT, ORIGIN),
SCREEN = new CanvasScreen(ENGINE)


function draw_population(population : population) {
	const
	worst = 300,
	states = []

	let
	mean = 0,
	min = Infinity

	for (let agent of population) {
		const
		[trj, state] = ENGINE.trajectory(agent[0]),
		density = fspeed(state)/worst
		states.push(state)
		//console.log(get(state, pos))
		
		let color = `rgb(${255 * density}, ${255 * (1 - density)}, 0)`
		if (ENGINE.succesful(state)) {SCREEN.polyline(trj, 'teal', 3); console.log(JSON.stringify(agent[0])); alert()}
		else SCREEN.polyline(trj, color)

		mean += agent[1]
		min = Math.min(min, agent[1])
	}
	console.log(mean, min)
}

function standard_evaluator(fitf : Function) {
	return (genotype : genotype) => {
		let state : state
		for (let s of ENGINE.simulator(genotype))
			state = s

		if(ENGINE.succesful(state)) return -get(state, fuel)
		return fitf(state, SPOT)
	}
}

function kamil() {
	const
	fitness = kamilfit,
	init = full_random,
	selection = kbest,
	crossover = continuous2,
	mutation = uniform_multiple,
	evaluator = standard_evaluator( (state : state, spot : [number, number]) => fitness(state,spot) ),
	POPULATION_SIZE = 500, HORIZON = 200


	/*----- main ----- */
	let POPULATION = init([], evaluator, POPULATION_SIZE, HORIZON)
	draw_population(POPULATION)

	function next_generation() {
		SCREEN.clear(1)
		POPULATION = selection(POPULATION, POPULATION_SIZE * 0.5)
		
		const generation = []
		for(let i = 1; i < POPULATION.length; i+=2) {
			const
			parent1 = POPULATION[i],
			parent2 = POPULATION[i-1]

			generation.push( ...crossover(parent1, parent2, evaluator) )
		}
		for (let i = 0; i < generation.length; i++) generation[i] = mutation(generation[i], 0.01)
		
		POPULATION = POPULATION.concat(generation)
		draw_population(POPULATION)
	}


	return next_generation
}


const gen = kamil()
for(let i = 0; i < 10; i++) gen()

