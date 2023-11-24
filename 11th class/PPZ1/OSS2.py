matrix = []
for i in range(8):
    matrix.append(list(map(float, input().split())))

targetRow = int(input())

#prints the index of the largest number in the targeted row

print(matrix[targetRow].index(max(matrix[targetRow])))

input()