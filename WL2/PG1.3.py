#zadnji less goooo
success = 1
points=0
while points <= 20 and success !=0:
    shoottype, success = map(int, input().split())
    if shoottype == 1 and success != 0:
        points+=1
    if shoottype == 2 and success != 0:
        points+=2
    if shoottype == 3 and success != 0:
        points+=3
    
print(points)
