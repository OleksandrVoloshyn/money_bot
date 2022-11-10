import os

import telebot
from dotenv import load_dotenv

from currency import get_interbank, get_black_store, get_bitcoin

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def menu(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('/interbank')
    keyboard.row('/black_store')
    keyboard.row('/bitok')
    bot.send_message(message.chat.id, "Hi there, I am CourseBot. I am here to give u course of money!",
                     reply_markup=keyboard)


@bot.message_handler(commands=['interbank'])
def echo_message(message):
    res_msg = get_interbank()
    bot.reply_to(message, res_msg)


@bot.message_handler(commands=['black_store'])
def echo_message(message):
    res_msg = get_black_store()
    bot.reply_to(message, res_msg)


@bot.message_handler(commands=['bitok'])
def echo_message(message):
    res_msg = get_bitcoin()
    bot.reply_to(message, res_msg)


if __name__ == '__main__':
    bot.infinity_polling()
