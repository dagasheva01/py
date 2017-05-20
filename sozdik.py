import requests
word = 'собака'
url = "https://sozdik.kz/translate/ru/kk/%s/" %word
r = requests.get(url)
data = r.json()
translation = data['translation']
from bs4 import BeautifulSoup
soup = BeautifulSoup(translation, "html.parser")
l = soup.select("span a")
for item in l:
	print(item.text)