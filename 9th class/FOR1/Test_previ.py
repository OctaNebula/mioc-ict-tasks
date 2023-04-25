genericlist = []

numberstuff = int(input())
for i in range(numberstuff):
    number = int(input())
    genericlist.append(number%10)
print(sum(genericlist))
