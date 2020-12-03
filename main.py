#from time import sleep
from random import randint

import telebot

from base import addUserIfItIsNotInStatistic, increaseUserStatistic, winner, returnStatistic, returnGameArray
from config import botToken

bot = telebot.TeleBot(botToken)

def returnNameOrId(msg):
    if not((msg.chat.first_name is None) or (msg.chat.last_name is None)):
        return msg.chat.first_name + '_' + msg.chat.last_name
    return msg.chat.id

@bot.message_handler(commands = ['help'])
def help(msg):
    ans = returnGameArray()
    bot.send_message(msg.chat.id, ans)

@bot.message_handler(commands = ['statistic'])
def coll(msg):
    bot.send_message(msg.chat.id, returnStatistic())

@bot.message_handler(commands = ['Paper', 'Stone', 'Scissors'])
def answer(msg):
    text = msg.text[1::]
    win = winner(text)
    bot.send_message(msg.chat.id, win[1])
    if (win[0]):
        bot.send_message(msg.chat.id, "User won")
    else:
        bot.send_message(msg.chat.id, "Bot won")
    id = returnNameOrId(msg)
    addUserIfItIsNotInStatistic(id)
    increaseUserStatistic(id, text, win[0])

@bot.message_handler(content_types = ['text'])
def answer_(msg):
    pass
bot.polling()