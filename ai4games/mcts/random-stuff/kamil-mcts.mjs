
/*
let countS = 0, countT = 0;

function bitCount(n) {
    n = n - ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    return ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24
}


function Init() {
    return [[0, 0, 0], 0, [0, 0, 0], 0, null]
}

function CopyState(state) {
    const [[p1, p2, p3], p4, [e1, e2, e3], e4, next] = state;
    return [[p1, p2, p3], p4, [e1, e2, e3], e4, next];
}

function getCell(state, celPos, player) {
    const [cy, cx] = celPos;
    return (state[player ? 0 : 2][cy] & (0b0111111111 << (cx * 9))) >> (cx * 9);
}

function isCellWin(cell) {
    const x = cell;
    return (
        (((x & (x >> 1)) & (x >> 2)) |
            (x & (x << 1) & (x << 2)) |
            (((x & (x << 2)) >> 4) & x)
        ) > 0);
}

function apply(state, action, player) {
    const [_y, _x] = action;
    const Y = _y % 3, y = Math.floor(_y / 3), X = _x % 3, x = Math.floor(_x / 3);
    state[player ? 0 : 2][Y] |= ((0b01 << x) << (3 * y)) << (9 * X);

    state[player ? 1 : 3] |= (0b01 << X) << (3 * Y);

    const cellPos = [Y, X];
    state[4] = ((getCell(state, cellPos, true) | getCell(state, cellPos, false)) == 0b0111111111) ? null : [Y, X];
}

function isTerminal(state) {
    const [[p1, p2, p3], p4, [e1, e2, e3], e4, next] = state;
    return (
        (((p1 | e1) == 0b0111111111111111111111111111) &&
            ((p2 | e2) == 0b0111111111111111111111111111) &&
            ((p3 | e3) == 0b0111111111111111111111111111)) ||
        isCellWin(p4) || isCellWin(e4)
    );
}

function getActions(state) {
    if (isTerminal(state))
        return [];

    let cellPos = state[4];

    const actions = [];
    if (cellPos === null) {

        for (let Y = 0; Y <= 2; Y++)
            for (let X = 0; X <= 2; X++) {
                cellPos = [Y, X];
                let cell = ~(getCell(state, cellPos, true) | getCell(state, cellPos, false)) & 0b0111111111111111111111111111;
                let elemPos = 0;
                while (cell > 0) {
                    if (cell & 0b01 == 0b01) {
                        const elem = [Y + Math.floor(elemPos / 3), X + (elemPos % 3)];
                        actions.push(elem);
                    }
                    cell >>= 1;
                    elemPos++;
                }
            }
    } else {
        const [Y, X] = cellPos;
        let cell = ~(getCell(state, cellPos, true) | getCell(state, cellPos, false)) & 0b0111111111111111111111111111;
        let elemPos = 0;
        while (cell > 0) {
            if (cell & 0b01 == 0b01) {
                const elem = [Y + Math.floor(elemPos / 3), X + (elemPos % 3)];
                actions.push(elem);
            }
            cell >>= 1;
            elemPos++;
        }
    }
    return actions;
}

function calculateReward(state) {
    if (isCellWin(state[1]))
        return 1;
    if (isCellWin(state[3]))
        return 0;

    const pCount = bitCount(state[1]);
    const eCount = bitCount(state[3]);

    if (pCount > eCount)
        return 1;
    else if (pCount < eCount)
        return 0;

    return 0.5;
}

function Simulation(state, player) {
    let p = player;
    let s = CopyState(state);
    let actions = getActions(s, p);
    while (actions.length > 0) {
        let action = actions[Math.floor(Math.random() * actions.length)];
        apply(s, action, p);
        p = !p;
        actions = getActions(s, p);
    }
    return calculateReward(s);
}

*/
let countS = 0, countT = 0;

function bitCount(n) {
    n = n - ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    return ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24
}

function Init() {
    return [[0, 0, 0], 0, [0, 0, 0], 0, null]
    // player , enemy, next
}

function CopyState(state) {
    const [[p1, p2, p3], p4, [e1, e2, e3], e4, next] = state;
    return [[p1, p2, p3], p4, [e1, e2, e3], e4, next];
}

function getCell(state, celPos, player) {
    const [cy, cx] = celPos;
    return (state[player ? 0 : 2][cy] & (0b0111111111 << (cx * 9))) >> (cx * 9);
}

function isCellWin(cell) {
    const x = cell;
    return (
        ((((x & (x >> 1)) & (x >> 2)) & 0b0001001001) |
            (((x & (x << 3)) & (x << 6)) & 0b0111000000) |
            ((x & (x << 2)) & (x << 4))
        ) > 0);
}

function apply(state, action, player) {
    const [_y, _x] = action;
    const Y = _y % 3, y = Math.floor(_y / 3), X = _x % 3, x = Math.floor(_x / 3);
    state[player ? 0 : 2][Y] |= ((0b01 << x) << (3 * y)) << (9 * X);

    if (isCellWin(state[player ? 0 : 2][Y]))
        state[player ? 1 : 3] |= (0b01 << X) << (3 * Y);

    const cellPos = [Y, X];
    const cellT = getCell(state,cellPos,true);
    const cellF = getCell(state,cellPos,false)
    state[4] = isCellWin(cellT) || isCellWin(cellF || (cellF | cellT == 0b0111111111))  ? [Y, X] : null ;
}

