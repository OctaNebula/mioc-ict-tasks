p1lenght = int(input()) # useless variable but the task requires it so yea
p1 = list(map(int, input().split()))
p2lenght = int(input()) # same here lol
p2 = list(map(int, input().split()))
p1 = {i: p1[i] for i in range(len(p1))}
p2 = {i: p2[i] for i in range(len(p2))}

result = {}
for i in p1:
    for j in p2:
        if i+j in result:
            result[i+j] += p1[i] * p2[j]
        else:
            result[i+j] = p1[i] * p2[j]

for keys in result:
    print(result[keys], end=' ')
print()