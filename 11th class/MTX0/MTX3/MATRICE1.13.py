#inputs the matrix dimension
matrixDimension = int(input())
#inputs the matrix
matrix = []
for i in range(matrixDimension):
    matrix.append(list(map(int, input().split())))

#checks if the matrix is symetrical
#NOTE: A symetrical matrix is a matrix which has symetrical elements on the sides of the main diagonal
symetrical = True
for i in range(matrixDimension):
    for j in range(matrixDimension):
        if matrix[i][j] != matrix[j][i]:
            symetrical = False
            break
    if not symetrical:
        break

#prints the result
if symetrical:
    print("DA")
else:
    print("NE")
