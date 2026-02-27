import telebot
import random
from bs4 import BeautifulSoup
import requests
import pandas as pd
from logic import gen_pass
from logica import sleeping
from logicb import gen_passnow
from logicc import timeng
from logic import translator
from bro import news
from bruh import crat
bot = telebot.TeleBot("8428582508:AAEcaj3EkYP-pxS7kfGzur_dq0cUbbrDErQ")
questions = [ 
    "глобальное потепление это постоянное повышение температуры из-за вырубки лесов и добычи топлива газа, угля, нефти",
    "глобальное потепление может на нас сильно отреагировать",
    "Глобальное потепление сказывается на продовольственной и водной безопасности каждого человека. Изменение климата является непосредственной причиной деградации почв"
]
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! команды: /sleep, /start, /bye, /password, /hello, /you_are_buttefull, /super_defense_password, /time, /global_temperature, /global_temper, /global_temperut")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands={"password"})
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands={"sleep"})
def send_sleep(message):
    bot.reply_to(message, sleeping(3500))

@bot.message_handler(commands=["global_temperature"])
def randomizers(message):
    answer = random.choice(questions)
    bot.reply_to(message, answer)

@bot.message_handler(commands=["global_temper"])
def newser(message):
    bot.reply_to(message, news())

@bot.message_handler(commands=["global_temperut"])
def newseru(message):
    bot.reply_to(message, crat())

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['you_are_buttefull'])
def send_you_are_buttefull(message):
    bot.reply_to(message, "Ты прекрасен(на)")

@bot.message_handler(commands=['time'])
def send_times(message):
    bot.reply_to(message, timeng())

@bot.message_handler(commands={"super_defense_password"})
def send_super_defence_password(message):
    bot.reply_to(message, gen_passnow(50))

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'я нашел нового пользователя!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = f"voice_{message.chat.id}_{message.message_id}.ogg"
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    audio = translator(file_name)
    bot.reply_to(message, audio)
bot.infinity_polling(allowed_updates=telebot.util.update_types)