import telebot
from telebot import types
import sqlite3
bot = telebot.TeleBot('7851592511:AAGbEgQhfQRW6DyQ0TLBuJlaTh2V5a1L4HY')


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('minibd.sql')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))")
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, я бот менеджер инвентаризации.\n что бы продолжить нужно авторизоватся')
    murkup = types.InlineKeyboardMarkup()
    murkup.add(types.InlineKeyboardButton('Зарегисрироваться'))
    murkup.add(types.InlineKeyboardButton('Авторизоватся'))