nameNumberDictionary = {}

for i in range(5):
    name = input("Enter name: ")
    number = input("Enter number: ")
    nameNumberDictionary[name] = number

name = input("Enter name to search: ")

if name in nameNumberDictionary:
    print(nameNumberDictionary[name])
else:
    print(f"{name} not found in dictionary")
