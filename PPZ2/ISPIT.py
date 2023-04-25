numberoftasks = int(input())
positivescore = int(input())
negativescore = int(input())
neutralscore = 0
numberoffriends = int(input())
friendscores = [int(x) for x in input().split()]
#checks if its possible to get the friends total scores
#in other words, tries to construct the friends scores using the positivescore and negativescore
#prints how many friends are impossible to get
#then it prints the highest possible score from the friendlist list

def checkifpossible(friendscores, positivescore, negativescore):
    impossible = 0
    for i in range(len(friendscores)):
        if friendscores[i] > positivescore:
            impossible += 1
        elif friendscores[i] < negativescore:
            impossible += 1
    return impossible
impossibles = checkifpossible(friendscores, positivescore, negativescore)
print(impossibles)
def gethighestscore(friendscores, positivescore, negativescore):
    highestscore = 0
    for i in range(len(friendscores)):
        if friendscores[i] > 0:
            highestscore += positivescore
        elif friendscores[i] < 0:
            highestscore += negativescore
    return highestscore
highestscore = gethighestscore(friendscores, positivescore, negativescore)
print(highestscore)