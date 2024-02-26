import {state, vector, genotype, get, pos, angle, randint, choice,speed} from "./engine.js";

type agent = [genotype, number]
type population = Array<agent>

function make_agent(genotype : genotype, evalf : Function) : agent { return [genotype, evalf(genotype)] }

function vdiff(v : genotype, u : genotype) {
	let diff = 0
	for (let i = 0; i < v.length; i++)
		diff += Math.abs(v[i] - u[i])
	return diff
}


// the closer to 0 the better!
const fitness_function : any = {

	generic: (state : state, spot : [number, number], angle_coeff = 1, speed_coeff = 1) => {
		const
		sq = (x : number) => Math.pow(x, 2),
		[x, y] = get(state, pos) as vector,
		[sx, sy] = spot,
		dist = sq(x - sx) + sq(y - sy),
		ang = Math.abs(get(state, angle) as number),
		[hs, vs] = get(state, speed) as vector

		return Math.sqrt(dist) + angle_coeff*ang + speed_coeff * (Math.abs(hs) + Math.abs(vs))
	},

	bounded_MSE: (state : state, spot : [number, number], angle_coeff = 1, speed_coeff = 1) => {
		const
		sq = (x : number) => Math.pow(x, 2),
		[x, y] = get(state, pos) as vector,
		[sx, sy] = spot,
		dist = sq(Math.max(Math.abs(x - sx) - 400, 0)) + sq(y - sy),
		ang = Math.abs(get(state, angle) as number),
		[hs, vs] = get(state, speed) as vector,

		bhs = Math.max(Math.abs(hs) - 20, 0),
		bvs = Math.max(Math.abs(vs) - 40, 0)
		
		return dist + angle_coeff * sq(ang) + speed_coeff * (sq(bhs) + sq(bvs))
	},

	speed: (state : state) => {
		const [hs, vs] = get(state, speed) as vector

		return Math.abs(hs) + Math.abs(vs)
	},

	kamilfit: (state : state, spot : [number,number]) => {
		let speedVertical = Math.abs(state[3])
		speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
		let speedHorizontal = Math.abs(state[2]);
		speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
		//angle
		let angle = state[5];
		angle *= angle;
		//dist
		let dist = Math.pow(spot[0] - state[0], 2) + Math.pow(spot[1] - state[1], 2);

		return (dist + 1 * angle + 1 * Math.pow(speedHorizontal + speedVertical, 2))
	}


}

const initialization : any = {
	full_random: (population : population, genotype_eval_function : Function, size : number, horizon : number) => {
		while (population.length < size) {
			const genotype = []
			for (let j = 0; j < horizon / 2; j++)
				genotype.push( randint(-15, 15), randint(-1,1) )
			population.push(make_agent(genotype, genotype_eval_function))
		}
		return population
	},


	full_spread: (population : population, genotype_eval_function : Function, size : number, horizon : number) => {
		while (population.length < size) {
			const genotype = []
			for (let j = 0; j < horizon / 2; j++)
				genotype.push( choice([-15, 0, 15]), 1 )
			population.push(make_agent(genotype, genotype_eval_function))
		}
		return population
	}


}

const selection : any = {
	kbest: (population : population, k : number) => {
		population.sort( (a, b) => a[1] - b[1] )
		population.length = Math.round(k)
		return population
	},

	roulette: (population : population, k : number) => {
		k = Math.round(k)

		population = population.sort( (a : agent, b : agent) => a[1] - b[1] )

		const 
		table = [...population].map( (a : agent) => [a[0], 1/a[1]]) as Array<agent>,
		n = table.length

		let sum = 0
		for (let a of table) sum += a[1]

		let sums = Array(n)
		sums[n-1] = table[n-1][1] / sum
		for (let i = n - 2; i >= 0; i--) sums[i] = (table[i][1] / sum) + sums[i+1]


		const POPULATION = []
		while (POPULATION.length < k) {
			const pivot = Math.random()
			for (let i = n - 1; i >= 0; i--)
				if (pivot <= sums[i]) {POPULATION.push(population[i]); break}
		}
		return POPULATION
	},

	diverse: (population : population, k : number) => {
		const 
		horizon = population[0][0].length,
		mean = population[0][0]

		for (let p of population)
			for(let i = 0; i < horizon; i++)
				mean[i] += p[0][i]

		for(let i = 0; i < horizon; i++) mean[i] /= population.length

		population.sort( (a, b) => vdiff(b[0], mean) - vdiff(a[0], mean) )
		population.length = Math.round(k)
		return population
	}
}


const crossover : any = {
	single_split1: (a : agent, b : agent, genotype_eval_function : Function) => {
		const
		g = a[0], h = b[0],
		n = g.length, split = randint(0, n)
	
		const new_genotype = []
		for (let i = 0; i < n; i++)
			if (i <= split) new_genotype.push(g[i])
			else new_genotype.push(h[i])
		return make_agent(new_genotype, genotype_eval_function)
	},

	continuous1: (a : agent, b : agent, genotype_eval_function : Function) => {
		const
		g = a[0], h = b[0],
		n = g.length, split = Math.random()

		const new_genotype = []
		for (let i = 0; i < n; i++) {
			new_genotype.push( Math.round(split*g[i] + (1 - split)*h[i]) )
		}
		return make_agent(new_genotype, genotype_eval_function)
	},

	continuous2: (a : agent, b : agent, genotype_eval_function : Function) => {
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
}

const mutation : any = {
	single_random: (agent : agent) => {
		const idx = randint(0, agent[0].length - 1)
		if (idx % 2) agent[0][idx] = randint(-1, 1)
		else agent[0][idx] = randint(-15, 15)
		return agent
	},

	uniform_multiple: (agent : agent, chance : number = 0.01) => {
		const genotype = agent[0]
		for (let i = 0; i < genotype.length; i++)
			if (Math.random() <= chance)
				if (i % 2) genotype[i] = randint(-1, 1)
				else genotype[i] = randint(-15,15)
		return agent
	},

	directed_uniform_multiple: (agent : agent, chance : number = 0.1) => {
		const genotype = agent[0]
		for (let i = 0; i < genotype.length; i++)
			if (Math.random() <= chance)
			if (i % 2) genotype[i] = 1
			else genotype[i] = choice([-15, 15])
		return agent
	},

	biased_uniform_multiple: (agent : agent, chance : number = 0.2) => {
		const genotype = agent[0]
		for (let i = 0; i < genotype.length; i++)
			if (Math.random() <= chance * (i/genotype.length))
				if (i % 2) genotype[i] = randint(-1, 1)
				else genotype[i] = randint(-15,15)
		return agent
	},
}

export {fitness_function, initialization, selection, crossover, mutation, make_agent, population, agent}