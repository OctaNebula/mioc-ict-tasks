cakenumber = int(input())
eggnumber = int(input())
yellownumber = int(input())
whitenumber = int(input())
if yellownumber > whitenumber:
    cakenumber = yellownumber + eggnumber * whitenumber
elif whitenumber > yellownumber:
    cakenumber = (whitenumber + eggnumber) * yellownumber

print(cakenumber)