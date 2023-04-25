def prim(n):
  # Return False if n is less than 2
  if n < 2:
    return False

  # Loop through the possible divisors of n, starting from 2
  for i in range(2, n):
    # If n is divisible by i, it is not prime, so return False
    if n % i == 0:
      return False

  # If no divisors were found, n is prime, so return True
  return True

def izbrojiprim(a, b):
  count = 0
  for i in range(a, b+1):
    if prim(i):
      count += 1
  return count

def ispisiprim(n):
  pronalazak = False
  for i in range(2, n-1):
    if prim(i) and prim(i+2):
      print(i, i+2)
      pronalazak = True

  if not pronalazak:
    print("Ne postoje prim brojevi do broja", n)

print(prim(11))
print(prim(12))
print(izbrojiprim(1, 10))
print(izbrojiprim(100, 200))
ispisiprim(20)
ispisiprim(100)
