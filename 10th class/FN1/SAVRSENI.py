def savrseniline(n):
  zbrojdjeljitelja = 0
  for i in range(1, n):
    if n % i == 0:
      zbrojdjeljitelja += i
  return zbrojdjeljitelja == n

def ispisisavrseno(n):
  nasaosavrseni = False
  for i in range(1, n+1):
    if savrseniline(i):
      print(i)
      nasaosavrseni = True
  if not nasaosavrseni:
    print("Nema savrsenih brojeva do", n)

ispisisavrseno(6)
ispisisavrseno(100)
ispisisavrseno(1000) 
