n = int(input())

cityAndAvgYearlyTemp = {}

for i in range(n):
    cityAndAvgMonthlyTemp = input().split()

    # puts yearly average yearly temperature in dictionary along with city name
    cityAndAvgYearlyTemp[cityAndAvgMonthlyTemp[0]] = sum(
        [int(temp) for temp in cityAndAvgMonthlyTemp[1:]]) / 12
    
# sorts dictionary by value
cityAndAvgYearlyTemp = sorted(cityAndAvgYearlyTemp.items(), key=lambda x: x[1])

for city in cityAndAvgYearlyTemp:
    print(city[0])
