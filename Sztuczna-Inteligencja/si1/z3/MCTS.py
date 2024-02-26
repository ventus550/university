from random import choices, sample

class Card:

	val = {
		"2": 2,		"3": 3,		"4": 4,		"5": 5,		"6": 6,
		"7": 7,		"8": 8,		"9": 9,		"10": 10,	"J": 11,
		"Q": 12, 	"K": 13,	"A": 14
	}
	
	def __init__(self, color, card):
		self.color = color
		self.card = card
	def __str__(self):
		return "[" + self.color + self.card + "]"
	def __gt__(self, other):
		return self.val[self.card] > self.val[other.card]
	def __int__(self):
		return self.val[self.card]

class Deck:


	cards = [Card(co, ca) for co in ['a', 'b', 'c', 'd'] for ca in ['J', 'Q', 'K', 'A']] + [Card(co, str(ca)) for co in ['a', 'b', 'c', 'd'] for ca in range(2,11)] 

	val = {
		"highcard": 1,	"1pair": 2,	"2pair": 3, "3kind": 4,
		"straight": 5,	"flush": 6,	"full": 7,	"4kind": 8,	"straightflush": 9
	}

	def __init__(self, cards_str):
		self.deck = []; self.hand = []

		k = 0
		for x in cards_str:
			if int(x):
				self.deck.append(self.cards[k])
			k += 1


	def isMonochromatic(self):
		return all([c.color == self.hand[0].color for c in self.hand])

	def isOrdered(self):
		self.hand = sorted(self.hand, key=lambda x: int(x))
		ok = True
		for i in range(len(self.hand)-1):
			if int(self.hand[i+1]) - int(self.hand[i]) != 1:
				ok = False
		return ok
	
	def cproperties(self):
		ordered = self.isOrdered()
		monochromatic = self.isMonochromatic()

		if ordered and monochromatic:
			return "straightflush"
		elif monochromatic:
			return "flush"
		elif ordered:
			return "straight"
		else:
			return "highcard"

	def cmultiples(self):
		h = self.hand.copy()
		d = dict()
		while len(h) > 0:
			c = h.pop().card
			if c in d:
				d[c] += 1
			else:
				d[c] = 1
			
		d = list(d.values())
		if max(d) > 3:
			return "4kind"
		elif 2 in d and 3 in d:
			return "full"
		elif 3 in d:
			return "3kind"
		elif 2 in d:
			return str(d.count(2)) + "pair"
		else:
			return "highcard"
	
	def evaluate(self):
		return max([self.val[x] for x in [self.cproperties(), self.cmultiples()]])

	def __str__(self):
		strr = "("
		for c in self.deck:
			strr += str(c)
		return strr + ")"

	def draw(self):
		self.hand = choices(self.deck, k=5)
		return self




Figurant = Deck('1'*16 + '0'*36)

class Memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memo
def simulate(deck, r = 100):

	B = Deck(deck)
	def roll():
		return B.draw().evaluate() > Figurant.draw().evaluate()

	Bwins = 0; rolls = r
	for i in range(rolls):
		Bwins += roll()
	return Bwins/rolls


def DFS():
	fill = '0'*16; depth = 0; max_depth = 10**6
	res = (0, '1'*36, 0)
	def search(p, dck, length):
		nonlocal res
		nonlocal depth
		nonlocal max_depth
		
		if length <= res[2]:
			return

		cands = []
		for i in range(len(dck)):
			if dck[i] == '1':
				ndck = dck[0:i] + '0' + dck[i+1:]
				prob = simulate(fill + ndck)
				#search(prob, ndck, length-1)

				if prob < p:
					continue
				elif prob > 0.5:

					prob = simulate(fill + ndck, 1000)
					if prob > 0.5:
						res = (prob, ndck, length)
						print(res)
						return
				else:
					cands.append( (prob, ndck) )
		cands.sort(key=lambda x: x[0], reverse=True)
		#print(cands)
		k = 0
		for c in cands:
			if k == 3:
				break
			search(c[0], c[1], length-1)
			k += 1


	
	search(res[0], res[1], 36)

DFS()
#d = Deck( '0'*16 + '100011000100011000101011000100011000')
#print(d)
