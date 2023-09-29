#inputs the matrix1
r, c = map(int, input().split())
matrix1 = []
for i in range(r):
    matrix1.append(list(map(int, input().split())))

#inputs the matrix2

matrix2 = []
for i in range(r):
    matrix2.append(list(map(int, input().split())))

#replaces the every third column of matrix1 with matrix2, starting from 0th column (actually first becasue of 0 indexing)
for i in range(0, c, 3):
    for j in range(r):
        matrix1[j][i] = matrix2[j][i]
    
#prints matrix1
for i in range(r):
    for j in range(c):
        print(matrix1[i][j], end=" ")
    print()