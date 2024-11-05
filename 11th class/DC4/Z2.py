p1length = int(input()) # useless variable but the task requires it so yea
p1 = list(map(int, input().split()))
p2length = int(input()) # same here lol
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

print(' '.join(map(str, result.keys())))
print()

# Alternate solution (lines 8-14):

# from collections import defaultdict
#
# result = defaultdict(int)
# for i in p1:
#     for j in p2:
#         result[i+j] += p1[i] * p2[j]
