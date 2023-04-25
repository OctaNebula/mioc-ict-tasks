n = int(input())
gaming = []
thefinalnumber = []
for i in range(n):
    thefinalnumber = []
    number = int(input())
    gaming = [int(x) for x in str(number)]
    thefinalnumber.append(max(gaming))
    thefinalnumber.append(gaming[-2])
    thefinalnumber.append(gaming[-1])
    print(*thefinalnumber, sep = "")