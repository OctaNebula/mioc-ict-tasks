#prosjekatt2
#number of days
numberofdays = int(input())
#list of days
days = []
#list of temperatures
temperature = []
#input the temperatures
for i in range(numberofdays):
    temp = int(input())
    temperature.append(temp)
    days.append(i)
#calculate the average temperature
average = sum(temperature)/numberofdays
#find the closest day to the average temperature
temperaturecopy = temperature[:]
temperature.sort(key=lambda x:abs(x - average))
closest = temperature[0]
#find the index of the closest day
index = temperaturecopy.index(closest)
#find the temperature of the closest day
temp = temperaturecopy[index]
print(index+1)
print(temp)