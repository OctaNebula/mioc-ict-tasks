numberofdigits = int(input())
number = ""
for i in range(numberofdigits):
    number = number + input()
#converts the string containing letters to a number the following way:
# A = 1... Z = 26 after that multiple letters represent multiple digits like AA = 27, AB = 28, BA = 53 ... ZZ = 702
# the following code converts the string to a list of numbers
number = list(number)
for i in range(len(number)):
    number[i] = ord(number[i]) - 64 # ord() returns the ASCII value of the character
# the following code converts the list of numbers to a number
for i in range(len(number)):
    number[i] = number[i] * (26 ** (len(number) - 1 - i))
number = sum(number)

print(number)