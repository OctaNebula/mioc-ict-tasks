matrix = []
#prints the dum of even columns
total = 0
for i in matrix:
    for j in i:
        if j%2==0:
            j+=total
print(total)