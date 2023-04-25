ikz = int(input())
if ikz <= 50:
    MainOutputText = ("dobra kvaliteta zraka")
elif ikz >= 50 and ikz <= 100:
    MainOutputText = ("umjerena kvaliteta zraka")
elif ikz >= 100 and ikz <= 150:
    MainOutputText = ("zrak nezdrav za osjetljive grupe")
elif ikz >= 150 and ikz <= 200:
    MainOutputText = ("nezdrav zrak")
elif ikz >= 200 and ikz <= 300:
    MainOutputText = ("vrlo nezdrav zrak")
elif ikz >= 300 and ikz <= 500:
    MainOutputText = ("opasan zrak")
print(MainOutputText)