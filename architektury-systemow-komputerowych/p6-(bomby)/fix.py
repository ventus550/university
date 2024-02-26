f = open("./psol.txt")
strings = []
for line in f:
	strings += [line.strip()]
f.close()

f = open("./psol.txt", "w")
for s in strings:
	f.write(s + '\n')
f.close()

print("fixed psol")
