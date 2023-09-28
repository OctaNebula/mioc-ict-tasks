#inputs the matrix dimension
matrixDimension = int(input())
#inputs the matrix
matrix = []
for i in range(matrixDimension):
    matrix.append(list(map(int, input().split())))

#checks if the matrix is a triangle matrix
#NOTE: a triangle matrix is a matrix where all the elements above the main diagonal are 0
isTriangleMatrix = True
for i in range(matrixDimension):
    for j in range(i + 1, matrixDimension):
        if matrix[i][j] != 0:
            isTriangleMatrix = False
            break
    if not isTriangleMatrix:
        break

#prints the result
if isTriangleMatrix:
    print("DA")
else:
    print("NE")
