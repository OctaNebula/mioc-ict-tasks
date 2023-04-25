#caegns
cup = int(input())
move = ()
while move != "G":
    move = input()
    if move == "L" and cup - 1 != 0:
            cup-=1
    elif move == "D" and cup + 1 != 4:
            cup+=1
print(cup)
