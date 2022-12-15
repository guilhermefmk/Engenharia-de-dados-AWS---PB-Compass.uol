'''
Dado o array abaixo, some 10 em todos os elementos da última coluna.
• np.random.uniform(size=(8, 8))

'''
import numpy as np

array = np.random.uniform(size=(8, 8))
soma = lambda x : x + 10
array[:,-1] = soma(array[:,-1])
print(array)
