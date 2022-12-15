'''
Dado o array abaixo, selecione os valores Pares e todos os valores maiores que 8, seu código não deve conter
nenhum tipo de loop (for / while):
• np.arange(25).reshape(5, 5)
'''
import numpy as np

array = np.arange(25).reshape(5, 5)

print(array[np.where((array>8) & (array % 2 == 0))])


