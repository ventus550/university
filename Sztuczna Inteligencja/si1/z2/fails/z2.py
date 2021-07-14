def reconstruct(t):
	RECONTRUCTION = []

	dct = dict()
	with open("polish_words.txt", encoding='utf-8') as f:
		for word in f:
			word = word.strip()

			try:
				dct[len(word)] += [word]
			except:
				dct[len(word)] = [word]
		
	
	skeys = sorted(dct.keys(), reverse=True) + [0]; max_len = skeys[0]
	def match(pos, limit):
		
		for k in skeys:
			if k > limit or k == 0:
				continue

			sub = t[pos:pos+k]
			for word in dct[k]:
				if word == sub:
					return word

		return False

	
	
	pos = 0; limit = max_len
	while pos != 0 or limit != 0:
		m = match(pos, limit)
		#print(RECONTRUCTION, m)

		if(pos == len(t)):
			best_match = []
			w = 0
			summ = 0
			for word in RECONTRUCTION:
				summ += len(word)**2

			#print("Reconstruction weight:", summ)
			if w < summ:
				best_match = RECONTRUCTION[:]
				w = summ

		if m:
			RECONTRUCTION += [m]
			pos += len(m)
			limit = max_len
		else:
			poplen = 0
			try:
				poplen = len(RECONTRUCTION.pop())
				pos -= poplen
			except:
				pass

			for k in skeys:
				if k < poplen or k == 0:
					limit = k
					break
			#print("Returning to", pos, limit, "...")

	return best_match


print("best recontruction:", reconstruct("tamatematykapustkinieznosi"))