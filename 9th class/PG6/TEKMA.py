a, b = map(int, input().split())
c, d = map(int, input().split())
z = 0
if a+c == b+d:
     
     e, f = map(int, input().split())
     z += e + f
     
     if e == f:
          g, h = map(int, input().split())
          z += g + h
          if g > h:
               print('domacin')
          elif g < h:
               print('gost')
     elif e > f:
          print('domacin')
     elif e < f:
          print('gost')
elif a+c > b+d:
     print('domacin')
elif a+c < b+d:
     print('gost')
     
print(a+c+b+d+z)
