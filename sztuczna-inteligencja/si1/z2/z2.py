from fio import fio

class Memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

WORDS = dict()
with open("polish_words.txt", encoding='utf-8') as f:
	for word in f:
		word = word.strip()

		try:
			WORDS[len(word)] += [word]
		except:
			WORDS[len(word)] = [word]


def reconstruct(t):

	def lookup(word):
		if len(word) in WORDS and word in WORDS[len(word)]:
			return [word]
		return False
	
	def weight(words):	
		s = 0
		for w in words:
			s += len(w)**2
		return s

	@Memo
	def match(string):
		lk = lookup(string)
		if lk:
			return lk

		best_match = (0, [])
		for i in range(1, len(string)):

			r1 = match(string[0:i]);
			if not r1:
				continue

			r2 = match(string[i:len(string)])
			if not r2:
				continue

			w = weight(r1) + weight(r2)
			if w > best_match[0]:
				best_match = (w, r1 + r2)

		if best_match[0]:
			return best_match[1]
			
		return False
	
	m = match(t)
	if m:
		return " ".join(m)
	return m
		


fio("zad2_input.txt", "zad2_output.txt", reconstruct)

