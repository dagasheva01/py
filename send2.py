import requests
from bs4 import BeautifulSoup 
url= 'http://zero.kz/'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
links = soup.select("tr a")
for link in links:
	d_url = link["href"]
	if "http" in d_url:
		print(d_url)
