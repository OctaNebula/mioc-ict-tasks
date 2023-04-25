number = int(input())
randomvariableiusetodotuf = number
funny = 0
bags = 0
while randomvariableiusetodotuf>0:
    if randomvariableiusetodotuf % 5 == 0:
        funny+=randomvariableiusetodotuf//5
        break
    randomvariableiusetodotuf +=3
    bags+=1
if number==4 or number==7 or number<3:
    print(-1)
elif number == 3:
    print(1)
else:
    print(bags+funny)
    
