import random
import json

game = {"Stone": 0, "Paper": 1, "Scissors": 2}
statistic = dict()


def addUserIfItIsNotInStatistic(name):
    try:
        statistic[name]
    except KeyError:
        statistic[name] = [{}, [[0, 0] for i in range(len(game))]]


def addUserAnswerPoll(name, question, answer):
    global statistic
    statistic[name][0][question] = answer


def increaseUserStatistic(name, answer, win):
    # An name may be also an id of user
    statistic[name][1][game[answer]][0] += 1  # Added a game to user
    if win:
        statistic[name][1][game[answer]][1] += 1  # Added a win of user


def winner(user):
    """function return (True, when user won. False when bot won, an answer of a bot)"""
    bot = random.choice(list(game.keys()))
    # user - string user input
    # bot - number bot selected
    user = game[user]
    if user == 0 and game[bot] == (len(game) - 1):
        return True, bot
    if user == (len(game) - 1) and game[bot] == 0:
        return False, bot
    return (user >= game[bot]), bot


def returnStatistic():
    a = ''
    for key, value in statistic.items():
        a += str(key) + " { "
        for k, v in value[0].items():
            a += k + ' : ' + v + "\n"
        a = a[:-1:] + ' } : '
        for j in value[1]:
            a += str(j[0]) + '/' + str(j[1]) + " "
        a += "\n"
    if a == "":
        return "Users are not playing"
    return a


def returnGameArray():
    a = ''
    for key in game.keys():
        a += "/" + key
        a += " "
    if a == "":
        return "Sorry, we couldn`t find any commands"
    return a


def readFromFile():
    global statistic
    with open("st.json", "r") as input_file:
        statistic = json.load(input_file)
    input_file.close()


def writeToFile():
    with open("st.json", "w") as output_file:
        json.dump(statistic, output_file)
