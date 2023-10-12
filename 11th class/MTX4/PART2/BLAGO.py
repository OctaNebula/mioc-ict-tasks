notanimportantinput = int(input()) # this input usually states the lenght of the next input but its totally useless lol
directions = list(input()) # this is the input that we need

r, c = map(int, input().split())

matrix = []
for i in range(r):
    matrix.append(list(input()))

pos = [0, 0]
score = 0
skip = 0

for i in range(len(directions)):
    print(pos)
    if directions[i+skip] == "S":
        pos[1] += 1
    elif directions[i+skip] == "J":
        pos[1] -= 1
    elif directions[i+skip] ==  "I":
        pos[0] += 1
    elif directions[i+skip] == "Z":
        pos[0] -= 1
    skip = 0
    if matrix[pos[0]][pos[1]] == "B":
        score += 1
        matrix[pos[0]][pos[1]] = "."
    elif matrix[pos[0]][pos[1]] == int:
        skip+=(matrix[pos[0]][pos[1]])
        matrix[pos[0]][pos[1]] = "."
print(score)