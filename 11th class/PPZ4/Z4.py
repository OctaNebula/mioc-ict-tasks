file = open('Ulaz4.txt', 'r')

ncontestants = int(file.readline())

contestants = []
scores = []

for i in range(ncontestants):
    contestants.append(file.readline().strip().split())

for i in range(ncontestants):
    scores.append(file.readline().strip().split())

for i in range(ncontestants):
    scores[i] = int(scores[i][0])

leaderboard = {}

for i in range(ncontestants):
    leaderboard[contestants[i][0]] = scores[i]

leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

output = open('Izlaz4.txt', 'w')

for i in range(ncontestants):
    output.write(list(leaderboard.keys())[i] + ' ' + str(list(leaderboard.values())[i]) + '\n')