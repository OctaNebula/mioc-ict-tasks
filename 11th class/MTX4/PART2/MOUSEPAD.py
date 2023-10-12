r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(input()))

#prints the matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end='')
    for j in range(c):
        print(matrix[i][j], end='')
    print()
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end='')
    for j in range(c):
        print(matrix[i][j], end='')
    print()
