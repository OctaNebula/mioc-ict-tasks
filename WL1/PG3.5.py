a = int(input())
bina = bin(a)[2:].zfill(0)
gaming = []
numberofnums = 0
gaming = [int(x) for x in str(bina)]
while max(gaming) > 0:
    gaming.remove(max(gaming))
    numberofnums += 1
    if gaming == []:
        break

print(numberofnums)
