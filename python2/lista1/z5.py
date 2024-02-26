from collections import defaultdict

def common_prefix(L):
	L = [ x.lower() for x in L ]
	mx = min(len(x) for x in L)

	for i in reversed(range(mx)):
		D = defaultdict(int)
		for word in L:
			D[word[:i]] += 1

		for item, count in D.items():
			if count >= 3:
				return item


print(common_prefix(["Cyprian", "cyberotoman", "cynik", "ceniąc", "czule"]))