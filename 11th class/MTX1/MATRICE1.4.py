#inputs the matrix, r, c, and also the variable a which will be important for later (all numbers are integers)
r, c, a = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(r)]
#sums all the elements of the a-th row
sum = 0
for i in range(c):
    sum += matrix[a-1][i]
print(sum)
