
def insert(L):
	for i in range(1, len(L)):
		x = L[i]; j = i - 1
		while j >= 0 and x < L[j]:
			L[j+1] = L[j]
			j -= 1
		L[j+1] = x
	return L


def bubble(L):
	for i in range(len(L)):
		for j in range(i+1, len(L)):
			if L[i] > L[j]:
				L[i], L[j] = L[j], L[i]
	return L

print(bubble([5, 3, 4, 6, 1, 0, 2]))