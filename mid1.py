import telegram

bot = telegram.Bot(token='247466188:AAH0lUMKLqs_K_nNDJS1FYlbGx8vXGM2ZN0')

from telegram.ext import Updater
updater = Updater(token='247466188:AAH0lUMKLqs_K_nNDJS1FYlbGx8vXGM2ZN0')
dispatcher = updater.dispatcher

def weather(bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/astana'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	
	gr = wtext[8]
	
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")
	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)

from telegram.ext import CommandHandler
start_handler = CommandHandler('weather', weather)
dispatcher.add_handler(start_handler)

weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

updater.start_polling()
