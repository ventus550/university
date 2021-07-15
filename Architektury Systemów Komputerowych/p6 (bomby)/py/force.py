import subprocess
import sys
from itertools import combinations_with_replacement as cwr
from itertools import permutations as prm

strings = []
# ---------------- 1
# f = open("./strings.txt")
# strings = []
# for line in f:
# 	strings += [line.strip()]
# f.close()

# --------------- 3
mp = {
	0: "424",
	1: "119",
	2: "134",
	3: "947",
	4: "930",
	5: "526",
	6: "353",
	7: "858"
}


# for i in range(8):
# 	for j in range(1000):
# 		strings += [str(i) + " " + str(j) + mp[i]]


# --------------- 4

# for i in range(1000):
# 	for j in range(1000):
# 		strings += [str(i) + " " + str(j)]

# --------------- 5
# chars = "qwertyuiopasdfghjklzxcvbnm"
# strings = ["".join(t) for t in cwr(chars, 6)]

# --------------- 6
# r = range(10)
# chars = "123456"
# strings = [" ".join(t) for t in prm(chars)]

# --------------- 7
strings = [str(i) for i in range(100)]

def bomb(txt):

	win = open("./win.txt")
	inp = open("./psol.txt", "w")

	for line in win:
		inp.write(line)
	inp.write(txt + '\n')

	inp.close()
	win.close()

	res = subprocess.run(["./bomb", "psol.txt"], stdout=subprocess.PIPE)
	if "BOOM!!!" in str(res.stdout):
		print(txt, "=> failed")
	else:
		print(txt, "=> success")
		win = open("./win.txt", "a")
		win.write(txt + '\n')
		win.close()

for s in strings:
	bomb(s)




# bomb("You can Russia from land here in Alaska.")


