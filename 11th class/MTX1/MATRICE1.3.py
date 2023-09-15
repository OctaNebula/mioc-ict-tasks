#inputs the matrix
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
#sums all positive elements of the matrix
sum = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            sum += a[i][j]
print(sum)