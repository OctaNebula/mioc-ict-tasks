classic = int(input())
notalist = []
for i in range(classic):
    a = int(input())
    notalist.append(a)
ones = notalist.count(1)
zeros = notalist.count(0)
if ones < zeros:
    for i in range(len(notalist)):
        if notalist[i] == 1:
            notalist[i] = "$"
        if notalist[i] == 0:
            notalist[i] = "#"
else:
    for j in range(len(notalist)):
        if notalist[j] == 0:
            notalist[j] = "$"
        if notalist[j] == 1:
            notalist[j] = "#"
for pljup in range(len(notalist)):
    print(notalist[pljup], end="")
