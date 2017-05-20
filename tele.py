import telegram

bot = telegram.Bot(token='247466188:AAH0lUMKLqs_K_nNDJS1FYlbGx8vXGM2ZN0')

from telegram.ext import Updater
updater = Updater(token='247466188:AAH0lUMKLqs_K_nNDJS1FYlbGx8vXGM2ZN0')
dispatcher = updater.dispatcher

def easy_start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Salem, Alem!")

def salem(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Aleikum asalam!")


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', easy_start)
dispatcher.add_handler(start_handler)


salem_handler = CommandHandler('salem', salem)
dispatcher.add_handler(salem_handler)

def weather(bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)

weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

def benzin(bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://helios.kz/toplivo/tseny-na-benzin/'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	lis = soup.select("#petroil-prices li")
	print(lis)
	for li in lis:
		name = li.select("span.name")[0].text
		ff = float(li.select("span.value")[0].text.replace(",", "."))
		print(name)
		bot.sendMessage(chat_id=update.message.chat_id, text="%s\t%f" % (name, ff))
	
benzin_handler = CommandHandler('benzin', benzin)
dispatcher.add_handler(benzin_handler)



updater.start_polling()