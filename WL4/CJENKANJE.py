greedyprice = int(input())
betterprice = int(input())
while True:
    if greedyprice - betterprice < 10:
        print (betterprice)
        break
    greedyprice -= 10
    if greedyprice - betterprice < 10:
        print (greedyprice)
        break
    betterprice += 10