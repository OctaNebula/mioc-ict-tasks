numberofplayers = int(input())
playerscores = []
playerwins = 0
check = True
#a player can win a minimum of 1 point and a maximum of depending on the number of players
#the best player gets the maximum number of points, the second one less and so on to the last one, who gets 1 point
#the task of this program is to calculate how many players had a chance of winning
for i in range(numberofplayers):
    playerscores.append(int(input()))
while check == True:
    check = True
    for i in range(numberofplayers):
        for j in range(numberofplayers):
            if playerscores[i] > max(playerscores)+1:
                playerscores[i] -=1
        else:
            check = False
        if check == True:
            playerwins +=1
print(playerwins)


#unfinished lol