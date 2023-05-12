numberofquestions = int(input())
questionabcanswers = input()
questionabcanswers = list(questionabcanswers)

#compares the questionabcanswers to the following orders: ABCABCABC... BABCBABC... CCAABBCCAABB... and counts the number of correct answers
#generates lists using the rows and numberofquestions

#ABCABCABC...
ABCABCABC = []
for i in range(numberofquestions):
    if i % 3 == 0:
        ABCABCABC.append("A")
    elif i % 3 == 1:
        ABCABCABC.append("B")
    elif i % 3 == 2:
        ABCABCABC.append("C")
#BABCBABC...
BABCBABC = []
for i in range(numberofquestions):
    if i % 2 == 0:
        BABCBABC.append("B")
    elif i % 4 == 1:
        BABCBABC.append("A")
    elif i % 4 == 3:
        BABCBABC.append("C")
#CCAABBCCAABB...
CCAABBCCAABB = []
for i in range(numberofquestions):
    if i % 6 == 0 or i % 6 == 1:
        CCAABBCCAABB.append("C")
    elif i % 6 == 2 or i % 6 == 3:
        CCAABBCCAABB.append("A")
    elif i % 6 == 4 or i % 6 == 5:
        CCAABBCCAABB.append("B")
#counts the number of correct answers
ABCABCABCcorrect = 0
BABCBABCcorrect = 0
CCAABBCCAABBcorrect = 0
for i in range(numberofquestions):
    if questionabcanswers[i] == ABCABCABC[i]:
        ABCABCABCcorrect += 1
    if questionabcanswers[i] == BABCBABC[i]:
        BABCBABCcorrect += 1
    if questionabcanswers[i] == CCAABBCCAABB[i]:
        CCAABBCCAABBcorrect += 1
#finds the maximum number of correct answers, and prints it alongside with the winner

maximumcorrect = max(ABCABCABCcorrect, BABCBABCcorrect, CCAABBCCAABBcorrect)
print(maximumcorrect)
if ABCABCABCcorrect == maximumcorrect:
    print("Adrian")
if BABCBABCcorrect == maximumcorrect:
    print("Bruno")
if CCAABBCCAABBcorrect == maximumcorrect:
    print("Goran")