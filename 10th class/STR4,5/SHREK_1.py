#this actually has nothing to do with shrek lol, the task is just called that for some reason
numberofregistrations = int(input())
positives = 0
for i in range(numberofregistrations):
    registration = input()
    #splits the registration into a list of strings
    registration = registration.split("*")
    #checks the registration
    if registration[1] == "SW" and int(registration[2]) % 2 == 0:
        #if the registration is correct, adds 1 to the number of positives
        positives += 1

print(positives)