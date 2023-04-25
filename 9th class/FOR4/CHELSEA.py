cijela = prvo = drugo = 0
koliko = int(input())
for i in range(koliko):
 Du, Gu, D1, G1 = map(int, input().split())
 D2 = Du - D1
 G2 = Gu - G1
 if Du > Gu: cijela += 3
 if Du == Gu: cijela += 1
 if D1 > G1: prvo += 3
 if D1 == G1: prvo += 1
 if D2 > G2: drugo += 3
 if D2 == G2: drugo += 1
print(cijela, prvo, drugo, sep = '\n')