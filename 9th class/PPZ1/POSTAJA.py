z = int(input()) #sci number
k = int(input()) #their weight
x = int(input()) #data's weight
y = int(input()) #kireek's weight

if z < 9 and (k + x + y) <= 1000:
    print(z + 2)
    print(k + x + y)
elif z < 9 and (k + x ) > 1000 and (k + z) > 1000:
    print(z)
    print(k)
    #thebestending
elif z < 9 and ((k + x <= 1000) or (k + z <= 1000)):
    if x > z:
        passanger = z
    elif z > x:
        passanger = x
    if passanger + k <= 1000:
        print(z+1)
        print(passanger + k)
    elif passanger + k > 1000:
        print(z)
        print(k)

elif z == 9:
    if x > z:
            passanger = z
    elif z > x:
        passanger = x
if passanger + k <= 1000:
        print("10")
        print(passanger + k)
elif passanger + k > 1000:
        print("9")
        print(k)
    #the good ending
elif z == 10:
        print("10")
        print(k)