def factorialRecursion(n):
    if n == 0:
        return 1
    return n * factorialRecursion(n - 1)

print(factorialRecursion(5)) # Output: 120
