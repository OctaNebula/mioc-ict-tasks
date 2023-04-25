classic = int(input())
notalist = []
new = []
for i in range(classic):
    a = int(input())
    notalist.append(a)
    if sum(notalist)%2==0 and i%2==0:
        new.append("$")
    if sum(notalist)%2==0 and i%2!=0:
        new.append("#")
    if sum(notalist)%2!=0 and i%2==0:
        new.append("#")
    if sum(notalist)%2==0 and i%2!=0:
        new.append("$")
for pljup in range(len(new)):
    print(new[pljup], end="")