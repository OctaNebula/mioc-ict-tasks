thing = int(input())
lista = [int(x) for x in str(thing)]
lista = lista[::-1]
while lista[0] == 0:
    lista.remove(lista[0]) 

for i in range(len(lista)):
    print(lista[i], end = "")
