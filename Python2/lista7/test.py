import urllib.request
import bs4
import re
import threading
from queue import Queue



def crawl(start_page, distance, action):
	
	visited = set()

	def read(url, q):
		try: q.put(urllib.request.urlopen(url).read())
		except: pass
	
	def scan(html, distance, action):

		if distance == 0: return

		data = bs4.BeautifulSoup(html, 'html.parser')
		text = data.get_text()
		yield action(text)
	

		Q = Queue()
		for url in data.find_all('a'):
			url = url.get('href')
			if url not in visited:
				visited.add(url)
				t = threading.Thread(target = read, args = (url, Q))
				t.daemon = True
				t.start()

		while not Q.empty():
			for r in scan(Q.get(), distance - 1, action): yield r


	
	for r in scan(urllib.request.urlopen(start_page).read(), distance, action): yield r
	


def grep(expression):

	def match(text):
		return [ line for line in text.split('\n') if re.search(expression, line) ]
	return match




# driver code
lnk = "https://www.python.org/"
for res in crawl(lnk, 2, grep("Python")):
	print(res)