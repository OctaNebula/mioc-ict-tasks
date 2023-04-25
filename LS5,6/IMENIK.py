def search(phonebook, number):
    res = [idx for idx in phonebook if idx.lower().startswith(string.lower())]
    return len(res)

phonebook = []
wantedNumber = int(input())
numberofNumbers = int(input())
for i in range(numberofNumbers):
    number = input()
    phonebook.append(number)
splitwantedNumber = [str(x) for x in str(wantedNumber)]
#reconstructs the list into a string digit by digit
#each time it adds a digit to the string it searches the phonebook with that string
#and it prints the ammount of results

string=""
for i in range(len(splitwantedNumber)):
    string = string + str(splitwantedNumber[i])
    #counts the ammount of results
    print(search(phonebook, string))

#YOO IT ACTUALLY WORKS