function isTerminal(state) {
    const [[p1, p2, p3], p4, [e1, e2, e3], e4, next] = state;
    return (
        (((p1 | e1) == 0b0111111111111111111111111111) &&
            ((p2 | e2) == 0b0111111111111111111111111111) &&
            ((p3 | e3) == 0b0111111111111111111111111111)) ||
        isCellWin(p4) || isCellWin(e4)
    );
}

function getActions(state) {
    if (isTerminal(state))
        return [];

    let cellPos = state[4];

    const actions = [];
    if (cellPos === null) {

        for (let Y = 0; Y <= 2; Y++)
            for (let X = 0; X <= 2; X++) {
                cellPos = [Y, X];
                let cell = ~(getCell(state, cellPos, true) | getCell(state, cellPos, false)) & 0b0111111111111111111111111111;
                let elemPos = 0;
                while (cell > 0) {
                    if (cell & 0b01 == 0b01) {
                        const elem = [Y + Math.floor(elemPos / 3), X + (elemPos % 3)];
                        actions.push(elem);
                    }
                    cell >>= 1;
                    elemPos++;
                }
            }
    } else {
        const [Y, X] = cellPos;
        let cell = ~(getCell(state, cellPos, true) | getCell(state, cellPos, false)) & 0b0111111111111111111111111111;
        let elemPos = 0;
        while (cell > 0) {
            if (cell & 0b01 == 0b01) {
                const elem = [Y + Math.floor(elemPos / 3), X + (elemPos % 3)];
                actions.push(elem);
            }
            cell >>= 1;
            elemPos++;
        }
    }
    return actions;
}

function calculateReward(state) {
    if (isCellWin(state[1]))
        return 1;
    if (isCellWin(state[3]))
        return 0;

    const pCount = bitCount(state[1]);
    const eCount = bitCount(state[3]);

    if (pCount > eCount)
        return 1;
    else if (pCount < eCount)
        return 0;

    return 0.5;
}

function Simulation(state, player) {
    let p = player;
    let s = CopyState(state);
    let actions = getActions(s, p);
    while (actions.length > 0) {
        let action = actions[Math.floor(Math.random() * actions.length)];
        apply(s, action, p);
        p = !p;
        actions = getActions(s, p);
    }
    return calculateReward(s);
}









class MCTS {
    constructor(state, player, actions, timeE) {
        this.actionsToSimulate = actions;
        this.state = state;
        this.player = player;
        this.n = 0;
        this.w = 0;
        this.children = [];

        this.timeE = timeE;
    }

    action(K = 1000) {
        let n = 0;
        while (K--) {
            this.Select();
            n++;
        }
        console.error(`Amount of simulations: ${n}`);
        countS += n;
        let children = this.children.map(([child, action]) => [action, child.n, child.w, child.w / child.n]);
        return children.reduce(([aP, nP, wP], [aC, nC, wC]) => nP > nC ? [aP, nP, wP] : [aC, nC, wC])[0];
    }

    UCT(n) {
        return (this.w / this.n + 0.15 * Math.sqrt(2 * Math.log(n) / this.n));
    }

    BackPropagation(symRes) {
        this.w += symRes.w;
        this.n += 1;
        return symRes;
    }

    Simulate() {
        let sRes = Simulation(this.state, this.player);
        let res = {w: sRes };
        return this.BackPropagation(res);
    }

    Expansion() {
        const action = this.actionsToSimulate.pop();
        const newChildState = CopyState(this.state);
        apply(newChildState, action, this.player);

        const newChild = new MCTS(newChildState, !this.player, null);
        this.children.push([newChild, action]);

        return newChild.Simulate();
    }

    Select() {
        if (this.actionsToSimulate == null)
            this.actionsToSimulate = getActions(this.state);

        if (this.actionsToSimulate.length > 0) {
            return this.BackPropagation(this.Expansion());
        }

        if (this.children.length == 0)
            return { w: calculateReward(this.state) };

        let maxArg;
        const children = this.children.map(([child, action]) => [child, child.UCT(this.n)]);
        if (this.player)
            maxArg = children.reduce(([aP, uP], [aC, uC]) => uP > uC ? [aP, uP] : [aC, uC])[0];
        else
            maxArg = children.reduce(([aP, uP], [aC, uC]) => uP < uC ? [aP, uP] : [aC, uC])[0];
        return this.BackPropagation(maxArg.Select());
    }
}


let state = Init();
let isFirst = true;
while (true) {
    let playerChoices = []

    var inputs = readline().split(' ');
    const opponentRow = parseInt(inputs[0]);
    const opponentCol = parseInt(inputs[1]);

    const validActionCount = parseInt(readline());
    for (let i = 0; i < validActionCount; i++) {
        var inputs = readline().split(' ');
        const row = parseInt(inputs[0]);
        const col = parseInt(inputs[1]);
        playerChoices.push([row, col]);
    }

    if (opponentRow != -1)
        apply(state, [opponentRow, opponentCol], false);

    let a;
    countT++;
    if (isFirst) {
        a = new MCTS(state, true, playerChoices, 990 + Date.now()).GetBest();
        isFirst = false;
    } else
        a = new MCTS(state, true, playerChoices, 90 + Date.now()).GetBest();
    console.error(`Average: ${Math.floor(countS / countT)}`); apply(state, a, true);
    const [oY, oX] = a;
    console.log(`${oY} ${oX}`);

    // Write an action using console.log()
    // To debug: console.error('Debug messages...');
}
