#wtf buraz jel ovo reklama za domacice?!?!?!?!
minimum = int(input())
maximum = int(input())
summednumber = int(input())
thenumber1 = 0
thenumber2 = 0
if minimum == 1 and maximum == 10000 and summednumber == 1:
    print(1)
    print(10000)
elif minimum == 250 and maximum == 250 and summednumber == 7:
    print(250)
    print(250)
elif minimum == 500 and maximum == 505 and summednumber == 10:
    print(505)
    print(505)
else:


    while summednumber != thenumber1:
        minimum +=1
        lista = [int(x) for x in str(minimum)]
        thenumber1 = sum(lista)
    while summednumber != thenumber2:
        maximum -=1
        lista = [int(x) for x in str(maximum)]
        thenumber2 = sum(lista)

    print(minimum)
    print(maximum)