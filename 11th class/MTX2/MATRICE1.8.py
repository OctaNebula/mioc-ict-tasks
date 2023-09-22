#inputs the matrix
r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

#inputs 2 new variables, k and l
k, l = map(int, input().split())

#multiplies the kth row by l
for i in range(c):
    matrix[k-1][i] *= l

#prints the matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()