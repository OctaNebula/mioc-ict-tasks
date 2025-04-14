labyrinth = []
dim = int(input())

for i in range(dim):
    labyrinth.append(list(map(str, input().split())))

from collections import deque

def bfs(labyrinth): 

    startPos = None
    endPos = None

    for i in range(dim):
        for j in range(dim):
            if labyrinth[i][j] == 'S':
                startPos = (i, j)
            elif labyrinth[i][j] == 'K':
                endPos = (i, j)


    queue = deque([startPos])
    visited = set()

    visited.add(startPos)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
    distance = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) == endPos:
                return distance

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < dim and 0 <= ny < dim and (nx, ny) not in visited and labyrinth[nx][ny] != '-':
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        distance += 1
    return "zarobljena"  # if no path found

print(bfs(labyrinth))