# 3x13 matrix

ticketmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36], [37, 38, 39]]

cross = 0

for i in range(7):
    cross = int(input())

    # replaces the number in the matrix with an X

    for i in ticketmatrix:
        for j in i:
            if j == cross:
                i[i.index(j)] = "X"

# nukes everything else by replacing all non x's with *

for i in ticketmatrix:
    for j in i:
        if j != "X":
            i[i.index(j)] = "*"

# prints the matrix

for i in ticketmatrix:
    for j in i:
        print(j, end="")
    print()
