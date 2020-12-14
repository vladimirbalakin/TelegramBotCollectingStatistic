# from time import sleep
from random import randint

import telebot

from base import addUserIfItIsNotInStatistic, increaseUserStatistic, winner, returnStatistic, returnGameArray, \
    readFromFile, writeToFile, addUserAnswerPoll
from config import botToken

bot = telebot.TeleBot(botToken)

readFromFile()


def returnNameOrId(msg):
    if not ((msg.chat.first_name is None) or (msg.chat.last_name is None)):
        return msg.chat.first_name + '_' + msg.chat.last_name
    return msg.chat.id


def returnNameOrIdPoll(msg):
    if not ((msg.user.first_name is None) or (msg.user.last_name is None)):
        return msg.user.first_name + '_' + msg.user.last_name
    return msg.user.id


closedPoll = 0
messageID = {}
questions = [["Ваш пол", "Мужской", "Женский"],
             ["Ваш возраст", "Меньше или равен 18", "Больше 18 и меньше 25", "Больше или равен 25"],
             ["Вы - нервный человек? ", "Да", "Скорее да, чем нет", "Скорее нет, чем да", "Нет"], [
                 "Что бы вы делали, если бы на вас хотел напасть некий человек(у вас с ним равные физические "
                 "показатели)",
                 "Попробовал бы договориться", "Убежал", "Встал бы в ступор", "Защитился", "Атаковал"],
             ["Вы склонны к депрессии?", "Да", "Скорее да, чем нет", "Скорее нет, чем да", "Нет"],
             ["Вы - апатичный человек?", "Да", "Скорее да, чем нет", "Скорее нет, чем да", "Нет"],
             ["Как часто вы играете в камень ножницы бумага?", "Больше 1 раза в день", "1 раз в день",
              "1 раз в неделю", "1 раз в месяц", "1 раз в год", "Меньше 1 раза в год", "Никогда"]]


@bot.message_handler(commands=['start'])
def starting(msg):
    global closedPoll, messageID, questions
    addUserIfItIsNotInStatistic(returnNameOrId(msg))
    indexes = 0
    for i in questions:
        message = bot.send_poll(msg.chat.id, i[0], i[1::], is_anonymous=False)
        messageID[message.poll.id] = indexes
        indexes += 1
        while messageID[message.poll.id] != -1:
            pass
    ans = returnGameArray()
    bot.send_message(msg.chat.id, ans)


@bot.poll_answer_handler()
def answering(msg):
    global closedPoll, questions
    if msg.poll_id in messageID.keys():
        name = returnNameOrIdPoll(msg)
        closedPoll = messageID[msg.poll_id]
        addUserAnswerPoll(name, questions[closedPoll][0], questions[closedPoll][msg.options_ids[0] + 1])
        messageID[msg.poll_id] = -1


@bot.message_handler(commands=['help'])
def helping(msg):
    ans = returnGameArray()
    bot.send_message(msg.chat.id, ans)


@bot.message_handler(commands=['statistic'])
def coll(msg):
    bot.send_message(msg.chat.id, returnStatistic())


@bot.message_handler(commands=['Paper', 'Stone', 'Scissors'])
def answer(msg):
    if msg.text[-24::] == "@CollectingStatisticsBot":
        text = msg.text[:-24:]
        text = text[1::]
    else:
        text = msg.text[1::]
    win = winner(text)
    bot.reply_to(msg, win[1])
    # bot.send_message(msg.chat.id, win[1])
    if (win[0]):
        bot.reply_to(msg, "User won")
    else:
        bot.reply_to(msg, "Bot won")
    id = returnNameOrId(msg)
    addUserIfItIsNotInStatistic(id)
    increaseUserStatistic(id, text, win[0])
    writeToFile()


@bot.message_handler(content_types=['text'])
def answer_(msg):
    pass


bot.polling()
