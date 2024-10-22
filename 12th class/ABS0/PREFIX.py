from collections import deque

class Stack(deque):
    def push(self, value):
        self.append(value)
    def pop(self):
        return super().pop()
    def peek(self):
        return self[-1]
    def is_empty(self):
        return len(self) == 0
    
# Calculate the value of a prefix expression

s = Stack()

for o in reversed(input().split()): # (this is just sufix expression but reversed lol)
    if o in "+-*/":
        a = s.pop()
        b = s.pop()
        s.push(str(eval(b + o + a)))
    else:
        s.push(o)

print(s.pop())