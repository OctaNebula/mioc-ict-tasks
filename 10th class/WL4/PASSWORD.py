a=input()
b=input()
c=a+b
i=0
while True:
    c+=str(int(c[-2])+int(c[-1]))[-1]
    i+=1
    if c[-2:]==a+b:
        break
print(len(c))
