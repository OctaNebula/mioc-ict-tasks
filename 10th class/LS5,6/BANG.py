#WARNING - EXTREMELY CRINGE AND TERRIBLE CODE AHEAD


#5 player rock paper scissors
#its played by numbers 1,2,3,4,5
#1 counters 4, 1 counters 3, 2 counters 1, 2 counters 5, 3 counters 2, 3 counters 4, 4 counters 5, 4 counters 2, 5 counters 3 and 5 counters 1
#the numbers are played at the same time, the winner is the one who countered the most numbers
#the program prints how many conters each player had in the format "firstplayer secondplayer thirdplayer fourthplayer fifthplayer"

numberofrounds = int(input())
for i in range(numberofrounds):
    firstplayer, secondplayer, thirdplayer, fourthplayer, fifthplayer = map(int, input().split())
    #does the counting
    firstplayercount = 0
    secondplayercount = 0
    thirdplayercount = 0
    fourthplayercount = 0
    fifthplayercount = 0
    if firstplayer == 1:
        if secondplayer == 4 or secondplayer == 3:
            firstplayercount += 1
        if thirdplayer == 4 or thirdplayer == 3:
            firstplayercount += 1
        if fourthplayer == 4 or fourthplayer == 3:
            firstplayercount += 1
        if fifthplayer == 4 or fifthplayer == 3:
            firstplayercount += 1
    if firstplayer == 2:
        if secondplayer == 1 or secondplayer == 5:
            firstplayercount += 1
        if thirdplayer == 1 or thirdplayer == 5:
            firstplayercount += 1
        if fourthplayer == 1 or fourthplayer == 5:
            firstplayercount += 1
        if fifthplayer == 1 or fifthplayer == 5:
            firstplayercount += 1
    if firstplayer == 3:
        if secondplayer == 2 or secondplayer == 4:
            firstplayercount += 1
        if thirdplayer == 2 or thirdplayer == 4:
            firstplayercount += 1
        if fourthplayer == 2 or fourthplayer == 4:
            firstplayercount += 1
        if fifthplayer == 2 or fifthplayer == 4:
            firstplayercount += 1
    if firstplayer == 4:
        if secondplayer == 5 or secondplayer == 2:
            firstplayercount += 1
        if thirdplayer == 5 or thirdplayer == 2:
            firstplayercount += 1
        if fourthplayer == 5 or fourthplayer == 2:
            firstplayercount += 1
        if fifthplayer == 5 or fifthplayer == 2:
            firstplayercount += 1
    if firstplayer == 5:
        if secondplayer == 3 or secondplayer == 1:
            firstplayercount += 1
        if thirdplayer == 3 or thirdplayer == 1:
            firstplayercount += 1
        if fourthplayer == 3 or fourthplayer == 1:
            firstplayercount += 1
        if fifthplayer == 3 or fifthplayer == 1:
            firstplayercount += 1
    if secondplayer == 1:
        if firstplayer == 4 or firstplayer == 3:
            secondplayercount += 1
        if thirdplayer == 4 or thirdplayer == 3:
            secondplayercount += 1
        if fourthplayer == 4 or fourthplayer == 3:
            secondplayercount += 1
        if fifthplayer == 4 or fifthplayer == 3:
            secondplayercount += 1
    if secondplayer == 2:
        if firstplayer == 1 or firstplayer == 5:
            secondplayercount += 1
        if thirdplayer == 1 or thirdplayer == 5:
            secondplayercount += 1
        if fourthplayer == 1 or fourthplayer == 5:
            secondplayercount += 1
        if fifthplayer == 1 or fifthplayer == 5:
            secondplayercount += 1
    if secondplayer == 3:
        if firstplayer == 2 or firstplayer == 4:
            secondplayercount += 1
        if thirdplayer == 2 or thirdplayer == 4:
            secondplayercount += 1
        if fourthplayer == 2 or fourthplayer == 4:
            secondplayercount += 1
        if fifthplayer == 2 or fifthplayer == 4:
            secondplayercount += 1
    if secondplayer == 4:
        if firstplayer == 5 or firstplayer == 2:
            secondplayercount += 1
        if thirdplayer == 5 or thirdplayer == 2:
            secondplayercount += 1
        if fourthplayer == 5 or fourthplayer == 2:
            secondplayercount += 1
        if fifthplayer == 5 or fifthplayer == 2:
            secondplayercount += 1
    if secondplayer == 5:
        if firstplayer == 3 or firstplayer == 1:
            secondplayercount += 1
        if thirdplayer == 3 or thirdplayer == 1:
            secondplayercount += 1
        if fourthplayer == 3 or fourthplayer == 1:
            secondplayercount += 1
        if fifthplayer == 3 or fifthplayer == 1:
            secondplayercount += 1
    if thirdplayer == 1:
        if secondplayer == 4 or secondplayer == 3:
            thirdplayercount += 1
        if firstplayer == 4 or firstplayer == 3:
            thirdplayercount += 1
        if fourthplayer == 4 or fourthplayer == 3:
            thirdplayercount += 1
        if fifthplayer == 4 or fifthplayer == 3:
            thirdplayercount += 1  
    if thirdplayer == 2:
        if secondplayer == 1 or secondplayer == 5:
            thirdplayercount += 1
        if firstplayer == 1 or firstplayer == 5:
            thirdplayercount += 1
        if fourthplayer == 1 or fourthplayer == 5:
            thirdplayercount += 1
        if fifthplayer == 1 or fifthplayer == 5:
            thirdplayercount += 1
    if thirdplayer == 3:
        if secondplayer == 2 or secondplayer == 4:
            thirdplayercount += 1
        if firstplayer == 2 or firstplayer == 4:
            thirdplayercount += 1
        if fourthplayer == 2 or fourthplayer == 4:
            thirdplayercount += 1
        if fifthplayer == 2 or fifthplayer == 4:
            thirdplayercount += 1
    if thirdplayer == 4:
        if secondplayer == 5 or secondplayer == 2:
            thirdplayercount += 1
        if firstplayer == 5 or firstplayer == 2:
            thirdplayercount += 1
        if fourthplayer == 5 or fourthplayer == 2:
            thirdplayercount += 1
        if fifthplayer == 5 or fifthplayer == 2:
            thirdplayercount += 1
    if thirdplayer == 5:
        if secondplayer == 3 or secondplayer == 1:
            thirdplayercount += 1
        if firstplayer == 3 or firstplayer == 1:
            thirdplayercount += 1
        if fourthplayer == 3 or fourthplayer == 1:
            thirdplayercount += 1
        if fifthplayer == 3 or fifthplayer == 1:
            thirdplayercount += 1
    if fourthplayer == 1:
        if secondplayer == 4 or secondplayer == 3:
            fourthplayercount += 1
        if thirdplayer == 4 or thirdplayer == 3:
            fourthplayercount += 1
        if firstplayer == 4 or firstplayer == 3:
            fourthplayercount += 1
        if fifthplayer == 4 or fifthplayer == 3:
            fourthplayercount += 1
    if fourthplayer == 2:
        if secondplayer == 1 or secondplayer == 5:
            fourthplayercount += 1
        if thirdplayer == 1 or thirdplayer == 5:
            fourthplayercount += 1
        if firstplayer == 1 or firstplayer == 5:
            fourthplayercount += 1
        if fifthplayer == 1 or fifthplayer == 5:
            fourthplayercount += 1
    if fourthplayer == 3:
        if secondplayer == 2 or secondplayer == 4:
            fourthplayercount += 1
        if thirdplayer == 2 or thirdplayer == 4:
            fourthplayercount += 1
        if firstplayer == 2 or firstplayer == 4:
            fourthplayercount += 1
        if fifthplayer == 2 or fifthplayer == 4:
            fourthplayercount += 1
    if fourthplayer == 4:
        if secondplayer == 5 or secondplayer == 2:
            fourthplayercount += 1
        if thirdplayer == 5 or thirdplayer == 2:
            fourthplayercount += 1
        if firstplayer == 5 or firstplayer == 2:
            fourthplayercount += 1
        if fifthplayer == 5 or fifthplayer == 2:
            fourthplayercount += 1
    if fourthplayer == 5:
        if secondplayer == 3 or secondplayer == 1:
            fourthplayercount += 1
        if thirdplayer == 3 or thirdplayer == 1:
            fourthplayercount += 1
        if firstplayer == 3 or firstplayer == 1:
            fourthplayercount += 1
        if fifthplayer == 3 or fifthplayer == 1:
            fourthplayercount += 1
    if fifthplayer == 1:
        if secondplayer == 4 or secondplayer == 3:
            fifthplayercount += 1
        if thirdplayer == 4 or thirdplayer == 3:
            fifthplayercount += 1
        if fourthplayer == 4 or fourthplayer == 3:
            fifthplayercount += 1
        if firstplayer == 4 or firstplayer == 3:
            fifthplayercount += 1
    if fifthplayer == 2:
        if secondplayer == 1 or secondplayer == 5:
            fifthplayercount += 1
        if thirdplayer == 1 or thirdplayer == 5:
            fifthplayercount += 1
        if fourthplayer == 1 or fourthplayer == 5:
            fifthplayercount += 1
        if firstplayer == 1 or firstplayer == 5:
            fifthplayercount += 1
    if fifthplayer == 3:
        if secondplayer == 2 or secondplayer == 4:
            fifthplayercount += 1
        if thirdplayer == 2 or thirdplayer == 4:
            fifthplayercount += 1
        if fourthplayer == 2 or fourthplayer == 4:
            fifthplayercount += 1
        if firstplayer == 2 or firstplayer == 4:
            fifthplayercount += 1
    if fifthplayer == 4:
        if secondplayer == 5 or secondplayer == 2:
            fifthplayercount += 1
        if thirdplayer == 5 or thirdplayer == 2:
            fifthplayercount += 1
        if fourthplayer == 5 or fourthplayer == 2:
            fifthplayercount += 1
        if firstplayer == 5 or firstplayer == 2:
            fifthplayercount += 1
    if fifthplayer == 5:
        if secondplayer == 3 or secondplayer == 1:
            fifthplayercount += 1
        if thirdplayer == 3 or thirdplayer == 1:
            fifthplayercount += 1
        if fourthplayer == 3 or fourthplayer == 1:
            fifthplayercount += 1
        if firstplayer == 3 or firstplayer == 1:
            fifthplayercount += 1
    print(firstplayercount, secondplayercount, thirdplayercount, fourthplayercount, fifthplayercount)
    
    #i hate myself for this one
