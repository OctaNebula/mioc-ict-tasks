def recursiveRowSum(n):
    if n == 1:
        return 1
    return n + recursiveRowSum(1/(n-1))
