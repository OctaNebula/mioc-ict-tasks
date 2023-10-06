matrix = []
for i in range(8):
    matrix.append(list(map(float, input().split())))

#prints the row number (1st is 1 not 0) where the biggest number is

max = 0
row = 0

for i in range(8):
    for j in range(8):
        if matrix[i][j] > max:
            max = matrix[i][j]
            row = i+1
        
print(row)