import urllib.request
import bs4
import re



def crawl(start_page, distance, action):
	
	visited = set()
	def scan(page, distance, action):

		if distance == 0 or page in visited: return

		visited.add(page)
		web_url = urllib.request.urlopen(page)
		html = web_url.read()
		data = bs4.BeautifulSoup(html, 'html.parser')
		text = data.get_text()
		yield action(text)

		for link in data.find_all('a'):
			try:
				scanner = scan(link.get('href'), distance - 1, action)
				for res in scanner: yield res
			except:
				continue

	return scan(start_page, distance, action)
	
	


def grep(expression):

	def match(text):
		return [ line for line in text.split('\n') if re.search(expression, line) ]
	return match




# driver code
lnk = "https://www.python.org/"
for res in crawl(lnk, 2, grep("Python")):
	print(res)
