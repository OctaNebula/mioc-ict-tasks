#inputs the matrix1
r1, c1 = map(int, input().split())
matrix1 = []
for i in range(r1):
    matrix1.append(list(map(int, input().split())))

#inputs the matrix2
r2, c2 = map(int, input().split())
matrix2 = []
for i in range(r2):
    matrix2.append(list(map(int, input().split())))

#replaces the every third column of matrix1 with matrix2, starting from 0th column (actually first becasue of 0 indexing)
for i in range(0, c1, 3):
    for j in range(r1):
        matrix1[j][i] = matrix2[j][i]
    
#prints matrix1
for i in range(r1):
    for j in range(c1):
        print(matrix1[i][j], end=" ")
    print()