x=int(input())
l=int(input())
k=int(input())

if abs(x-l)>abs(x-k):
    a=abs(x-k)
elif abs(x-l)<abs(x-k):
    a=abs(x-l)
else:
    a=abs(x-l)
print(a)

b=a+abs(k-l)
print(b)


if abs(x-l)>abs(x-k) and x>k:
    print('D')
elif abs(x-l)>abs(x-k) and x<k:
    print('G')

elif abs(x-l)<abs(x-k) and x>l:
    print('D')
elif abs(x-l)<abs(x-k) and x<l:
    print('G')
else:
    if l<x:
        print('D')
    elif l>x:
        print('G')
