from collections import deque

Deck = deque()

for i in range(1, int(input())):
    Deck.appendleft(i)
    Deck.append(Deck.pop())

while Deck.__len__() > 1:
    Deck.append(Deck.popleft())
    Deck.popleft()

print(Deck[0])