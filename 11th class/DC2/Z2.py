import string

emptyDictionary = {}

# Fills the dictionary with the letters of the alphabet with empty values

for letter in string.ascii_uppercase:
    emptyDictionary[letter] = []

print(emptyDictionary)

newInputs = int(input())

for i in range(newInputs):

    #inputs name surname and number, name and surname are inputed as key and number as value, e.g. "John Doe 123456789" is inputed as {"John Doe": "123456789}

    name, surname, number = input().split()
    emptyDictionary[name + " " + surname] = number

letter = input()

if letter in emptyDictionary:
    print(*emptyDictionary[letter])

letter2 = input()

#prints the surname of the person with the first letter of their name equal to the inputed letter

for key in emptyDictionary:
    if key[0] == letter2:
        print(key.split()[1])

# does the same but prints the number instead of their surname
        
letter3 = input()

for key in emptyDictionary:
    if key[0] == letter3:
        print(emptyDictionary[key])

surname = input()

# prints the name surname and number of the person with the inputed surname

for key in emptyDictionary:
    if key.split()[1] == surname:
        print(key, emptyDictionary[key])

