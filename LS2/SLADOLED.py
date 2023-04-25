alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sillylist = []
for i in range(26):
    n = int(input())
    sillylist.append(n)

firstflavor = sillylist.index(max(sillylist))
sillylist.pop(firstflavor)
secondflavor = sillylist.index(max(sillylist))
sillylist.pop(secondflavor)

print(f"""{firstflavor}{secondflavor}""")