import urllib.request
import bs4
import re
import threading
from queue import Queue



def crawl(start_page, distance, action):
	
	Q = Queue()
	lock = threading.Lock()
	visited = set()
	
	def scan(page, distance, action):

		lock.acquire()
		if distance == 0 or page in visited:
			return
		visited.add(page)
		lock.release()


		try: web_url = urllib.request.urlopen(page)
		except: return
		
		html = web_url.read()
		data = bs4.BeautifulSoup(html, 'html.parser')
		text = data.get_text()
		Q.put(action(text))
	

		for link in data.find_all('a'):
			t = threading.Thread(target = scan, args = (link.get('href'), distance - 1, action))
			t.daemon = True
			t.start()


	scan(start_page, distance, action)
	while not Q.empty(): yield Q.get()
	


def grep(expression):

	def match(text):
		return [ line for line in text.split('\n') if re.search(expression, line) ]
	return match




# driver code
lnk = "https://www.python.org/"
for res in crawl(lnk, 2, grep("Python")):
	print(res)