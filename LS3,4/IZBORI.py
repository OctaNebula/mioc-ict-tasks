candidates = list(map(int, input().split()))
letters = ["A", "B", "C", "D"]
while len(letters) != 2:
    purge = candidates.index(min(candidates))
    candidates.remove(candidates[purge])
    letters.remove(letters[purge])
candidates2 = list(map(int, input().split()))
print(letters[candidates2.index(max(candidates2))])

