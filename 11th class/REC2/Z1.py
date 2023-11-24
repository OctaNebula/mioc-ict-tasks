def recursion(x):
    if x > 1:
        return recursion(x - 1) + x
    elif x == 1:
        return 1

print(recursion(recursion(3)))

# Result: 21