def test(a, b, c):
  diskriminanta = b**2 - 4*a*c
  if diskriminanta < 0:
    return False
  if diskriminanta == 0:
    return True
  if diskriminanta > 0:
    return True

print(test(1, 2, 3))
print(test(1, -1, -2))
print(test(1, -4, 4)) 
