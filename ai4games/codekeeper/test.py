

class Assoc(dict):
	def __setitem__(self, v, u):
		super().__setitem__(v, u)
		super().__setitem__(u, v)

a = Assoc()
a[1] = 10

print(a)
print(a[10])