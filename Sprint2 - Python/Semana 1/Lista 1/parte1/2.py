numero = 1
numero = int(input('Digite um número:\n'))
while(numero!=0):
    
    result = 'É par!' if numero % 2 == 0 else 'É impar!'
    print(result)
    numero = int(input('Digite um número:\n'))
