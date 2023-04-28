numberofiterations = int(input())
sample = input()
#leftsample is sample until the *
leftsample = sample[:sample.find("*")]
#rightsample is sample after the *
rightsample = sample[sample.find("*")+1:]
for i in range(numberofiterations):
    string = input()
    #checks if the string contains the leftsample and the rightsample at the right places
    if string.startswith(leftsample) and string.endswith(rightsample):
        print("DA")
    else:
        print("NE")