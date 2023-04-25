j1,s1=map(int,input().split())
s2,j2=map(int,input().split())
j=j1+j2
s=s1+s2
print(j, s)
if j > s:
    print('Junak')
elif j < s:
    print('Segesta')
elif j == s:
    if j2 > s1:
        print('Junak')
    elif j2 < s1:
        print('Segesta')
    else:
        print('Jedanaesterci')
