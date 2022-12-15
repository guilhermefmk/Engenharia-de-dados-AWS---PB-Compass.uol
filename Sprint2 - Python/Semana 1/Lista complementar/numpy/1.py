'''
    Exercício 1
    Crie um array 5x5 com a sequência 1...25 (incluso) e faça a soma dos elementos da diagonal.
'''


import numpy as np


y = np.arange(1,26)
y = y.reshape(5,5)
diag = np.diagonal(y)
soma = sum(diag)
print(y)
print(soma)