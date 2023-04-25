chocolatePrice, rosePrice, batteryPrice = map(int, input().split())
fullprice = chocolatePrice + rosePrice + 3*batteryPrice
if fullprice <= 10:
    MainOutputText = ("10")
elif fullprice >10 and fullprice <= 20:
    MainOutputText = ("20")
elif fullprice >20 and fullprice <= 50:
    MainOutputText = ("50")
elif fullprice >50 and fullprice <= 100:
    MainOutputText = ("100")
else:
    print("error:expectedCalculatedNumbernumberBelow100 code=1")
print(MainOutputText)