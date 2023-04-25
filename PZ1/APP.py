mainnumber = int(input())
jedinice = mainnumber % 10
desetice = (mainnumber % 100 - jedinice)//10
stotice = (mainnumber % 1000 - desetice*10 - jedinice)//100
tisucice = (mainnumber - stotice*100 - desetice*10 - jedinice)//1000


x = int(input())
f = 0

for i in range(x):
    a = int(input())
    if a < 0:
        f += 1
    if a == -1:
        jedinice = ("")
        mainnumber = (stotice*100, desetice*10, jedinice)
        if f == 2:
            mainnumber = (desetice*10, jedinice)
        elif f == 3:
            mainnumber = jedinice

    elif a == -2:
        desetice = ("")
        mainnumber = (stotice*100, desetice*10, jedinice)
        if f == 2:
            mainnumber = (desetice*10, jedinice)
        elif f == 3:
            mainnumber = jedinice
    elif a == -3:
        stotice = ("")
        mainnumber = (stotice*100, desetice*10, jedinice)
        if f == 2:
            mainnumber = (desetice*10, jedinice)
        elif f == 3:
            mainnumber = jedinice
    elif a == -4:
        tisucice = ("")
        mainnumber = (stotice*100, desetice*10, jedinice)
        if f == 2:
            mainnumber = (desetice*10, jedinice)
        elif f == 3:
            mainnumber = jedinice
    elif a == 1:
        jedinice += 1
    elif a == 2:
        desetice += 1
    elif a == 3:
        stotice += 1
    elif a == 4:
        tisucice += 1
    #filter
    
    jedinice = mainnumber % 10
    desetice = (mainnumber % 100 - jedinice)//10
    stotice = (mainnumber % 1000 - desetice*10 - jedinice)//100
    if tisucice == (""):
        tisucice = (mainnumber - stotice*100 - desetice*10 - jedinice)//1000

print(tisucice, stotice, desetice, jedinice, sep="")