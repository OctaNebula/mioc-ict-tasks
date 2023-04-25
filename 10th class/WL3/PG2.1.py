a = int(input("Enter the first digit: "))
b = int(input("Enter the second digit: "))

c = a + b

if c > 9:
    password = c % 10
else:
    password = c

print(str(a) + str(b) + str(password))