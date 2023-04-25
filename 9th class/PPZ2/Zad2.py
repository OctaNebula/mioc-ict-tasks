#Zad2 - Real
variablemomen = 0
number = int(input())
for i in range(number):
    first, secondf, third, imhoiranouttaideas = map(int, input().split())
    if first > secondf:
        if third < imhoiranouttaideas:
            variablemomen += 3
        elif third == imhoiranouttaideas:
            variablemomen += 2
    elif first == secondf:
        if third < imhoiranouttaideas:
            variablemomen += 1
print(variablemomen)
