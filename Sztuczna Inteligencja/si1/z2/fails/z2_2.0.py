
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

		if word in MEMORY[len(word)].keys():
			return MEMORY[len(word)][word]
		if word in WORDS[len(word)]:
			return [word]
		return False
	
	def weight(word):
		return len(word)**2

	def match(string):
		global SIZE
		#print(string)

		if lookup(string):
			return lookup(string)

		best_match = (0, [])
		for i in range(1,len(string)): # <- można lepiej
			r1 = match(string[0:i]); r2 = match(string[i:len(string)]) # <- można lepiej
			if r1 and r2:
				w = weight(r1) + weight(r2) # <- można lepiej

				if w > best_match[0]:
					best_match = (w, r1 + r2)

		if best_match[0]:
			MEMORY[len(string)][string] = best_match[1]
			SIZE += 1
			return best_match[1]
		MEMORY[len(string)][string] = False
		SIZE += 1
		return False
	
	m = match(t)
	if m:
		return " ".join(m)
	return m

print("best recontruction:", reconstruct("tamatematykapustkinieznosi"))