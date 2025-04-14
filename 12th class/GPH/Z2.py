chartDimensions = int(input())
branches = int(input())

chart = []

def nodeWithMostNeighbors(chart):
    neighbors = {}
    for i in chart:
        if i[0] in neighbors:
            neighbors[i[0]] += 1
        else:
            neighbors[i[0]] = 1
        if i[1] in neighbors:
            neighbors[i[1]] += 1
        else:
            neighbors[i[1]] = 1
    return max(neighbors, key=neighbors.get)

for i in range(branches):
    node, neighbor = map(int, input().split())
    chart.append([node, neighbor])

print(nodeWithMostNeighbors(chart))