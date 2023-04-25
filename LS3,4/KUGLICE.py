pozicije = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "dontcrash"]
positionA, positionB = map(int, input().split())
pozicije[positionA] = "A"
pozicije[positionB] = "B"

#mijenjanje mjesta pozicija 5 puta
for i in range(5):
    positionA, positionB = map(int, input().split())
    pozicije[positionA], pozicije[positionB] = pozicije[positionB], pozicije[positionA]

#lokacije kuglica, prva je manja pa je druga veca
locs = [pozicije.index("A"), pozicije.index("B")]
print(min(locs), max(locs))
