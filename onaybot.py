import telegram 
import requests 
from bs4 import BeautifulSoup
bot = telegram.Bot(token = '365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')
from telegram.ext import Updater
updater = Updater(token = '365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')
dispatcher = updater.dispatcher
def balance(bot, update): 
 session = requests.Session()
 r = session.get('https://cabinet.onay.kz/')
 html = r.text
 soup = BeautifulSoup(html, "html.parser")
 csrf_token = soup.select('#csrftoken')[0]['value']
 r = session.get('https://cabinet.onay.kz/content/img/SiteLogo.png') 
 my_data = {
 	'csrf' : csrf_token,
 	'pan': '9643908503306604962'
 }
 headers = {
  ''
 	'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
	'X-Requested-With':"XMLHttpRequest",
 }
 r = session.post('https://cabinet.onay.kz/check', data = my_data, headers = headers)
 result = r.json()
 balance1 = int(result['result']['balance'])//100
 bot.sendMessage(chat_id=update.message.chat_id, text=balance1)
from telegram.ext import CommandHandler
balance_handler = CommandHandler('balance', balance)
dispatcher.add_handler(balance_handler)
updater.start_polling()