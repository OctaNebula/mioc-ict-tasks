#inputs the matrix
r = int(input())
c = r
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

splitStrategy = ""
halfA = 0
halfB = 0


if r % 2 == 0:
    splitStrategy = "half"
else:
    splitStrategy = "outline"

#if the splitStrategy is set to half, sums all of the elements in the upper and lower half of the matrix
if splitStrategy == "half":
    for i in range(r):
        for j in range(c):
            if i < r // 2:
                halfA += matrix[i][j]
            else:
                halfB += matrix[i][j]

#if the splitStrategy is set to outline, sums all of the elements in the outline of the matrix
elif splitStrategy == "outline":
    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                halfA += matrix[i][j]
            else:
                halfB += matrix[i][j]

#prints the result
print("A:{halfA} B:{halfB}".format(halfA=halfA, halfB=halfB))
