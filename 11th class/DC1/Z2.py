gradesDictionary = {}
n = int(input())
gpaList = []

for i in range(n):
    name, grade = input().split()
    gradesDictionary[name] = float(grade)
    gpaList.append(float(grade))

highestGPA = max(gradesDictionary.values())

print(sum(gpaList) / len(gpaList))

for name, grade in gradesDictionary.items():
    if grade == highestGPA:
        print(name)

sortedGPAList = sorted(gpaList)

res = []
for i in range(len(gpaList)):
    res.append(str(sortedGPAList[i]))

print(' '.join(res))
