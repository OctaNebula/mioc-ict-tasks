placeDataDictionary = {}

print("note: type in 'END' to stop inputing stuff")

while True:
    # data is inputed in the form of "PLACE LISTOFINTVALUES"
    data = list(map(str, input().split()))    
    if data[0] != "END":    
        key = data[0]
        data.remove(key)
        placeDataDictionary[key] = data
    else:
        break

print(placeDataDictionary)

# prints values for a given key

key = input()

if key in placeDataDictionary:
    keyedList = placeDataDictionary[key]

    print(f"OS: {keyedList[0]} SS: {keyedList[1]}")
else:
    print("Key not found")

# sums up all the the 0th values of the lists in the dictionary

sumA = 0
for key in placeDataDictionary:
    sumA += int(placeDataDictionary[key][0])
sumB = 0
for key in placeDataDictionary:
    sumB += int(placeDataDictionary[key][1])

print(f"Zbroj nat u OS: {sumA} Zbroj nat u SS: {sumB}")

# inputs another key and value like previous ones

data = list(map(str, input().split()))
key = data[0]
data.remove(key)
placeDataDictionary[key] = data

# prints the dictionary again sorted by keys alphabetically (with fancy lambda stuff)

for key in sorted(placeDataDictionary, key=lambda x: x.lower()):
    print(f"{key}: {placeDataDictionary[key][0]} {placeDataDictionary[key][1]}")

