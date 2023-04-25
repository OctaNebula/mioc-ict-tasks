lista = []
for i in range(9):
    x = int(input())
    lista.append(x)

var = sum(lista)-100
#ide sauce zadatka
for i in range(9):
    var-=lista[i]
    if lista.count (var) == 0:
        var += lista[i]
    else:
        lista.remove(var)
        lista.remove(lista[i])
        break
for i in range(7):
    print(lista[i])

#ok hvala bogu ovo radi