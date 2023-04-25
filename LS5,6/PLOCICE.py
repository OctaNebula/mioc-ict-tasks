plocice = []
sortedplocice = [1, 2 ,3 ,4 ,5]
first, second, third, fourth, fifth = map(int, input().split())
plocice.append(first)
plocice.append(second)
plocice.append(third)
plocice.append(fourth)
plocice.append(fifth)
while plocice != sortedplocice:
    #if the first plocica is bigger than the second one, swap them
    if plocice[0] > plocice[1]:
        plocice[0], plocice[1] = plocice[1], plocice[0]
        print(plocice[0], plocice[1], plocice[2], plocice[3], plocice[4])
    #same for the second and third
    if plocice[1] > plocice[2]:
        plocice[1], plocice[2] = plocice[2], plocice[1]
        print(plocice[0], plocice[1], plocice[2], plocice[3], plocice[4])
    #same for third and fourth
    if plocice[2] > plocice[3]:
        plocice[2], plocice[3] = plocice[3], plocice[2]
        print(plocice[0], plocice[1], plocice[2], plocice[3], plocice[4])
    #same for fourth and fifth
    if plocice[3] > plocice[4]:
        plocice[3], plocice[4] = plocice[4], plocice[3]
        print(plocice[0], plocice[1], plocice[2], plocice[3], plocice[4])