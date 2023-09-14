matrix = []
largest = 0
#finds the largest value in the matrix
for i in matrix:
    for j in i:
        if j > largest:
            largest = j
#prints the location of the largest value
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == largest:
            print(i+1) #its plus 1 because it converts python's index to normal index lol
