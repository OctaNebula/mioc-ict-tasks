cmajormainnotes = ["C", "F", "G"]
cmajorammount = 0
aminormainnotes = ["A", "D", "E"]
cminorammount = 0
string = input()
#counts the ammount of major notes for each string
for i in string:
    if i in cmajormainnotes:
        cmajorammount += 1
    elif i in aminormainnotes:
        cminorammount += 1

if cmajorammount > cminorammount:
    print("C-dur")
elif cminorammount > cmajorammount:
    print("A-mol")