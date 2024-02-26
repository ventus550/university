from random import choices

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

	val = {
		"highcard": 1,	"1pair": 2,	"2pair": 3, "3kind": 4,
		"straight": 5,	"flush": 6,	"full": 7,	"4kind": 8,	"straightflush": 9
	}

	def __init__(self, cards):
		self.deck = []
		self.hand = []
		for co in ["a", "b", "c", "d"]: #colors
			for ca in cards:
				self.deck.append(Card(co, ca))

	def copy(self):
		d = Deck([])
		d.deck = self.deck.copy()
		return d

	def __str__(self):
		strr = "("
		for c in self.deck:
			strr += str(c)
		return strr + ")"

	def draw(self):
		self.hand = choices(self.deck, k=5)
		return self

	def isMonochromatic(self):
		return all([c.color == self.hand[0].color for c in self.hand])

	def isOrdered(self):
		self.hand = sorted(self.hand)
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
			
class Memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]
		



			



def statistics():

	Figurant = Deck(["J", "Q", "K", "A"])
	Blotkarz = Deck([str(n) for n in range(2,11)])
	
	

	def probability(B):

		def roll():
			return B.draw().evaluate() > Figurant.draw().evaluate()

		Bwins = 0; rolls = 100
		for i in range(rolls):
			Bwins += roll()
		return Bwins/rolls

	stack = [Blotkarz.deck]
	stack2 = []
	res = ()

	MEMO = dict()
	def search(ls):
		nonlocal res

		if str(t) in MEMO:
			return MEMO[str(t)]

		B = Deck([]); B.deck = t
		prob = probability(B)
			
		if prob > 0.5:
			res = (B, prob)
			print("WEEEEEEEEEEEEEEEEEEEEEEE", B, prob)

		MEMO[str(t)] = t
		return t
		
		
	count = 32
	while not res:
		count -= 1
		print(count)

		for e in stack:
			for i in range(len(e)):
				t = e.copy()
				t.pop(i)

				stack2.append(search(t))
		
		stack, stack2 = stack2, []



statistics()




