def consume(person):
    return results.pop(0)
def checker(person):
    return results[0]
numberofdicethrowings = int(input())
results = []
for i in range(numberofdicethrowings):
    throw = int(input())
    results.append(throw)
totalnumber = sum(results)
Marin = 0
Stjepan = 0
Vedran = 0
#if the result is 6, consume() is called again for the same person

while results != []:
    #checks if the result is 6, if it is, the person throws again
    while checker(Marin) == 6:
        consume(Marin)
        if results == []:
            break
    Marin += consume(Marin)
    if results == []:
        break
    while checker(Stjepan) == 6:
        consume(Stjepan)
        if results == []:
            break
    Stjepan += consume(Stjepan)
    if results == []:
        break
    while checker(Vedran) == 6:
        consume(Vedran)
        if results == []:
            break
    Vedran += consume(Vedran)
print(totalnumber)
print(Marin, Stjepan, Vedran)