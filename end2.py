import requests
from bs4 import BeautifulSoup
from urllib.parse import *
start_url = "https://yvision.kz"

counters = []

def parse_url(url):
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	text = soup.select("body")[0].text
	base_url = url
	#page_counter = count_words(text)
	#global counters
	#counters.append(page_counter)
	links = soup.select('a')
	for link in links:
		if link.has_attr('href'):
			href = link["href"]
			#соединяем URL если он не был абсолютным 
			new_url = urljoin(base_url, href, allow_fragments = False)
			new_url = urldefrag(new_url).url
			print(new_url)

parse_url(start_url)
