precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infixToSufix(infix):
    stack = []
    postfix = ""
    for i in infix:
        if i.isalnum():
            postfix += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[i] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix

# example

infix = "(7+9)*3-(2+4)/6"
print(infixToSufix(infix))
