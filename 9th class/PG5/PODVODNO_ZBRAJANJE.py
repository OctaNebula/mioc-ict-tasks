N = int(input())
M = int(input())

Nj = N % 10
Nd = (N // 10) % 10
Ns = N // 100

Kj = Mj = M % 10
Kd = Md = (M // 10) % 10
Ks = Ms = M // 100

Kj = Nj * (Nj <= Mj) + Mj * (Mj < Nj)
Kd = Nd * (Nd <= Md) + Md * (Md < Nd)
Ks = Ns * (Ns <= Ms) + Ms * (Ms < Ns)

print(Ks * 100 + Kd * 10 + Kj)

