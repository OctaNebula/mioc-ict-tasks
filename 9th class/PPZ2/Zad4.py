#Zad4 - bombanje
randomnumber = int(input())
seggs = int(input())
rp = 0
letterb = 0
rf = 0
for iloverenamingvariables in range(randomnumber):
    g = int(input())
    p = int(input())

    if g == p:
        letterb += seggs+rp
        rp += 1
    else:
        if letterb-((rf*2)+1) <= 0:
            letterb = 0
            rf+=1
        else:
            letterb -= ((rf*2)+1)
            rf+=1
print(rp)
print(letterb)
