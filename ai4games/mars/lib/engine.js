function addv(v, u) {
    return [v[0] + u[0], v[1] + u[1]];
}
function randint(a, b) {
    const n = b - a + 1;
    return ~~(Math.random() * n) + a;
}
function uniform(a, b) {
    const n = b - a + 1;
    return Math.random() * n + a;
}
function choice(arr) {
    let n = arr.length;
    return arr[randint(0, n - 1)];
}
function stringify(state) {
    state = [...state].map(x => Math.round(x));
    return `[ X: ${state[0]}, Y: ${state[1]}, HS: ${state[2]}, VS: ${state[3]}, fuel: ${state[4]}, angle: ${state[5]}, thrust: ${state[6]} ]`;
}
function bounds(val, low, high) {
    const ltest = Number(val < low), htest = Number(val > high), vtest = Number(ltest + htest == 0);
    return ltest * low + htest * high + vtest * val;
}
const DEFAULT_STATE = [0, 0, 0, 0, 0, 0, 0], gravity_acceleration = -3.711, pos = 0, speed = 2, fuel = 4, angle = 5, thrust = 6;
function set(state, field, val) {
    if (typeof val == "number") {
        state[field] = val;
    }
    else if (field < 2) {
        state[0] = val[0];
        state[1] = val[1];
    }
    else {
        state[2] = val[0];
        state[3] = val[1];
    }
}
function get(state, field) {
    if (field < 2) {
        return [state[0], state[1]];
    }
    else if (field < 4) {
        return [state[2], state[3]];
    }
    else {
        return state[field];
    }
}
function update(state, set_angle, set_thrust) {
    const ang = get(state, angle), thrst = get(state, thrust), fl = get(state, fuel), spd = get(state, speed), position = get(state, pos);
    if (fl <= 0)
        set_thrust = -4;
    const new_ang = bounds(ang + set_angle, -90.0, 90.0), new_thrst = bounds(thrst + set_thrust, 0, 4), arcAngle = -new_ang * Math.PI / 180.0, acc = [Math.sin(arcAngle) * new_thrst, Math.cos(arcAngle) * new_thrst + gravity_acceleration], new_spd = addv(spd, acc), new_pos = addv(position, addv(new_spd, [-acc[0] * 0.5, -acc[1] * 0.5]));
    set(state, pos, new_pos);
    set(state, fuel, fl - new_thrst);
    set(state, angle, new_ang);
    set(state, thrust, new_thrst);
    set(state, speed, new_spd);
}
function collision(a, b, A, B, x, y) {
    const bounded = (x1, p, x2) => (x1 <= p && p <= x2) || (x1 >= p && p >= x2);
    return (x - a) * (B - b) - (y - b) * (A - a) >= 0 && bounded(a, x, A);
}
class Engine {
    constructor(surfaceN, spot, origin = DEFAULT_STATE) {
        this.surface = surfaceN;
        this.origin = origin;
        this.spot = spot;
        this.surfaceX = [];
        this.surfaceY = [];
        for (let i = 0; i < surfaceN.length; i++)
            if (i % 2)
                this.surfaceY.push(surfaceN[i]);
            else
                this.surfaceX.push(surfaceN[i]);
    }
    make_state() { return [...this.origin]; }
    succesful(state) {
        const [x, y] = get(state, pos);
        return Math.abs(get(state, speed)[0]) <= 20
            && Math.abs(get(state, speed)[1]) <= 40
            && Math.abs(get(state, angle)) == 0
            && this.spot[0] - 400 <= x
            && this.spot[0] + 400 >= x
            && this.spot[1] >= y - 100;
    }
    terminal(state) {
        const X = this.surfaceX, Y = this.surfaceY, n = X.length, [x, y] = get(state, pos);
        if (x < 0 || x > 7000)
            return true;
        for (let i = 1; i < n; i++) {
            const a = X[i - 1], b = Y[i - 1], A = X[i], B = Y[i];
            if (collision(a, b, A, B, x, y))
                return true;
        }
        return false;
    }
    update_state(state, angle, thrust) {
        if (this.terminal(state))
            return false;
        update(state, angle, thrust);
        return true;
    }
    *simulator(genotype) {
        console.assert(genotype.length % 2 == 0, "corrupted genotype " + genotype.length);
        const state = this.make_state();
        for (let i = 0; i < genotype.length; i += 2)
            if (this.update_state(state, genotype[i], genotype[i + 1]))
                yield state;
            else
                break;
        while (this.update_state(state, 0, 0))
            yield state;
        yield state;
    }
    trajectory(genotype) {
        const res = [...get(this.origin, pos)];
        let state;
        for (let s of this.simulator(genotype)) {
            state = s;
            res.push(...get(s, pos));
        }
        return [res, state];
    }
}
export { Engine, set, get, update, addv, choice, randint, uniform, stringify, collision, pos, speed, fuel, angle, thrust };
