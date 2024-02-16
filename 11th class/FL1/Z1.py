mainFile = open("zadatak1a.txt", "r")
mainList = mainFile.readlines()
mainList = [i.strip() for i in mainList]
mainList = " ".join(mainList).split(" ")
evens = []

for i in mainList:
    if int(i) % 2 == 0:
        evens.append(i)

output = open("output.txt", "w")
output.write(" ".join(evens))