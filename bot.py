#import telebot

#bot = telebot.TeleBot('7746187663:AAEjMnSkkab0bzOWkCH2VechJp5KY_rQSyw')

#@bot.message_handler(commands=['meme'])
#def send_meme(message):
#    with open('images\cat.png', 'rb') as f:
#        bot.send_photo(message.chat.id, f)

#@bot.message_handler(commands=['start'])
#def start_command(message):
#    bot.send_message(message.chat.id, 'Привет используй команду /meme чтобы получить мем')

#bot.polling()
import telebot
import os, random

bot = telebot.TeleBot('7746187663:AAEjMnSkkab0bzOWkCH2VechJp5KY_rQSyw')

@bot.message_handler(commands=['meme'])
def send_meme(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['ameme'])
def send_meme(message):
    img_name = random.choice(os.listdir('animal'))
    with open(f'animal/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Привет используй команду /meme чтобы получить мем')
