# inputs the matrix

r = int(input())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

# the matrix is divided in 2 quadrants like a checkerboard, the program sums the numbers on the white and black squares


sum1 = 0
sum2 = 0

for i in range(r):
    for j in range(r):
        if (i + j) % 2 == 0:
            sum1 += matrix[i][j]
        else:
            sum2 += matrix[i][j]

# prints the result "A:sum1 B:sum2"

print("A:" + str(sum2) + " B:" + str(sum1))
