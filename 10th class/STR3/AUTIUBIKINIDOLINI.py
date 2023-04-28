numberOfCars = int(input())
carRegistrationList = []
carSumList = []
for i in range(numberOfCars):
    carRegistration = input()
    carWithOnlyNumbers = carRegistration
    carRegistrationList.append(carRegistration)
    #removes everything that isnt a number
    for i in carRegistration:
        if not i.isdigit():
            carWithOnlyNumbers = carWithOnlyNumbers.replace(i, "")
    #sums the digits of the number
    gaming = [int(x) for x in str(carWithOnlyNumbers)]
    carSum = sum(gaming)
    carSumList.append(carSum)
highestsum = carSumList.index(max(carSumList))
print(carRegistrationList[highestsum])
#gaming = [int(x) for x in str(number)]