numberofgoals = int(input(""))
goals = input()
diff = []
h = 0
s = 0
#counts the ammount of the letter H in the string
print(goals.count("H"))
#counts the biggest difference between the ammount of H and S in the string
for i in goals:
    if i == "H":
        h += 1
        diff.append(abs(h-s))
    elif i == "S":
        s += 1
        diff.append(abs(h-s))
print(max(diff))

