numberofplayers = int(input())
playersfirstletters = []
#appends the first letter of each player's name to the list
for i in range(numberofplayers):
    playersfirstletters.append(input()[0])
#removes the letters that appear less than 5 times
for i in playersfirstletters:
    if playersfirstletters.count(i) < 5:
        while i in playersfirstletters:
            playersfirstletters.remove(i)
#gets rid of the duplicates
for i in playersfirstletters:
    while playersfirstletters.count(i) != 1:
        playersfirstletters.remove(i)
#sorts the list alphabetically
playersfirstletters.sort()
for i in playersfirstletters:
    print(i, end = "")