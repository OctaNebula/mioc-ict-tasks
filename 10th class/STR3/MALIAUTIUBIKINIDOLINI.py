carRegistration = input()
#removes everything that isnt a number
for i in carRegistration:
    if not i.isdigit():
        carRegistration = carRegistration.replace(i, "")
#sums the digits of the number
gaming = [int(x) for x in str(carRegistration)]
print(max(gaming))
