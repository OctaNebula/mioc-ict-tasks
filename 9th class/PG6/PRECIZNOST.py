a=float(input())
b=float(input())
c=float(input())


if abs(a+b-c)<0.000001:
     print('=')
elif a+b<c:
     print('<')
elif a+b>c:
     print('>')
