file = open("Ulaz1.txt", "r")

for line in file:
    numbers = ((line.strip()).split())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i][0])

output = open("Izlaz1.txt", "w")

a = numbers[0]
b = numbers[1]

output.write(str(a + b) + "\n")
output.write(str(a - b) + "\n")
output.write(str(a * b) + "\n")
output.write(str(a / b) + "\n")