numberofthings = int(input())

ivicalist = []

maricalist = []

for i in range(numberofthings - 1):
    dice = int(input())
    ivicalist.append(dice)
    if dice == 6:
        while dice == 6:
            dice = int(input())
            ivicalist.append(dice)
    dice = int(input())
    maricalist.append(dice)
    if dice == 6:
        while dice == 6:
            dice = int(input())
            maricalist.append(dice)

if numberofthings % 2 == 1:
    print("MARICA")
elif numberofthings % 2 == 0:
    print("IVICA")

ivicapos = sum(ivicalist)
maricapos = sum(maricalist)

if sum(ivicalist) == maricalist:
    if numberofthings % 2 == 1:
        maricapos = 0
    elif numberofthings % 2 == 0:
        ivicapos = 0


print(ivicapos)

print(maricapos)