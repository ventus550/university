
def fio(iput, oput, transform, encoding='utf-8'):
	res = []
	with open(iput, encoding=encoding) as f:
		for line in f:
			line = [int(x) for x in line.strip().split()]
			res.append(line)

	rnum = res[0][0]; cnum = res[0][1];
	rows = res[1:rnum+1]; cols = res[rnum+1:]
	for i in range(len(rows)):
		rows[i] = Partition(cnum, rows[i], "row", i)

	for i in range(len(cols)):
		cols[i] = Partition(rnum, cols[i], "col", i)

	res = transform(rows, cols)
	with open(oput, mode="w", encoding=encoding) as f:
		f.write(res)











class PSET:
	def __init__(self, rows, cols, debug=0):
		self.Q = set()
		self.ROWS = rows
		self.COLS = cols
		self.debug = debug

		for e in rows+cols:
			self.add(e)
	
	def print(self):
		print("Printing set of partitions -------------------")
		for r in self.ROWS:
			print(r)
		for c in self.COLS:
			print(c)
		print("----------------------------------------------------------")
	
	def textify(self):
		strr = ""
		for r in self.ROWS:
			strr += "".join( ["." if x == 0 else "#" for x in r.FXP] )
			strr += "\n"
		
		return strr


	def add(self, p):
		self.Q.add(p)
		if self.debug:
			print("ADD:", p)

	def pop(self):
		p = self.Q.pop()
		if self.debug:
			print("POP:", p)
		changes = p.deduceFXP()
		cpartitions = self.COLS
		if p.type == "col":
			cpartitions = self.ROWS
		for i in changes:
			cp = cpartitions[i]
			if cp.fixPoint(p.index, p.FXP[i]): #jeśli w cp zaszła zmiana
				self.add(cp)
	
	def start(self):
		while self.Q:
			self.pop()
			


class Partition:
	def __init__(self, length, blocks, t="col", index=0):
		self.FXP = [-1 for i in range(length)] #fixed points
		self.blocks = blocks
		self.placements = []
		self.type = t
		self.index = index

		spots = length - sum([b for b in blocks]) + len(blocks) #liczba pól

		def place(i = -2, b = []):
			if len(b) == len(blocks):
				self.placements.append(b)
				return 

			for j in range(i+2, spots):
				place(j, b + [j])
		place()

		for k in range(len(self.placements)):
			s = self.placements[k]
			P = []

			prev_pos = 0
			for i in range(len(s)):
				P += [0 for _ in range(s[i] - prev_pos)]
				P += [1 for _ in range(blocks[i])]
				prev_pos = s[i] + 1

			P += [0 for _ in range(length - len(P))]
			self.placements[k] = P

	def deduceFXP(self):
		D = self.FXP
		changed = []
		for i in range(len(D)):
			if D[i] != -1:
				continue
			s = 0
			for p in self.placements:
				s += p[i]
			if s == 0:
				D[i] = 0
				changed.append(i)
			elif s == len(self.placements):
				D[i] = 1
				changed.append(i)

		return changed

	def fixPoint(self, idx, val=1):
		if self.FXP[idx] == val:
			return False #no changes
		
		self.placements = [p for p in self.placements if p[idx] == val]
		self.FXP[idx] = val
		return True #changes made
	
	def __str__(self):
		return self.type + " " + str(self.index) + " [ blocks: " + str(self.blocks) + ", FXP: " + str(self.FXP) + ", size: " + str(len(self.placements)) + " ]"

	def print(self):
		print("Printing partition with condition block", self.blocks)
		print("with fixed following fixed points:", self.FXP)
		for p in self.placements:
			print(p)


def solve(rows, cols):
	PS = PSET(rows, cols)
	PS.start()
	#PS.print()
	return PS.textify()

#python3 validator.py zad1 python3 obrazki1.py
fio("/mnt/c/Users/ventu/Desktop/si5/obrazki/zad_input.txt", "/mnt/c/Users/ventu/Desktop/si5/obrazki/zad_output.txt", solve)
