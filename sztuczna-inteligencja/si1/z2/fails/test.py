from time import time
def timeit(f):
	s = time()
	r = f(100)
	e = time()
	print(e-s, r)

def waste_time():
	for i in range(10):
		pass
#----------------------------------
class Memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memo
def A(n):
	if n == 0 or n == 1:
		return 1
	waste_time()
	return A(n-1) + A(n-2)



#-------------------to samo, ale ze słownikiem-----------------------------
MEMO = dict()
def B(n):
	if n in MEMO:
		return MEMO[n]
	if n == 0 or n == 1:
		return 1
	r = B(n-1) + B(n-2)
	MEMO[n] = r
	waste_time()
	return r


timeit(A)
timeit(B)

