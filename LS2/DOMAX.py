n = int(input())
x = ()
x = input()
num = x.split(" ")
a = max(num)
while num.__contains__(a):
    num.remove(max(num))
if len(num) != 0:
    print(max(num))
else:
    print("0")