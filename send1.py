import requests
from bs4 import BeautifulSoup 
url= 'http://sozdik.kz/'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
wtext = soup.select("body")[0].text
if "ә" in wtext :
	if "і" in wtext:
		if "ң" in wtext:
			if "ғ" in wtext:
				if "ү" in wtext:
					if "қ" in wtext:
						if "ө" in wtext:
							if "kz" or "kk" in url:
								print("YES")
else:
	print("NO")