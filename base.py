game = ['Stone', 'Paper', 'Scissors']
m = len(game)
statistic = [['', [[0, 0] for i in range(m)]]]
#print(statistic)
n = 1
def add(name):
    if name == "" or name == None:
        name = "Pearson wihtout nickname"
    global n, m, statistic
    #print(n, m, name, statistic)
    i = 0
    while (statistic[i][0] != name) and (i < n):
        i += 1
        if (n <= i):
            break
    if i != n:
        return
    statistic.append([name, [[0, 0] for i in range(m)]])
    n += 1
def increase(name, win, turn):
    if name == "" or name == None:
        name = "Pearson wihtout nickname"
    global n, m, statistic
    i = 0
    while (statistic[i][0] != name) and (i < n):
        i += 1
        if (n <= i):
            break
    j = 0
    while (game[j] != turn) and (j < m):
        j += 1
        if (m <= j):
            break
    if j == m or i == n:
        return
    statistic[i][1][j][1] += int(win)
    statistic[i][1][j][0] += 1
def returnStatistic():
    global statistic
    print(statistic)
    ans = ''''''
    for i in statistic[1::]:
        ans += i[0]
        ans += ': '
        for j in i[1]:
            ans += str(j[0]) + '/' + str(j[1]) + ' '
        ans += '\n'
    return ans

def winner(j, answer):
    global game, m
    if (j == 0 and answer == m - 1):
        return True
        return
    if (answer == 0 and j == m - 1):
        return False
        return
    return j > answer