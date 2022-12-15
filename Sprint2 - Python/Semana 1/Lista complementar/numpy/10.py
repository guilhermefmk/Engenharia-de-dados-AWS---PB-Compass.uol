'''
Dado o array 2D abaixo, substitua os 5 menores valores por -1, seu código não deve conter nenhum tipo de
loop (for / while):
• a = np.random.randint(0, 50, (5, 5))
'''
import numpy as np

array = np.random.randint(0, 50, (5, 5))
cinco_minimos = np.unique(np.sort(array.flatten()))[:5]

array[np.where(array <= cinco_minimos[4])] = -1
print(array)
