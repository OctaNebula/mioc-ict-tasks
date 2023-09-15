n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
#prints the smallest element of the matrix
min = a[0][0]
for i in a:
    for j in i:
        if j < min:
            min = j
print(min)