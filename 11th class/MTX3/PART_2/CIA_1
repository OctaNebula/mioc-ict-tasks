#inputs the matrix
r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

#removes all lines containing a 5

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 5:
            #sets the line to []
            matrix[i] = []
            r -= 1
            break

#removes any empty lines
for i in range(r):
    if matrix[i] == []:
        matrix.remove(matrix[i])
        r -= 1

#prints the matrix
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()