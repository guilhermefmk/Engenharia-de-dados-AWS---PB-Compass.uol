

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]


def reparteLista(lista: list, size: int):
    result = [[] for x in range(size)]
    resto = len(lista) % size
    tamanhos = [len(lista)// size for x in range(size)]
    iterador = 0
    if resto != 0:
        for i in range(resto):
            tamanhos[iterador] += 1
            iterador += 1
    for i in range(size):
        for j in range(tamanhos[i]):
            result[i].append(lista.pop(0))
    return(result)

print(reparteLista(b,7))
