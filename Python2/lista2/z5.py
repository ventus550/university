from urllib.request import urlopen

def kompresja(tekst):	
	count = [0]; chars = [tekst[0]]

	for char in tekst:
		if char == chars[-1]:
			count[-1] += 1
		else:
			count.append(1)
			chars.append(char)
	return zip(count, chars)
		

def dekompresja(teskt_skompresowany):
	return "".join( count * char for count, char in teskt_skompresowany )


tekst = urlopen("http://textfiles.com/humor/COMPUTER/alice.txt").read().decode("utf-8")
assert(dekompresja(kompresja(tekst)))



