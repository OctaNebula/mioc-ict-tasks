matrix = []
for i in range(8):
    matrix.append(list(map(float, input().split())))

targetRow = int(input())

#prints the index of the largest number in the targeted row

targetRowThrowings = matrix[targetRow-1]
largestThrowing = max(targetRowThrowings)
print(targetRowThrowings.index(largestThrowing)+1)
