moneyammount, capacity = map(float, input().split())

ammountinside = 0
cost = 0
bought = -1
while ammountinside <= capacity and cost <=moneyammount:
    bought += 1
    treat = input()
    if treat == "B":
        ammountinside += 0.6
        cost += 0.3
    elif treat == "G":
        ammountinside += 0.3
        cost += 0.6

print(bought)
