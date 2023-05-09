roundsponge = input()
roundpatrick = input()

#Replaces "x" with " " and removes any spaces before or after the "x"
if roundsponge.__contains__("x"):
    roundsponge = roundsponge.replace(" x ", " ")
    roundsponge = roundsponge.replace("x ", "")
    roundsponge = roundsponge.replace(" x", "")
if roundpatrick.__contains__("x"):
    roundpatrick = roundpatrick.replace(" x ", " ")
    roundpatrick = roundpatrick.replace("x ", "")
    roundpatrick = roundpatrick.replace(" x", "")

#Splits the string into a list of strings, ex. 1 2 3 4 becomes ["1", "2", "3", "4"]
roundsponge = roundsponge.split(" ")
roundpatrick = roundpatrick.split(" ")
roundsponge = [int(i) for i in roundsponge]
roundpatrick = [int(i) for i in roundpatrick]

#If the sum of the spongebob's points is greater than the sum of patrick's points, spongebob wins
if sum(roundsponge) > sum(roundpatrick):
    print("DA")
else:
    print("NE")