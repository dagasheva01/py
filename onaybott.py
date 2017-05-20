import telegram 
import requests 
import re
import json
from telegram.ext import CommandHandler
from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, Filters
def load_status():
	with open('status.json', 'r') as outfile:
		status = json.load(outfile)
		return status

def save_status(status):
	with open('status.json', 'w') as outfile:
		json.dump(status, outfile)

def load_cards():
	with open('cards.json', 'r') as outfile:
		cards = json.load(outfile)
		return cards


def save_cards(cards):
	with open('cards.json', 'w') as outfile:
		json.dump(cards, outfile)


bot = telegram.Bot(token = '365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')

from telegram.ext import Updater
updater = Updater(token = '365630534:AAEAxv6IzH4yYDqobJ-6bOyHt4RAwPURiIs')
dispatcher = updater.dispatcher

from logic import *

def start(bot, update):
	text = 'Привет! Чтобы добавить свою карту Онай, наберите команду /new_card.'
	bot.sendMessage(chat_id=update.message.chat_id, text=text)



card_type_keyboard = [['Единая транспортная карта (ЕТК)'], ['Карта школьника'], ['Карта студента'], ['Социальная карта']]

def new_card(bot, update):
	status = load_status()
	cards = load_cards()
	user_id = update.message.from_user.id
	status[user_id] = 'choose_type'	
	save_status(status)
	global card_type_keyboard
	bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, Выберите вашу карту:', reply_markup = telegram.ReplyKeyboardMarkup(card_type_keyboard))	

def echo(bot, update):
	status = load_status()
	cards = load_cards()
	global card_type_keyboard	
	user_id = str(update.message.from_user.id)
	if user_id in status:
		if status[user_id] == 'choose_type':
			numberMask = 0
			card = update.message.text
			if card == 'Единая транспортная карта (ЕТК)':
				numberMask = '96431085033'
			elif card == 'Карта школьника' or card == 'Карта студента' or card == 'Социальная карта':
				numberMask = '96439085033'
			else:
				bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, Выберите вашу карту:')
				return echo
			if user_id not in cards:
				cards[user_id] = []
			cards[user_id].append(numberMask)
			status[user_id] = 'waiting_card'
			save_status(status)
			save_cards(cards)
			bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, введите последние 8 цифр вашей онай-карты:', reply_markup = telegram.ReplyKeyboardRemove())
		elif status[user_id] == 'waiting_card':
			numberMask = cards[user_id][-1]
			print(numberMask)
			text = numberMask + update.message.text
			pattern = re.compile('^\d{19}$')
			if pattern.match(text) != None: 	
				card_number = text
				exist = check_card(card_number)
				if exist == True:
					if user_id in cards:
						if card_number not in cards[user_id]:
							cards[user_id][-1] = card_number
							bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена.' % card_number)
							bot.sendMessage(chat_id=update.message.chat_id, text='Для проверки баланса наберите команду /balance.')
							save_cards(cards)
						else:
							del cards[user_id][-1]
							save_cards(cards)
							bot.sendMessage(chat_id=update.message.chat_id, text='Номер вашей карты уже сохранен.')
					else:
						cards[user_id] = [card_number]
						bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена' % card_number)
						bot.sendMessage(chat_id=update.message.chat_id, text='Для проверки баланса наберите команду /balance.')
						save_cards(cards)
					del status[user_id]		
					save_status(status)		
				else:
					bot.sendMessage(chat_id=update.message.chat_id, text='Карты с таким не существует. Пожалуйста, введите номер карты ещё раз.')
			else:
				bot.sendMessage(chat_id=update.message.chat_id, text='Неверный формат карты. Пожалуйста, введите номер карты ещё раз.')
		elif status[user_id] == 'waiting_balance':
			card_number = update.message.text
			custom_keyboard = []
			for card in cards[user_id]:
				custom_keyboard.append([card])
			if card_number not in cards[user_id]:
				reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
				bot.sendMessage(chat_id=update.message.chat_id, text= 'Выберите одну из карт ниже', reply_markup=telegram.reply_markup())
			else:
				bal = get_balance(card_number)
				bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваш баланс: %d тг.' % bal, reply_markup=telegram.ReplyKeyboardRemove())
			del status[user_id]
			save_status(status)
		else:
			text = 'Чтобы добавить свою карту Онай, наберите команду /new_card. 143'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
	else:
		text = 'Чтобы добавить свою карту Онай, наберите команду /new_card. 146'
		bot.sendMessage(chat_id=update.message.chat_id, text=text)

def balance(bot, update):
	status = load_status()
	cards = load_cards()
	user_id = str(update.message.from_user.id)
	n = 0
	if status[user_id] != None:
		bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, введите последние 8 цифр вашей онай-карты:')
		
	else:
		if user_id in cards:
			n = len(cards[user_id])
			if n == 0:
				text = 'У нас нет сохраненных карт, добавьте их с помощью команды /new_card'
				bot.sendMessage(chat_id=update.message.chat_id, text=text)
			elif n > 1:
				status[user_id] = 'waiting_balance'
				status = save_status(status)
				custom_keyboard = []
				for card in cards[user_id]:
					custom_keyboard.append([card])
				reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
				bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			else:
				card_number = cards[user_id][0]
				bal = get_balance(card_number)
				bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваш баланс: %d тг.' % bal)
				del status[user_id]
				status = save_status(status)
		else:
			text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
			return False	

def delete(bot, update):

	user_id = str(update.message.from_user.id)
	n = 0
	if user_id in cards:
		print('enter')
		n = len(cards[user_id])
		if n == 0:
			text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
			return False 
		elif n > 1:
			status[user_id] = 'choose_card'
			custom_keyboard = []
			for card in cards[user_id]:
				custom_keyboard.append([card])
			reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
			bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			card_number = update.message.text
			cards[user_id].remove(card_number)
			save_cards(cards)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваша карта была успешна удалена.', reply_markup = telegram.ReplyKeyboardRemove(custom_keyboard))
		else:
			del cards[user_id]
			save_cards(cards)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваша карта была успешна удалена.')
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


delete_handler = CommandHandler('delete', delete)
dispatcher.add_handler(delete_handler)

updater.start_polling()


