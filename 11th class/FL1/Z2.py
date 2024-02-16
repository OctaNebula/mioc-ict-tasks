mainFile = open("zadatak2a.txt", "r")
mainList = mainFile.readlines()
mainList = [i.strip() for i in mainList]
mainList = " ".join(mainList).split(" ")
mainList = [int(i) for i in mainList]

output = open("output2.txt", "w")
output.write(f"""{max((mainList))}
{min(mainList)}
{sum(mainList)}
""")

