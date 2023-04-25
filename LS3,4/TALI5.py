#tali5

for i in range(3):
    a1, a2, a3, a4 = map(int, input().split())
    b1, b2, b3, b4 = map(int, input().split())
    c1, c2, c3, c4 = map(int, input().split())
    listA = [a1, a2, a3, a4]
    listB = [b1, b2, b3, b4]
    listC = [c1, c2, c3, c4]
    
    #checks who has an unique number in their list, if two have it then the first one alphabetically wins
    if listA.count(1) == 1 and listA.count(3) == 1 and listA.count(4) == 1 and listA.count(6) == 1:
        print("A")
    elif listB.count(1) == 1 and listB.count(3) == 1 and listB.count(4) == 1 and listB.count(6) == 1:
        print("B")
    elif listC.count(1) == 1 and listC.count(3) == 1 and listC.count(4) == 1 and listC.count(6) == 1:
        print("C")
    # if no one has an unique number, the player with the highest sum of numbers wins
    else:
        if sum(listA) > sum(listB) and sum(listA) > sum(listC):
            print("A")
        elif sum(listB) > sum(listA) and sum(listB) > sum(listC):
            print("B")
        elif sum(listC) > sum(listA) and sum(listC) > sum(listB):
            print("C")
        #if two players have the same sum, the first one alphabetically wins
        else:
            if sum(listA) == sum(listB):
                print("A")
            elif sum(listA) == sum(listC):
                print("A")
            elif sum(listB) == sum(listC):
                print("B")
    
    #clears the lists for repetition
    listA.clear()
    listB.clear()
    listC.clear()

