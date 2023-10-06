#inputs the matrix
r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(input()))

evenScore = 0
oddScore = 0

#counts the number of x's in each row and adds to the score of the corresponding player

for i in range(c):
    for j in range(r):
        if matrix[j][i] == "x":
            if (j+1) % 2 == 0 and (i+1) % 2 == 0:
                evenScore += 1
            elif (j+1) % 2 == 1 and (i+1) % 2 == 1:
                oddScore += 1

#outputs the winner

if evenScore > oddScore:
    print("Itchy")
elif oddScore > evenScore:
    print("Scratchy")
else:
    print("Isto")