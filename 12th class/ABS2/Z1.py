#expression = input()
#
#count = 0
#
#for i in expression: #checks the validity of brackets
#    if i == '(':
#        count += 1
#    elif i == ')':
#        count -= 1
#    if count < 0:
#        print(False)
#        break
#
#if count == 0:
#    print(True)
#
#if count > 0:
#    print(False)

#idk this is supposed to be a stack problem but its easier to do it this way

# alternate solution that uses stacks

from collections import deque

expression = input()

stack = deque()

for i in expression:
    if i == "(":
        stack.append(i)
    elif i == ")":
        if len(stack) == 0:
            print(False)
            break
        stack.pop()

if len(stack) == 0:
    print(True)
else:
    print(False)