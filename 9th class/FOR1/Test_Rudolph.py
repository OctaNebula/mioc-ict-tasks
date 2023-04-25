FirstRoundRudolph, FirstRoundSanta = map(int, input().split())
SecondRoundRudolph, SecondRoundSanta = map(int, input().split())
ThirdRoundRudolph, ThirdRoundSanta = map(int, input().split())
FourthRoundRudolph, FourthRoundSanta = map(int, input().split())
FifthRoundRudolph, FifthRoundSanta = map(int, input().split())
SixthRoundRudolph, SixthRoundSanta = map(int, input().split())
if FirstRoundRudolph + SecondRoundRudolph + ThirdRoundRudolph + FourthRoundRudolph + FifthRoundRudolph + SixthRoundRudolph > FirstRoundSanta + SecondRoundSanta + ThirdRoundSanta + FourthRoundSanta + FifthRoundSanta + SixthRoundSanta:
    print("Hoce!")
elif FirstRoundRudolph + SecondRoundRudolph + ThirdRoundRudolph + FourthRoundRudolph + FifthRoundRudolph + SixthRoundRudolph < FirstRoundSanta + SecondRoundSanta + ThirdRoundSanta + FourthRoundSanta + FifthRoundSanta + SixthRoundSanta:
    print("Nece!")
elif FirstRoundRudolph + SecondRoundRudolph + ThirdRoundRudolph + FourthRoundRudolph + FifthRoundRudolph + SixthRoundRudolph == FirstRoundSanta + SecondRoundSanta + ThirdRoundSanta + FourthRoundSanta + FifthRoundSanta + SixthRoundSanta:
    print("Ostaje doma!")
