#inputs the matrix, r, c, and also the variable a which will be important for later (all numbers are integers)
r, c, a = input().split()
x = 0
for i in range(int(r)):
    #inputs the row
    row = input().split()
    #outputs the matrix and multiplies each element by the variable a
    #also prints row by row
    for j in range(int(c)):
        x +=1
        print(int(row[j])*int(a), end=" ")
        if x == int(c):
            print()
            x = 0