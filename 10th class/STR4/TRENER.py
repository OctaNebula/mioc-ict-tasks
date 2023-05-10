firstletternames = []
uniquefirstletternames = []
firstletternamescount = []
numberofnames = int(input())
#Adds the names of the players to the list
names = []
for i in range(numberofnames):
    names.append(input())
for i in names:
    firstletternames.append(i[0])
#Removes all duplicates from the list and adds it to the list uniquefirstletternames
for i in firstletternames:
    if i not in uniquefirstletternames:
        uniquefirstletternames.append(i)
#Counts the number of times each letter appears in the list firstletternames
for i in uniquefirstletternames:
    firstletternamescount.append(firstletternames.count(i))
#Removes all letters that appear less than 5 times
for i in uniquefirstletternames:
    if firstletternamescount[firstletternames.index(i)] < 5:
        uniquefirstletternames.replace(i, 0)
#Sorts the list alphabetically
uniquefirstletternames.sort()
#if the list contains a letter, joins it and prints it, otherwise prints "PREDAJA"
if uniquefirstletternames == []:
    print("PREDAJA")
else: print("".join(uniquefirstletternames))
