def arithmeticRowSumRecursion(n):
    if n == 1:
        return 1
    else:
        return n + arithmeticRowSumRecursion(n-1)
    
print(arithmeticRowSumRecursion(5)) # Output: 15