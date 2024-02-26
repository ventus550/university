from queue import PriorityQueue

class Foo:
	pass


q = PriorityQueue()
for _ in range(10):
	q.put(Foo())

while not q.empty():
	q.get()