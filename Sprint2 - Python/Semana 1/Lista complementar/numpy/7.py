'''
Dados os dois arrays 2x4 abaixo, empilhe ambos formando um novo array 4x4.
• np.array([[0,3,4,5], [7, 10, 9, 2]])
• np.array([[1,4,9,12], [15, 22, 19, 17]])
'''
import numpy as np
array1 = np.array([[0,3,4,5], [7, 10, 9, 2]])
array2 = np.array([[1,4,9,12], [15, 22, 19, 17]])

matriz = np.concatenate((array1, array2))

print(matriz)