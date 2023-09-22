#inputs the matrix
r, c, k = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

#sorts the kth column

column = []

for i in range(r):
    column.append(matrix[i][k-1])

column.sort()
column.reverse()

for i in range(r):
    matrix[i][k-1] = column[i]

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()