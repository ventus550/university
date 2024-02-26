
class State:
	def __init__(self, dct):
		self.content = dct
	
	def __str__(self):
		return " <" + str(self.content["whiteK"]) + str(self.content["whiteT"]) + str(self.content["blackK"]) + "> "
	
	def __getitem__(self, key):
		return self.content[key]
	def __setitem__(self, key, item):
		self.content[key] = item

def sprint(seq):
	strr = ""
	for s in seq:
		strr += str(s) 
	print("[" + strr + "]")
