def recursion(x):
    if x > 10:
        return recursion(recursion(x - 5)) + 1
    elif x <= 10 and x > 0:
        return recursion(x - 3) - 2
    elif x <= 0:
        return 1 - x

print(recursion(12))

# Result: 5