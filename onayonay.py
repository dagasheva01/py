import telegram 
import requests 
from telegram.ext import CommandHandler
from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, Filters

bot = telegram.Bot(token = '365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')

from telegram.ext import Updater
updater = Updater(token = '365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')
dispatcher = updater.dispatcher

def start(bot, update):
	text = 'Привет! Чтобы добавить свою карту Онай, наберите команду /new_card.'
	bot.sendMessage(chat_id=update.message.chat_id, text=text)

status = {
	'@user_id' : 'waiting_card'
}
cards = {
	'@user_id' : []
}

# load cards and status from json
# status.json cards.json

# def save_json()

def new_card(bot, update):	
	bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, введите номер вашей онай-карты:')
	global status
	user_id = update.message.from_user.id
	status[user_id] = 'waiting_card'

	#save_json()

status = {}
cards = {}
import json
with open('status.json', 'r') as outfile:
	status = json.load(outfile)
with open('cards.json',  'r') as outfile:
    cards = json.load(outfile)



def echo(bot, update):
	global status
	global cards
	user_id = update.message.from_user.id 
	if user_id in status:
		if status[user_id] == 'waiting_card':
			text = update.message.text
			import re
			pattern = re.compile('^\d{19}$')
			if pattern.match(text) != None:
				# card is correct, save this card
				card_number = text
				if user_id in cards:
					if card_number not in cards[user_id]:
						cards[user_id].append(card_number)

						bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена.' % card_number)
						bot.sendMessage(chat_id=update.message.chat_id, text='Для проверки баланса наберите команду /balance.')
					else:
						bot.sendMessage(chat_id=update.message.chat_id, text='Номер вашей карты уже сохранен.')
				else:
					cards[user_id] = [card_number]
					bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена' % card_number)
					bot.sendMessage(chat_id=update.message.chat_id, text='Для проверки баланса наберите команду /balance.')
				# delete current status
				del status[user_id]				
			else:
				bot.sendMessage(chat_id=update.message.chat_id, text='Неверный формат карты. Пожалуйста, введите номер карты ещё раз.')
		elif status[user_id] == 'choose_card':
			for card in cards[user_id]:
				custom_keyboard = []
				custom_keyboard.append([card])
			reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
			bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			card_number = update.message.text
			bal = get_balance(card_number)
			text ='Ваш баланс: %d тг.' % bal
			bot.sendMessage(chat_id=update.message.chat_id, text= text, reply_markup=telegram.ReplyKeyboardRemove(custom_keyboard))
		else:
			text = 'Чтобы добавить свою карту Онай, наберите команду /new_card.'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
	else:
		text = 'Чтобы добавить свою карту Онай, наберите команду /new_card.'
		bot.sendMessage(chat_id=update.message.chat_id, text=text)
	#save_json()

def get_balance(card_number):
	session = requests.Session()
	r = session.get('https://cabinet.onay.kz/')
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	csrf_token = soup.select('#csrftoken')[0]['value']
	r = session.get('https://cabinet.onay.kz/content/img/SiteLogo.png') 
	my_data = {
		'csrf' : csrf_token,
		'pan': card_number
	}
	headers = {
		''
	    'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
		'X-Requested-With':"XMLHttpRequest",
	}
	r = session.post('https://cabinet.onay.kz/check', data = my_data, headers = headers)
	result = r.json()
	balance = int(result['result']['balance'])//100
	return balance

def balance(bot, update):
	user_id = update.message.from_user.id
	n = 0
	if user_id in cards:
		n = len(cards[user_id])
		if n == 0:
			text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
			return False 
		elif n > 1:
			global status
			status[user_id] = 'choose_card'
			custom_keyboard = []
			for card in cards[user_id]:
				custom_keyboard.append([card])
			reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
			bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			card_number = update.message.text
			bal = get_balance(card_number)
			text ='Ваш баланс: %d тг.' % bal
			bot.sendMessage(chat_id=update.message.chat_id, text= text, reply_markup = telegram.ReplyKeyboardRemove(custom_keyboard))
		else:
			card_number = cards[user_id][0]
			bal = get_balance(card_number)
			text ='Ваш баланс: %d тг.' % bal
			bot.sendMessage(chat_id=update.message.chat_id, text= text)
	else:
		text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
		bot.sendMessage(chat_id=update.message.chat_id, text=text)
		return False	
	
new_card_handler = CommandHandler('new_card', new_card)
dispatcher.add_handler(new_card_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
 
balance_handler = CommandHandler('balance', balance)
dispatcher.add_handler(balance_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()