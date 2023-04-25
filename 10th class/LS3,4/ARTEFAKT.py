n = int(input())
mfw = []
unique = []
for i in range(n):
    a = int(input())
    mfw.append(a)
for j in mfw:
    if mfw.count(j) == 1:
        unique.append(j)
unique.sort()
if unique != []:
    print(unique[0])
else: print ("0")