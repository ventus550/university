import {Engine, state, genotype, get, fuel} from "./engine.js";
import {CanvasScreen} from "./screen.js"
import * as genetics from "./genetics.js"
import {population} from "./genetics.js"

const /* level specific stuff */
//surface1 = [0, 100, 1000, 500, 1500, 100, 3000, 100, 5000, 1500, 6999, 1000],
//spot1 = [1500, 3000],
// easy_right_surface = [0, 100, 1000, 500, 1500, 1500, 3000, 1000, 4000, 150, 5500, 150, 6999, 800],
// easy_right_spot = [4750, 150],
// easy_right_origin = [2500, 2700, 0, 0, 550, 0, 0] as state

highground_surface = [
	0, 1000, 300, 1500, 350, 1400, 500, 2100, 1500, 2100,
	2000, 200, 2500, 500, 2900, 300, 3000, 200, 3200, 1000,
	3500, 500, 3800, 800, 4000, 200, 4200, 800, 4800, 600,
	5000, 1200, 5500, 900, 6000, 500, 6500, 300, 6999, 500
],
highground_spot = [1500, 2100],
highground_origin = [6500, 2700, -50, 0, 1000, 90, 0] as state

const
SURFACE = highground_surface,
SPOT = highground_spot as [number, number],
ORIGIN = highground_origin,
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
		density = genetics.fitness_function.speed(state)/worst
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

// BASE -- nie dotykać!1
// function base() {
// 	const fitness = genetics.fitness_function.bounded_MSE,
// 		  init = genetics.initialization.full_random,
// 		  selection = genetics.selection.roulette,
// 		  crossover = genetics.crossover.continuous2,
// 		  mutation = genetics.mutation.biased_uniform_multiple,
// 		  POPULATION_SIZE = 500, HORIZON = 300

	
// 	function evaluate(genotype : genotype) {
// 		let state : state
// 		for (let s of ENGINE.simulator(genotype))
// 			state = s
// 		return fitness(state, SPOT, 100, 100)
// 	}

// 	/*----- main ----- */
// 	let POPULATION = init([], evaluate, POPULATION_SIZE, HORIZON)
// 	draw_population(POPULATION)

// 	function next_generation() {
// 		SCREEN.clear(1)
// 		POPULATION = selection(POPULATION, POPULATION_SIZE * 0.5)
		
// 		const generation = []
// 		while (generation.length < POPULATION.length) {
// 			for(let i = 1; i < POPULATION.length; i++) {
// 				const parent1 = POPULATION[i]
// 				let parent2 = POPULATION[i-1]
// 				while (parent1[1] == parent2[1]) {parent2 = choice(POPULATION)}

// 				generation.push( ...crossover(parent1, parent2, evaluate) )
// 			}
// 		}

// 		for (let i = 0; i < generation.length; i++) generation[i] = mutation(generation[i], 0.01)
		
// 		POPULATION = generation
// 		draw_population(POPULATION)
// 		console.log(POPULATION.length)
// 	}

// 	return next_generation
// }


// function model1() {
// 	const fitness = genetics.fitness_function.generic,
// 		  init = genetics.initialization.full_random,
// 		  selection = genetics.selection.kbest,
// 		  crossover = genetics.crossover.single_split1,
// 		  mutation = genetics.mutation.single_random,
// 		  POPULATION_SIZE = 200, HORIZON = 200

	
// 	function evaluate(genotype : genotype) {
// 		let state : state
// 		for (let s of ENGINE.simulator(genotype))
// 			state = s
// 		return fitness(state, SPOT, 100, 100)
// 	}

// 	/*----- main ----- */
// 	let POPULATION = init([], evaluate, POPULATION_SIZE, HORIZON)

// 	function next_generation() {
// 		SCREEN.clear(1)
// 		draw_population(POPULATION, fitness)
// 		POPULATION = selection(POPULATION, Math.sqrt(POPULATION_SIZE))
		
// 		const generation = []
// 		for (let a of POPULATION)
// 			for (let b of POPULATION)
// 				generation.push( crossover(a, b, evaluate) )
	
// 		for (let a of generation) mutation(a)
	
// 		POPULATION = generation
// 	}

// 	return next_generation
// }


// function model2() {
// 	const fitness = genetics.fitness_function.generic,
// 		  init = genetics.initialization.full_spread,
// 		  selection = genetics.selection.roulette,
// 		  crossover = genetics.crossover.continuous1,
// 		  mutation = genetics.mutation.uniform_multiple,
// 		  POPULATION_SIZE = 200, HORIZON = 300

	
// 	function evaluate(genotype : genotype) {
// 		let state : state
// 		for (let s of ENGINE.simulator(genotype))
// 			state = s
// 		return fitness(state, SPOT, 20, 20)
// 	}

// 	/*----- main ----- */
// 	let POPULATION = init([], evaluate, POPULATION_SIZE, HORIZON)
// 	draw_population(POPULATION)

// 	function next_generation() {
// 		SCREEN.clear(1)
// 		POPULATION = selection(POPULATION, Math.sqrt(POPULATION_SIZE))
		
