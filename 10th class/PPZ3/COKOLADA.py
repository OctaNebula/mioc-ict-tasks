chocox, chocoy = map(int, input().split())
for i in range(3):
    string = input()
    string = string.split()
    #2nd member of the list is either "redova" or "stupaca", redova is rows, stupaca is columns
    #1st is the ammount of rows/columns
    if string[1] == "redova":
        print(chocox)
        chocox -= int(string[0])
    elif string[1] == "stupaca":
        print(chocoy)
        chocoy -= int(string[0])
#doesn't work sucks to suck