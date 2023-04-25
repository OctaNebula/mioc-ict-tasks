peoplethatCame = int(input())
peopleAwarded = int(input())
if peoplethatCame < 10000:
    moneyAward = peoplethatCame*peopleAwarded
else:
    moneyAward = 2*peoplethatCame*peopleAwarded
MainOutputText = moneyAward
print(MainOutputText)
