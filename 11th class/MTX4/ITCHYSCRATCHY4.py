#inputs the matrix
r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(input()))

evenScore = 0
oddScore = 0

#if the the row is even and contains an x, add 1 to the even score
#same applies to odd

for i in range(r):
    for j in range(c):
        if (j+1)%2 == 0:
            if matrix[i][j] == "x":
                evenScore += 1
        else:
            if matrix[i][j] == "x":
                oddScore += 1

#outputs the winner

if evenScore > oddScore:
    print("Itchy")
elif oddScore > evenScore:
    print("Scratchy")
else:
    print("Isto")