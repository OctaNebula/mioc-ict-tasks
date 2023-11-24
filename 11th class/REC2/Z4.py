def recursiveRowSum(n):
    if n == 1:
        return 1
    return n + recursiveRowSum(n - 1)

print(recursiveRowSum(int(input())))

# Output: depends on whatever you input lol