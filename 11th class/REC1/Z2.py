from collections import deque

def recursion(n):
    z = 0

    if memo[n] != -1:
        return memo[n]
    elif(n == 0):
        return 1
    elif n < 0:
        return 0
    for i in range (1, 3):
        z += recursion(n - i)
    memo[n] = z
    return z

memo = deque()
for i in range(10**6):
    memo.append(-1)

n = int(input())
print(recursion(n))
