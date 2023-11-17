def recursion(x, y):
    if x > 3:
        return recursion(x - 3, y + 2) - 1
    elif x == 3:
        return(x + y)
    else:
        return recursion(x * 2 + 1, y - 4) + 1

x = int(input())
y = int(input())
print(recursion(x, y))