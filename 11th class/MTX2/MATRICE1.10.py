#inputs the matrix, r, c, and also the variable x, y which will be important for later (all numbers are integers)
r, c, x, y = map(int, input().split())
matrix = []

#inputs the matrix
for i in range(r):
    matrix.append(list(map(int, input().split())))

#switches the xth column with the yth column
for i in range(r):
    matrix[i][x-1], matrix[i][y-1] = matrix[i][y-1], matrix[i][x-1]

#prints the matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()
