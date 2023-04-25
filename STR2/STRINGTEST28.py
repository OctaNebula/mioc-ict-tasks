thing = input()

thinglist = thing.split()

#sorts the list by the ammount of letters in each word

thinglist.sort(key=len)

for i in thinglist:
    print(i)