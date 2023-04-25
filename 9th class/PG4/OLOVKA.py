number=int(input())
number100s = number//100
number1s = number%10

if number100s > number1s:
    setBalanceValule = 1
elif number100s < number1s:
    setBalanceValule = 2
else:
    setBalanceValule = 0


if setBalanceValule == 1:
    print("LIJEVI NAGIB")
if setBalanceValule == 2:
    print("DESNI NAGIB")
if setBalanceValule == 0:
    print("RAVNOTEZA")
