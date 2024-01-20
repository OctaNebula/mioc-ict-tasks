countriesandcities = {"Vienna": "Austria", "Rome": "Italy", "Milano": "Italy", "Zagreb": "Croatia"}

newinputs = int(input())

for i in range(newinputs):
    # adds a new city and country to the dictionary
    city, country = input().split()
    countriesandcities[city] = country

        
for i in countriesandcities.values():
    print(i)
    
country = input()

for i in countriesandcities:
    if countriesandcities[i] == country:
        print(i)
    
for i in countriesandcities.keys():
    print(i)

