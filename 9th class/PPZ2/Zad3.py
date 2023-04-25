#Zad3 - Simpsoni
deeh = int(input())
neznamkakonazivamvarijable = int(input())
period = deeh % 2
kodo = 0
koda = 0
kodaodr = 0
nx = 0


for i in range(neznamkakonazivamvarijable):
    d1, d2 = map(int, input().split())
    if period==0:
        if d1 > d2:
            koda += d1+d2
            kodaodr += 1
        elif d1 < d2:
            kodo += d1+d2
            nx += 1
    if period==1:
        if d2 > d1:
            koda += d1+d2
            kodaodr += 1
        elif d2 < d1:
            kodo += d1+d2
            nx += 1
    if d1 == d2 and period == 0:
        period = 1
    elif d1 == d2 and period == 1:
        period = 0


if deeh % 2 == 0:
    print("KANG")
elif deeh % 2 != 0:
    print("KONOS")

print(kodaodr, nx)
print(koda, kodo)
