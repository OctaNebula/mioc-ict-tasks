numberofpeople = int(input())
pizzaslices = int(input())
guyeating = 0
while pizzaslices != 0:
    pizzaslices -= 1
    guyeating += 1
    if guyeating == numberofpeople and pizzaslices != 0:
        guyeating = 0
print(guyeating)