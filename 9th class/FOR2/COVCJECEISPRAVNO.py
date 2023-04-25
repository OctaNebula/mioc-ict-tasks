n = int(input())
a = b = 0
red = "IVICA"
for i in range(n):
    m = int(input())
    if m!=6 and red  == "IVICA":
        a = a + m
        if a == b:
            b = 0
        red = "MARICA"
    elif m!=6 and red == "MARICA":
        b = b + m
        if a == b:
            a = 0
        red = "IVICA"
    elif m == 6 and red == "IVICA":
        a = a + m
        if a == b:
            b = 0
        red = "IVICA"
    elif m == 6 and red == "MARICA":
        b = b + m
        if b == a:
            a = 0
        red = "MARICA"
print(red)
print(a)
print(b)