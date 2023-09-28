matrixDimension = int(input())
#inputs the matrix dimension ^^^

#inputs the matrix
matrix = []

for i in range(matrixDimension):
    matrix.append(list(map(int, input().split())))

#checks if the matrix is a binary matrix
#NOTE: a binary matrix is a matrix that only contains 1s on the main diagonal, and 0s everywhere else
isBinaryMatrix = True
for i in range(matrixDimension):
    for j in range(matrixDimension):
        if i == j:
            if matrix[i][j] != 1:
                isBinaryMatrix = False
        else:
            if matrix[i][j] != 0:
                isBinaryMatrix = False

if isBinaryMatrix:
    print("DA")
else:
    print("NE")