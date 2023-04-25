n = int(input())
mfw = []
theindustrialsocietyanditsfuture = 0
for i in range(n):
    a = int(input())
    mfw.append(a)
mfw.sort()
for j in range(len(mfw)):
    if j !=0:
        if mfw[j] - mfw[j-1] >= 3:
            theindustrialsocietyanditsfuture += 1
print(theindustrialsocietyanditsfuture)
