chartDimensions = int(input())
branches = int(input())

chart = []

def printNeighbors(node):
    neighbors = []
    for i in range(len(chart)):
        if chart[i][0] == node:
            neighbors.append(chart[i][1])
    return neighbors

for i in range(chartDimensions):
    node, neighbor = map(int, input().split())
    chart.append([node, neighbor])

print(printNeighbors(int(input())))
