
def is_palindrom(text):
	banned = "!\",.;: `'"
	text = "".join([ ch for ch in text.lower().strip() if ch not in banned ])

	for i in range(len(text) // 2):
		if text[i] != text[-i-1]:
			return False
	return True


print(is_palindrom("Kobyła ma mały bok."))
print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))