// 		const generation = []
// 		for (let a of POPULATION)
// 			for (let b of POPULATION)
// 				generation.push( crossover(a, b, evaluate) )
			
// 		for (let a of generation) mutation(a)
		
// 		POPULATION = generation
// 		draw_population(POPULATION)
// 	}

// 	return next_generation
// }



// function model4() {
// 	const fitness = genetics.fitness_function.bounded_MSE,
// 		  init = genetics.initialization.full_spread,
// 		  selection = genetics.selection.diverse,
// 		  eliselect = genetics.selection.kbest,
// 		  crossover = genetics.crossover.continuous1,
// 		  mutation = genetics.mutation.uniform_multiple,
// 		  POPULATION_SIZE = 500, HORIZON = 300

	
// 	function evaluate(genotype : genotype) {
// 		let state : state
// 		for (let s of ENGINE.simulator(genotype))
// 			state = s
// 		return fitness(state, SPOT, 20, 20)
// 	}

// 	/*----- main ----- */
// 	let POPULATION = init([], evaluate, POPULATION_SIZE, HORIZON),
// 		ELITES = []
// 	draw_population(POPULATION)

// 	function next_generation() {
// 		SCREEN.clear(1)
// 		ELITES = []
// 		POPULATION = selection(POPULATION, Math.sqrt(POPULATION_SIZE) * 0.5).concat(eliselect([...POPULATION], Math.sqrt(POPULATION_SIZE) * 0.5))
// 		//POPULATION.concat(ELITES)
// 		alert(POPULATION.length + " " + ELITES.length + " " + POPULATION.concat(ELITES).length)
		
// 		const generation = []
// 		for (let a of POPULATION)
// 			for (let b of POPULATION)
// 				generation.push( crossover(a, b, evaluate) )
			
// 		for (let a of generation) mutation(a)
		
// 		POPULATION = generation
// 		draw_population(POPULATION)
// 	}

// 	return next_generation
// }

// function model5() {
// 	const fitness = genetics.fitness_function.bounded_MSE,
// 		  init = genetics.initialization.full_random, // random > spread ??
// 		  selection = genetics.selection.kbest, // roulette > kbest
// 		  crossover = genetics.crossover.continuous1, // there seems to be no difference between double offspring and sqrt
// 		  mutation = genetics.mutation.biased_uniform_multiple, // only a slight improvement
// 		  evaluator = standard_evaluator( (state : state, spot : [number, number]) => fitness(state,spot, 100, 100) ),
// 		  POPULATION_SIZE = 100, HORIZON = 300 // the larger the horizon the better?

	
// 	/*----- main ----- */
// 	let POPULATION = init([], evaluator, POPULATION_SIZE, HORIZON)
// 	draw_population(POPULATION)

// 	function next_generation() {
// 		SCREEN.clear(1)
// 		POPULATION = selection(POPULATION, Math.sqrt(POPULATION_SIZE))
		
// 		const generation = []
// 		for (let a of POPULATION)
// 			for (let b of POPULATION)
// 				generation.push( crossover(a, b, evaluator) )

// 		for (let i = 0; i < generation.length; i++) generation[i] = mutation(generation[i], 0.05)
		
// 		POPULATION = generation
// 		draw_population(POPULATION)
// 	}
// 	console.log("best",best(POPULATION))
// 	return next_generation
// }


function kamil() {
	const
	fitness = genetics.fitness_function.kamilfit,
	init = genetics.initialization.full_spread,
	selection = genetics.selection.kbest,
	crossover = genetics.crossover.continuous2,
	mutation = genetics.mutation.uniform_multiple,
	evaluator = standard_evaluator( (state : state, spot : [number, number]) => fitness(state,spot, 10000, 100) ),
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



const wind = window as any
wind.next = kamil()
wind.play = () => { setInterval(wind.next, 500) }


// const A = [
// 	[-8,0,-4,0,-4,0,1,0,0,0,1,0,4,1,-5,1,-2,1,-2,0,-1,0,-6,0,2,1,-3,1,2,0,-4,0,1,0,2,0,2,1,-1,0,1,0,5,0,1,0,2,0,2,-1,2,1,6,0,-1,0,-1,1,0,0,-1,0,-3,0,0,1,5,0,3,0,1,0,1,0,2,0,-2,1,5,0,-2,0,0,0,1,0,2,0,3,0,-2,0,2,0,2,0,3,0,-6,0,1,-1,-5,0,-2,0,-4,-1,5,0,0,0,-1,1,2,0,2,0,-1,1,-1,0,0,0,4,0,-1,0,4,0,-2,0,4,0,-5,0,2,1,0,0,2,1,0,0,-2,0,-2,0,-4,0,0,0,-1,0,-1,0,-4,0,5,1,1,0,-1,0,-7,-1,2,0,1,0,3,0,4,0,-4,0,3,1,-2,0,0,0,0,-1,1,0,-3,1,-6,0,-2,0,2,0,1,0,3,0,0,0],
// 	0
// ]

// draw_population([A as any])