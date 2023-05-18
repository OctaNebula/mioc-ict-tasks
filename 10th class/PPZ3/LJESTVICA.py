cmajormainnotes = ["C", "F", "G"]
cmajorammount = 0
aminormainnotes = ["A", "D", "E"]
cminorammount = 0
string = input()
stringoriginal = string
string = string.split("|")
#nukes everything after the first note
for i in range(len(string)):
    string[i] = string[i][0]
string = "".join(string)
#counts the ammount of major notes for each string
for i in string:
    if i in cmajormainnotes:
        cmajorammount += 1
    elif i in aminormainnotes:
        cminorammount += 1
print(cmajorammount, cminorammount)
print(string)
if cmajorammount > cminorammount:
    print("C-dur")
elif cminorammount > cmajorammount:
    print("A-mol")
elif cmajorammount == cminorammount:
    if stringoriginal[-1] in cmajormainnotes:
        print("C-dur")
    elif stringoriginal[-1] in aminormainnotes:
        print("A-mol")
