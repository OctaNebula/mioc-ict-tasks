r, c, x, y = map(int, input().split())
matrix = []

#inputs the matrix
for i in range(r):
    matrix.append(list(map(int, input().split())))

#the program adds the yth row to the xth row
for i in range(c):
    matrix[x-1][i] += matrix[y-1][i]

#prints the matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()