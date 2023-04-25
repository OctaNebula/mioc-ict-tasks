NormalState = 0
PreparedState = 0
OrdinaryMesaures = 0
OutrageousMesaures = 0
OutrageousState = 0

Input1, Input2, Input3, Input4, Input5 = map(int, input().split())

#input1

if Input1 < 200:
    Input1 = 1
elif Input1 >= 200 and Input1 <= 370:
    Input1 = 2
elif Input1 >= 370 and Input1 <= 470:
    Input1 = 3
elif Input1 >= 470 and Input1 <= 570:
    Input1 = 4
else:
    Input1 = 5

#input2

if Input2 < 200:
    Input2 = 1
elif Input2 >= 200 and Input2 <= 370:
    Input2 = 2
elif Input2 >= 370 and Input2 <= 470:
    Input2 = 3
elif Input2 >= 470 and Input2 <= 570:
    Input2 = 4
else:
    Input2 = 5

#input3

if Input3 < 200:
    Input3 = 1
elif Input3 >= 200 and Input3 <= 370:
    Input3 = 2
elif Input3 >= 370 and Input3 <= 470:
    Input3 = 3
elif Input3 >= 470 and Input3 <= 570:
    Input3 = 4
else:
    Input3 = 5

#input4

if Input4 < 200:
    Input4 = 1
elif Input4 >= 200 and Input4 <= 370:
    Input4 = 2
elif Input4 >= 370 and Input4 <= 470:
    Input4 = 3
elif Input4 >= 470 and Input4 <= 570:
    Input4 = 4
else:
    Input4 = 5

#input5

if Input5 < 200:
    Input5 = 1
elif Input5 >= 200 and Input5 <= 370:
    Input5 = 2
elif Input5 >= 370 and Input5 <= 470:
    Input5 = 3
elif Input5 >= 470 and Input5 <= 570:
    Input5 = 4
else:
    Input5 = 5

#state definitions

if Input1 == 1:
    NormalState = NormalState + 1
elif Input1 == 2:
    PreparedState = PreparedState + 1
elif Input1 == 3:
    OrdinaryMesaures = OrdinaryMesaures + 1
elif Input1 == 4:
    OutrageousMesaures = OutrageousMesaures + 1
elif Input1 == 5:
    OutrageousState = OutrageousState + 1

if Input2 == 1:
    NormalState = NormalState + 1
elif Input2 == 2:
    PreparedState = PreparedState + 1
elif Input2 == 3:
    OrdinaryMesaures = OrdinaryMesaures + 1
elif Input2 == 4:
    OutrageousMesaures = OutrageousMesaures + 1
elif Input2 == 5:
    OutrageousState = OutrageousState + 1

if Input3 == 1:
    NormalState = NormalState + 1
elif Input3 == 2:
    PreparedState = PreparedState + 1
elif Input3 == 3:
    OrdinaryMesaures = OrdinaryMesaures + 1
elif Input3 == 4:
    OutrageousMesaures = OutrageousMesaures + 1
elif Input3 == 5:
    OutrageousState = OutrageousState + 1

if Input4 == 1:
    NormalState = NormalState + 1
elif Input4 == 2:
    PreparedState = PreparedState + 1
elif Input4 == 3:
    OrdinaryMesaures = OrdinaryMesaures + 1
elif Input4 == 4:
    OutrageousMesaures = OutrageousMesaures + 1
elif Input4 == 5:
    OutrageousState = OutrageousState + 1

if Input5 == 1:
    NormalState = NormalState + 1
elif Input5 == 2:
    PreparedState = PreparedState + 1
elif Input5 == 3:
    OrdinaryMesaures = OrdinaryMesaures + 1
elif Input5 == 4:
    OutrageousMesaures = OutrageousMesaures + 1
elif Input5 == 5:
    OutrageousState = OutrageousState + 1

print(NormalState, PreparedState, OrdinaryMesaures, OutrageousMesaures, OutrageousState)

#Mogao sam ovo bolje napraviti ali nije mi se dalo brisati cijeli kod i ponovno ga tipkati pa sam ga samo nadogradio,.
