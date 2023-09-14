matrix = []
for i in matrix:
    if max(i) >= 10:
        #prints the position of the cell in the matrix
        print(matrix.index(i), i.index(max(i)))
