import telebot
from telebot import types
bot = telebot.TeleBot('7851592511:AAGbEgQhfQRW6DyQ0TLBuJlaTh2V5a1L4HY')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет")



