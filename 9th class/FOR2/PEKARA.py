n = int(input())
f = 0
h = 0
for i in range(n):
    a = str(input())
    b = str(input())
    t = int(input())
    d = str(input())
    B = int(input())
    if a==b and d==a and t==B:
        f+=0
        h+=0
    elif(a==b and d==a and t<B):
        f+=1
    elif(a==b and d==a and B<t):
        h+=1
    elif (a==b): f+=1
    elif(d==a): h+=1

print("Tom:",f,sep="")
print("Brad:",h,sep="")
