import numpy

n = int(input())
for i in range(n):
    num = int(input())
    with open("z3a.txt", "a") as file:
        file.write(str(num) + "\n")

main = open("z3a.txt", "r")

data = main.readlines()
main.close()
data = [x.strip() for x in data]
data = [int(x) for x in data]

print(data)
print(max(data))

counter = 0
for i in data:
    if i > numpy.mean(data):
        counter += 1
print(counter)

data = sorted(data)
data = data[::-1]

for i in data:
    print(i)

counter = 0
for i in data:
    if i > -2 and i < 7 and i % 3 == 0:
        counter += 1
print(counter)

templist = []
for i in data:
    if i % 2 != 0:
        templist.append(i)

print(numpy.prod(templist))