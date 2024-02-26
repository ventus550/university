import urllib.request
import bs4
import re
from multiprocessing.pool import ThreadPool

def crawl(start_page, distance, action):
	
	visited = set()

	def read(url):
		if url in visited: return ""
		else: visited.add(url)

		try: return urllib.request.urlopen(url).read()
		except: return ""
	

	def scan(html, distance):
		data = bs4.BeautifulSoup(html, 'html.parser')
		text = data.get_text()
		yield text
	
		if distance == 0: return
		urls = [url.get('href') for url in data.find_all('a')]
		pages = ThreadPool(20).imap_unordered(read, urls)

		for p in pages:
			for r in scan(p, distance - 1): yield r			

	for text in scan(urllib.request.urlopen(start_page).read(), distance):
		res =  action(text)
		if res != []: yield res
	


def grep(expression):

	def match(text):
		return [ line for line in text.split('\n') if re.search(expression, line) ]
	return match




# driver code
lnk = "https://www.python.org/"
for res in crawl(lnk, 1, grep("Python")):
	print(res)