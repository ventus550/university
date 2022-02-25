import { Engine, get, fuel } from "./engine.js";
import { CanvasScreen } from "./screen.js";
import * as genetics from "./genetics.js";
const highground_surface = [
    0, 1000, 300, 1500, 350, 1400, 500, 2100, 1500, 2100,
    2000, 200, 2500, 500, 2900, 300, 3000, 200, 3200, 1000,
    3500, 500, 3800, 800, 4000, 200, 4200, 800, 4800, 600,
    5000, 1200, 5500, 900, 6000, 500, 6500, 300, 6999, 500
], highground_spot = [1500, 2100], highground_origin = [6500, 2700, -50, 0, 1000, 90, 0];
const SURFACE = highground_surface, SPOT = highground_spot, ORIGIN = highground_origin, ENGINE = new Engine(SURFACE, SPOT, ORIGIN), SCREEN = new CanvasScreen(ENGINE);
function draw_population(population) {
    const worst = 300, states = [];
    let mean = 0, min = Infinity;
    for (let agent of population) {
        const [trj, state] = ENGINE.trajectory(agent[0]), density = genetics.fitness_function.speed(state) / worst;
        states.push(state);
        let color = `rgb(${255 * density}, ${255 * (1 - density)}, 0)`;
        if (ENGINE.succesful(state)) {
            SCREEN.polyline(trj, 'teal', 3);
            console.log(JSON.stringify(agent[0]));
            alert();
        }
        else
            SCREEN.polyline(trj, color);
        mean += agent[1];
        min = Math.min(min, agent[1]);
    }
    console.log(mean, min);
}
function standard_evaluator(fitf) {
    return (genotype) => {
        let state;
        for (let s of ENGINE.simulator(genotype))
            state = s;
        if (ENGINE.succesful(state))
            return -get(state, fuel);
        return fitf(state, SPOT);
    };
}
function kamil() {
    const fitness = genetics.fitness_function.kamilfit, init = genetics.initialization.full_spread, selection = genetics.selection.kbest, crossover = genetics.crossover.continuous2, mutation = genetics.mutation.uniform_multiple, evaluator = standard_evaluator((state, spot) => fitness(state, spot, 10000, 100)), POPULATION_SIZE = 500, HORIZON = 200;
    let POPULATION = init([], evaluator, POPULATION_SIZE, HORIZON);
    draw_population(POPULATION);
    function next_generation() {
        SCREEN.clear(1);
        POPULATION = selection(POPULATION, POPULATION_SIZE * 0.5);
        const generation = [];
        for (let i = 1; i < POPULATION.length; i += 2) {
            const parent1 = POPULATION[i], parent2 = POPULATION[i - 1];
            generation.push(...crossover(parent1, parent2, evaluator));
        }
        for (let i = 0; i < generation.length; i++)
            generation[i] = mutation(generation[i], 0.01);
        POPULATION = POPULATION.concat(generation);
        draw_population(POPULATION);
    }
    return next_generation;
}
const wind = window;
wind.next = kamil();
wind.play = () => { setInterval(wind.next, 500); };
