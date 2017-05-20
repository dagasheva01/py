import requests 
session = requests.Session()
r = session.get('https://cabinet.onay.kz/')
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
csrf_token = soup.select('#csrftoken')[0]['value']
my_data = {
	'csrf' : csrf_token,
	'pan': '9643908503306604962'
}
headers = {
	''
    'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
	'X-Requested-With':"XMLHttpRequest",
	'Cookie':"_ga=GA1.2.878194879.1488272524; PHPSESSID=5p9t3fn4o90v26fnd7i1sm5vm1; lang=ru; _pk_ref.1.4deb=%5B%22%22%2C%22%22%2C1488272550%2C%22https%3A%2F%2Fwww.google.kz%2F%22%5D; _pk_id.1.4deb=99aceb68dca3436e.1488272550.1.1488272550.1488272550.; _pk_ses.1.4deb=*"
}
r = session.post('https://cabinet.onay.kz/check', data = my_data, headers = headers)
result = r.json()
balance = int(result['result']['balance'])//100
print(balance)