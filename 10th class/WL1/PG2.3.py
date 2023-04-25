n = int(input())
numbers = 0
gaming = []
for i in range(n):
    number = int(input())
    gaming = [int(x) for x in str(number)]
    if max(gaming) <= 3:
        numbers+=1

print(numbers)
