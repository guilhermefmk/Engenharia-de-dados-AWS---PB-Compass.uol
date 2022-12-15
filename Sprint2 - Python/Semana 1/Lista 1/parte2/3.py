


palavra = str(input('Digite uma palavra:\n'))

result = 'é palindromo' if (palavra.lower() == palavra[::-1].lower()) else 'Não é palindromo'

print(result)