numberofthings = int(input())
fancypantsstuff = []
for i in range(numberofthings):
    number = int(input())
    if number % 10 + (number % 100 // 10) <= (number // 100):
        fancypantsstuff.append(number)
for elem in fancypantsstuff:
    print(elem)





