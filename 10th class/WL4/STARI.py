#stari paedrs
numberofnumbers = int(input())
y = ""
for i in range(numberofnumbers):
    list = []
    number = input()
    for randomeasdjnmaogftaj in range(len(number)):
        list.append(int(number[randomeasdjnmaogftaj]))
    y += str(min(list))
print(int(y))