p1lenght = int(input()) # useless variable #1 (again lol)
polynome1 = (list(map(int, input().split())))[::-1]
p2lenght = int(input()) # useless variable #2
polynome2 = (list(map(int, input().split())))[::-1]

# NOTE: the for loop goes backwards. reason why: 1st member of the polynome is the highest power
polynome1 = {i: polynome1[i] for i in range(len(polynome1)-1, -1, -1)}
polynome2 = {i: polynome2[i] for i in range(len(polynome2)-1, -1, -1)}
result = {}

# sums the polynomes by summing the numbers with the same key
for key in polynome1:
    if key in polynome2:
        result[key] = polynome1[key] + polynome2[key]
    else:
        result[key] = polynome1[key]

for keys in result:
    print(result[keys], end=' ')
print()