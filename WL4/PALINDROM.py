numberofnumbers = int(input())
numberofpalindromes = 0
wowlist2 = []
for i in range(numberofnumbers):
    number = int(input())
    wowlist = [int(x) for x in str(number)]
    wowlist2 = wowlist[::-1]
    if wowlist == wowlist2:
        numberofpalindromes += number
print(numberofpalindromes)
