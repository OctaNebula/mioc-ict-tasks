r, c, x, y = map(int, input().split())
matrix = []

#inputs the matrix
for i in range(r):
    matrix.append(list(map(int, input().split())))

#removes the xth row and the yth column
matrix.pop(x-1)
for i in range(r-1):
    matrix[i].pop(y-1)

#prints the matrix
for i in range(r-1):
    for j in range(c-1):
        print(matrix[i][j], end=" ")
    print()
