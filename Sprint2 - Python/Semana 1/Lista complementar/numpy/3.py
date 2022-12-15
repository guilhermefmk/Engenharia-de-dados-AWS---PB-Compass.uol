'''
Dado o array 2D abaixo, substitua o seu maior valor por 0.
• np.random.normal(0, 3, size=(5, 5))

'''
import numpy as np

array = np.random.normal(0, 3, size=(5, 5))
array[array == array.max()] = 0


print(array)