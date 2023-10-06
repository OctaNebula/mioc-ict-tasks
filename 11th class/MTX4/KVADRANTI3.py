r = int(input())
c = r
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

white = 0
black = 0

#the matrix is basically a checkerboard; it sums the numbers in the white and black squares
for i in range(r):
    for j in range(c):
        if (i + j) % 2 == 0:
            white += matrix[i][j]
        else:
            black += matrix[i][j]


#prints the result
print("A:{halfA} B:{halfB}".format(halfA=white, halfB=black))