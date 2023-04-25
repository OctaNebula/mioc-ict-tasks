points = []
pointsreplica = []
for i in range(8):
    number = int(input())
    points.append(number)
    pointsreplica.append(number)
#the total score is calculated by summing the 5 highest scores from the tasks
print(sum(sorted(points, reverse=True)[:5]))
for i in range(3):
    pointsreplica.remove(min(pointsreplica))
for i in pointsreplica:
    print(points.index(i)+1, end=" ")