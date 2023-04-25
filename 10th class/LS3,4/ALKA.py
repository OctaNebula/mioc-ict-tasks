genericlist = []

numberofiterations = int(input())
for i in range(numberofiterations):
    value = int(input())
    genericlist.append(value)
funny = len(genericlist)
for j in genericlist:
    if not j+3 >= max(genericlist):
         funny -= 1
print(funny)