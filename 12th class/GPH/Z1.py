chartDimensions = int(input())
branches = int(input())

chart = []

def printNeighbors(node, chart):
    neighbors = []
    for i in chart:
        if node in i:
            neighbors.append(i[1] if i[0] == node else i[0])
    return neighbors

for i in range(branches):
    node, neighbor = map(int, input().split())
    chart.append([node, neighbor])


for i in printNeighbors(int(input()), chart):
    print(i, end=' ')


