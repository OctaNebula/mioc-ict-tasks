Pat1 = int(input())
Pat2 = int(input())
Pat3 = int(input())
Pat4 = int(input())
Mat1 = int(input())
Mat2 = int(input())
Mat3 = int(input())
Mat4 = int(input())
if Pat1 > Mat1:
    print("PAT")
else:
    print("MAT")
if Pat1 + Pat2 > Mat2 + Mat1:
    print("PAT")
else:
    print("MAT")
if Pat1 + Pat2 + Pat3 > Mat3 + Mat2 + Mat1:
    print("PAT")
else:
    print("MAT")
if Pat1 + Pat2 + Pat3 + Pat4 > Mat4 + Mat3 + Mat2 + Mat1:
    print("PAT")
else:
    print("MAT")
