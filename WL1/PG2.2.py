#nadam se da je ovo prije tocno
vozac1 = 0
vozac2 = 0
vozac1uk = 0
vozac2uk = 0
krug = 1
while krug<10:
    vozac1, vozac2 = map(int, input().split())
    vozac1uk += vozac1
    vozac2uk += vozac2
    if vozac1uk == vozac2uk:
        break
    krug += 1
print(krug)



