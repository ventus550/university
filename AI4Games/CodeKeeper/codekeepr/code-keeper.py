import sys
import numpy as np
from queue import Queue
import math
from random import randint
DEBUG = 1


def log(*msg):
    if DEBUG: print(*msg, file=sys.stderr, flush=True)

def notvalid(pos):
    x, y = pos
    return x < 0 or y < 0 or x > 15 or y > 11

def MOVE(x, y, msg = "move"):
    print(f"MOVE {x} {y} {msg}")

def ATTACK(x, y, weapon, msg = "attack"):
    print(f"ATTACK {weapon} {x} {y} {msg}")

class Player:
    def __init__(self, x, y, health, score, cham, cscy, cbow):
        self.pos = np.array([x, y])
        self.health = health
        self.score = score
        self.cham = cham
        self.cscy = cscy
        self.cbow = cbow

class Map:
    def __init__(self):
        self.map = [ [None]*12 for _ in range(16) ]
    def __getitem__(self, pos):
        if notvalid(pos): return 1
        else: return self.map[pos[0]][pos[1]]
    def __setitem__(self, pos, val):
        x, y = pos
        if not notvalid(pos):
            self.map[x][y] = val

# weapons
SWORD = 0
HAMMER = 1
SCYTHE = 2
BOW = 3

# types
EXIT = 0; VOID = 1; GOLD = 2
HPOT = 3; CHAM = 4; CSCY = 5
CBOW = 6; BOX  = 7; SKEL = 8
GARG = 9; ORC  = 10; VAMP = 11
UNKN = None

MONSTERS = [SKEL, GARG, ORC, VAMP]

BOUNTIES = [GOLD, HPOT, CHAM, CSCY, CBOW]

SCORE = [
    0, 0, 100,
    0, 0, 0,
    0, 1, 6,
    14, 8, 11
]

INF = math.inf

#MAP = [ [UNKN]*12 for _ in range(16) ]
MAP = Map()

TIME = 0
EXTDOOR = UNKN

def mapscan():
    for x in range(16):
        for y in range(12):
            yield (x, y), MAP[x, y]

def addv(v, u):
    return (v[0] + u[0], v[1] + u[1])

def ismonster(type):
    return type in MONSTERS

def isbounty(type):
    return type in BOUNTIES

def manhattan(source, target):
    sx, sy = source; tx, ty = target
    return abs(sx - tx) + abs(sy - ty)

def BFS(player):
    directions = [(0, -1), (+1, 0), (0, +1), (-1, 0)]
    dist = [ [None]*12 for _ in range(16) ]
    ptr  = [ [None]*12 for _ in range(16) ]
    Q = Queue()

    px, py = player.pos
    dist[px][py] = 0
    ptr[px][py] = player.pos
    Q.put(player.pos)

    while not Q.empty():
        px, py = pop = Q.get()
        #log(f"POPPED {pop} with dist={dist[px][py]}, ptr={ptr[px][py]}, parent pointer={ptr[ppx][ppy]}")

        for d in directions:
            x, y = cell = pop + d
            if notvalid(cell): continue

            #log(f"CHECK {cell} with dist={dist[x][y]}, void: {MAP[x, y] == VOID}, unkown: {MAP[x, y] == UNKN}, NoneDist: {dist[x][y] == None}")
            if MAP[cell] == VOID or MAP[cell] == UNKN or (MAP[cell] == EXIT and any( MAP[cell + d] == GOLD for d in directions )):
                # log(f"void if {x} {y}")
                dist[x][y] = dist[px][py] + 1 # hmmm...
                ptr[x][y] = pop
            elif dist[x][y] == None:
                # log(f"new if {x} {y}")
                dist[x][y] = dist[px][py] + 1
                Q.put(cell)
                ptr[x][y] = pop

    for d in dist:
        for i in range(len(d)):
            if d[i] == None: d[i] = INF
    return dist, ptr

