countriesandcities = {"Vienna": "Austria", "Rome": "Italy", "Milano": "Italy", "Zagreb": "Croatia"}

newinputs = int(input())

for i in range(newinputs):
    city = input()
    if city in countriesandcities:
        print(countriesandcities[city])
    else:
        print("bruh")
        
for i in countriesandcities.values():
    print(i)
    
country = input()

for i in countriesandcities:
    if countriesandcities[i] == country:
        print(i)
    
for i in countriesandcities.keys():
    print(i)

