def recursiveFibbonaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursiveFibbonaci(n-1) + recursiveFibbonaci(n-2)

print(recursiveFibbonaci(10)) #Output: 55
