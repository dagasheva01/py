import telegram

bot = telegram.Bot(token='365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')

from telegram.ext import Updater
updater = Updater(token='365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')
dispatcher = updater.dispatcher

def salam(bot, update):
	name = update.message.from_user.first_name
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Приветствую, %s' % name)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Из какого вы города?")
from telegram.ext import CommandHandler
salem_handler = CommandHandler('start', salam)
dispatcher.add_handler(salem_handler) 

def almaty(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text	
	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)
	gr = wtext[8]
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")

from telegram.ext import CommandHandler
almaty_handler = CommandHandler('almaty', almaty)
dispatcher.add_handler(almaty_handler)


def aktau(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/aktau'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text	
	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)
	gr = wtext[8]
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")

from telegram.ext import CommandHandler
aktau_handler = CommandHandler('aktau', aktau)
dispatcher.add_handler(aktau_handler)

def astana(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/astana'
	r=requests.get(url)
	html=r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text	
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
	gr = wtext[8]
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")

from telegram.ext import CommandHandler
astana_handler = CommandHandler('astana', astana)
dispatcher.add_handler(astana_handler)

def taldykorgan(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://www.kazhydromet.kz/ru/toldykorgan'
	r=requests.get(url)
	html= r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text	
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
	gr = wtext[8]
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")

from telegram.ext import CommandHandler
taldyk_handler = CommandHandler('taldykorgan', taldykorgan)
dispatcher.add_handler(taldyk_handler)

def atyrau(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/atyrau'
	r=requests.get(url)
	html= r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text	
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
	gr = wtext[8]
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")

from telegram.ext import CommandHandler
atyrau_handler = CommandHandler('atyrau', atyrau)
dispatcher.add_handler(atyrau_handler)


def shymkent(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/shymkent'
	r=requests.get(url)
	html= r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text	
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
	gr = wtext[8]
	ww = int(wtext[9])
	if ww>0 and ww<10 and gr=="+":
		bot.sendMessage(chat_id=update.message.chat_id, text="Погода хорошая, можно без шапки")
	elif ww>0 and ww<10 and gr=='-':
		bot.sendMessage(chat_id=update.message.chat_id, text="Немножко прохладно, оденьте шапку")

from telegram.ext import CommandHandler
shymkent_handler = CommandHandler('shymkent', shymkent)
dispatcher.add_handler(shymkent_handler)

def john(bot, update):
	if "алматы" in update.message.text.lower():
		almaty(bot,update)
	elif "актау" in update.message.text.lower():
		aktau(bot, update)
		
	elif "астана" in update.message.text.lower():
		astana(bot,update)

	elif "талдыкорган" in update.message.text.lower():
		taldykorgan(bot, update)

	elif "атырау" in update.message.text.lower():
		atyrau(bot, update)
		
	elif "шымкент" in update.message.text.lower():
		shymkent(bot,update)
		
	elif "спасибо" in update.message.text.lower():
		bot.sendMessage(chat_id=update.message.chat_id, text="обращайтесь!")
	elif "пока" in update.message.text.lower():
		bot.sendMessage(chat_id=update.message.chat_id, text="до свидания!")
	else :
		bot.sendMessage(chat_id = update.message.chat_id, text = "404 еррор, чау")
from telegram.ext import MessageHandler, Filters
john_handler = MessageHandler(Filters.text, john)
dispatcher.add_handler(john_handler)

updater.start_polling()
