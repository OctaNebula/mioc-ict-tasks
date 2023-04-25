#UV
a = int(input())
if a <=2:
    print("Niska opasnost")
elif a > 2 and a <= 5:
    print("Umjerena opasnost")
elif a > 5 and a <= 7:
    print("Visoka opasnost")
elif a > 7 and a <= 10:
    print("Vrlo visoka opasnost")
elif a > 10:
    print("Ekstremna opasnost")