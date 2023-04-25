def zbrojznamenki(n):
  stringstvar = str(n)
  sum = 0
  for znamenka in stringstvar:
    sum += int(znamenka)

  return sum

result = zbrojznamenki(12345)
print(result)
