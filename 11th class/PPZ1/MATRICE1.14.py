# inputs the matrix
r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

transposedMatrix = []
for i in range(c):
    transposedMatrix.append([])
    for j in range(r):
        transposedMatrix[i].append(matrix[j][i])
    
# prints the transposed matrix

for i in range(c):
    for j in range(r):
        print(transposedMatrix[i][j], end=" ")
    print()