def fight(player):

    def bow():
        if player.cbow == 0: return None
        for target, type in mapscan():
            px, py = player.pos
            tx, ty = target
            if type == ORC and abs(px - tx) <= 2 and abs(py - ty) <= 2:
                return target
        return None

    def hammer():
        best = None; bval = 0
        directions = [
            (-1, -1), (0,  -1), (+1, -1), (+1,  0),
            (+1, +1), (0,  +1), (-1, +1), (-1,  0)
        ]

        if player.cham == 0: return best, bval
        for dx in range(8):
            d0 = directions[dx] + player.pos
            d1 = directions[dx - 1] + player.pos
            d2 = directions[dx - 2] + player.pos

            t0 = MAP[d0]
            t1 = MAP[d1]
            t2 = MAP[d2]

            types = [t0, t1, t2]
            val = sum( ismonster(t) for t in types )
            if val > bval: best, bval = d1, val
        return best, bval

    def scythe():
        best = None; bval = 0
        directions = [(0, -1), (+1, 0), (0, +1), (-1, 0)] # fix this!
        
        if player.cscy == 0: return best, bval
        for d in directions:
            d0 = d + player.pos
            d1 = 2*np.array(d) + player.pos

            t0 = MAP[d0]
            t1 = MAP[d1]

            val = ismonster(t0) + 2*ismonster(t1)
            if val > bval: best, bval = d0, val
        return best, bval
    
    def sword():
        directions = [(0, -1), (+1, 0), (0, +1), (-1, 0)]
        for d in directions:
            d0 = d + player.pos
            t0 = MAP[d0]
            if ismonster(t0): return d0
        return None


    
    bow_target = bow()
    if player.cbow and bow_target:
        ATTACK(bow_target[0], bow_target[1], BOW)
        return True
    
    ham_target, ham_value = hammer()
    scy_target, scy_value = scythe()
    if ham_value == 3:
        ATTACK(ham_target[0], ham_target[1], HAMMER)
        return True
    if scy_value >= 2:
        ATTACK(scy_target[0], scy_target[1], SCYTHE)
        return True
    if ham_value == 2:
        ATTACK(ham_target[0], ham_target[1], HAMMER)
        return True
    if not sword() is None:
        sw = sword()
        ATTACK(sw[0], sw[1], SWORD)
        return True
    return False
    
    
        

def goto(player, target, ptr):
    tx, ty = target
    assert(ptr[tx][ty] != None, "<go to unreachable target>")
    while not np.array_equal(ptr[tx][ty], player.pos):
        tx, ty = ptr[tx][ty]
    MOVE(tx, ty, "goto")




def explore(player, ptr, dist):
    log("explore!")
    try:
        spot = min([target for target, type in mapscan() if type == UNKN], key=lambda x: dist[x[0]][x[1]])
        goto(player, spot, ptr)
        #MOVE(spot[0], spot[1], "exploring")
    except:
        try:
            spot = min([target for target, type in mapscan() if type == BOX], key=lambda x: dist[x[0]][x[1]])
            goto(player, spot, ptr)
        except:
            MOVE(randint(0, 15), randint(0,11), "just walking...")

def loot(player, target, type, dist):
    dist = dist[target[0]][target[1]]

    if type == GOLD:
        return 100 / dist
    elif type == HPOT:
        return (20 - player.health)**2 / dist
    elif type == CHAM:
        return 10 * (10 - player.cham) / dist
    elif type == CSCY:
        return 10 * (10 - player.cscy) / dist
    elif type == CBOW:
        return 15 * (10 - player.cbow) / dist
    raise Exception(f"bad target {type}")


def exploit(player, dist, ptr):
    log("exploit!")

    best = None; bval = 0
    for target, type in mapscan():
        if isbounty(type):
            d = loot(player, target, type, dist)
            if d > bval:
                best = target
                bval = d

    if best: goto(player, best, ptr)
    else: explore(player, ptr, dist)


def ACTION(player):

    if fight(player): return # fix this!
    log("fight over")

    dist, ptr = BFS(player)
    log("bfs over")

    if player.health <= 15:
        directions = (-1, 0, 1,)
        x, y = player.pos
        potions = [ (x + i, y + j) for i in directions for j in directions if MAP[x+i, y+j] == HPOT ]
        if potions:
            goto(player, potions[0], ptr)
            return

    log("TESTEXIT:", player.health >= 8 and TIME < 100, EXTDOOR and not ptr[EXTDOOR[0]][EXTDOOR[1]] is None)
    if player.health >= 10 and TIME < 112:
        exploit(player, dist, ptr)
    elif EXTDOOR and not ptr[EXTDOOR[0]][EXTDOOR[1]] is None:
        goto(player, EXTDOOR, ptr)
    else:
        explore(player, ptr, dist)







# game loop
while True:
    # x: x position of the hero
    # y: y position of the hero
    # health: current health points
    # score: current score
    # charges_hammer: how many times the hammer can be used
    # charges_scythe: how many times the scythe can be used
    # charges_bow: how many times the bow can be used
    x, y, health, score, charges_hammer, charges_scythe, charges_bow = [int(i) for i in input().split()]
    directions = (-3, -2, -1, 0, 1, 2, 3)
    for i in directions:
        for j in directions:
            MAP[x + i, y + j] = -1

    visible_entities = int(input())  # the number of visible entities
    for i in range(visible_entities):
        # ex: x position of the entity
        # ey: y position of the entity
        # etype: the type of the entity
        # evalue: value associated with the entity
        ex, ey, etype, evalue = [int(j) for j in input().split()]
        if etype == EXIT: EXTDOOR = (ex, ey)
        MAP[ex, ey] = etype
    
    #log(np.array(MAP.map).T)

    mapscan()
    # MOVE x y [message] | ATTACK weapon x y [message]
    ACTION(Player(x, y, health, score, charges_hammer, charges_scythe, charges_bow))

    # if TIME < 5:
    #     MOVE(14, 5)
    # elif TIME < 9:
    #     MOVE(15, 7, (15, 7))
    # elif TIME == 10:
    #     MOVE(15, 8)
    # else:
    #     MOVE(11, 11)

    TIME += 1
