try:
    import numpy
except ImportError:
    import pip
    pip.main(['install', 'numpy'])
    import numpy

matrix = open('Ulaz3.txt', 'r')

mat = []

for line in matrix:
    mat.append((line.strip()).split())

for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] = int(mat[i][j])

output = open('Izlaz3.txt', 'w')


o1 = mat[0][0]
for i in range(len(mat)):
    if mat[i][0] < o1:
        o1 = mat[i][0]
    
o2 = []

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i + j == len(mat) - 1 and mat[i][j] < 5:
            o2.append(mat[i][j])
    
o3 = []

for i in range(len(mat)):
    if mat[i][i] % 3 == 0:
        o3.append(mat[i][i])
sum = 0

for i in mat:
    for j in i:
        sum += j

avg = sum / (len(mat) * len(mat[0]))

output.write(str(o1) + '\n')
output.write(str(len(o2)) + '\n')
output.write(str(numpy.prod(o3)) + '\n')
output.write(str(avg) + '\n')