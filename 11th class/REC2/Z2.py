def recursion(x, y):
    if x > 5:
        return recursion(x - 2, y + 1) + x
    elif x <= 5 and x >= 0:
        return recursion(x - 3, y + 2) + y
    elif x < 0:
        return x**2 + x
    
print(recursion(10, 3))

# Result: 40