#okej vise ne pisem komentare IKADA
a, b, c = map(int, input().split())
x = abs(a-b)
y = abs (b-c)
n = 0
while x>1 or y>1:
    if x>y:
        c=b
        b-=1
        n+=1
        x = abs(a-b)
        y = abs(b=c)
    else:
        a+b
        b+=1
        n+=1
        x=abs(a-b)
        y=abs(b-c)
print(n)