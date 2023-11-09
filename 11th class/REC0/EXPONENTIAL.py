def exponentialRecursion(n):
    if n == 0:
        return 1
    else:
        return 2 * exponentialRecursion(n - 1)
    
print(exponentialRecursion(3)) # Output: 8

