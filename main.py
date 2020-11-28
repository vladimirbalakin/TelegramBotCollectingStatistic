from time import sleep
from random import randint

import telebot

from config import botToken
from base import game, add, increase, returnStatistic, winner

bot = telebot.TeleBot(botToken)

@bot.message_handler(commands = ['start'])
def st(msg):
    bot.send_message(msg.chat.id, "Hello")

@bot.message_handler(commands = ['statistic'])
def coll(msg):
    bot.send_message(msg.chat.id, returnStatistic())

@bot.message_handler(commands = ['help'])
def help(msg):
    ans = ""
    for i in game:
        ans += ' /' + str(i)
    bot.send_message(msg.chat.id, ans)

@bot.message_handler(commands = ['Paper', 'Stone', 'Scissors'])
def answer(msg):
    textt = msg.text[1::]
    j = 0
    while (game[j] != textt):
        j += 1
        if (j >= len(game)):
            break

    answer = randint(0, len(game) - 1)
    while (answer == j):
        answer = randint(0, len(game) - 1)
    add(msg.chat.username)
    bot.send_message(msg.chat.id, game[answer])
    won = winner(j, answer)
    if won:
        bot.send_message(msg.chat.id, "User won")
    else:
        bot.send_message(msg.chat.id, "Bot won")
    increase(msg.chat.username, won, textt)

@bot.message_handler(content_types = ['text'])
def answer(msg):
    if msg.text in game:
        j = 0
        while (game[j] != msg.text):
            j += 1
        answer = randint(0, len(game) - 1)
        while (answer == j):
            answer = randint(0, len(game) - 1)
        add(msg.chat.username)
        bot.send_message(msg.chat.id, game[answer])
        won = winner(j, answer)
        if won:
            bot.send_message(msg.chat.id, "User won")
        else:
            bot.send_message(msg.chat.id, "Bot won")
        increase(msg.chat.username, won, msg.text)
bot.polling()