import telegram 
bot = telegram.Bot(token='247466188:AAH0lUMKLqs_K_nNDJS1FYlbGx8vXGM2ZN0')

from telegram.ext import Updater
updater = Updater(token='247466188:AAH0lUMKLqs_K_nNDJS1FYlbGx8vXGM2ZN0')
dispatcher = updater.dispatcher

def say_start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = "Давай начнем!")
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_start)
dispatcher.add_handler(start_handler)

def say_stop(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = "Всего доброго!")
from telegram.ext import CommandHandler
stop_handler = CommandHandler('stop', say_stop)
dispatcher.add_handler(stop_handler)

def say_salem(bot, update):
	name = update.message.from_user.first_name
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Hello, %s' % name)
from telegram.ext import CommandHandler
salem_handler = CommandHandler('Hello', say_salem)
dispatcher.add_handler(salem_handler) 

def almaty(bot, update):
	import requests
	from bs4 import BeautifulSoup 

	url = "https://sinoptik.ua/погода-алматы"
	r = requests.get(url)
	html = r.text 
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select("div.lSide div.imgBlock p")[1].text
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)
from telegram.ext import MessageHandler, Filters
almaty_handler = CommandHandler('almaty', almaty)
dispatcher.add_handler(almaty_handler) 

def astana(bot, update):
	import requests
	from bs4 import BeautifulSoup 

	url = "https://sinoptik.com.ru/погода-астана"
	r = requests.get(url)
	html = r.text 
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select("div.lSide div.imgBlock p")[1].text
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)
from telegram.ext import MessageHandler, Filters
astana_handler = CommandHandler('astana', astana)
dispatcher.add_handler(astana_handler)

def shymkent(bot, update):
	import requests
	from bs4 import BeautifulSoup 

	url = "https://sinoptik.com.ru/погода-шымкент"
	r = requests.get(url)
	html = r.text 
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select("div.lSide div.imgBlock p")[1].text
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)
from telegram.ext import MessageHandler, Filters
shymkent_handler = CommandHandler('shymkent', shymkent)
dispatcher.add_handler(shymkent_handler)

def communication(bot, update):
	if "привет" in update.message.text.lower():
		say_salem(bot, update)
		wtext ='приветствую! каких городов хочешь узнать погоду? нажми "/" и узнаю погоду: алматы, астаны, шымкента. также можно просто написать названия этих городов)' 
	elif "алматы" in update.message.text.lower():
		almaty(bot,update)
		wtext = 'надень шапку!'
	elif "астана" in update.message.text.lower():
		astana(bot,update)
		wtext = 'надень шапку!'
	elif "шымкент" in update.message.text.lower():
		shymkent(bot,update)
		wtext = 'надень шапку!'
	elif "спасибо" in update.message.text.lower():
		wtext ='обращайся!'
	elif "пока" in update.message.text.lower():
		wtext ='до скорого!'
	else:
		wtext = "%s, ой, прости, кажется какая-то ошибка!" % update.message.from_user.first_name
		bot.sendMessage(chat_id=update.message.chat_id, text=wtext)
from telegram.ext import MessageHandler, Filters
communication_handler = MessageHandler(Filters.text, communication)
dispatcher.add_handler(communication_handler)

updater.start_polling()