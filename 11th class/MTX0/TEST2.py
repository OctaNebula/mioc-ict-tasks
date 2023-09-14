matrix = []
for i in matrix:
    for j in i:
        if j >= 10:
            #prints the position of the cell in the matrix
            print(matrix.index(i), i.index(j))

