#inputs the square matrix and outputs the sum of the elements of the main diagonal

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

sum = 0

for i in range(n):
    sum += matrix[i][i]

print(sum)
