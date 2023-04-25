NumberToBeSplit = int(input())
if NumberToBeSplit//10 < 10:
    SetIndentifierAs2 = True
    SetIndentifierAs4 = False
    SetIndentifierAs6 = False
elif NumberToBeSplit//100 < 100:
    SetIndentifierAs4 = True
    SetIndentifierAs2 = False
    SetIndentifierAs6 = False
else:
    SetIndentifierAs6 = True
    SetIndentifierAs2 = False
    SetIndentifierAs4 = False

if SetIndentifierAs2 == True:
    Num1 = NumberToBeSplit//10
    Num2 = NumberToBeSplit - 10*Num1
elif SetIndentifierAs4 == True:
    Num1 = NumberToBeSplit//100
    Num2 = NumberToBeSplit - 100*Num1
else:
    Num1 = NumberToBeSplit//1000
    Num2 = NumberToBeSplit-1000*Num1
if Num1 > Num2:
    MainOutputText = Num1 - Num2
else:
    MainOutputText = Num2 - Num1
print(MainOutputText)
