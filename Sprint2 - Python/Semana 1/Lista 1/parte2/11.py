string = input()
soma = 0
lista = string.split(',')

for x in lista:
    soma += int(x)
print(soma)
