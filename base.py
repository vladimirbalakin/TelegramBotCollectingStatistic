import random

game = {"Stone": 0, "Paper": 1, "Scissors": 2}
statistic = dict()

def addUserIfItIsNotInStatistic(id):
    try:
        statistic[id]
    except KeyError:
        statistic[id] = [[0, 0] for i in range(len(game))]

def increaseUserStatistic(id, answer, win): # An id may be also a name of user
    statistic[id][game[answer]][0] += 1 # Added a game to user
    if win:
        statistic[id][game[answer]][1] += 1 # Added a win/lose of user

def winner(user): ##function return True, when user won. False when bot won
    bot = random.choice(list(game.keys()))
    #user - string user input
    #bot - number bot selected
    user = game[user]
    if user == 0 and game[bot] == (len(game) - 1):
        return (True, bot)
    if user == (len(game) - 1) and game[bot] == 0:
        return (False, bot)
    return ((user >= game[bot]), bot)

def returnStatistic():
    a = ''
    for key, value in statistic.items():
        a += str(key) + ": "
        for j in value:
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
    with open("st.txt", "r") as input_file:
        text = input_file.read()
    statistic = eval(text)
    input_file.close()

def writeToFile():
    with open("st.txt", "w") as output_file:
        text = output_file.write(str(statistic))