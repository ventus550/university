def FILEFY(input, output, transform, encoding='utf-8'):
	res = []
	with open(input, encoding=encoding) as f:
		for line in f:
			line = line.strip()
			print(transform(line))
	with open(output, mode="w", encoding=encoding) as f:
		for r in res:
			f.write(r)




WORDS = dict()
with open("polish_words.txt", encoding='utf-8') as f:
	for word in f:
		word = word.strip()

		try:
			WORDS[len(word)] += [word]
		except:
			WORDS[len(word)] = [word]


MEMORY = dict()
for i in range(1, 1000):
	MEMORY[i] = dict()
SIZE = 0
			
def reconstruct(t):

	def lookup(word):
		l = len(word)
		if word in MEMORY[l].keys():
			return MEMORY[l][word]
		if l in WORDS and word in WORDS[l]:
			return [word]
		return False
	
	def weight(words):
		s = 0
		for w in words:
			s += len(w)**2
		return s

	def match(string):
		lk = lookup(string)
		if lk:
			MEMORY[len(string)][string] = lk
			return lk

		best_match = (0, [])
		for i in range(1,len(string)):

			r1 = match(string[0:i]);
			if not r1:
				continue

			r2 = match(string[i:len(string)])
			if not r2:
				continue

			w = weight(r1) + weight(r2)
			if w > best_match[0]:
				best_match = (w, r1 + r2)
				return best_match[1]

		if best_match[0]:
			MEMORY[len(string)][string] = best_match[1]
			return best_match[1]
			
		MEMORY[len(string)][string] = False
		return False
	
	m = match(t)
	if m:
		return " ".join(m)
	return m






FILEFY("zad2_input.txt", "zad2_output.txt", reconstruct)
