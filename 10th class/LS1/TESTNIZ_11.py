classic = int(input())
origigilist = []
comparisonlist = []
for i in range(classic):
    a = int(input())
    origigilist.append(a)
avgnum = sum(origigilist)/len(origigilist)
for _ in range(len(origigilist)):
    if origigilist[_] > avgnum:
        comparisonlist.append("$")
    else:
        comparisonlist.append("#")
for pljup in range(len(comparisonlist)):
    print(comparisonlist[pljup], end="")