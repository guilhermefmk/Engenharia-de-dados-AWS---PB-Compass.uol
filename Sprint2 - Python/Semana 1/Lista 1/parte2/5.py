

def limpaLista(lista: list):
    result = []
    for x in lista:
        if x not in result:
            result.append(x)
    return result

a = [1,1,1,2,2,3,4,4,5,5,6,6,7,7,8,9,9]

print(limpaLista(a))