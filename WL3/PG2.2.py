numberofnums = int(input())
slozeni = False
val = 0
for i in range(numberofnums):
    nx = int(input())
    list = [int(x) for x in str(nx)]
    n = list[0]
    if n==1 or n == 2 or n == 3 or n == 5 or n == 7:
        val+=1
    else:
        val+=0
print(val)
#NEK SE JEBE TKO GOD DA JE REKAO DA JE 1 PROSTI BROJ