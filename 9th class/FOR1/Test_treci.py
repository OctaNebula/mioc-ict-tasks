numberofnumbers = int(input())
epiclist = []
for i in range(numberofnumbers):
    number = int(input())
    if number % 3 == 0:
        epiclist.append(number)
numberofvalids = len(epiclist)
print(numberofvalids)