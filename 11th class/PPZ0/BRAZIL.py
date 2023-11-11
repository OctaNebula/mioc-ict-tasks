# this task doesn't even require matrixes lol

# inputs scores into the list

numberOfInputs = int(input())
scores = []
for i in range(numberOfInputs):
    scores.append(input())

# finds the most frequent score

max = 0
maxscore = ()
largestGuest = 0
largestGuestScore = ()
sum = 0
sumScore = ()
sameScoresCheck = False


for i in scores:
    scores.count(i)
    if scores.count(i) > max:
        max = scores.count(i)
        maxscore = i
    if int(i[2]) > largestGuest:
        largestGuest = int(i[2])
        largestGuestScore = i
    if int(i[0]) + int(i[2]) > sum:
        sum = int(i[0]) + int(i[2])
        sumScore = i
        sameScoresCheck = False
    elif int(i[0]) + int(i[2]) == sum:
        sameScoresCheck = True

if max == 1 and sameScoresCheck == False:
    print(sumScore)

# if max = 1, prints the largest guest score

elif max == 1 and sameScoresCheck == True:
    print(largestGuestScore)

# otherwise just prints the most frequent score

else:
    print(maxscore)

# bam it's done

# lol what a free task