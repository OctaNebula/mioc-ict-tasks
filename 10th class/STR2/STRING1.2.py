score = input()

#score has format of club1 score1:score2 club2
#program prints the name of the club that won the match

score = score.replace(":"," ")
score = score.split()
if int(score[1]) > int(score[2]):
    print(score[0])
elif int(score[1]) < int(score[2]):
    print(score[3])
else:
    print("nerijeseno")